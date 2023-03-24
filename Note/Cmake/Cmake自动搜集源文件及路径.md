```cmake
#功能:搜索当前目录及子目录下的"*.h"文件，存储文件夹路径在result中。
#参数:result
#作者:vic
#版本:1.0
#日期:2022-4-15
macro(find_inc_dir result)                                              #定义宏(宏名 参数1 参数2 ... 参数n)
    file(GLOB_RECURSE incs "${CMAKE_CURRENT_SOURCE_DIR}/*.h" )          #在当前路径下搜索符合GLOB表达式的文件,输出文件列表到incs;
    set(incdirs "")                                                     #定义空字符串变量incdirs
    foreach(inc ${incs})                                                #遍历列表incs(列表即以'；'分隔的字符串)，每个单元的值输出到inc
        string(REGEX REPLACE "(.*)/.*" "\\1" incdir ${inc})             #正则表达式替换,匹配的结果分为两个部分，将整个匹配的结果替换成第一次匹配的结果，并输出到incdir中
        if(IS_DIRECTORY ${incdir})                                      #判断incdir是否是一个目录
            LIST(APPEND incdirs ${incdir})                              #文件夹存在，追加incdir到列表incdirs中
        endif()                                                         #判断结束
    endforeach()                                                        #遍历循环结束
    LIST(REMOVE_DUPLICATES incdirs)                                     #去出重复的文件夹路径(字符串列表中重复的字符串)
    set(${result} ${incdirs})                                           #将列表赋值到输出形参
endmacro()                                                              #宏结束

#功能:搜索当前目录及子目录下的"*.c"文件，存储文件路径在result中
#参数:result
#作者:vic
#版本:1.0
#日期:2022-4-15
macro(find_src_doc result)                                              #定义宏(宏名 参数1 参数2 ... 参数n)
    file(GLOB_RECURSE srcs "${CMAKE_CURRENT_SOURCE_DIR}/*.c" )          #在当前路径下搜索符合GLOB表达式的文件,输出文件列表到srcs;
    set(srcdocs "")                                                     #定义空字符串变量srcdocs
    foreach(src ${srcs})                                                #遍历列表srcs(列表即以'；'分隔的字符串)，每个单元的值输出到src
        if(EXISTS ${src})                                               #判断文件是否存在
            LIST(APPEND srcdocs ${src})                                 #文件存在则追加src到列表srcdocs中
        endif()                                                         #判断结束
    endforeach()                                                        #遍历循环结束
    set(${result} ${srcdocs})                                           #将列表赋值到输出形参
endmacro()                                                              #宏结束


#功能:1.搜索当前目录及子目录下的"*.c"文件，存储文件路径在result中；
#     2.搜索当前目录及子目录下指定类型文件，存储文件路径在result中。
#参数:result ...
#作者:vic
#版本:2.0
#日期:2022-4-15
macro(find_src_doc result)                                              #定义宏(宏名 参数1 参数2 ... 参数n)
    if(${ARGC} GREATER 1)                                               #判读输入参数个数是否大于1 (result为参数1，如果只输入result，则此值为1)
        set(exps ${ARGN})                                               #参数大于1，则取所有参数列表赋值给exps
    else()
        set(exps "${CMAKE_CURRENT_SOURCE_DIR}/*.c")                     #参数不大于1，定义默认表达式，赋值给exps
    endif()
    #message("find_src_doc ${ARGC} ${ARGN}")                            #打印字符串
    file(GLOB_RECURSE srcs ${exps})                                     #搜索符合exps表达式的文件（GLOB表达式）
    set(srcdocs "")                                                     #定义空字符串变量srcdocs，作为列表
    foreach(src ${srcs})                                                #遍历搜索结果列表
        if(EXISTS ${src})                                               #判断文件是否存在
            LIST(APPEND srcdocs ${src})                                 #文件存在则追加src到列表srcdocs中
        endif()
    endforeach()
    set(${result} ${srcdocs})                                           #将列表赋值到输出形参
endmacro()

#功能:1.搜索当前目录及子目录下的"*.h"文件，存储文件夹路径在result中；
#     2.搜索当前目录及子目录下指定类型文件，存储文件夹路径在result中。
#参数:result ...
#作者:vic
#版本:2.0
#日期:2022-4-15
macro(find_src_dir result)
    if(${ARGC} GREATER 2)
        set(exps ${ARGN})
    else()
        set(exps "${CMAKE_CURRENT_SOURCE_DIR}/*.h")
    endif()
    file(GLOB_RECURSE srcs ${exps})
    set(srcdirs "")
    foreach(src ${srcs})
        string(REGEX REPLACE "(.*)/.*" "\\1" srcdir ${src})
        if(IS_DIRECTORY ${srcdir})
            LIST(APPEND srcdirs ${srcdir})
        endif()
    endforeach()
    LIST(REMOVE_DUPLICATES srcdirs)
    set(${result} ${srcdirs})
endmacro()
```

### example: find_src_doc

**功能1:**
```cmake
find_src_doc(out)
message("${out}")
```
**功能2:**
```cmake
find_src_doc(out *.h *.c)
message("${out}")
```

### example: find_src_dir

**功能1:**
```cmake
find_src_doc(out)
message("${out}")
```
**功能2:**
```cmake
find_src_doc(out *.h *.c)
message("${out}")
```


### 错误总结
> 之前写的脚本错误原因:
> 
> 1.不能使用`dir`作为变量，这个是cmake文件中的关键字；使用dir作为变量，很可能取不到正确的值；
