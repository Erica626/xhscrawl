## Table of content
- [简介](#简介)
- [性能](#性能)
- [如何运行demo](#如何运行demo)
- [作者提供的服务](#作者提供的服务)
  - [提供web api的源码服务]
- [作者联系方式、寻求帮助、合作](#作者联系方式--寻求帮助--合作)
- 
  ![Static Badge](https://img.shields.io/badge/GitHub-blue?logo=GitHub&labelColor=black)
  ![Static Badge](https://img.shields.io/badge/author-3.7/3.8-blue?logo=Python&label=python&labelColor=black)
  ![Static Badge](https://img.shields.io/badge/Node.js-v18.16.1-blue?logo=Node.js&labelColor=black)

## 声明
**作者声明：没有在任何平台进行代码售卖，请谨慎鉴别，上当受骗作者一律不负责**
**本项目仅供学习交流，严禁用于任何商业和非法用途，非本人使用而产生的纠纷与一切后果均与本人无关。**
## 简介
本项项目是针对web端。小红书web的api都有加密，主要就是x-s。本项目是用python逆向小红书x-s。
## 性能
1. 本项目采用js计算，不使用playwright/selenium调用浏览器内核的方式。因为起浏览器太耗资源了，如果有高并发、多账号需求的生产环境很难容忍。
2. 整个请求(包括本地计算xs、发起请求、小红书处理请求、返回数据)，速度非常块且稳定
## 如何运行demo
找到[demo/xhs.py] ,将自己需要的参数、cookie进行手动替换运行即可
- python环境
  - execjs包(可能编辑器会找不到这个包，真正名字叫PyExecJS)
  - 等其他import依赖
- node js环境，需要支持ES13的 node js版本，也就是node js版本要晚于June 2022
## 作者提供的服务
### 提供逆向api的源码
- **以下api均为web端api**
- 代码以最简单朴素的方式编写。
- 有详细的运行文档，接口文档，每一个请求参数都有说明。
- 作者会一直跟到在本地跑起来为止，因为代码原因跑不起来直接退款，都是做技术的，不玩那些虚。
由于出售的是源码，无法在线测试。介意勿扰

| 接口列表        | 
|-------------|
| [发送评论]      |
| [获取笔记详情]    |
| [笔记搜索]      |
| [用户搜索]      |
| [获取笔记评论]    |
| [收藏笔记]      |
| [给笔记点赞]     |
| [获取用户所有笔记]  |
| [获取用户详情]    |
| [获取关键词搜索笔记列表] |
| [homefeed频道推荐] |
| [小红书热点]     |
| [消息-评论和@列表] |
| [消息-赞和收藏]   |
| [消息-新增关注列表] |
| [未读通知数]     |
| [关注用户]      |
| [若没有你需要的接口,联系作者有偿开]          |

## 价格
### 全部接口打包价格：3500

## 作者联系方式 || 寻求帮助 || 合作
### QQ: 1411833685
### GMAIL: adaswrqwr234@gmail.com
