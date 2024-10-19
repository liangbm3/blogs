---
title: Git的使用总结
date: 2024-10-19 20:56:30
tags: 
    - Git
    - 日常总结
top_img: /img/Git的使用总结/cover.png
cover: /img/Git的使用总结/cover.png
---
## 1. 前言

自己在平时的学习中，Git是使用比较多的工具，但是有一些命令常常忘记，或是对一些命令理解不透彻，这里做一个总结和记录。

## 2. Git简介

这里长话短说，Git是目前世界上最先进的分布式版本控制系统，Git 采用分布式架构，在 Git 中每个开发人员的代码工作副本也是一个可以包含所有变更完整历史记录的存储库。

每当你在Git中提交更新或保存项目状态时，它基本上就会对当时的全部文件创建一个快照并保存这个快照的索引。 为了效率，如果文件没有修改，Git 不再重新存储该文件，而是只保留一个链接指向之前存储的文件。 Git 对待数据更像是一个 **快照流**。如图

<img src="/img/Git的使用总结/image-20241014234011540.png" alt="/img/Git的使用总结/image-20241014234011540" style="zoom:50%;" />

你执行的 Git 操作，几乎只往 Git 数据库中 **添加** 数据。 你很难使用 Git 从数据库中删除数据，也就是说 Git 几乎不会执行任何可能导致文件不可恢复的操作。

## 3. 基本知识

### 3.1 版本管理

Git 有三种状态：

-   **已修改(modified)：**表示修改了文件，但还没保存到数据库中。
-   **已暂存(staged)：**表示对一个已修改文件的当前版本做了标记，使之包含在下次提交的快照中。
-   **已提交(committed)：**表示数据已经安全地保存在本地数据库中。

Git 项目拥有三个阶段：

+   **工作区**：工作区是对项目的某个版本独立提取出来的内容。可以理解为你正在编辑的那些文件就在工作区之中。
+   **暂存区**：是一个文件，保存了下次将要提交的文件列表信息。
+   **Git 仓库**： Git 用来保存项目的元数据和对象数据库的地方。 这是 Git 中最重要的部分，从其它计算机克隆仓库时，复制的就是这里的数据。

基本的 Git 工作流程如下图

<img src="/img/Git的使用总结/image-20241014235221867.png" alt="/img/Git的使用总结/image-20241014235221867" style="zoom:50%;" />

即：

1.   在工作区修改文件
2.   将你想要下次提交的更改选择性地暂存，这样只会将更改的部分添加到暂存区。
3.   提交更新，找到暂存区的文件，将快照永久性存储到 Git 目录。

### 3.2 分支

分支模型是Git的一个重要特性。其实在每次提交时，Git都会包含一个指向父对象的指针（首次提交对象没有父对象），Git的分支，本质上是指向提交对象的可变指针，Git的默认分支名字是master，多次提交后，我们其实已经有一个指向最后那个提交对象的master分支。

HEAD严格来说不是指向提交，而是指向master，master才是指向提交的，所以，HEAD指向的就是当前分支。如图

<img src="/img/Git的使用总结/image-20241015123909809.png" alt="/img/Git的使用总结/image-20241015123909809" style="zoom:50%;" />

当我们创建分支时，相当于创建了一个类似于master的指针，如图

<img src="/img/Git的使用总结/image-20241015124125630.png" alt="/img/Git的使用总结/image-20241015124125630" style="zoom:50%;" />

如果HEAD指向dev，那么所作出的修改都会提交到dev分支，如图

<img src="/img/Git的使用总结/image-20241015124323636.png" alt="/img/Git的使用总结/image-20241015124323636" style="zoom:50%;" />

合并分支相当于修改master的指针指向dev。

## 4. Git的安装

参考：[Windows系统Git安装教程（详解Git安装过程） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/242540359)

每次安装完Git时，记得配置用户名和邮件地址。每一个 Git 提交都会使用这些信息，并且会写入到每一次提交中，不可更改。配置命令：

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

## 5. 基础的工作流程

### 5.1 使用Git进行版本管理

#### 5.1.1 获取 Git 仓库

有两种方式：

1.   将尚未进行版本控制的本地目录转换为 Git 仓库。

     执行命令

     ```bash
     git init
     ```

     将创建一个名为 `.git` 的子目录，这个子目录含有初始化的 Git 仓库中所有的必须文件。

2.   从其它服务器 **克隆** 一个已存在的 Git 仓库。

     ```bash
     git clone https://github.com/libgit2/libgit2 mylibgit
     ```

     可以在克隆的时候指定本地仓库名

     ```bash
     git clone https://github.com/libgit2/libgit2 mylibgit
     ```

     可以指定分支

     ```bash
     git clone -b master https://github.com/libgit2/libgit2
     ```

