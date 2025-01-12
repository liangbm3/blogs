---
title: Linux中使用Terminator进行分屏
date: 2024-11-02 09:28:02
description: 在进行复杂的任务时，通常需要开多个终端，有时候非常凌乱，而Terminator则是一个很好的工具，能够很好地帮助我们帮助我们同时管理多个终端
tags: 
    - Linux
    - 日常总结
    - 工具
top_img: /img/Linux中使用Terminator进行分屏/cover.png
cover: /img/Linux中使用Terminator进行分屏/cover.png
---

# 1. 前言

在进行复杂的任务时，通常需要开多个终端，有时候非常凌乱，而Terminator则是一个很好的工具，能够很好地帮助我们帮助我们同时管理多个终端。Terminator 的核心功能在于其便捷的“分屏”能力，允许用户在单个窗口内垂直或水平分割屏幕，从而同时显示多个终端会话。对于开发者、系统管理员或需要处理多任务的用户来说，Terminator 是一个高效的工具。

## 2.安装
在Ubuntu上，可以使用如下命令进行安装

```bash
sudo apt update
sudo apt install terminator
```

## 3. 基本使用
1. 启动

    使用快捷键`ctrl+Alt+T`或者在终端中输入`terminator`

2. 分屏

    + 垂直分屏：按下 `Ctrl + Shift + E`
    + 水平分屏：按下 `Ctrl + Shift + O`
    + 可以通过鼠标拖动分隔线来调整各个窗口的大小
3. 管理分屏

    + 关闭窗口：右键单击窗口，选择 “关闭” 或使用 `Ctrl + Shift + W`。
    + 切换焦点：使用鼠标单击在不同窗口之间切换焦点。
    + 组合窗口：使用鼠标可以将窗口拖拽到其他窗口旁边，形成组合。
4. 设置配置

    + 右键选择 “首选项” 可以进行个性化配置，包括配色方案、字体、背景透明度等。
    + Terminator 支持保存多种配置，可以根据不同任务选择对应的终端配置，提高使用效率。

# 4. 总结
以上就是terminator的常用命令，非常简单，只是顺手记录一下~