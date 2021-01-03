#!/usr/bin/env python3
"""
Sublime Text plugin to switch between different pre defined user envionments.
"""
import os

import sublime
import sublime_plugin

DEBUG = False
ENV_GROUP = "envs"
SYSTEM_ENVS = dict()

SETTINGS_FILENAME = "EnvSwitcher.sublime-settings"


def trace(message):
    """
    print a debug messgae
    """
    if DEBUG:
        print(message)


def plugin_loaded():
    """
    Load the plugin
    """
    settings = sublime.load_settings(SETTINGS_FILENAME)
    global DEBUG
    DEBUG = settings.get("debug")

    # store the system environment at startup
    EnvSwitcher.store_system_environment(settings)

    # load the default environment at startup
    EnvSwitcher.load_default_env(settings)


def plugin_unloaded():
    """
    Unload the plugin
    """
    EnvSwitcher.reset_system_environment()


class EnvSwitcher(sublime_plugin.WindowCommand):

    def run(self):
        trace("run environment switcher")
        names = self.get_environments()
        sublime.active_window().show_quick_panel(names, self.on_set_env)

    @staticmethod
    def reset_system_environment():
        trace("overwrite the current envs with the default values")
        for key in SYSTEM_ENVS:
            os.environ[key] = SYSTEM_ENVS[key]
            trace("reset {}: {}".format(key, os.environ[key]))

    @staticmethod
    def store_system_environment(settings):
        trace("store the system defined environments")
        if settings is None:
            settings = sublime.load_settings(SETTINGS_FILENAME)

        if settings.has(ENV_GROUP):
            envs = settings.get(ENV_GROUP)
            lis = list(envs.values())
            for item in lis:
                for key in item:
                    if key not in SYSTEM_ENVS.keys():
                        if key in os.environ.keys():
                            SYSTEM_ENVS[key] = os.environ[key]
                            trace("stored {}: {}".format(key, os.environ[key]))
                        else:
                            SYSTEM_ENVS[key] = ""

    @staticmethod
    def load_default_env(settings):
        trace("load default environment")
        if settings is None:
            settings = sublime.load_settings(SETTINGS_FILENAME)

        default_env = settings.get("default_env")
        envs = settings.get(ENV_GROUP)
        if default_env in envs.keys():
            EnvSwitcher.on_set_env(None, list(envs.keys()).index(default_env))
        else:
            msg = "EnvSwitcher:\nCould not find default environment: '{}'".format(default_env)
            sublime.message_dialog(msg)

    def get_environments(self):
        trace("get all defined environments")
        settings = sublime.load_settings(SETTINGS_FILENAME)
        ret = list()
        envs = settings.get(ENV_GROUP)
        if envs:
            ret = list(envs.keys())
        else:
            trace("None envs")
        return ret

    def on_set_env(self, item):
        trace("set the indexed environment")
        if -1 == item:
            trace("cancel ...")
        else:
            # reset to th default values
            EnvSwitcher.reset_system_environment()

            # load the settings to set the new defined Values
            settings = sublime.load_settings(SETTINGS_FILENAME)
            envs = settings.get(ENV_GROUP)
            env_name = list(envs.keys())[item]
            lis = list(envs.values())
            sublime.status_message("Env: '{}'".format(env_name))

            # check to see if there is an env file specified
            if settings.get("env_file_support"):
                try:
                    # get the name of the env file we're using
                    env_file = lis[item][settings.get("env_file_key")]
                    package_dir =\
                        sublime.active_window().extract_variables()['project_path']
                    # load the values from the file
                    with open(os.path.join(package_dir, env_file), 'r') as fh:
                        file_vars = [
                            (
                                l.strip().split("=", 1)[0],
                                l.strip().split("=", 1)[1]
                            ) for l in fh.readlines() if l[0] != "#"
                        ]
                    # expand the variables and store them in the environment
                    for key, val in file_vars:
                        os.environ[key] = os.path.expandvars(val)
                except FileNotFoundError as e:
                    trace("env_file_support is enabled, but env_file not "
                        "found.")

            # continue loading the non-env file variables
            for key, value in lis[item].items():

                if settings.get("env_file_support") \
                        and key == settings.get("env_file_key"):
                    continue

                if ("%{}%".format(key) in value) and (key in SYSTEM_ENVS):
                    value = value.replace("%{}%".format(key), SYSTEM_ENVS[key])

                os.environ[key] = value
                trace("{}: {}".format(key, os.environ[key]))
