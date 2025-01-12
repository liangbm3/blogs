---
title: 使用scp在计算机和远程服务器直接传输文件
date: 2024-11-04 20:18:09
description: SCP（Secure Copy Protocol）是一种用于在计算机之间安全传输文件的协议，通常用于在本地计算机和远程服务器之间复制文件。
tags: 
    - Linux
    - 日常总结
top_img: /img/使用scp在计算机和远程服务器直接传输文件/cover.png
cover: /img/使用scp在计算机和远程服务器直接传输文件/cover.png
---
# 1. 简介

SCP（Secure Copy Protocol）是一种用于在计算机之间安全传输文件的协议，通常用于在本地计算机和远程服务器之间复制文件。

# 2. 使用说明

语法：

```bash
scp [可选参数] file_source file_target 
```

可选参数如下：

-   `-1`： 强制scp命令使用协议ssh1
-   `-2`： 强制scp命令使用协议ssh2
-   `-4`： 强制scp命令只使用IPv4寻址
-   `-6`： 强制scp命令只使用IPv6寻址
-   `-C`： 允许压缩。（将-C标志传递给ssh，从而打开压缩功能）
-   `-p`：保留原文件的修改时间，访问时间和访问权限。
-   `-q`： 不显示传输进度条。
-   `-r`： 递归复制整个目录。
-   `-l limit`： 限定用户所能使用的带宽，以Kbit/s为单位。
-   `-P port`：注意是大写的P, port是指定数据传输用到的端口号

# 3. 使用示例

1.   将本地一个文件复制到远程服务器的桌面

     ```powershell
     scp file.zip root@192.168.2.1:/home/Desktop
     ```

2.   将本地一个文件夹复制到远程服务器的桌面

     ```powershell
     scp -r file root@192.168.2.1:/home/Desktop
     ```

3.   指定端口进行复制

     ```powershell
     scp -r 端口号 file root@192.168.2.1:/home/Desktop
     ```

4.   从服务器中下载

     ```powershell
     scp root@192.168.2.1:/home/Desktop/file.zip "D:\Downloads\Compressed"
     ```

# 4. 参考资料

[Linux scp命令 | 菜鸟教程](https://www.runoob.com/linux/linux-comm-scp.html)
