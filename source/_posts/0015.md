---
title: Git中对提交历史进行处理
date: 2024-11-14 12:54:53
description: 这篇博客将对Git中的版本管理操作作进一步总结。
tags: 
    - Git
    - 日常总结
top_img: /img/Git中对提交历史进行处理/cover.png
cover: /img/Git中对提交历史进行处理/cover.png
---

# 1. 前言

在之前的[Git 的使用总结](https://liangbm3.top/2024/10/19/git的使用总结/)这篇博客中，总结了一些Git的基础命令和用法，这篇博客将对Git中的版本管理操作作进一步总结。

# 2. 场景

我们使用Git来管理我们的项目时，有时候会不小心提交一些不该提交的文件，如果我们直接将这些文件删除，会留下提交记录。所以我们需要删除那次的提交记录，主要的方法有`git reset`和`git rebase`

# 3. 操作流程

## 3.1 使用git reset 命令

1.   先查看提交历史

     ```bash
     git log --oneline
     ```

     确认需要删除的提交的位置，假设提交历史如下

     ```
     abc1234 Third commit (最新提交)
     def5678 Second commit (需要删除的提交)
     ghi9101 First commit
     ```

2.   将指针重置到`First commit`，并将更改保留在暂存区。可以使用如下命令

     ```bash
     git reset --soft HEAD~3
     ```

     或使用

     ```bash
     git reset --soft ghi9101
     ```

3.   从暂存区删除我们错误提交的文件，然后重新commit

4.   然后执行以下命令推送到远程仓库

     ```bash
     git push origin main --force
     ```

     之所以要使用`--force`，是因为通常Git 在推送时会检查你本地的提交历史是否与远程仓库的历史一致。如果本地和远程仓库的提交历史有冲突（例如你使用 `git rebase` 或 `git reset` 修改了本地历史），Git 默认会拒绝推送，以防止你覆盖远程仓库中的提交历史。当你想要覆盖远程仓库的历史时（例如修改或删除提交），必须使用 `--force` 选项，告诉 Git 你明确地希望覆盖远程历史。

5.   完成

## 3.2 使用git rebase 命令
1.   先查看提交历史

     ```bash
     git log --oneline
     ```

     确认需要删除的提交的位置，假设提交历史如下

     ```
     abc1234 Third commit (最新提交)
     def5678 Second commit (需要删除的提交)
     ghi9101 First commit
     ```

2.   打开一个编辑器，并显示最近 3 个提交的列表

     ```bash
     git rebase -i HEAD~3
     ```

3.   在编辑器中找到需要删除的提交，将其对应的 `pick` 改成 `drop`，如下所示：

     ```
     pick abc1234 Third commit
     drop def5678 Second commit
     pick ghi9101 First commit
     ```

4.   完成 Rebase 后强制推送更改：

     ```bash
     git push origin main --force
     ```

5.   完成

# 4. git reset 和 git rebase 的不同

`git reset` 和 `git rebase` 是 Git 中两个常用的命令，它们都可以改变历史记录，但它们的用途和效果有所不同。下面是它们的主要区别和使用场景：

## 4.1. git reset

`git reset` 主要用于重置当前分支的 HEAD（当前提交的指针），它可以用于修改 Git 提交历史的指针位置，并根据不同的模式（如 `--soft`、`--mixed`、`--hard`）决定如何处理工作区和暂存区的内容。

**常用选项：**

-   `git reset --soft <commit>`：将 `HEAD` 移动到指定的提交位置，并将所有更改保留在暂存区（staging area），即重新准备提交这些更改。
-   `git reset --mixed <commit>`：将 `HEAD` 移动到指定的提交位置，并将更改保留在工作区，但从暂存区移除这些更改（相当于 `git rm --cached`）。
-   `git reset --hard <commit>`：将 `HEAD` 和工作区都移动到指定提交的位置，丢弃所有更改。所有的修改（无论是暂存区还是工作区的）都会丢失。

**使用场景：**

-   撤销提交：你可以用 `git reset` 撤销最近的提交（`git reset --soft HEAD~1` 或 `git reset --mixed HEAD~1`），并选择保留更改在工作区或暂存区。
-   撤销修改：通过 `git reset --hard` 可以彻底丢弃所有本地修改（包括工作区和暂存区），回到某个提交的状态。
-   调整历史记录指针：它通常用于调整 HEAD 指针的位置，可以方便地回到之前的某个提交。

**示例：**

```bash
# 撤销最后一次提交并将更改保留在暂存区
git reset --soft HEAD~1

# 撤销最后一次提交并将更改保留在工作区
git reset --mixed HEAD~1

# 完全撤销最后一次提交并丢弃所有更改
git reset --hard HEAD~1
```

## 4.2. git rebase

`git rebase` 是一个更为强大的命令，用于将一系列提交“重放”到另一分支上。`git rebase` 会修改分支的历史记录，它会“将你的提交移到另一个分支的后面”，就像你从一个新的基础上开始工作一样。

常用选项：

-   `git rebase <branch>`：将当前分支的所有提交“重放”到 `<branch>` 分支的末尾。例如，`git rebase main` 将当前分支的提交应用到 `main` 分支的末尾。
-   `git rebase -i <commit>`：交互式 rebase，用于编辑提交历史、删除、合并、修改提交信息等。你可以选择哪些提交进行修改。

**使用场景：**

-   清理历史提交：`git rebase -i` 允许你对提交进行重写、合并、修改提交信息等，非常适合清理提交历史。
-   合并提交：通过 `git rebase` 将多个提交合并成一个提交（`squash`），让历史更加整洁。
-   保持历史线性：使用 `git rebase` 来避免合并提交（`merge commits`），让提交历史更干净。

**示例：**

```bash
# 将当前分支的提交重放到 main 分支上
git rebase main

# 交互式 rebase，用于修改提交历史
git rebase -i HEAD~3
```

