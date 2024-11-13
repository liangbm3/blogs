---
title: Obsidian复刻Typora的图片操作
date: 2024-11-14 00:06:23
description: 这篇博客主要记录一些图片相关的问题，例如：图片的自动居中，图片的缩放，图床的设置，如何利用脚本工具将图片从Markdown自动转换成HTML语法。
tags: 
    - 日常总结
    - 工具
    - Obsidian
top_img: /img/Obsidian复刻Typora的图片操作/cover.png
cover: /img/Obsidian复刻Typora的图片操作/cover.png
---

# 1. 前言

最近入坑了Obsidian🤗🤗🤗，由于学习成本太高，之前一直没有入坑，因为Typora真的挺好的。但是由于Obsidian可自定义程度非常高，所以还是决定从Typora迁移到Obsidian。这篇博客主要记录一些图片相关的问题，例如：图片的自动居中，图片的缩放，图床的设置，如何利用脚本工具将图片从Markdown自动转换成HTML语法。

# 2. 图片的自动居中

正常来说直接插入Markdown的图片是占满整个页宽的，所以居中不居中看不出来，但是如果对图片进行缩放时，如图

<img src="/img/Obsidian复刻Typora的图片操作/image-20241113230847978.png" alt="image-20241113230847978" style="zoom:50%;" />

图片会自动靠左，其实这主要取决于Markdown编辑器，例如在vscode中图片就是自动居中的，要在Typora中实现图片自动居中，可以通过添加CSS来实现，具体步骤如下：

1.   在设置界面，点击`外观`，然后打开CSS文件夹

     ![image-20241113231228686](/img/Obsidian复刻Typora的图片操作/image-20241113231228686.png)

     在该文件夹下，新建一个`center.css`，复制粘贴以下内容：

     ```css
     img {
         display: block !important;
         margin-left: auto !important;
         margin-right: auto !important;
     }
     
      .markdown-source-view.mod-cm6 .cm-content > * {
         margin: auto auto !important;
     }
     ```

2.   回到刚才的页面，开启该代码片段，如图

     <img src="/img/Obsidian复刻Typora的图片操作/image-20241113232256088.png" alt="image-20241113232256088"  />

# 3. 图片的缩放

如果是Markdown语法的缩放，可以使用插件 mousewheel-image-zoom ，但是这个语法不是Markdown的通用语法，一般在Markdown中图片的缩放是使用HTML语法的，例如：

```html
<img src="https://raw.githubusercontent.com/liangbm3/photos/main/Typora/20241113224150.png" style="zoom:67%;">
```

这个语句可以实现图片缩放67%，所以只要我们只要将图片写成HTML的表达方式，就可以很方便地缩放了。

# 4. 图床的设置

为什么要设置图床？一方面当然是方便Markdown文件的传播，还有一个重要的原因是Obsidian图片的HTML语法不支持相对路径（🙃🙃🙃），我们写Markdown一般不会写绝对路径，使用图床我们可以得到的是一个链接，这是一个非常完美的解决方案。关于图床，网上有很多种，这里以Github+PicGo-Core为例：

1.   安装了 node 或 yarn 之后，在终端中以下命令

     ```powershell
     npm install picgo -g
     
     # or
     
     yarn global add picgo
     ```

2.   进行配置

     picgo 的默认配置文件为`~/.picgo/config.json`。其中`~`为用户目录。不同系统的用户目录不太一样。

     Linux 和 macOS 均为`~/.picgo/config.json`。

     windows 则为`C:\Users\你的用户名\.picgo\config.json`

     一个示例如下图：

     ```json
     {
       "picBed": {
         "uploader": "github",
         "current": "github",
         "github": {
           "repo": "",
           "branch": "",
           "token": "",
           "path": "",
           "customUrl": ""
         },
         "transformer": "path"
       },
       "picgoPlugins": {}
     }
     ```

     注释如下：

     ```json
     {
       "repo": "", // 仓库名，格式是 username/reponame
       "token": "", // github token
       "path": "", // 自定义存储路径，比如 img/
       "customUrl": "", // 自定义域名，注意要加 http://或者 https://
       "branch": "" // 分支名，默认是 main
     }
     ```

3.   Github 获取个人 token

     -   访问：[settings-tokens](https://github.com/settings/tokens) ，点击**Generate new token**
     -   设置 token 属性
         -   Expiration：`no expiration`
         -   Select scopes：`repo` 选择存放的仓库
         -   点击`Generate token`，生成 token。

     >   这个 token 生成后只会显示这一次！注意复制、保存到其他地方以备后续使用。

4.   将信息填入上述json文件即可

     >   也可以通过在终端输入`picgo set uploader`按照提示自动生成json文件

5.   配置好picgo后进入Obsidian中下载插件 Image auto upload Plugin

     ![image-20241113234933073](/img/Obsidian复刻Typora的图片操作/image-20241113234933073.png)

6.   可以设置粘贴自动上传图片，如图

     <img src="/img/Obsidian复刻Typora的图片操作/image-20241113235049992.png" alt="image-20241113235049992" style="zoom:50%;" />

到这里图床已经完成了。

# 5. Markdown自动转换成HTML语法

这个是Typora中的一个特色功能，如图

<img src="/img/Obsidian复刻Typora的图片操作/71d6f77faabf7457985405753aefb65.png" alt="71d6f77faabf7457985405753aefb65" style="zoom:50%;" />

然而似乎Obsidian中没有类似的插件实现这个功能。

在Windows中，我们可以借助自动化工具 AutoHotkey 实现，步骤如下：

1.   进入[AutoHotkey ](https://www.autohotkey.com/)官网，下载安装包，安装。

2.   在合适的位置，右键，新建一个`.ahk`脚本

     <img src="/img/Obsidian复刻Typora的图片操作/image-20241113235818365.png" alt="image-20241113235818365" style="zoom:50%;" />

3.   用文本编辑器打开，复制粘贴如下内容

     ```
     ^p:: ; 按下 Ctrl + P 触发
         Clipboard := "" ; 清空剪贴板
         Send ^c ; 复制当前选中内容
         ClipWait, 1 ; 等待内容进入剪贴板
     
         ; 检查是否是 Markdown 图片格式并替换为 HTML 图片标签
         if (Clipboard ~= "!\[.*?\]\((.*?)\)") {
             ; 使用正则表达式将 Markdown 图片语法转换为 HTML <img> 标签
             newContent := RegExReplace(Clipboard, "!\[.*?\]\((.*?)\)", "<img src=""" . "$1" . """ style=""zoom:67%;"">")
             
             ; 将新内容设置为剪贴板内容
             Clipboard := newContent
             ClipWait, 1 ; 等待剪贴板更新
             Send ^v ; 粘贴替换后的内容
         }
     return
     
     ```

4.   保存退出，然后我们双击运行该脚本，运行之后可以在系统托盘中看到一个`H`图标

5.   之后我们只要在Obsidian里面选中要转换的Markdown图片语法，按住`Ctrl + P`，即可自动转换，非常方便。

# 6. 参考链接

+   [配置文件 | PicGo-Core](https://picgo.github.io/PicGo-Core-Doc/zh/guide/config.html)
+   [4.1.230226 obsidian的图片如何居中显示？ - 经验分享 - Obsidian 中文论坛](https://forum-zh.obsidian.md/t/topic/15964)
+   [使用PicGo + GitHub 搭建 Obsidian 图床 | Leehow的小站](https://www.haoyep.com/posts/github-graph-beds)