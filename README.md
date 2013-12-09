sublime-maya
============
仅测试了sublime-text 2 window版本，sublime-text 3没测试过，其他平台也没测试过

a plugin for sublime-text 2, you can send the selected code (or all) to maya

## 安装
将sublime-maya.py文件放置于sublime的User文件夹下，比如
`C:\Users\muyanru\AppData\Roaming\Sublime Text 2\Packages\User`

（可通过sublime执行菜单 Preferences -> Browse Packages...跳转到目录）

然后修改User文件夹下 `Default (Windows).sublime-keymap` 文件。
添加如下内容

<pre>
{ "keys": ["ctrl+shift+x"], "command": "maya" }
</pre>
保存退出

# 使用
###1. 在maya窗口中


如果你的代码是python代码，执行如下python脚本
<pre>
import maya.cmds as mc
mc.commandPort(sourceType = 'python', name = '127.0.0.1:8888' )
</pre>
如果你的代码是mel，执行如下python脚本
<pre>
import maya.cmds as mc
mc.commandPort(sourceType = 'mel', name = '127.0.0.1:8888' )
</pre>
###2. 在sublime窗口中
在当前窗口中，选中若干行代码（
如果没有选中任何代码，则整个文件代码都被发送到maya运行）

#### 快捷键方式
按下快捷键“ctrl+shift+x”，即可将代码发送到执行了第一步操作的maya窗口中运行。


#### 命令行方式
若快捷键不好用（跟别的快捷键冲突等情况），请执行菜单 View -> Show Console
或者快捷键 ctrl + ` 调出python命令行，输入

<pre>
view.run_command('maya')
</pre>
回车运行即可