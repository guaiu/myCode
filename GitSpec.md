# Git 规范

## 操作规范

1. 现在本地中工作区中提交 (`git commit`) 修改或者要提交的内容。
2. 获取远端 (`git pull`) 服务器的最新内容。
3. 如果有冲突，先合并处理冲突。
4. 如果没有冲突，提交本地内容到远端 (`git push`) 。

> 注: `Excel`、`Word`等相关文档无法通过 `Git` 相关工具自动合并。

## 操作流程图

![GitSpec.png](res/designer/GitSpec.png)

## 消息提交

Git 提交消息模板:

```plain
[version]
type(scoop):subject
blank line
body
Header
footer
```

样例如下:

```plain
[1.0.0]
fix(mq):修复Rabbitmq通讯以及数据校验的bug

1. 修复 MQ 消息传递丢失的bug
2. 修复电池数据读取错误的bug

关闭 错误13、错误11
```

###  Version

该节点是版本，一般为 **大版本.小版本.修订版本**。版本制定由产品决定。

### Type

提交类型,该字段是必填的。如下所示：

* feat: 新功能
* fix: 修复bug
* docs: 只有文档改变
* style: 并没有影响代码的意义(空格，去掉分号，格式的修改等)
* refactor: 代码的修改并没有修改bug，也没有添加新功能
* perf: 代码的修改提高的性能
* test: 添加测试
* chore: 构建过程或构建工具的改变(并没有生产环境代码的改变)

### Scoop

影响范围，该字段是可选的。简要说明主要影响的功能范围。

### Subject

提交消息主题，该字段是必填的。主要说明修改的内容是什么。

### Body

消息主体，该字段是可选的。如果需要详细说明，那么按照条目详细说明。

### Footer

消息标注，该字段是可选的。如果关闭某个wiki、issue或者错误的时候使用。

> 注：注意消息模板中的空行。

## 建议

推荐使用GUI工具 `SourceTree` 等相关工具。

> 注:各种工具请参考 **引用2**。

## 引用

1. [Git](https://git-scm.com/)
2. [Git GUI Clients](https://git-scm.com/downloads/guis)
3. [git基本操作，一篇文章就够了！](https://juejin.im/post/5ae072906fb9a07a9e4ce596)