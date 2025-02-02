# codescrap

## Overview
This Python script generates a markdown file containing the structure of a directory and the contents of its text-based files. It provides a GUI interface for previewing, copying, and saving the generated markdown content.

## Features
- Recursively scans the parent directory of the script.
- Generates a structured markdown representation of the directory tree.
- Reads and includes non-binary file contents in the output.
- Skips unwanted directories such as `venv`, `__pycache__`, `node_modules`, and `codescrap`.
- Avoids binary files such as images and executables.
- Displays the generated markdown in a Tkinter GUI with options to copy or save the output.

## Requirements
- Python 3.x
- Tkinter (pre-installed with Python)

## Installation
Clone the repository or download the script


## Usage
Run the script using Python:
```sh
$ python codescrap.py
```
or use the run.bat

This will open a Tkinter window displaying the generated markdown. You can copy it to the clipboard or save it as `generated_output.md` in the parent directory.

## How It Works
1. **`generate_tree(root_dir)`**:
   - Recursively builds a tree structure of the directory.
   - Ignores unwanted directories.
2. **`generate_file_contents(root_dir)`**:
   - Reads the content of non-binary files and includes them in markdown format.
3. **`generate_markdown()`**:
   - Calls `generate_file_contents` to prepare the markdown output.
4. **`save_to_file(markdown_text)`**:
   - Saves the generated markdown content to `generated_output.md`.
5. **`display_output(markdown_text)`**:
   - Opens a Tkinter window to preview the generated markdown.
   - Provides buttons to copy or save the markdown.

## Example Output
The generated markdown will look something like this:
```markdown
- .
  - src
    - main.py
  - README.md

## src/main.py
```plaintext
print("Hello, World!")
```
```

## License
This project is licensed under the MIT License.

## Contributions
Feel free to fork the repository and submit pull requests for improvements.
