---
title: Windows的PowerShell美化教程
date: 2024-11-23 20:48:31
description: 记录在一次Windows中升级PowerShell 5.1至PowerShell 7的，并使用 oh my posh 对终端进行美化的折腾过程。
tags: 
    - Windows
    - 美化
top_img: /img/Windows的PowerShell美化教程/cover.png
cover: /img/Windows的PowerShell美化教程/cover.png
---

# 1. 前言

记录在一次Windows中升级PowerShell 5.1至PowerShell 7的，并使用 oh my posh 对终端进行美化的折腾过程。

# 2. 升级PowerShell

参考[在 Windows 上安装 PowerShell - PowerShell | Microsoft Learn](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4)，在PowerShell中直接运行如下命令安装最新版本

```powershell
winget install --id Microsoft.Powershell --source winget
```

安装完成后需要修改默认终端，随便打开一个终端，点击设置，然后将默认启动改为PowerShell 7，如图：

<img src="/img/Windows的PowerShell美化教程/image-20241123193847041.png" alt="image-20241123193958156" style="zoom:50%;" />

# 3. 使用 oh my posh 进行美化

在PowerShell中进行安装：

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
```

重启终端，输入`oh-my-posh`，若打印如下内容，则说明安装成功：

<img src="/img/Windows的PowerShell美化教程/image-20241123194432500.png" alt="image-20241123194432500" style="zoom:50%;" />

更改PowerShell的安全策略：以管理员身份运行，然后输入如下内容：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

打开配置文件

```powershell
notepad $PROFILE
```

如果提示该文件不存在，可以使用如下命令创建

```powershell
New-Item -Path $PROFILE -Type File -Force
```

在打开的配置文件添加以下代码并保存

```
oh-my-posh init pwsh | Invoke-Expression
```

重新打开终端会加载默认主题。

在[Nerd Fonts 官网](https://www.nerdfonts.com/font-downloads)下载一款自己喜欢的字体，这里以`Cousine Nerd Font`为例，解压压缩包后，右键安装所有字体

<img src="/img/Windows的PowerShell美化教程/image-20241123194822118.png" alt="image-20241123194822118" style="zoom:50%;" />

然后在外观中配置刚刚下载的字体，如图

<img src="/img/Windows的PowerShell美化教程/image-20241123202608377.png" alt="image-20241123202608377" style="zoom:50%;" />

显示可用的主题：

```powershell
Get-PoshThemes
```

记住好自己要切换的主题名称，然后`ctrl+左键`打开主题文件夹，如图

<img src="/img/Windows的PowerShell美化教程/image-20241123202959183.png" alt="image-20241123202959183" style="zoom:50%;" />

打开配置文件：

```powershell
notepad $PROFILE 
```

配置主题路径，以`wholespace`主题为例：

```
oh-my-posh init pwsh  --config "Senv:POSH_THEMES_PATH/wholespace.omp.json" | Invoke-Expression
```

重载主题，命令如下

```powershell
. $PROFILE
```

当然，还可以在终端外观设置中设置背景和透明度。

# 4. Vsocde中的乱码配置
使用的时候发现在VScode中会乱码，安装下面步骤更改终端字体即可：
1. 打开设置
2. 搜索`Integrated:Font Family` 
3. 将字体修改为上面设置的字体

# 5. 参考资料
<https://mp.weixin.qq.com/s/KWlN5s_rdLn8oO_iL2vbgg>











 

