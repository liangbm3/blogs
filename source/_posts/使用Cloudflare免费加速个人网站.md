---
title: 使用Cloudflare免费加速个人网站
date: 2024-10-12 16:20:59
tags: 博客搭建,教程
description: 使用Cloudflare的CDN服务，通过其免费的free计划，来加速博客网站的访问速度。
top_img: /img/使用Cloudflare免费加速个人网站/top_img.jpg
cover: /img/使用Cloudflare免费加速个人网站/top_img.jpg
---

## 前言
在搭建博客的过程中，发现网站访问的速度有些慢，便参考了网上的许多教程和博客，并成功使用了Cloudflare 来加速我的博客网站，因此特地写了一篇blog来总结一下。

## 前置知识

### Cloudflare

Cloudflare（Cloudflare, Inc.）是一家总部位于旧金山的美国跨国科技企业，以向客户提供基于反向代理的内容分发网络（Content Delivery Network, CDN）及分布式域名解析服务（Distributed Domain Name Server）为主要业务。Cloudflare 已经成为互联网上运行的最大网络之一。

Cloudflare的优势有：
+ DDoS保护：过滤恶意流量，保护网站免受分布式拒绝服务的攻击。
+ 内容分发网络（CDN）：帮助加速网站内容在全球范围内的传输。
+ SSL/TLS加密安全保护：帮助保护网站和访问者的安全。
+ 提升网页访问速度：通过压缩代码、压缩资源和缓存内容来优化网站性能。
+ 详细流量分析和报告：包括请求、带宽使用和安全事件等信息。
+ 简单直观的界面：易于使用的管理网站设置和配置。
+ 免费和收费计划：可以是获得CDN、DDoS保护和安全等优势的经济实惠方式。
+ 更重要的是有中文的控制面板🫣

### CDN是什么

我们主要是使用Cloudflare的CDN服务进行加速，那么CDN到底是什么呢？

CDN (Content Delivery Network或Content Distribution Network)是一个互连服务器网络，可加快数据密集型应用程序的网页加载速度。CDN 可以表示内容分发网络或内容分配网络。当用户访问某个网站时，来自该网站服务器的数据必须通过互联网传输到用户的计算机。如果用户距离该服务器较远，则加载大文件（例如视频或网站图像）将需要很长时间。相反，如果网站内容存储在距离用户较近的 CDN 服务器上，就可以更快到达他们的计算机。

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012170948597.png" alt="image-20241012170948597" style="zoom: 33%;" />

## 操作流程

### 配置服务

首先你需要一个私有域名，没有可先去注册：
+ [阿里云](https://wanwang.aliyun.com/domain/)
+ [腾讯云](https://buy.cloud.tencent.com/domain)
+ [华为云](https://www.huaweicloud.com/product/domain.html)

然后登录[Cloudflare](https://dash.cloudflare.com/sign-up)，没有账号先注册账号。进入的面板如图：

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012171108680.png" alt="image-20241012171108680" style="zoom: 50%;" />

我们输入我们的私有域名，点击继续，然后选择免费的计划

>   注意：不要填带有www.域名

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012171120482.png" alt="image-20241012171120482" style="zoom: 50%;" />

点击继续，我们可以看到如下界面

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012171133590.png" alt="image-20241012171133590" style="zoom: 50%;" />

### 3.2 按照下方的快速入门指南进行配置

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012172732085.png" alt="image-20241012172732085" style="zoom:50%;" />

一律保存即可。

### 更改DNS服务器

先在Cloudflare中找到给我们分配的DNS服务器，如图

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012171651888.png" alt="image-20241012171651888" style="zoom: 50%;" />

接下来需要到我们的服务器商那里更换我们域名的DNS服务器，以阿里云为例，进入[域名控制台 (aliyun.com)](https://dc.console.aliyun.com/#/domain-list/all)，找到我们需要加速的域名

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012171932162.png" alt="image-20241012171932162" style="zoom:50%;" />

点击管理

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012172054672.png" alt="image-20241012173653312" style="zoom:50%;" />

在DNS修改中，输入刚才复制的域名

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012172444890.png" alt="image-20241012172444890" style="zoom:50%;" />

等待一段时间后，会收到Cloudflare发来的邮件

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012172903024.png" alt="image-20241012172903024" style="zoom:50%;" />

>   这里每个人的等待时间不一样，请耐心等待

成功后，界面变成如图所示

<img src="/img/使用Cloudflare免费加速个人网站/image-20241012173124328.png" alt="image-20241012173124328" style="zoom:50%;" />

到此我们已经可以使用Cloudflare进行CDN加速了，我们还可以进行其他配置。

### 其他配置

1.   将SSL/TLS设置成完全（严格），增加网页安全性。

     <img src="/img/使用Cloudflare免费加速个人网站/image-20241012173653312.png" alt="image-20241012173653312" style="zoom:50%;" />

2.   启用 Always Online 后，即使你源服务器一时瘫痪，也会显示 Cloudflare 创建好的网站副本。这样就可以始终向访问者提供信息。

     <img src="/img/使用Cloudflare免费加速个人网站/image-20241012173855897.png" alt="image-20241012173653312" style="zoom:50%;" />

## 参考资料

[Cloudflare设置流程 免费CDN加速你的网站【2024年最新】](https://for-tiger.com/cloudflare-setup-tutorial-for-cdn-acceleration)