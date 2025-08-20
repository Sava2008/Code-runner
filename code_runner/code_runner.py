from os import system, path
from sys import argv
import logging

class EmptyFileError(Exception):
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        super().__init__(f"attempted to run an empty file at: {file_path}")
        
class FileTypeError(Exception):
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        super().__init__(f"the file at: {file_path} can't be open")
                          
def main() -> None:
    logging.basicConfig(filename=r"C:\Users\user\AppData\Roaming\Notepad++"
                        r"\Scripts\logs.txt",
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    try:
        passed_file = argv[1].strip()
        logging.info(f"directory: {passed_file}")
        with open(passed_file, "r") as python_file:
            if not python_file.read().strip():
                raise EmptyFileError(passed_file)
        extentions: dict[str, str] = {".py": "Python", ".cs": "Csharp",
                                      ".rs": "Rustc"}
        extention: str = path.splitext(passed_file)[-1]
        if extention not in extentions.keys():
            raise FileTypeError(passed_file)

        file_type: str = extentions[extention]
        if passed_file.endswith(".rs"):
            passed_file = passed_file.removesuffix(r"\src\main.rs")

        commands: dict[str, str] = {
                                    "Python": f"python {passed_file}",
                                    "Csharp": f"dotnet run {passed_file}",
                                    "Rustc": f"cd {passed_file}" 
                                    " && cargo run -q",
                                   }      
        print(f"runnning: {passed_file}")
        print(f"using: {file_type.lower()}")
        system(commands[file_type])
    except Exception as e:
        logging.error(e, exc_info=True)

    logging.info("ended session")
        
if __name__ == "__main__":
    main()