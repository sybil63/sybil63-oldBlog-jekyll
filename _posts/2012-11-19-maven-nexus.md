---
published: true
layout: post
title: 搭建maven repo私服
date: 2012-11-19
comments: false
categories: [maven]
---
# 关于Maven
最近几天开始看hadoop的代码，hadoop使用maven构建项目，所以顺便看了下maven。感觉这个东西对于开源的项目来说，确实是很有意义的。

开源项目一个很大的问题是规范，每个人都有自己的写法，导致项目的结构各不相同。maven直接强制的规定了项目的结构，流程，依赖，使得多个项目的结构都统一了，就像maven文档说的，看明白了一个项目，对于其他项目就不需要熟悉新的项目规范了。

不过对于已经有自己规范的公司来说，意义就没有这么大了。习惯了贵司的ant结构后，感觉maven好难上手。
如果是对于对java的项目规范还没有积累的公司，那么maven的也是非常有意义的。省去了项目规范的制定，并且可以无缝的进行开源项目的研究开发。

maven的另一个好处是，依赖的管理。这个问题对于贵司来说用ant+ivy解决了。

# 关于nexus
## 为什么想用nexus呢
各个开源的repo服务器，提供了大量的开源代码，非常的方便。
以往在贵司更新一个开源的jar包，比如jetty1.6，需要自己去下载代码，然后上传到ivy的服务器上，然后再自己修改一些ivy依赖。好吧，不方便的是没有开源repo的镜像服务器。需要啥还要自己手工去下载上传，非常恶心。

在编译hadoop的时候我遇到一个问题，直接用maven下载公用服务器的jar包非常慢，非常令人崩溃，当然第一次下载完后有本地的缓存就很快了。不过很快的我又遇到另一个问题，我有好几台电脑都需要做下载jar的事情，当然其实最方便的是直接rsync maven的本地缓存，不过我感觉这个稍稍不够优雅，最后发觉可以用nexus搭建自己的repo私服，完美的解决了我的问题（可是这真的是我目前要处理的问题么？还是我在D疼的折腾而已？）。

搭建nexus的私服非常的方便，基本直接下载代码，然后运行就行了。nexus内置jetty，所以也可以不用tomcat等服务器了。
不得不表示nexus的用户体验非常好，非常容易上手

## nexus搭建
 * 下载源码 
 
 [nexus源码](http://www.sonatype.org/nexus/)

 * 解压源码

        tar -zxvf nexus-2.2-01-bundle.tar.gz 

 * 运行nexus

        cd nexus-2.2-01
        ./bin/nexus start

 * 访问nexus

        http://localhost:8081/nexus/

## nexus配置
 * nexus默认管理员账户

        帐号：admin
        密码：admin123

 * nexus里可以配置3种类型的仓库，分别是proxy、hosted、group

        * proxy是远程仓库的代理。比如说在nexus中配置了一个central repository的proxy，当用户向这个proxy请求一个artifact，这个proxy就会先在本地查找，如果找不到的话，就会从远程仓库下载，然后返回给用户，可以理解为公用repo服务器的一个镜像。

        * hosted是宿主仓库，用户可以把自己的一些构件，deploy到hosted中，也可以手工上传构件到hosted里。相当于自己公司项目的代码库。

        * group是仓库组，在maven里没有这个概念，是nexus特有的，实际上group并不是实际的仓库，而是一个聚合多个仓库的虚拟仓库。目的是将上述多个仓库聚合，对用户暴露统一的地址，这样用户就不需要在pom中配置多个地址，只要统一配置group的地址就可以了

         nexus装好之后，已经初始化定义了一些repository，我们熟悉之后，就可以自行删除、新增、编辑

 * 访问nexus后登录为管理员就能进行repo的相关操作

 ![nexus-repo](/images/nexus.png)

 * proxy仓库的配置

 ![nexus-proxy](/images/nexus-proxy.jpeg)

 需要注意的是，把 **Download Remote Indexes** 选为 **True**，这样就可以使用私服进行jar的搜索

 * group仓库的配置

 ![nexus-group](/images/nexus-group.jpeg)

 右边的仓库表示聚合的仓库，所有右边的仓库都可以通过group仓库的url访问。

## 使用nexus私服
编辑maven用户配置文件

    ~/.m2/settings.xml

添加相应的mirror配置
{% highlight xml %}
<?xml version="1.0"?>
<settings>
    <mirrors>  
        <mirror>  
            <id>nexus-central</id>  
            <name>internal nexus repository</name>  
            <url>http://localhost:8081/nexus/content/repositories/public/</url>
            <mirrorOf>*</mirrorOf>  
        </mirror>  
    </mirrors>
</settings>
{% endhighlight %}

这个配置表示把所有的源请求都转发到http://localhost:8081/nexus/content/repositories/public/上。这也是之前配置的group仓库路径

配置好之后在本地运行mvn命令就会把相应的repo下载请求转发到私服上了。
