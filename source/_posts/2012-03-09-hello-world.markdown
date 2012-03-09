---
published: true
layout: post
title: "Hello World"
date: 2012-03-09 00:33
comments: false
categories: ['test']
---

## 测试img插件
{% codeblock %}
{% img http://placekitten.com/890/280 %}
{% img left http://placekitten.com/320/250 Place Kitten #2 %}
{% img right http://placekitten.com/300/500 150 250 Place Kitten #3 %}
{% img right http://placekitten.com/300/500 150 250 'Place Kitten #4' 'An image of a very cute kitten' %}
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
{% endcodeblock %}

{% img http://placekitten.com/890/280 %}
{% img left http://placekitten.com/320/250 Place Kitten #2 %}
{% img right http://placekitten.com/300/500 150 250 Place Kitten #3 %}
{% img right http://placekitten.com/300/500 150 250 'Place Kitten #4' 'An image of a very cute kitten' %}
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world

## 测试codeblock
{% codeblock %}
{% codeblock Javascript Array Syntax lang:js http://github.com  github %}
var arr1 = new Array(arrayLength);
var arr2 = new Array(element0, element1, ..., elementN);
{% endcodeblock %}
{% endcodeblock %}

{% codeblock Javascript Array Syntax lang:js http://github.com  github %}
var arr1 = new Array(arrayLength);
var arr2 = new Array(element0, element1, ..., elementN);
{% endcodeblock %}
