import os
import tkinter as tk
from tkinter import scrolledtext

def generate_tree(root_dir):
    tree = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip unwanted directories
        dirnames[:] = [d for d in dirnames if d.lower() not in ('venv', '__pycache__', 'node_modules')]
        # Calculate the depth based on the relative path
        depth = os.path.relpath(dirpath, root_dir).count(os.sep) if os.path.relpath(dirpath, root_dir) != '.' else 0
        indent = '  ' * depth
        # Show directory name; for root, show '.'
        dir_name = os.path.basename(dirpath) if os.path.basename(dirpath) else dirpath
        display_name = dir_name if depth > 0 else '.'
        tree.append(f"{indent}- {display_name}")
        for f in sorted(filenames):
            tree.append(f"{indent}  - {f}")
    return "\n".join(tree)


def generate_file_contents(root_dir):
    contents = []
    # Define common binary file extensions to skip
    binary_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.exe', '.dll', '.bin'}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip unwanted directories, including the 'codescrap' folder
        dirnames[:] = [d for d in dirnames if d.lower() not in ('venv', '__pycache__', 'node_modules', 'codescrap')]
        for f in filenames:
            file_path = os.path.join(dirpath, f)
            # Skip binary files based on extension
            _, ext = os.path.splitext(f)
            if ext.lower() in binary_extensions:
                continue
            # Skip the generated markdown file to avoid recursion
            if os.path.abspath(file_path) == os.path.abspath(os.path.join(root_dir, 'code_structure.md')):
                continue
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_text = file.read()
            except Exception as e:
                file_text = f"Error reading file: {e}"
            relative_path = os.path.relpath(file_path, root_dir)
            contents.append(f"## {relative_path}\n")
            contents.append("```plaintext\n")
            contents.append(file_text)
            contents.append("\n```\n")
    return "\n".join(contents)


def generate_markdown():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    return generate_file_contents(root_dir)


def save_to_file(markdown_text):
    """Save the markdown content to a file named 'generated_output.md' in the parent folder of the codescrap directory."""
    try:
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        output_path = os.path.join(parent_dir, "generated_output.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)
    except Exception as e:
        print(f"Error saving markdown: {e}")


def copy_to_clipboard(text, root):
    root.clipboard_clear()
    root.clipboard_append(text)


def display_output(markdown_text):
    """Create a Tkinter window to display markdown content with copy and save buttons."""
    root = tk.Tk()
    root.title("Generated Markdown")
    root.geometry("800x600")

    st = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    st.pack(expand=True, fill=tk.BOTH)
    st.insert(tk.END, markdown_text)
    st.config(state=tk.DISABLED)

    copy_button = tk.Button(root, text="Copy Markdown", command=lambda: copy_to_clipboard(markdown_text, root))
    copy_button.pack(pady=5)

    save_button = tk.Button(root, text="Save Markdown to File", command=lambda: save_to_file(markdown_text))
    save_button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    md_content = generate_markdown()
    display_output(md_content)