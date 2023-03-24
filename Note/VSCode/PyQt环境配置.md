## Window下VScode下配置PYQT环境

### 1.安装python
    (1)安装python;
    (2)添加Python到环境变量：在Python安装目录下找到"python.exe",添加其目录全路径到系统环境变量；
### 2.安装插件PyQT
    (1)添加PIP到环境变量：在Python安装目录下找到"pip.exe",添加其目录全路径到系统环境变量；
    (2)安装Pyqt: `pip install PyQt5`
### 3.VScode中安装插件"Python"、"Qt for Python"
### 4.VSCO的中配置"Qt for Python"
    (1)配置pyuic;
```json
{
    "qtForPython.uic.path": "D:/ProgramFiles/Python/Python39/Scripts/pyuic5",
    "qtForPython.uic.args": [
    " -x -o \"${fileDirname}${pathSeparator}${fileBasenameNoExtension}.py\""
    ]
}
```
    
    (2)配置pyrcc;
```json
{
    "qtForPython.rcc.path": "D:/ProgramFiles/Python/Python39/Scripts/pyrcc5",
    "qtForPython.rcc.args": [
        "-o \"${fileDirname}${pathSeparator}${fileBasenameNoExtension}.py\""
    ]
}
