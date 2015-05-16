# Welcome to Marxico

H.264视频编码基础知识点
=====================
2015-05-14

## 码率控制 (RDO: Rate Distortion Optimization)
- 受到缓冲区，宽带的限制，编码码率不能无限制的增长，因此需要通过码率控制来将编码码流控制在目标码率范围内。
- 码率控制的主要环节： DCT变换，量化，缓冲区调整，分层编码(可分级编码和精细编码)，网络状况反馈调节编码。
- 一般通过调整量化参数QP的手段来控制码率：
    1. frame level
    2. slice level
    3. Macroblock level
- 码率控制考虑的问题：
    1. 防止码流有较大的波动，导致缓冲区溢出
    2. 同时保持缓冲区尽可能的充满，然图片质量尽可能的好而且稳定
- CBR (Constant Bit Rate), 比特率稳定，但图片质量变化大
- VBR (Variable Bit Rate) , 比特率波动大，但图片质量稳定
- 码率控制算法
    1. 码率分配
    2. 码率控制
- 码率控制属于非标准技术, 编码端有, 解码端没有

## Introducing Markdown

> Markdown is a plain text formatting syntax designed to be converted to HTML. Markdown is popularly used as format for readme files, ... or in text editors for the quick creation of rich text documents.  - [Wikipedia](http://en.wikipedia.org/wiki/Markdown)

As showed in this manual, it uses hash(#) to identify headings, emphasizes some text to be **bold** or *italic*. You can insert a [link](http://www.example.com) , or a footnote[^demo]. Serveral advanced syntax are listed below, please press `Ctrl + /` to view Markdown cheatsheet.

### Code block
``` python
@requires_authorization
def somefunc(param1='', param2=0):
    '''A docstring'''
    if param1 > param2: # interesting
        print 'Greater'
    return (param2 - param1 + 1) or None
class SomeClass:
    pass
>>> message = '''interpreter
... prompt'''
```

### LaTeX expression
$$	x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

### Table
| Item      |    Value | Qty  |
| :-------- | --------:| :--: |
| Computer  | 1600 USD |  5   |
| Phone     |   12 USD |  12  |
| Pipe      |    1 USD | 234  |


> **Note:** You can find more information:

> - about **Sequence diagrams** syntax [here][2],
> - about **Flow charts** syntax [here][3].

### Checkbox
You can use `- [ ]` and `- [x]` to create checkboxes, for example:

- [x] Item1
- [ ] Item2
- [ ] Item3

> **Note:** Currently it is only partially supported. You can't toggle checkboxes in Evernote. You can only modify the Markdown in Marxico to do that. Next version will fix this.  


### Dancing with Evernote

#### Notebook & Tags
**Marxico** add `@(Notebook)[tag1|tag2|tag3]` syntax to select notebook and set tags for the note. After typing `@(`, the notebook list would appear, please select one from it.  

#### Title
**Marxico** would adopt the first heading encountered as the note title. For example, in this manual the first line `Welcome to Marxico` is the title.

#### Quick Editing
Note saved by **Marxico** in Evernote would have a red ribbon button on the top-right corner. Click it and it would bring you back to **Marxico** to edit the note. 

> **Note:** Currently **Marxico** is unable to detect and merge any modifications in Evernote by user. Please go back to **Marxico** to edit.

#### Data Synchronization
While saving rich HTML content in Evernote, **Marxico** puts the Markdown text in a hidden area of the note, which makes it possible to get the original text in **Marxico** and edit it again. This is a really brilliant design because:

- it is beyond just one-way exporting HTML which other services do;
- and it avoids privacy and security problems caused by storing content in a intermediate server. 

> **Privacy Statement: All of your notes data are saved in Evernote. Marxico doesn't save any of them.** 

#### Offline Storage
**Marxico** stores your unsynchronized content locally in browser storage, so no worries about network and broswer crash. It also keeps the recent file list you've edited in `Document Management(Ctrl + O)`.

> **Note:** Although browser storage is reliable in the most time, Evernote is born to do that. So please sync the document regularly while writing.

## About Pro
**Marixo** offers a free trial of 10 days. After that, you need to [purchase](http://marxi.co/purchase.html) the Pro service. Otherwise, you would not be able to sync new notes. Previous notes can be edited and synced all the time.

## Credits
**Marxico** was first built upon [Dillinger][4], and the newest version is almost based on the awesome [StackEdit][5]. Acknowledgments to them and other incredible open source projects!

## Feedback & Bug Report
- Twitter: [@gock2][6]
- Email: <hustgock@gmail.com>

----------
Thank you for reading this manual. Now please press `Ctrl + M` and click `Link with Evernote`. Enjoy your **Marxico** journey!


[^demo]: This is a demo footnote. Read the [MultiMarkdown Syntax Guide](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#footnotes) to learn more. Note that Evernote disables ID attributes in its notes , so `footnote` and `TOC` are not actually working. 

  [1]: https://chrome.google.com/webstore/detail/kidnkfckhbdkfgbicccmdggmpgogehop
  [2]: http://bramp.github.io/js-sequence-diagrams/
  [3]: http://adrai.github.io/flowchart.js/
  [4]: http://dillinger.io
  [5]: http://stackedit.io
  [6]: https://twitter.com/gock2



