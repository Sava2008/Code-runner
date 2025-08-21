# Code-runner
## How to use
Download both the logs.txt and code_runner.py files, dump them into one directory, copy the path to the script and add a shortcut with the following command:
```text
cmd /k python "C:\path\to\code_runner.py" "$(FULL_CURRENT_PATH)"
```
logs.txt will collect every log and track errors. For bug reports, feel free to send me the logs.txt file.
right now only 3 three programming languages are supported, which includes python, rust and C#, but more are planned to be implemented.
## What to do your programming language is not on the list above?
open the code_runner.py file and look for the "extensions" dict and the "commands" dict:
```python
extentions: dict[str, str] = {".py": "Python", ".cs": "Csharp",
                              ".rs": "Rustc"}
```
```python
commands: dict[str, str] = {
                            "Python": f"python {passed_file}",
                            "Csharp": f"dotnet run {passed_file}",
                            "Rustc": f"cd {passed_file}"
                            " && cargo run -q",
                           }
```
notice that some strings ```f"cd {passed_file}" " && cargo run -q"``` are implicitly concatenated to not exceed the 79 characters in a single line limit, but using the "+" operator is completely valid
```f"cd {passed_file}" + " && cargo run -q"```.

Add your programming language to the dictionary and add the extension of the corresponding file:
```python
extentions: dict[str, str] = {".py": "Python", ".cs": "Csharp",
                              ".rs": "Rustc", ".rb": "Ruby",
                              ".php": "PHP"}
```
```python
commands: dict[str, str] = {
                            "Python": f"python {passed_file}",
                            "Csharp": f"dotnet run {passed_file}",
                            "Rustc": f"cd {passed_file}"
                            " && cargo run -q",
                            "Ruby": "ruby {passed_file}",
                            "PHP": "php {passed_file}"
                           }
```
notice that the value of extensions can be anything. Just ensure that it's the same and the key to the matching command. JSON will be added soon for better interaction.
## What will be added
1. JSON file instead of raw dictionaries
2. More programming languages
3. Bugfixes
## Credits
Sava2008
