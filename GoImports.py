# Sublime3 Plugin that runs goimports on the current file
#
# Author: Lukas Zilka (lukas@zilka.me)
# 
import sublime
import sublime_plugin
import subprocess
import io


class GoImportsCommand(sublime_plugin.TextCommand):
    def run(self, edit, saving=False):
        selection = sublime.Region(0, self.view.size())
        content = self.view.substr(selection)
        process = subprocess.Popen(['/xdisk/devel/go/bin/goimports'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        process.stdin.write(bytes(content, 'utf8'))
        process.stdin.close()
        process.wait()

        self.view.replace(edit, selection, process.stdout.read().decode('utf8'))
