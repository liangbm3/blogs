---
title: VPIphotonics10.1安装教程
date: 2024-10-30 15:40:03
description: 在数字信号处理课程中，需要用到VPIphotonics工具，由于没有正版，需要进行破解安装。这里记录的是在Windows下安装VPIphotonics的完整过程。
tags: 
    - 环境配置
top_img: /img/VPIphotonics10.1安装教程/cover.jpg
cover: /img/VPIphotonics10.1安装教程/cover.jpg
---

在数字信号处理课程中，需要用到VPIphotonics工具，由于没有正版，需要进行破解安装。这里记录的是在Windows下安装VPIphotonics的完整过程。

# 1. VPIphotonics介绍

VPIphotonics是一家知名的光通信和光电设计软件供应商，专注于提供仿真和设计工具，广泛应用于光通信、光子集成、传感等领域。其产品主要面向科研机构、企业和学术界，为用户提供高效的仿真与分析能力，支持复杂光学系统和网络的设计、优化与验证。我们主要用它对信道进行仿真。

# 2. 资源获取

+   VPIphotonics 10.1 安装包

    通过网盘分享的文件：VPIphotonics_DesignSuite_10.1_Windows_Expert_x64 .zip
    链接: https://pan.baidu.com/s/1LbwBRit74FTAQT41_tnhSQ?pwd=yv3t 提取码: yv3t

+   虚拟网卡工具

    通过网盘分享的文件：TAP-windows.zip 
    链接: https://pan.baidu.com/s/10SuNfryHzsWJf87LsLU4Lw?pwd=2ufg 提取码: 2ufg

# 3. 安装流程

## 3.1 使用管理员账号登录

Windows是一个多用户系统，在这些用户中会有一个超级管理员，也就是 Administrator 账户，相当于Linux下的root。我们使用的一般是普通用户，因此需要先开启管理员账户，然后登入该账户，步骤如下：

1.   使用组合键`win+x`，点击`计算机管理`
2.   进入到计算机管理界面，在左侧栏中点击`本地用户和组`
3.   点击`用户`，找到`Administrator`，双击
4.   在Administrator的属性界面，将`账户已禁用`的勾去掉
5.   重启，在锁屏界面那里点击头像可以切换 Administrator 账户登录

> 注意：如果是Windows家庭版的话，无法安装该方法配置`本地用户和组`来开启 Administrator 账户，可以以管理员身份运行CMD，然后输入命令`net user administrator /active:yes`即可

## 3.2 安装虚拟网卡

由于是通过修改网卡的mac地址来破解的，而笔记本使用的一般是无线网卡，通常无法进行修改，因此我们需要安装虚拟网卡来完成破解，步骤如下：

1.   安装Tap-Windows

     Tap-Windows 是一种**虚拟网络适配器驱动程序**，它创建了一个虚拟的TAP (以太网桥接)设备，允许用户在计算机上模拟一个额外的网络适配器。直接解压上述压缩包，正常安装即可。

2.   验证安装

     安装完成后，可以使用组合键`win+x`，点击`设备管理器`，在网络适配器中可以看到虚拟网卡，如图：

     <img src="/img/VPIphotonics10.1安装教程/image-20241030062424581.png" alt="image-20241030062424581" style="zoom:50%;" />

## 3.3 更改虚拟网卡的mac地址

1.   进入控制面板，点击`网络和Internet`，点击`网络和共享中心`，点击`更改适配器设置`，进入到如图界面

     <img src="/img/VPIphotonics10.1安装教程/image-20241030063056371.png" alt="image-20241030063056371" style="zoom:50%;" />

2.   右键虚拟网卡（下面标着`TAP-Window Adapter V9`），选择`Internet 协议版本4(TCP/IPv4)`后点击`配置`，如图：

     <img src="/img/VPIphotonics10.1安装教程/image-20241030063406931.png" alt="image-20241030063406931" style="zoom:50%;" />

3.   点击`高级`，找到`MAC Address`属性

     <img src="/img/VPIphotonics10.1安装教程/image-20241030063500026.png" alt="image-20241030063500026" style="zoom:50%;" />

4.   用记事本打开`vpi-permanent.vpl`文件，将文件中的地址填入上述`MAC Address`属性的值中，如图：

     <img src="/img/VPIphotonics10.1安装教程/image-20241030063836753.png" alt="image-20241030063836753" style="zoom:50%;" />

## 3.4 保持计算机名称和文件一致

保持计算机名称和`vpi-permanent.vpl`文件一致，可以选择更改本机计算机名称或者选择更改`vpi-permanent.vpl`中的计算机名称

+   本机计算机名称在`设置->属性中查看和更改`

+   `vpi-permanent.vpl`文件中计算机名称字段位置如图所示

    <img src="/img/VPIphotonics10.1安装教程/image-20241030064828223.png" alt="image-20241030064828223" style="zoom:50%;" />

## 3.5 安装VPIphotonics

打开下载的压缩包，打开`autorun`文件夹，运行里面的`Autorun.exe`，选择`Install`，无论遇到什么，都选择 “Next”，不要更改路径 ，默认安装到 C 盘。

## 3.6 运行license文件

双击`vpi-permanent.vpl`文件，点击确定运行。

## 3.7 安装完成

安装完成，可以退出`Administrator`账户，进入普通账户使用。打开 VPIphotonics， Select Products选第一个`VPItransmissionMaker Optical Systems`，即可使用VPIphotonics。  







