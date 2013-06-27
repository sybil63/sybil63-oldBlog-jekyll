---
published: true
layout: post
title: 使用GoDaddy和DnsPod配置github blog域名
date: 2013-04-16 15:17
comments: false
categories: [github, blog]
---

## 配置DnsPod解析域名
 * 原因: GoDaddy默认的DNS解析比较慢
 * 方法: 登陆DnsPod，配置域名的CNAME

 ![nexus-repo](/images/dnsPod4Blog)

## 配置域名
 * 登陆GoDaddy的域名管理页面，配置Dns。GoDaddy的配置会在1~2小时后才生效

 ![nexus-repo](/images/goDaddy4Blog)

 * 设置好的效果:

 ![nexus-repo](/images/goDaddy4Blog2)

