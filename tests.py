from functions.get_files_info import get_files_info
from functions.get_file_contents import get_file_contents

def main():
   # print(get_files_info("calculator", ".") + "\n") 
   # print(get_files_info("calculator", "pkg") + "\n") 
   # print(get_files_info("calculator", "/bin") + "\n") 
   # print(get_files_info("calculator", "../")) 

   print(get_file_contents("calculator", "main.py") + "\n")
   print(get_file_contents("calculator", "pkg/calculator.py") + "\n")
   print(get_file_contents("calculator", "/bin/cat"))

if __name__ == "__main__":
    main()