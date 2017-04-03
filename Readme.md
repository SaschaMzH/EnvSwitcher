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
3. Download [zip package][master] rename it to `EnvSwitcher.sublime-package` and copy it into the `Installed Packages/` directory
4. Restart Sublime Text

## Usage :

### To configure :

Use <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>P</kbd> (<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>P</kbd> on Windows) then `EnvSwitcher: Settings - User` to change the user settings and add new environments for you system.

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
 - use <kbd>cmd</kbd>+<kbd>alt</kbd>+<kbd>P</kbd> (<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>P</kbd> on Windows) to show the list of your defined environments.

## Support :

- Any bugs about Markdown Preview please feel free to report [here][issue].
- And you are welcome to fork and submit pullrequests.


## License :

The code is available at github [project][home] under [MIT licence][licence].



 [home]: https://github.com/SaschaMzH/sublimetext-env-switcher
 [issue]: https://github.com/SaschaMzH/sublimetext-env-switcher/issues
 [settings]: https://github.com/SaschaMzH/sublimetext-env-switcher/blob/master/MarkdownPreview.sublime-settings
 [master]: https://github.com/revolunet/sublimetext-markdown-preview/archive/master.zip
 [licence]: http://SaschaMzH.mit-license.org

 [1]: https://packagecontrol.io/
 [2]: https://packagecontrol.io/installation
