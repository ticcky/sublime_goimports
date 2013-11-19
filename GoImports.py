# Sublime3 Plugin that runs goimports on the current file
#
# Author: Lukas Zilka (lukas@zilka.me)
#
import sublime
import sublime_plugin
import subprocess
import io


s = sublime.load_settings("GoImports.sublime-settings")


class GoImportsCommand(sublime_plugin.TextCommand):
    def run(self, edit, saving=False):
        # Get the content of the current window from the text editor.
        selection = sublime.Region(0, self.view.size())
        content = self.view.substr(selection)

        # Shove that content down goimports process's throat.
        process = subprocess.Popen([s.get("go_imports_bin_path")], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        process.stdin.write(bytes(content, 'utf8'))
        process.stdin.close()
        process.wait()

        # Put the result back.
        self.view.replace(edit, selection, process.stdout.read().decode('utf8'))
