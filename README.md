# 🤖 AI Agent

The program is a CLI tool that:

1.  Accepts a coding task (e.g., "strings aren't splitting in my app, please fix")
2.  Chooses from a set of predefined functions to work on the task, for example:

    -   Scan the files in a directory
    -   Read a file's contents
    -   Overwrite a file's contents
    -   Execute the python interpreter on a file

3.  Repeats step 2 until the task is complete (or it fails miserably, which is possible)

## ⚠️ Warning

This program does not have all the security and safety features that a production AI agent would have. It is for learning purposes only. The LLM can run arbitrary code that we (or it) places in the working directory... so be careful.

## 🛍️ Prerequisites

-   Python 3.10+ installed
-   [uv installed](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)

## 💾 Installation

1.  Clone the repo
2.  In terminal, `cd` into it

## 📘 How-To (example)

1.  Introduce the bug - Manually update `pkg/calculator.py` and change the precedence of the `+` operator to `3`
2.  Run the calculator app, to make sure it's now producing incorrect results:

    ```bash
    uv run calculator/main.py "3 + 7 * 2"
    ```

    This should be 17, but because we broke it, it says 20

3.  Run the agent:

    ```bash
    uv run main.py "Result of '3 + 7 * 2' should not be 20"
    ```
