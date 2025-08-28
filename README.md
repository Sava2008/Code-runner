# Code-runner
## How to use
Download files from the directory Code_runner_1.0.0, dump them into one directory on your computer, copy the path to the script and add a shortcut with the following command into your code editor:
```text
cmd /k python "C:\path\to\code_runner.py" "$(FULL_CURRENT_PATH)"
```
Replace ```"C:\path\to\code_runner.py"``` with directory valid for your case.
logs.txt will collect every log and track errors. For bug reports, feel free to send exception logs from the logs.txt file to me!
Right now only 3 three programming languages are supported, which includes python, rust and C#, but more are planned to be implemented.
## What to do if your programming language is not on the list above?
Open the extension.json and file and add anything you need:
```json
{
  ".py": "Python",
  ".cs": "Csharp",
  ".rs": "Rustc",
  ".rb": "Ruby"
}
```
Open the commands.json and add cmd commands reciprocately:
```json
{
  "Python": "python ",
  "Csharp": "dotnet run ",
  "Rustc": "cd PATH && cargo run -q",
  "Ruby": "ruby "
}
```
Notice that some strings ```"cd PATH && cargo run -q"``` have PATH in all capitals. It's a placeholder which is replaced by file directory.
Wherever a value doesn't have PATH, the path is appended to the end ```ruby file.rb```
Notice that the value of extensions can be anything. Just ensure that it's the same and the key to the matching command (e.g. value "Python" in extensions.json
matches key "Python" in commands.json

## What will be added
1. More programming languages
2. Bugfixes
## Credits
Sava2008
