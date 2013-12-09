# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.12
# Email : muyanru345@163.com
###################################################################

import sublime, sublime_plugin
import socket

class MayaCommand(sublime_plugin.TextCommand):  
    def run(self, args): 
        view = self.view 
        pythonCode = view.substr(view.sel()[0])
        if pythonCode:
            sendCode(pythonCode)
        else:
            allRegion = sublime.Region(0, view.size())
            sendCode(view.substr(allRegion))

def sendCode(pythonCode):
    tmpPort = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', tmpPort))
    except:
        sublime.message_dialog("Maya CommandPort does\'t connect!")
        return
    s.send(pythonCode)
    s.close()