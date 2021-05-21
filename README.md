# Python Watcher Office File
Watch office file and convert to pdf file

## Prerequest
Please install the following program
- Libreoffice on Path
- Python 3.x.x

## Convert XLS to PDF
watcher use command to convert office file to pdf
```
soffice --headless --convert-to pdf --outdir complete '.\UID HMSR PRODUCTION CONTROL PLAN REVISION 06_Protected.xlsx'
```

## Folder Structure
Follow the standard bellow:
```
    .
    ./complete
    ./log
    ./receive
```

## Build Watcher
Build py to exe
```
    pyinstaller --onefile .\watcher.py
```
Build [Reference](https://datatofish.com/executable-pyinstaller/)

---
Author: Ana Nurdiana