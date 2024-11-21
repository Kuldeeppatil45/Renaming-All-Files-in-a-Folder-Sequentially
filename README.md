# Renaming-All-Files-in-a-Folder-Sequentially

## Description:
This script renames all files in a specified folder sequentially, starting from 1.ext, 2.ext, and so on, while preserving the original file extensions. Directories and hidden files are ignored.

## Features:
Renames only regular files.
Retains file extensions.
Sorts files alphabetically before renaming.
Handles invalid folder paths and permission issues gracefully.
Skips empty folders or non-renamable files.

## Usage:
Save the script to a file, e.g., rename_files.py.

## Run the script:
python rename_files.py
Enter the folder path when prompted.

## Example:
Input: Please enter the path to the folder: /path/to/folder

Output:
Renaming files...
 - File 'image1.jpg' renamed to '1.jpg'
 - File 'document.txt' renamed to '2.txt'
 - File 'report.pdf' renamed to '3.pdf'
 - File 'notes.docx' renamed to '4.docx'
-  File 'music.mp3' renamed to '5.mp3'
Renaming completed.

## Edge Cases:
Invalid folder path:
Error: The folder '/path/to/folder' does not exist.

## Empty folder:
The folder is empty. No files to rename.

## Permission issues:
Error: Unable to rename file 'image1.jpg' due to permission issues.
