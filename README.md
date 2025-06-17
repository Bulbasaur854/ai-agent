# 🤖 AI Agent

The program is a CLI tool that:

1.  Accepts a coding task (e.g., "strings aren't splitting in my app, please fix")
2.  Chooses from a set of predefined functions to work on the task, for example:
   
    -   Scan the files in a directory
    -   Read a file's contents
    -   Overwrite a file's contents
    -   Execute the python interpreter on a file
      
4.  Repeats step 2 until the task is complete (or it fails miserably, which is possible)

## 🛍️ Prerequisites

-   Python 3.10+ installed

## 📘 How-To

1.  Download source code as ZIP and extract it somehwere on your PC
2.  Open a terminal session inside the extracted folder
3.  Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```
