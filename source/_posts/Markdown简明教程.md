---
title: Markdown简明教程
date: 2024-10-26 00:10:09
tags: 
    - 日常总结
top_img: /img/Markdown简明教程/cover.png
cover: /img/Markdown简明教程/cover.png
---

Markdown已经渗透到我的方方面面，闲来无事，总结一下。😀😀

Markdown是一种轻量级标记语言，排版语法简洁，让人们更多地关注内容本身而非排版。它使用易读易写的纯文本格式编写文档，可与HTML混编，可导出 HTML、PDF 以及本身的 .md 格式的文件。因简洁、高效、易读、易写，Markdown被大量使用，如Github、Wikipedia、简书等。

----

# 1. 速查表

|元素       |Markdown 语法  |
|---        |---           |
|标题（Heading）|# H1       |
|粗体（Bold）   |\*\*bold text\*\*|
|斜体（Italic）|    \*italicized text\*|
|引用块（Blockquote）|   > blockquote|
|有序列表（Ordered List） |1. First item|
|无序列表（Unordered List）   |- First item|
|代码（Code）   |\`code\`|
|分隔线（Horizontal Rule）   |---|
|链接（Link）   |\[title\]\(https://www.example.com\)|
|图片（Image）  |\!\[alt text\]\(image.jpg)|
|表格（Table）  |\|标题\|标题\|<br>\|---\|---\|<br>\|内容\|内容\||
|代码块（Fenced Code Block）|    \```<br>{<br>"firstName": "John"<br>"lastName": "Smith",<br>"age": 25<br>}<br>\```|
|删除线（Strikethrough） |\~\~The world is flat.~~|
|任务列表（Task List）    |- [x] Write the press release<br>- [ ] Update the website<br>- [ ] Contact the media|

# 2. 具体语法

## 2.1. 标题语法

在单词或短语前面添加井号 (#) 。# 的数量代表了标题的级别。例如，添加三个 # 表示创建一个三级标题 (\<h3>) 

```markdown
### My Header
```

考虑到兼容问题，#和标题直接要有空格

## 2.2. 段落语法
使用空白行将一行或多行文本进行分隔。不要用空格（spaces）或制表符（ tabs）缩进段落。

## 2.3. 换行语法
+   可以在一行的末尾添加两个或多个空格，然后按回车键，即可创建一个换行(\<br>)。  几乎每个 Markdown 应用程序都支持两个或多个空格进行换行，称为结尾空格(trailing whitespace) 的方式。

+   几乎每个 Markdown 应用程序都支持另一种换行方式：HTML 的 \<br> 标签。

    ```markdown
    hello world<br>
    hello world
    ```

## 2.4. 强调语法

### 2.4.1 粗体
在单词或短语的前后各添加两个星号（asterisks）

```markdown
**加粗**
```

### 2.4.2 斜体
在单词或短语前后添加一个星号（asterisk）

```markdown
*斜体*
```

### 2.4.3 粗体和斜体
要同时使用用粗体和斜体时，在单词或短语的前后各添加三个星号。

```markdown
***加粗和斜体***
```

## 2.5. 引用语法
要创建块引用，请在段落前添加一个`>`符号。

```markdown
> 引用块
```

如果引用想包含多个段落，要在段落之间的空白行添加一个`>`符号。

```markdown
> 第一段
>
> 第二段
```

块引用可以嵌套。在要嵌套的段落前添加一个`>>`符号。  

```markdown
> 引用块
>> 引用块里面的引用块
```

## 2.6. 列表语法
有序列表用数字

```markdown
1. 第一点
2. 第二点
```

无序列表用`+ , - ,*`，一般用`-`

```markdown
- 内容
- 内容
```

## 2.7. 代码语法
行内代码，将将目标包裹在反引号(`)中。

```markdown
你好，`code`行内代码
```

如果单词或短语中包含一个或多个反引号，则可以通过将单词或短语包裹在双反引号(``)中.   

```markdown
你好，``code``行内代码
```

代码块使用三个反引号(```)，要添加语法突出显示，可以代码块之前的反引号旁边指定一种语言。

````markdown
```python
print("hello world")
```
````

## 2.8. 分割线语法
要创建分隔线，在单独一行上使用三个或多个破折号 (---) ，并且不能包含其他内容。为了兼容性，分隔线的前后都要添加空白行。

```markdown
内容1

---

内容2
```

## 2.9. 链接语法
超链接Markdown语法代码：

```markdown
[超链接显示名](超链接地址 "超链接title")
```

使用尖括号可以很方便地把URL或者email地址变成可点击的链接。

```markdown
<https://markdown.com.cn>
```

## 2.10. 图片语法
图片语法比链接语法多一个感叹号 (!)，然后在方括号增加替代文本，图片链接放在圆括号里，括号里的链接后可以增加一个可选的图片标题文本。

```markdown
![图片alt](图片链接 "图片title")
```

## 2.11. 表格
使用三个或多个连字符（---）创建每列的标题，并使用管道（|）分隔每列。您可以选择在表的任一端添加管道。 

```markdown
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```

您可以通过在标题行中的连字符的左侧，右侧或两侧添加冒号（:），将列中的文本对齐到左侧，右侧或中心。中间对齐示例

```
| Syntax      | Description |
| :---------: | :---------: |
| Header      | Title       |
| Paragraph   | Text        |
```

## 2.12. 删除线
在单词前后使用两个波浪号`~~`。

```
~~删除~~
```

## 2.13. 使用 Emoji 表情
有两种方法可以将表情符号添加到Markdown文件中：

+   将表情符号复制并粘贴到Markdown格式的文本中
+   键入emoji shortcodes。  

在大多数情况下，可以简单地从[Emojipedia](https://emojipedia.org/)等来源复制表情符号并将其粘贴到文档中。 还可以通过键入表情符号短代码来插入表情符号。这些以冒号开头和结尾，并包含表情符号的名称。
[表情简码表](https://gist.github.com/liangbm3/cefcf740d30f484c8f99b9581b5d213a)

## 2.14 任务列表

要创建任务列表，需要在任务列表项之前添加破折号`-`和方括号`[ ]`，并在`[ ]`前面加上空格。要选择一个复选框，请在方括号`[]`里面添加 `x`即可 。

```markdown
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

# 3. 参考资料

[Markdown 教程](https://markdown.com.cn/)