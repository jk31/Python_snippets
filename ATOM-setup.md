# Setup ATOM

* IDE-python package:
```
python -m pip install 'python-language-server[all]'
apm install atom-ide-ui
apm install ide-python
```

* script (little broken with envs)
* python-autopep8
  * and set *On safe*
* platformio-ide-terminal
  * Path to `C:\Program Files\Git\git-cmd.exe`
* kite


## config.cson

```
"*":
  Hydrogen:
    autocomplete: false
    showAutocompleteFirst: false
  "atom-ide-ui":
    "atom-ide-code-format":
      formatOnSave: true
    "atom-ide-diagnostics-ui": {}
    "atom-ide-terminal": {}
    use:
      "atom-ide-code-highlight": "always"
      "atom-ide-terminal": "always"
  "autocomplete-plus":
    enableBuiltinProvider: false
  "autocomplete-python":
    useKite: false
  core:
    disabledPackages: [
      "autocomplete-atom-api"
      "snippets"
      "script"
      "spell-check"
      "autocomplete-snippets"
    ]
    telemetryConsent: "no"
    themes: [
      "one-dark-ui"
      "monokai"
    ]
    useTreeSitterParsers: false
  editor:
    fontSize: 16
    preferredLineLength: 100
    scrollPastEnd: true
    softWrap: true
    softWrapAtPreferredLineLength: true
    tabLength: 4
  "exception-reporting":
    userId: "d730117e-ca34-481c-8a17-d7e878af5d9d"
  "ide-python":
    pylsPlugins:
      flake8: {}
      jedi_completion:
        enabled: false
        include_params: false
      jedi_definition:
        enabled: false
      jedi_hover: {}
      jedi_references: {}
      jedi_signature_help:
        enabled: false
      jedi_symbols:
        all_scopes: false
        enabled: false
      mccabe: {}
      preload:
        enabled: false
      pycodestyle:
        enabled: false
      pyflakes: {}
      pylint: {}
      rope_completion: {}
  kite:
    showWelcomeNotificationOnStartup: false
  "platformio-ide-terminal":
    core:
      shell: "C:\\Program Files\\Git\\git-cmd.exe"
    style:
      fontSize: "12"
      theme: "homebrew"
  "python-autopep8":
    formatOnSave: true
  welcome:
    showOnStartup: false

```

