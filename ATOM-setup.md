# Setup ATOM

* IDE-python package:
```
python -m pip install 'python-language-server[all]'
apm install atom-ide-ui
apm install ide-python
```

* python-autopep8
  * and set *On safe*
* platformio-ide-terminal
  * Path to `C:\Program Files\Git\git-cmd.exe`
* kite
* pytools
* minimap
* goto-definition
* hydrogen


## config.cson

```
"*":
  Hydrogen:
    autocomplete: false
    showAutocompleteFirst: false
  "atom-ide-ui":
    "atom-ide-code-format":
      formatOnSave: true
    "atom-ide-diagnostics-ui":
      showDiagnosticTraces: true
      showDirectoryColumn: true
    "atom-ide-outline-view":
      nameOnly: true
    "atom-ide-terminal": {}
    use:
      "atom-ide-busy-signal": "always"
      "atom-ide-code-actions": "always"
      "atom-ide-code-format": "always"
      "atom-ide-code-highlight": "always"
      "atom-ide-debugger": "always"
      "atom-ide-definitions": "always"
      "atom-ide-diagnostics": "always"
      "atom-ide-diagnostics-ui": "always"
      "atom-ide-signature-help": "always"
      "atom-ide-terminal": "always"
      hyperclick: "always"
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
      "python-autopep8"
    ]
    telemetryConsent: "no"
    uriHandlerRegistration: "always"
    useTreeSitterParsers: false
  editor:
    preferredLineLength: 100
    scrollPastEnd: true
    softWrap: true
    softWrapAtPreferredLineLength: true
    tabLength: 4
  "exception-reporting":
    userId: "d730117e-ca34-481c-8a17-d7e878af5d9d"
  fonts:
    fontFamily: "Hack"
  "ide-python":
    pylsPlugins:
      autopep8: {}
      flake8: {}
      jedi_completion: {}
      jedi_definition:
        follow_builtin_imports: true
        follow_imports: true
      jedi_hover: {}
      jedi_references: {}
      jedi_signature_help: {}
      jedi_symbols: {}
      mccabe: {}
      preload: {}
      pycodestyle:
        enabled: false
      pyflakes: {}
      pylint: {}
      rope_completion:
        enabled: true
      yapf:
        enabled: true
  kite:
    showWelcomeNotificationOnStartup: false
  minimap:
    adjustAbsoluteModeHeight: true
  "platformio-ide-terminal":
    core:
      shell: "C:\\Program Files\\Git\\git-cmd.exe"
    style:
      fontSize: "14"
      theme: "homebrew"
  "python-autopep8":
    formatOnSave: true
  welcome:
    showOnStartup: false
  "wrap-guide":
    enabled: false


```

