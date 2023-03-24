# Python、C混合编程



#### 1.C代码生成静态链接库文件

windows系统：`gcc -o D:\ProgramCode\Python\test\PyRunC\03-HexToDat\pyhtd\hextodata.dll -shared -fPIC [-m32/-m64]  main.c`

linux系统：`gcc -o D:\ProgramCode\Python\test\PyRunC\03-HexToDat\pyhtd\hextodata.so -shared -fPIC [-m32/-m64] main.c`

注：(1)实际测试`.so`文件在windows上可用。
    (2)-m32参数：生成32位动态库，-m64参数:生成64位动态库。
    

#### 2.python代码中使用ctypes库调用此文件



### 3.测试正常，将静态库文件（`.dll`或者`.so`）打包到exe

`>>>pyi-makespec -F test.py [-i my.ico --noconsole]`

`[]`中表示可选项：图标、是否显示控制台

#### 4.修改`.spec`文件

在datas中添加需要打包的资源文件


```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['htdpy2.0.py'],
             pathex=['D:\\ProgramCode\\Python\\test\\PyRunC\\03-HexToDat\\pyhtd'],
             binaries=[],
             datas=[],                    #-----修改
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='htdpy2.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='hex.ico')

```



```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['htdpy2.0.py'],
             pathex=['D:\\ProgramCode\\Python\\test\\PyRunC\\03-HexToDat\\pyhtd'],
             binaries=[],
             datas=[('hextodata.dll','.')],#-----修改为
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='htdpy2.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='hex.ico')

```

#### 5.生成exe文件

`pyinstaller name.spec`
