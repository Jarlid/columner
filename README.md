This program takes data from files in `./files/` directory and puts it as columns of `file.txt`

Uses `config.ini` file to configure behavior:
- `FileOrder = [file_1] [file_2] [file_3] ...`
  - puts specified files in specified order;
  - if some files are absent, ignores them;
  - other files in directory put afterwards.
- `ColumnWidth = [number]`
  - makes columns' width equal `[number]`;