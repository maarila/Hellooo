import sublime
import sublime_plugin


class HelloooCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        
        selections = self.view.sel()
        options = ["2", "3", "4", "5", "6", "7", "8", "9"]

        for selection in selections:
            preceding_selection_area = sublime.Region(selection.begin() - 1, selection.begin())
            preceding_symbol = self.view.substr(preceding_selection_area)
            
            if preceding_symbol in options:
                hellooo_to_insert = 'console.log("Hell'
                
                for i in range(int(preceding_symbol)):
                    hellooo_to_insert += "o"
                
                hellooo_to_insert += ' world!")'
                
                self.view.insert(edit, selection.begin(), hellooo_to_insert)
                self.view.erase(edit, preceding_selection_area)
            else:
                hellooo_to_insert = 'console.log("Hello world!")'
                self.view.insert(edit, selection.begin(), hellooo_to_insert)
                
        self.view.end_edit(edit)
        