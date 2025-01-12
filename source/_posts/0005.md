---
title: WSL的使用
date: 2024-10-27 14:54:20
description: 在使用WSL的过程中，由于默认安装到C盘的，导致C盘爆满，所以想着迁移到D盘，顺便总结了一下WSL的命令，固有此文。
tags: 
    - 日常总结
top_img: /img/WSL的使用/cover.png
cover: /img/WSL的使用/cover.png
---
在使用WSL的过程中，由于默认安装到C盘的，导致C盘爆满，所以想着迁移到D盘，顺便总结了一下WSL的命令，固有此文。

# 1. WSL的常用命令

## 1.1 基础 WSL 命令

-   **启动默认 WSL 发行版**：

    ```powershell
    wsl
    ```

-   **启动特定的 WSL 发行版**：

    ```powershell
    wsl -d <发行版名称>
    ```

    例如：

    ```powershell
    wsl -d Ubuntu-20.04
    ```

-   **查看所有已安装的 WSL 发行版**：

    ```powershell
    wsl --list --verbose
    ```

    或者简写：

    ```powershell
    wsl -l -v
    ```

-   **设置默认 WSL 发行版**：

    ```powershell
    wsl --set-default <发行版名称>
    ```

    例如：

    ```powershell
    wsl --set-default Ubuntu-20.04
    ```

## 1.2. WSL 版本管理

-   **检查 WSL 发行版版本**（1 或 2）：

    ```powershell
    wsl --list --verbose
    ```

-   **设置指定 WSL 发行版为 WSL 2**：

    ```powershell
    wsl --set-version <发行版名称> 2
    ```

    例如：

    ```powershell
    wsl --set-version Ubuntu-20.04 2
    ```

-   **设置新的默认 WSL 版本**（将新安装的发行版默认设置为 WSL 2）：

    ```powershell
    wsl --set-default-version 2
    ```

## 1.3. 启动和停止 WSL

-   **停止所有运行中的 WSL 发行版**：

    ```powershell
    wsl --shutdown
    ```

-   **终止特定 WSL 发行版**：

    ```powershell
    wsl --terminate <发行版名称>
    ```

    例如：

    ```powershell
    wsl --terminate Ubuntu-20.04
    ```

## 1.4. WSL 文件系统操作

-   **从 WSL 访问 Windows 文件系统**：

    -   在 WSL 中，可以通过 `/mnt/c` 等路径访问 Windows 的 C 盘文件。

    ```powershell
    cd /mnt/<windows路径>
    ```

    例如:

    ```powershell
    cd /mnt/c/Users/lbm/
    ```

-   **从 Windows 访问 WSL 文件系统**：

    在文件资源管理器的地址栏中输入：

    ```powershell
    \\wsl$\<发行版名称>
    ```

    例如：

    ```powershell
    \\wsl$\Ubuntu-20.04
    ```

## 1.5. 发行版的安装和卸载

-   **安装新的 WSL 发行版**：

    可以通过 **Microsoft Store** 下载和安装新的 WSL 发行版（如 Ubuntu、Debian 等）。

-   **卸载 WSL 发行版**：

    ```powershell
    wsl --unregister <发行版名称>
    ```

    例如：

    ```powershell
    wsl --unregister Ubuntu-20.04
    ```

## 1.6. 发行版的导入与导出

-   **导出 WSL 发行版**（备份）：

    ```powershell
    wsl --export <发行版名称> <文件路径>
    ```

    例如：

    ```powershell
    wsl --export Ubuntu-20.04 D:\backup\ubuntu_backup.tar
    ```

-   **导入 WSL 发行版**（恢复）：

    ```powershell
    wsl --import <自定义名称> <安装路径> <备份文件路径>
    ```

    例如：

    ```powershell
    wsl --import MyUbuntu D:\WSL\Ubuntu D:\backup\ubuntu_backup.tar
    ```

## 1.7. 设置和调试

-   **查看 WSL 帮助**：

    ```powershell
    wsl --help
    ```

-   **检查 WSL 状态和配置**：

    ```powershell
    wsl --status
    ```

# 2. 更改WSL的安装路径

Windows似乎不支持直接更改WSL的默认安装路径，但支持安装发行版的时候自定义安装路径，或者将已经安装好的发行版迁移到其他盘符。

## 2.1 自定义安装路径

若想自定义安装路径，不能直接从电脑的**Microsoft Store**中直接安装，这样的话会直接被安装到默认路径中。

1.   在<https://learn.microsoft.com/zh-cn/windows/wsl/install-manual>中找到发行版的下载链接，如图

     <img src="/img/WSL的使用/image-20241027142019943.png" alt="image-20241027142019943" style="zoom:50%;" />

2.   选择需要安装的发行版，这里以Kali Linux为例，下载完成后解压，得到如图文件夹

     <img src="/img/WSL的使用/image-20241027142516252.png" alt="image-20241027142516252" style="zoom:50%;" />

3.   选择合适的版本，我选择的是`x64`，将后缀改为`.zip`，解压，得到如图文件夹

     <img src="/img/WSL的使用/image-20241027142648245.png" alt="image-20241027142648245" style="zoom:50%;" />

     `install.tar.gz`就是我们安装需要用到的文件

4.   执行安装命令

     ```powershell
     wsl --import <自定义名称> <目标路径> <解压目录路径>\install.tar.gz
     ```

5.   设置WSL版本

     ```powershell
     wsl --set-version <自定义名称> 2
     ```

6.   启动安装的发行版

     ```powershell
     wsl --set-default <发行版名称>
     ```

7.   创建快捷方式：右键点击桌面，选择 **新建 > 快捷方式**，输入如下命令

     ```powershell
     wsl -d <发行版名称>
     ```

     点击 **下一步**，为快捷方式命名，然后点击 **完成**。创建完成后，右键点击快捷方式，可以选择 **固定到“开始”屏幕** 或 **固定到任务栏**。

## 2.2 将WSL安装的发行版迁移至其他盘符

1.   查看安装的发行版

     ```powershell
     wsl -l --all  -v
     ```

2.   导出分发版为`.tar`文件到d盘

     ```powershell
     wsl --export Ubuntu-20.04 d:\wsl-ubuntu20.04.tar
     ```

3.   注销当前分发版

     ```powershell
     wsl --unregister Ubuntu-20.04
     ```

4.   重新导入并安装WSL在`d:\wsl-ubuntu20.04`

     ```powershell
     wsl --import Ubuntu-20.04 d:\wsl-ubuntu20.04 d:\wsl-ubuntu20.04.tar --version 2
     ```

5.   设置默认登陆用户为安装时用户名

     ```powershell
     ubuntu2004 config --default-user Username
     ```

6.   删除`.tar`文件

     ```powershell
     del d:\wsl-ubuntu20.04.tar
     ```

# 3. 参考资料

[Win10/11下安装WSL并修改WSL默认安装目录到其他盘_wsl选择安装目录-CSDN博客](https://blog.csdn.net/farer_yyh/article/details/133934904)