import sublime
import sublime_plugin

def MakeURL(str):
    url='https://google.com/search?q=%s&?oq=%s/'%(str,str)
    return url

class SearchGoogleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        str_location=self.view.sel()          #get string location(list)
        str=self.view.substr(str_location[0]) #get string
        url=MakeURL(str)                      #make URL
        sublime.message_dialog(url)           #show URL