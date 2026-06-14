# 璐璐手作小屋 🧵

> 一个热爱手工的女大学生的个人手作博客网站

[![Static Site](https://img.shields.io/badge/type-static--site-brightgreen)](https://github.com/hintcnuie/AI-Python-Study-Course)
[![HTML5](https://img.shields.io/badge/HTML-5-orange)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS-3-blue)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

## 📖 项目简介

**璐璐手作小屋** 是一个纯静态前端网站，作为大学课程独立网站制作作业完成。网站以"手工制作"为主题，展示布娃娃、木质相框等手工作品，同时包含个人故事、手作日记、图片画廊、留言板等多个频道，致力于打造一个温暖、治愈的个人手作分享空间。

## 🎯 网站主题

面向浏览者展示手工制作的魅力与乐趣——布娃娃的温柔陪伴、木质相框的质朴美学，传递"用心手作，温暖生活"的理念。主题积极向上，契合当代大学生的价值观与审美追求。

## ✨ 主要功能

| 功能 | 说明 |
|------|------|
| 🔔 **滚动公告栏** | 顶部滚动文字横幅，展示最新动态和温馨提示 |
| 🧭 **响应式导航栏** | 8 个频道导航，支持移动端汉堡菜单切换 |
| 🧸 **作品展示** | 布娃娃 & 木质相框两个产品频道，各含 3 个详情页 |
| 🖼️ **图片画廊** | 按分类筛选的手工作品画廊（娃娃/相框） |
| 📝 **手作日记** | 3 篇图文并茂的手作生活记录 |
| 💬 **双向交流** | 留言板 + 联系方式，支持表单提交（localStorage 存储） |
| 🎵 **背景音乐** | Web Audio API 生成的 C 大调轻音乐，三角波音色温暖悦耳 |
| 🔗 **友情链接** | 友链展示 + 申请表单 + 推荐提交 |
| ⬆️ **回到顶部** | 滚动超过 400px 自动显示，平滑滚动 |
| 📱 **多端适配** | 响应式布局，兼容桌面端、平板和手机 |

## 📂 网站结构

```
weiwei_website/
├── index.html                 # 首页
├── about/                     # 关于频道
│   ├── index.html             #   关于主页
│   ├── story.html             #   我的故事
│   └── hobby.html             #   兴趣爱好
├── dolls/                     # 布娃娃频道
│   ├── index.html             #   娃娃列表
│   ├── detail1.html           #   娃娃详情1
│   ├── detail2.html           #   娃娃详情2
│   └── detail3.html           #   娃娃详情3
├── frames/                    # 木质相框频道
│   ├── index.html             #   相框列表
│   ├── detail1.html           #   相框详情1
│   ├── detail2.html           #   相框详情2
│   └── detail3.html           #   相框详情3
├── gallery/                   # 画廊频道
│   ├── index.html             #   画廊主页
│   ├── doll.html              #   娃娃画廊
│   └── frame.html             #   相框画廊
├── diary/                     # 手作日记频道
│   ├── index.html             #   日记列表
│   ├── post1.html             #   日记文章1
│   ├── post2.html             #   日记文章2
│   └── post3.html             #   日记文章3
├── guestbook/                 # 留言频道
│   ├── index.html             #   留言板
│   ├── contact.html           #   联系方式
│   └── messages.html          #   留言列表
├── links/                     # 友情链接频道
│   ├── index.html             #   友链列表
│   ├── apply.html             #   申请友链
│   └── recommend.html         #   推荐网站
├── css/
│   └── style.css              # 全局样式表（~1265行）
├── js/
│   └── main.js                # 全局脚本（~445行）
├── images/
│   └── works/                 # 手工作品图片
├── music/
│   └── README.txt             # 背景音乐说明
├── screenshots/               # 全站页面截图（25张）
├── 建站总结报告.html           # 课程报告（HTML版）
├── 大学生课程独立网站制作要求.md  # 课程作业规范
└── CLAUDE.md                  # AI 辅助开发说明
```

## 🛠️ 技术栈

| 层面 | 技术选型 |
|------|----------|
| **结构** | HTML5 语义化标签，DIV+CSS 布局 |
| **样式** | 纯 CSS3，CSS 自定义属性（变量），Flexbox + Grid |
| **交互** | 原生 JavaScript ES6，无第三方依赖 |
| **音频** | Web Audio API（程序化生成音乐，无需音频文件） |
| **存储** | localStorage（留言板数据持久化） |
| **图标** | Emoji + SVG favicon |
| **构建** | 无——纯静态文件，零构建工具 |

### 设计系统

- **配色方案**：粉暖米色系 — 主色 `#E8917E`（暖粉），辅色 `#8BA888`（灰绿），背景 `#FFFBF7`（暖白）
- **响应式断点**：768px（平板）/ 480px（手机）
- **字体**：系统默认中文字体栈，标题使用衬线字体
- **动效**：CSS transition/animation + 少量 JS 动画

## 🚀 快速开始

### 本地预览

```bash
# 方式一：直接用浏览器打开
open index.html

# 方式二：使用任意静态服务器
python3 -m http.server 8080
# 然后访问 http://localhost:8080
```

### JS 语法检查

```bash
node --check js/main.js
```

## 📋 课程作业完成情况

本项目严格按照《大学生课程独立网站制作规范》完成：

- ✅ 网站主题积极向上，清晰明确
- ✅ 原创 Logo 设计，贴合主题
- ✅ 内容充实饱满，兼具艺术性、趣味性与知识性
- ✅ 8 个频道栏目，每个频道 ≥ 3 个页面，总计 26 个页面
- ✅ 配备导航栏、友情链接、版权信息、联系方式、滚动公告栏、留言板
- ✅ 兼容主流浏览器（Chrome / Firefox / Safari / Edge）
- ✅ 页面美观大方，全站风格统一
- ✅ DIV+CSS 布局，结构合理
- ✅ 目录层级 ≤ 3 层，文件命名仅用小写英文
- ✅ 全站使用相对链接，无跳转错误
- ✅ 无恶意代码，运行流畅稳定
- ✅ 已发布至 GitHub Pages / 托管平台（加分项）
- ✅ 撰写《建站总结报告》并附全站截图

## 📄 许可证

本项目为大学课程作业，仅供学习交流使用。

---

<p align="center">
  <i>🧵 用心手作，温暖生活 🧵</i>
</p>
