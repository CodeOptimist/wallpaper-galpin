call venv\scripts\activate.bat
rem generates spec file, but won't have the version modification
rem pyi-makespec --add-data lib;lib --onefile --console --name onefile2 main.py
echo %1> build\version
pyinstaller onefile.spec
del build\version 2> nul
