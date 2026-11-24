# Desktop Cleaner

A small Python learning project that sorts files in the current working directory. It uses only the Python standard library; no third-party packages are required.

## How to run

Open a terminal in the folder you want to sort, then run the script by its path:

```text
python path/to/Desktop-Cleaner/main.py
```

Replace `path/to/Desktop-Cleaner/main.py` with the path to this project's `main.py`. The script sorts only files directly in the terminal's current working directory. It does not automatically target the Desktop. It creates destination folders in that working directory, lists no preview of the files, and waits for ENTER before moving them.

## File types

- `Videos/`: `.mp4`, `.mkv`
- `Music/`: `.mp3`, `.wav`
- `Pictures/`: `.png`, `.jpg`, `.jpeg`

File extensions are matched without regard to letter case. Matching files are moved into the corresponding folder.

## Notes

- If a destination already contains a file with the same name, the move fails and the source file remains in place; the script prints the error.
- If the destination folders cannot be created, the script reports the problem but still attempts the moves. Permission or other filesystem errors during a move may stop the program.
