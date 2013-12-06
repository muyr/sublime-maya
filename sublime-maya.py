import socket
import sublime, sublime_plugin

class MayaSelectionCommand(sublime_plugin.TextCommand):  
    def run(self, args): 
        view = self.view 
        pythonCode = view.substr(view.sel()[0])
        # sublime.message_dialog("generate is success!")
        print pythonCode
        tmpPort = 6001
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('127.0.0.1', tmpPort))
        except:
            return
        s.send(pythonCode)
        s.close()