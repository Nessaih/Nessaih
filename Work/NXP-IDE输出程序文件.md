工程中同时生成hex、bin文件：

> Project右键Properties->C/C++ Build->Settings->Build Steps->Post-build steps
> 
> 添加如下命令：
> 
> `arm-none-eabi-objcopy ${ProjName}.elf  -O ihex ${ProjDirPath}/Hexbin/${ProjName}.hex; arm-none-eabi-objcopy ${ProjName}.elf -O binary ${ProjDirPath}/Hexbin/${ProjName}.bin`
