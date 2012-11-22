import sublime, sublime_plugin
import re

class SwapWordsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pattern = sublime.load_settings('Preferences.sublime-settings').get("swap_words_pattern");
        if pattern is None:
            pattern = '\s*[\s,\|&]+\s*'

        for region in self.view.sel():
            if not region.empty():
                selected = self.view.substr(region)
                match = re.search(pattern, selected)
                if match:
                    splitter = match.group()
                    splited = selected.split(splitter, 1)
                    self.view.replace(edit, region, splitter.join(reversed(splited)))
