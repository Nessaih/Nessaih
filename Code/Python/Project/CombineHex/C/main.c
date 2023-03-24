//==========================================================================
// 文件名称: MAIN.C
// 程序功能: 将 STM32 的 HEX 程序文件转换为 程序升级的数据文件
// 微控制器: 
// 系统时钟: 
// 版权所有: 深圳市友讯达科技发展有限公司  保留所有版权
// 编辑软件: UE13.0
// 编译环境：Windows XP SP2 + Visual Studio C++ 6.0
// 编写时间: 2011-07-18
// 程序版本: 1.0
// 程序作者: 张孝龙 
// 程序修改: 
// 修改日期: 
// 修改内容: 
//==========================================================================

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#include <string.h>
#include <math.h>
#include "type.h"
#include "HEX_To_Data.H"
#include "HEX_To_Data.C"

INT16S main(int argc,char *argv[])
{
    unsigned char   i;                                                          // 
    char **temp = argv;
    printf("int argc ：%d\r\n",argc);
    while(temp != NULL)
    {
        printf("%s\r\n",*temp++);
    }

    getch();
    if( argc <= 1 ){                                                    // 主函数参数检测
	    printf("错误：指定文件无法打开。\n");                           // 
        getch();                                                        // 
        exit(0);                                                        // 
    }                                                                   // 

    i = sub_hex_to_updata( argv[1] );                                   // 
    if( i == HEX_SUCCESS ) {                                            // 
        printf("\n数据转换成功。\n");                                   // 
    }                                                                   // 
    else {                                                              // 
        printf("\n数据转换失败。\n");                                   // 
    }                                                                   // 

    printf("\n 按任意键退出。");                                        // 
    
    i = getch();                                                        // 
    exit(0);                                                            // 
}
    
    


