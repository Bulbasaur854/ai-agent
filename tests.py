from functions.get_files_info import get_files_info
from functions.get_file_contents import get_file_contents
from functions.write_file import write_file

def main():
   # print(get_files_info("calculator", ".") + "\n") 
   # print(get_files_info("calculator", "pkg") + "\n") 
   # print(get_files_info("calculator", "/bin") + "\n") 
   # print(get_files_info("calculator", "../")) 

   # print(get_file_contents("calculator", "main.py") + "\n")
   # print(get_file_contents("calculator", "pkg/calculator.py") + "\n")
   # print(get_file_contents("calculator", "/bin/cat"))

   print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum") + "\n")
   print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet") + "\n")
   print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


if __name__ == "__main__":
    main()