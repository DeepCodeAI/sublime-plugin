import os
import sublime
import sublime_plugin


from .utils import (
    get_pip_command,
    get_python_command,
    patch_local_deepcode,
)
from .settings import set_initial_settings_if_needed
from .session import (
    is_initial_analysis_ran_for_project,
    add_project_to_initial_analysis_ran_list,
)


def plugin_loaded():
    python_command = get_python_command()
    if not python_command:
        return
    pip_command = get_pip_command(python_command)
    if not pip_command:
        return
    patch_local_deepcode(pip_command)
    set_initial_settings_if_needed()


class Deepcode(sublime_plugin.EventListener):
    def analyze_project_on_load(self):
        for w in sublime.windows():
            if len(w.folders()) == 0:
                return
            elif not is_initial_analysis_ran_for_project(w.folders()[0]):
                print("INITIAL_ANALYSIS")
                sublime.set_timeout_async(
                    lambda: w.run_command("deepcode_analyze"), 1000
                )
                add_project_to_initial_analysis_ran_list(w.folders()[0])

    def on_activated(self, view):
        sublime.set_timeout_async(lambda: self.analyze_project_on_load(), 500)

    def on_post_save_async(self, view):
        view.window().run_command("deepcode_analyze", {"on_save": True})

    def on_post_window_command(self, *args):
        self.analyze_project_on_load()
