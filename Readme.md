EnvSwitcher
===========
A Plugin for **SublimeText 3** to switch through different environment settings. This can be helpful whenever you want to use a special environment to build.
With this plugin, it is possible to have different python version installed on your machin and use only one of these when you hit build in sublime text.

## Installation:
### Using [Package Control][1] (*Recommended*)

For all Sublime Text 3 users we recommend install via [Package Control][1].

1. [Install][2] Package Control if you haven't yet.
2. Use <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>P</kbd> (<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>P</kbd> on Windows) then `Package Control: Install Package`
3. Look for `EnvSwitcher` and install it.

### Manual Install

1. Click the `Preferences > Browse Packages…` menu
2. Browse up a folder and then into the `Installed Packages/` folder
3. Download the latest [zip package][master] rename it to `EnvSwitcher.sublime-package` and copy it into the `Installed Packages/` directory
4. Restart Sublime Text

## Usage :

### To configure :

Use <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>P</kbd> (<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>P</kbd> on Windows) then `EnvSwitcher: Settings - User` to change the user settings and add new environments for you system.

You can reference the default settings file by using the command `EnvSwitcher: Settings - User`.

For Example::

```js
    "envs":
    {
        "Python 3.5 with PyQt5":
        {
            "PATH": "C:\\Python\\3.5;C:\\Python\\3.5\\Lib\\site-packages\\PyQt5;%PATH%",
            "PYTHONPATH": "C:\\Python\\3.5\\Lib\\site-packages\\PyQt5;%PYTHONPATH%",
        },
        "Python 3.6 with PyQt5":
        {
            "PATH": "C:\\Python\\3.6;C:\\Python\\3.6\\Lib\\site-packages\\PyQt5;%PATH%",
            "PYTHONPATH": "C:\\Python\\3.6\\Lib\\site-packages\\PyQt5;%PYTHONPATH%",
        }
    }
```
### To switch :

 - use <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>P</kbd> (<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>P</kbd> on Windows) then `EnvSwitcher: Choose Environment` to show the list of your defined environments.
 - use <kbd>cmd</kbd>+<kbd>alt</kbd>+<kbd>E</kbd> (<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>E</kbd> on Windows) to show the list of your defined environments.

### Getting Variables from a File

By default, this package will attempt to load the environment variables stored in a file called `.env` located in the top directory of the current project. You can change which file to look for as well as whether or not the package should attempt to load variables from a file by changing your settings.

Each environment profile can use a different filename to read variables from, but in order for this to work properly, you must reserve a key in your profile using the `env_file_key` setting. While most of your keys (e.g. PATH) are used to define new environment variables, this reserved key does not become an environment variable and is used only to name the file.

```js
{
    "env_file_support": true,   // you can disable loading from a file
                                // entirely by changing this value
    "env_file_key": "env_file", // changing this value will change what the
                                // reserved key for the file name will be
    "envs":
    {
        "Default":
        {
            "env_file": ".env", // changing this value will change which file
                                // EnvSwitcher will look for
        },
    }
}

```

## Support :

- Any bugs about Markdown Preview please feel free to report [here][issue].
- And you are welcome to fork and submit pullrequests.


## License :

The code is available at github [project][home] under [MIT licence][licence].



 [home]: https://github.com/SaschaMzH/EnvSwitcher
 [issue]: https://github.com/SaschaMzH/EnvSwitcher/issues
 [settings]: https://github.com/SaschaMzH/EnvSwitcher/blob/master/MarkdownPreview.sublime-settings
 [master]: https://github.com/SaschaMzH/EnvSwitcher/releases
 [licence]: http://SaschaMzH.mit-license.org

 [1]: https://packagecontrol.io/
 [2]: https://packagecontrol.io/installation
