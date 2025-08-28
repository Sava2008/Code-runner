import os
import sys
import json
import logging
import tomllib
from typing import Any
from traceback import format_exc

def open_json(file_path: str) -> Any | None:
    if os.path.exists(file_path):
        with open(file_path, "r") as js_file:
            return json.load(js_file)
    raise FileNotFoundError(f"\033[31m{file_path} cannot be found\033[0m")

class Program:
    current_dir: str = sys.argv[0].removesuffix("SavaRun.py").strip()
    def __init__(self):
        self.logger: logging.Logger = logging.getLogger(__name__)
        logging.basicConfig(filename=Program.current_dir + "\\logs.txt",
                            format="%(asctime)s ||| %(levelname)s ||| %(name)s"
                            "\n%(message)s\n\n",
                            level=logging.INFO)
        self.passed_file: str = sys.argv[1].strip()
        self.extentions: dict[str, str] = open_json(self.current_dir + 
                                                    "extentions.json")
        self.extention: str = os.path.splitext(self.passed_file)[-1]
        self.run_file_dir: str = "\\".join(self.passed_file.split("\\")[:-1])
        self.file_type: str = self.extentions[self.extention]
        self.commands: dict[str, str] = open_json(self.current_dir +
                                                  "commands.json")

def open_toml(file_path: str) -> dict[Any] | None:
    if os.path.exists(file_path):
        with open(file_path, "rb") as toml_file:
            return tomllib.load(toml_file)
    raise FileNotFoundError(f"\033[31m{file_path} cannot be found\033[0m")

class System:
    python_version: str = sys.version.split()[0]
    split_python_version: list[str] = python_version.split(".")
    toml_assets: dict[str, dict[str, str | list | bool]] = \
    open_toml(Program.current_dir + "description.toml")


class EmptyFileError(Exception):
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        super().__init__(f"attempted to run an empty file at: {file_path}")
        
class FileTypeError(Exception):
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        super().__init__(f"the file at: {file_path} can't be open")
  
class BadPythonVersionError(Exception):
    def __init__(self) -> None:
        super().__init__("Python version is either invalid or too old. "
                         "Install python 3.10 or higher")

def validate() -> None:
    if System.split_python_version[0] != "3" or \
       int(System.split_python_version[1]) < 10:
        raise BadPythonVersionError

    with open(program.passed_file, "r") as code:
        if not code.read().strip():
            raise EmptyFileError(program.passed_file)

    if program.extention not in program.extentions.keys():
        raise FileTypeError(passed_file)

def main() -> None:
    print(f"Thanks for using \033[1m{System.toml_assets["project"]["name"]}"
          "\033[0m!\nYour python version is " 
          f"\033[1m\033[4m{System.toml_assets["user_data"]["python_version"]}"
          "\033[0m\033[0m")
    logging.info(f"directory - {program.passed_file}\npython version - "
                 f"{System.python_version}\nscript location - "
                 f"{Program.current_dir[:-1]}\nsetup - "
                 f"{tuple(os.listdir(Program.current_dir))}")
    print(program.passed_file)
    print(f"running: \033[97m{program.passed_file}\033[0m")
    
    command: str = program.commands[program.file_type]
    if program.passed_file.endswith(".rs"):
        program.passed_file = program.passed_file.removesuffix(r"\src\main.rs")
        command = command.replace("PATH", program.passed_file)
    elif program.passed_file.endswith(".py"):
        command = command.replace("PATH", program.run_file_dir)
    command += program.passed_file

    print(f"using: \033[97m{program.file_type.lower().capitalize()}\033[0m")
    print("\033[95mOUTPUT:\033[0m\n")
    os.system(command)

if __name__ == "__main__":
    try:
        program: Program = Program()
        validate()
        main()
    except Exception as e:
        print(f"\033[31m{format_exc()}\033[0m")

        logging.exception(e)