#### 5.1.2 查看文件的状态

文件会存在两种状态：

+   已跟踪：已经被纳入版本控制的文件
+   未跟踪：没有被纳入版本管理的文件

可以使用命令来检查文件处于什么状态

```bash
git status
```

要查看更加详细的信息可以使用

```bash
git diff
```

此命令比较的是工作目录中当前文件和暂存区域快照之间的差异。 也就是修改之后还没有暂存起来的变化内容。

#### 5.1.3 添加文件到暂存区

跟踪新文件和或把已跟踪的文件放到暂存区

```bash
git add 
```

参数列表：

+   `git add -A`：提交所有变化（ -A  ==  --all ）

+   `git add -u`：提交被修改（modified）和被删除（deleted）的文件，不包括新文件（new）。（ -u  ==  --update）

+   `git add .`：提交新文件（new）和被修改（modified）文件，不包括被删除（deleted）文件
+   `git add <path> `：等同于 `git add .`

#### 5.1.4 将暂存区内容提交到仓库

提交更新

```bash
git commit -m "提交说明"
```

可以使用以下命令跳过使用暂存区，即会自动把所有已经跟踪过的文件暂存起来一并提交

```bash
git commit -a -m "提交说明"
```

#### 5.1.5 查看提交历史

```bash
git log
```

显示每次提交的差异：

```bash
git log -p
```

只显示最近两次的提交：

```bash
git log -2
```

#### 5.1.6 撤销操作

如果发现漏了文件忘了提交，可以使用命令

```bash
git commit --amend
```

一个示例如下：

```bash
git commit -m 'initial commit'
git add forgotten_file
git commit --amend
```

取消暂存的文件，可以使用命令

```bash
git reset <file>...
```

撤销对文件的修改

```bash
git checkout --<file>
```

>     `git checkout — <file>` 是一个危险的命令。 你对那个文件在本地的任何修改都会消失——Git 会用最近提交的版本覆盖掉它。

#### 5.1.7 版本回退

命令为

```bash
git reset
```

回退到上一版本：

```bash
git reset --hard HEAD^
```

参数：

+   `--hard`：回退到上一个版本已提交状态
+   `--soft`：回退到是一个版本未提交的状态
+   `--mixed`：回退到上一个版本已添加但为提交的状态

回退到某个版本

```bash
git reset --hard 1094a
```

后面的字符串是版本号，写前几个即可，Git会自动查找。

如果想恢复到新版本，却找不到新版本的commit id时，可以使用`git reflog`命令，通过查看命令历史来找到新版本提交的commit id。

### 5.2 Git 分支的使用

#### 5.2.1 查看分支

查看所有分支

```bash
git branch
```

`git branch`命令会列出所有分支，当前分支前面会标一个`*`号。

查看远程分支

```bash
git branch -r
```

查看远程和本地分支

```bash
git branch -a
```

#### 5.2.2 创建分支

创建dev分支，然后切换到dev分支：

```bash
git checkout -b dev
```

`git checkout`命令加上`-b`参数表示创建并切换，相当于以下两条命令：

```bash
git branch dev
git checkout dev
```

新版本可以使用如下命令来创建和切换分支:

创建并切换到新的dev分支，可以使用：

```bash
git switch -c dev
```

直接切换到已有的master分支，可以使用：

```bash
git switch master
```

#### 5.2.3 合并分支

一种比较简单的情况是，我们在master分支中，创建并切换到dev分支上进行了修改后，如图

<img src="/img/Git的使用总结/image-20241015154405605.png" alt="/img/Git的使用总结/image-20241015154405605" style="zoom:50%;" />

然后我们将dev分支合并到master分支上，这时我们需要切换到master分支，执行命令

```bash
git merge dev
```

如果两者没有冲突，很快地就会合并成功了。但如果我们有一个新的feature1分支，master和feature1分支都有了新的提交，并且两者修改了同一地方，如图

<img src="/img/Git的使用总结/image-20241015154526015.png" alt="/img/Git的使用总结/image-20241015154526015" style="zoom:50%;" />

这样会产生冲突，必须手动解决冲突后才能合并。Git检测到这种冲突时，它会在冲突的文件中插入冲突标记。

冲突标记通常以`<<<<<<<`，`=======`和`>>>>>>>`开头，并在两个冲突部分的之间有额外的信息。一个示例如下：

```bash
<<<<<<< HEAD
这是版本A的修改内容
=======
这是版本B的修改内容
>>>>>>> branchB
```

我们对其修改后，再进行提交即可，如图

<img src="/img/Git的使用总结/image-20241015155351642.png" alt="/img/Git的使用总结/image-20241015155351642" style="zoom:50%;" />

