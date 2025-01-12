---
title: 华硕笔记本Linux系统的充电阈值控制
date: 2024-10-30 04:33:48
description: 解决华硕笔记本安装双系统后，在Linux中的充电阈值控制问题
tags: 
    - Linux
    - 日常总结
top_img: /img/华硕笔记本Linux系统的充电阈值控制/cover.png
cover: /img/华硕笔记本Linux系统的充电阈值控制/cover.png
---

# 1. 前言

如果电脑为华硕笔记本，那么是可以通过在Windows中安装华硕管家，来控制电池的充电阈值，使得电脑的电池保持健康的状态，如图：

<img src="/img/华硕笔记本Linux系统的充电阈值控制/image-20241030041828379.png" alt="image-20241030041828379" style="zoom:50%;" />

但是我们安装双系统后，在Linux系统中，该功能无法使用。目前，华硕官方没有发布在Linux中的驱动程序，但是有一个开源仓库可以解决这个问题。

# 2. 仓库介绍

[tshakalekholoane/bat: Battery management utility for Linux laptops.](https://github.com/tshakalekholoane/bat)仓库的目标是在 Windows 上复制适用于华硕笔记本电脑的华硕电池健康充电实用程序的功能，旨在延长电池的使用寿命

程序的说明如下（已翻译）：

```bash
NAME
    bat - Linux 笔记本电脑的电池管理实用程序

SYNOPSIS
    bat [-d | --debug] [-h | --help] [-v | --version]
        <command> [<arg>]

OPTIONS
    -d, --debug
        显示调试信息。

    -h, --help
        打印此帮助文档。

    -v, --version
        显示版本信息和退出。

COMMANDS
    capacity
        打印当前电池电量。

    health
        打印电池健康状态。

    persist
        在重启之间保持当前阈值。

    reset
        取消重启之间的充电阈值的持久设置。

    status
        打印充电状态。

    threshold num
        打印当前充电阈值限制。

        如果指定了 num（应该是 1 到 100 之间的一个值），则这将设置一个新的充电阈值限制。
```

# 2. 安装流程

在[发布页面](https://github.com/tshakalekholoane/bat/releases)下载二进制文件，并将他移动到你想保存的位置，假设移动到`$HOME/`目录下，执行以下命令，赋予该二进制文件执行权限

```bash
chmod +x $HOME/bat
```

设置软链接，这样任何用户可以从系统上的任何位置执行程序

```bash
sudo ln -s $HOME/bat /usr/local/bin/bat
```

# 3. 使用示例

1.  查看当前充电阈值

    ```bash
    bat threshold
    ```

2.  设置充电阈值

    ```bash
    sudo bat threshold 80
    ```

3.  重新启动时保持默认值设置

    ```bash
    sudo bat persist
    ```

# 4. 参考资料

https://github.com/tshakalekholoane/bat