#### 5.2.4 删除分支

```bash
git branch -d feature1
```

### 5.4 远程仓库的使用

<img src="https://pic3.zhimg.com/v2-e882ff20e4d7e0b5d3a3b197c531f2f8_r.jpg" alt="img" style="zoom:50%;" />

查看已经连接的远程仓库

```bash
git remote -v
```

添加远程仓库

```bash
git remote add <shortname> <url>
```

```bash
git remote add origin https://github.com/paulboone/ticgit
```

之后我们可以在命令行中使用pd代替后面整个URL。

此时我们可以运行`git fetch origin`命令来获得远程仓库的副本，但是不会自动修改或合并当前的工作，需要将当前分支合并到远程分支。我们可以设置当前分支跟踪远程分支，然后就可以使用`git pull`命令自动抓取后合并该分支到当前分支。

+   创建本地分支并跟踪远程分支

    ```bash
    git checkout -b <branch-name> origin/<branch-name>
    ```

+   为现有的本地分支设置跟踪远程分支

    ```bash
    git branch --set-upstream-to=origin/<branch-name> <branch-name>
    ```

    如果当前处于该分支，可以省略本地分支名

    ```bash
    git branch --set-upstream-to=origin/<branch-name>
    ```

如果仓库是使用`git clone`得到的，该命令会自动设置本地master分支跟踪克隆远程仓库的master分支。

## 6 .gitignore文件的编写

`.gitignore`文件用来告诉 Git 哪些文件或目录不应该被跟踪或提交到版本库中。

1.   忽略文件或目录的基本规则

     1.   忽略某个文件，直接写文件名称

          ```
          myfile.txt
          ```

     2.   忽略某个目录，在目录名称后面加`/`

          ```
          logs/
          ```

     3.   忽略特定类型的文件，使用通配符`*`来忽略某种类型的文件

          ```
          *.log
          ```

2.   忽略某个文件夹下的所有文件

     ```
     folder_name/*
     ```

3.   例外规则

     如果你想忽略大多数文件，但保留其中某些文件，可以使用 `!` 进行例外。

     ```
     *.log      # 忽略所有 .log 文件
     !important.log  # 但不忽略 important.log
     ```

4.   通配符的使用

     1.   `*`：匹配任意数量的字符。例如，忽略所有 `.tmp` 文件

          ```
          *.tmp
          ```

     2.   `?`：匹配任意单个字符。例如，忽略 `file1.txt`, `file2.txt`, 但不忽略 `file11.txt`

          ```
          file?.txt
          ```

     3.   `**`：匹配任意层级的目录。例如，忽略所有 `tmp` 目录下的文件，不论层级

          ```
          tmp/**/*
          ```

5.   忽略指定目录中特定文件类型

     ```
     logs/*.log
     ```

>   注意：即使文件被添加到 `.gitignore` 中，但它们之前已经被 Git 跟踪，这时需要先停止追踪
>
>   ```bash
>   git rm --cached <file>
>   ```

## 7. 配置git的ssh key

确保用户名和邮箱已经配置

```bash
git config --global  --list 
```

如未配置，则执行以下命令

```bash
git config --global  user.name "这里换上你的用户名"
git config --global user.email "这里换上你的邮箱"
```

生成公钥

```bash
ssh-keygen -t rsa -C "这里换上你的邮箱"
```

执行命令后需要进行3次或4次确认：

1.  确认秘钥的保存路径（如果不需要改路径则直接回车）；
2.  如果上一步置顶的保存路径下已经有秘钥文件，则需要确认是否覆盖（如果之前的秘钥不再需要则直接回车覆盖，如需要则手动拷贝到其他目录后再覆盖）；
3.  创建密码（如果不需要密码则直接回车）；
4.  确认密码；

找到生成的公钥文件，windows下一般在目录`C:\Users\用户名\.ssh\id_rsa.pub`，Linux一般在`~/.ssh/id_rsa.pub`，打开复制内容

然后打开GitHub，进入设置页面，点击“SSH and GPG keys”，粘贴刚才复制的内容，生成私钥，大功告成。

## 8. 参考资料

+   [Git冲突标记|极客教程 (geek-docs.com)](https://geek-docs.com/git/git-questions/518_git_git_conflict_markers.html)
+   [Git 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/git/git-tutorial.html)
+   [Git 系列四：Git远程仓库操作 - 知乎](https://zhuanlan.zhihu.com/p/418947255)
+   [Git](https://git-scm.com/book/zh/v2)
+   [简介 - Git教程 - 廖雪峰的官方网站](https://liaoxuefeng.com/books/git/introduction/index.html)

## 9. 结语

若有其它新内容，后续再补充。