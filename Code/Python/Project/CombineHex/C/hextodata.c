//==========================================================================
// 文件名称: Hex_To_Data.C
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
char dat_path[100] = {0};
//==========================================================================
// 函数名称：sub_ascii_to_hex
// 函数功能：将2byte字符转1byte十六进制数据
// 入口参数：ch1 ch0
// 出口参数：unsigned char 16进制数据
// 程序版本：1.0
// 编写日期：2008-05-16
// 程序作者：
// 修改次数：
// 修改作者：
// 修改日期：
// 修改内容：
// 版本升级：
//==========================================================================
static  unsigned char   sub_ascii_to_hex( unsigned char ch1, unsigned char ch0, unsigned char *hex )
{
    unsigned char   i;
    
    if( ( ch1 >= '0' ) && ( ch1 <= '9' ) ) {                            // 高4bit处理
        i = ch1 - '0';                                                  // 
        i <<= 4;                                                        // 高4bit
    }                                                                   // 
    else if( ( ch1 >= 'a' ) && ( ch1 <= 'f' ) ) {                       // 
        i = ch1 - 'a';                                                  // 
        i += 10;                                                        // 
        i <<= 4;                                                        // 高4bit
    }                                                                   // 
    else if( ( ch1 >= 'A' ) && ( ch1 <= 'F' ) ) {                       // 
        i = ch1 - 'A';                                                  // 
        i += 10;                                                        // 
        i <<= 4;                                                        // 高4bit
    }                                                                   // 
    else                                                                // 
        return HEX_ERROR;                                               // 数据错误


    if( ( ch0 >= '0' ) && ( ch0 <= '9' ) ) {                            // 低4bit处理
        i += ch0 - '0';                                                 // 
    }                                                                   // 
    else if( ( ch0 >= 'a' ) && ( ch0 <= 'f' ) ) {                       // 
        i += ch0 - 'a';                                                 // 
        i += 10;                                                        // 
    }                                                                   // 
    else if( ( ch0 >= 'A' ) && ( ch0 <= 'F' ) ) {                       // 
        i += ch0 - 'A';                                                 // 
        i += 10;                                                        // 
    }                                                                   // 
    else                                                                // 
        return HEX_ERROR;                                               // 数据错误
    
    *hex = i;                                                           // 
    return HEX_SUCCESS;                                                 // 
    
    
}
//==========================================================================
// 函数名称：sub_read_hex_file
// 函数功能：读取 HEX 文件到全部变量中 struct hex_format hex[]
// 入口参数：file_path HEX 文件路径
// 出口参数：
// 程序版本：1.0
// 编写日期：2011-07-18
// 程序作者：
// 修改次数：
// 修改作者：
// 修改日期：
// 修改内容：
// 版本升级：
//==========================================================================
static  unsigned char   sub_read_hex_file( unsigned char * file_path )
{
    unsigned short  i;                                                          // 
    unsigned char   j;                                                          // 
    unsigned char   flag;                                                       // 
    FILE    *fp;                                                        // 
    unsigned char   ch[4] = { 0x00, 0x00, 0x00, 0x00 };                         // 
    unsigned char   length;                                                     // 
    //printf("C print file_path function \"sub_read_hex_file\" : %s\r\n",file_path);
    for( i=strlen(file_path); i != 0; i-- ) {                           // ÅÐ¶ÏÎÄ¼þÀàÐÍ
        ch[3] = ch[2];                                                  // 
        ch[2] = ch[1];                                                  // 
        ch[1] = ch[0];                                                  // 
        ch[0] = file_path[i];                                           // 
        
        if( ( ch[0] == '.' )                         &&                 // 目前只能识别 intel HEX 文件
            ( ( ch[1] == 'h' ) || ( ch[1] == 'H' ) ) &&                 // 
            ( ( ch[2] == 'e' ) || ( ch[2] == 'E' ) ) &&                 // 
            ( ( ch[3] == 'x' ) || ( ch[3] == 'X' ) )    ) {             // 
                break;                                                  // 
        }                                                               // 
        else if( ch[0] == '.' ) {                                       // 
            printf("\n文件类型错误，目前软件只能识别 INTEL HEX 文件。\n"); 
            return HEX_ERROR;                                           // 
        }                                                               //         
    }                                                                   // 
    if( i==0 ) {                                                        // 
        printf("\n文件类型错误，目前软件只能识别 INTEL HEX 文件。\n");  // 
        return HEX_ERROR;                                               // 
    }                                                                   // 

    if( ( fp = fopen(file_path,"rb") ) == NULL ) {                      // 只读打开HEX文件
        printf("\n文件打开失败。\n");                                   // 
        return  HEX_ERROR;                                              // HEX文件错误
    }

    for( i=0; i<MAX_RECORD ;i++) {                                      // 读取HEX文件记录
        if( ( ch[0] = fgetc( fp ) ) == EOF )                            // 
            return  HEX_ERROR;                                          // 
        if( ch[0] != ':' )                                              // ':' 记录开始
            return   HEX_ERROR;                                         // 
        hex_data[i].start = ch[0];                                      // 
  
        if( ( ch[0] = fgetc( fp ) ) == EOF )                            // LL   记录数据长
            return  HEX_ERROR;                                          // 
        if( ( ch[1] = fgetc( fp ) ) == EOF )                            // 
            return  HEX_ERROR;                                          // 
        flag = sub_ascii_to_hex( ch[0], ch[1], &length );               // 2byte字符转1byte十六进制数据
        if( flag == HEX_ERROR )                                         // 
            return HEX_ERROR;                                           // 
        if( length > 0x40 )                                             // STM8S COSMIC HEX文件，每条记录数据长度不大于 0x20，这里定义为 0x40，留一些余量
            return HEX_ERROR;                                           // 
        hex_data[i].length[0] = ch[0];                                  // 
        hex_data[i].length[1] = ch[1];                                  // 
        
        if( ( ch[0] = fgetc( fp ) ) == EOF )                            // AAAA 起始地址
            return  HEX_ERROR;                                          // 
        if( ( ch[1] = fgetc( fp ) ) == EOF )                            // 
            return  HEX_ERROR;                                          // 
        if( ( ch[2] = fgetc( fp ) ) == EOF )                            // 
            return  HEX_ERROR;                                          // 
        if( ( ch[3] = fgetc( fp ) ) == EOF )                            // 
            return  HEX_ERROR;                                          // 
        hex_data[i].addr[0] = ch[0];                                    // 
        hex_data[i].addr[1] = ch[1];                                    // 
        hex_data[i].addr[2] = ch[2];                                    // 
        hex_data[i].addr[3] = ch[3];                                    // 
        
        if( ( ch[0] = fgetc( fp ) ) == EOF )                            // TT   类型码
            return  HEX_ERROR;                                          // 
        if( ( ch[1] = fgetc( fp ) ) == EOF )                            // 
            return  HEX_ERROR;                                          // 
        hex_data[i].type[0] = ch[0];                                    // 
        hex_data[i].type[1] = ch[1];                                    // 
        
        if( length != 0x00 ) {                                          // 如果数据长度不等于0，读取数据区
            for( j=0; j<length; j++ ) {                                 // DD   数据区
                if( ( ch[0] = fgetc( fp ) ) == EOF )                    // 
                    return  HEX_ERROR;                                  // 
                if( ( ch[1] = fgetc( fp ) ) == EOF )                    // 
                    return  HEX_ERROR;                                  // 
                hex_data[i].data[j][0] = ch[0];                         // 
                hex_data[i].data[j][1] = ch[1];                         // 
            }                                                           // 
        }                                                               // 

        if( ( ch[0] = fgetc( fp ) ) == EOF )                            // SUM  校验码
            return  HEX_ERROR;                                          // 
        if( ( ch[1] = fgetc( fp ) ) == EOF )                            // 
            return  HEX_ERROR;                                          // 
        hex_data[i].sum[0] = ch[0];                                     // 
        hex_data[i].sum[1] = ch[1];                                     // 
        
        if( ( hex_data[i].type[0] == '0' ) &&                           // 类型码 0x01: 记录结束
            ( hex_data[i].type[1] == '1' )    )                         // 
            break;                                                      //
        
        if( ( ch[0] = fgetc( fp ) ) == EOF )                            // END  回车换行
            return  HEX_ERROR;                                          // 
        if( ( ch[1] = fgetc( fp ) ) == EOF )                            // 
            return  HEX_ERROR;                                          // 
        hex_data[i].end[0] = ch[0];                                     // 
        hex_data[i].end[1] = ch[1];                                     // 
            
    }                                                                   // 

    fclose( fp );                                                       // 
    return HEX_SUCCESS;                                                 //       
}


//==========================================================================
// 函数名称：sub_hex_to_bin
// 函数功能：把HEX文件记录 转化为 二进制数据记录
// 入口参数：无
// 出口参数：
// 程序版本：1.0
// 编写日期：2011-07-18
// 程序作者：
// 修改次数：
// 修改作者：
// 修改日期：
// 修改内容：
// 版本升级：
//==========================================================================
static  unsigned char   sub_hex_to_bin( struct  hex_format   hex, struct  bin_data   * bin )
{
    unsigned char   i;                                                          // 
    unsigned char   j;                                                          // 
    unsigned char   length;                                                     // 
    unsigned char   flag;                                                       // 
    unsigned short  addr;                                                       // 
    unsigned char   sum = 0x00;                                                 // 
    
    
    if( hex.start != ':' )                                              // 记录起始标志
        return  HEX_ERROR;                                              // 
        
    flag = sub_ascii_to_hex( hex.length[0], hex.length[1], &i );        // 计算长度字段
    if( flag == HEX_ERROR )                                             // 
        return HEX_ERROR;                                               // 
    if( i > 0x40 )                                                      // 字段长度错误
        return  HEX_ERROR;                                              // 
    bin->length = i;                                                    // 
    length = i;                                                         // 
    sum += i;                                                           // 
    
    flag = sub_ascii_to_hex( hex.addr[0], hex.addr[1], &i );            // 计算地址字段
    if( flag == HEX_ERROR )                                             // 
        return HEX_ERROR;                                               // 
    sum += i;                                                           // 
    addr = ((unsigned short)i) << 8 ;                                           // 
    flag = sub_ascii_to_hex( hex.addr[2], hex.addr[3], &i );            // 
    if( flag == HEX_ERROR )                                             // 
        return HEX_ERROR;                                               // 
    sum  += i;                                                          // 
    addr += i;                                                          // 
    bin->addr = addr;                                                   // 
    
    flag = sub_ascii_to_hex( hex.type[0], hex.type[1], &i );            // 计算类型码字段
    if( flag == HEX_ERROR )                                             // 
        return HEX_ERROR;                                               // 
    if((i!=0x00)&&(i!=0x01)&&(i!=0x02)&&(i!=0x03)&&(i!=0x04)&&(i!=0x05))// 类型码错误
        return HEX_ERROR;                                               // 
    bin->type = i;                                                      // 
    sum += i;                                                           // 
    
    if( length != 0x00 ) {                                              // 
        for( j=0; j<length; j++ ) {                                     // 
            flag=sub_ascii_to_hex(hex.data[j][0],hex.data[j][1],&i );   // 计算数据
            if( flag == HEX_ERROR )                                     // 
                return HEX_ERROR;                                       // 
            sum += i;                                                   // 
            bin->data[j] = i;                                           // 
        }                                                               // 
    }                                                                   // 
    
    flag = sub_ascii_to_hex( hex.sum[0], hex.sum[1], &i );              // 计算校验
    if( flag == HEX_ERROR )                                             // 
        return HEX_ERROR;                                               // 
    bin->sum = i;                                                       // 
    sum += i;                                                           // 
    
    if( sum != 0x00 )                                                   // 累加和校验错误，返回记录错误
        return  HEX_ERROR;                                              // 
    else                                                                // 
        return  HEX_SUCCESS;                                            // 
}

//==========================================================================
// 函数名称：sub_hex_to_data_buff
// 函数功能：把HEX记录转化为二进制数据，并且保存到数据缓冲区中
// 入口参数：无
// 出口参数：
// 程序版本：1.0
// 编写日期：2011-07-18
// 程序作者：
// 修改次数：
// 修改作者：
// 修改日期：
// 修改内容：
// 版本升级：
//==========================================================================
static  unsigned char   sub_hex_to_data_buff( void )
{
    unsigned int  i;                                                          // 
    unsigned int  j;                                                          // 
    unsigned char   k;                                                          // 
    unsigned char   length;                                                     // 
    unsigned char   flag;                                                       // 
    struct  bin_data    bin;                                            // 
    unsigned short  pages;                                                      // 
    unsigned int  data_addr;                                                  // 数据地址
    unsigned int  data_line_addr;                                             // 数据段地址
    unsigned int  data;                                                       // 
    
    data_addr = 0x00000000;                                             // 
    data_line_addr = 0x00000000;                                        // 
    
    for( i=0; i<512*1024; i++ ) {                                       // 数据缓冲区初始化，空闲数据使用 0xFF 填充
        data_buff[i] = 0xFF;                                            // 
    }                                                                   // 
    
    for( i=0, pages = 0; ; i++) {                                       // 
        flag = sub_hex_to_bin( hex_data[i], &bin );                     // ASSCII 记录 转化为 二进制记录
        if( flag == HEX_ERROR )                                         // 
            return HEX_ERROR;                                           // 
     
        if( bin.type == 0x01 ) {                                        // 结束记录
            printf("结束：HEX记录 0x%04X 类型 01 结束记录。\n",i);      // 
            data_buff[0] = 0xFF;                                        // 2011-11-15修改，防止与M128升级错误
            data_buff[1] = 0xFF;                                        // 
            data_buff[2] = 0xFF;                                        // 
            data_buff[3] = (unsigned char)(pages) ;                             // 这部分是为了兼容老协议保留，2010-10-02
            data_buff[4] = (unsigned char)((pages>>8)&0x00FF);                  // 这部分是新协议所定义，2010-10-02
            data_buff[5] = (unsigned char)((pages>>0)&0x00FF) ;                 // 
            break;                                                      // 退出
        }                                                               // 
        if( bin.type == 0x02 ) {                                        // 扩展段地址，报错
            printf("错误：HEX记录 0x%04X 类型 02 扩展段地址。\n",i);    // 
            return HEX_ERROR;                                           // 
        }                                                               // 
        if( bin.type == 0x03 ){                                         // 
            printf("错误：HEX记录 0x%04X 类型 03 起始段地址。\n",i);    // 起始段地址，报错
            return HEX_ERROR;                                           // 
        }                                                               // 
        if( bin.type == 0x05 ){                                         // 
            printf("跳过：HEX记录 0x%04X 类型 05 起始线性地址。\n",i);  // 起始线性地址，跳过
            continue;                                                   // 
        }                                                               // 
        if( bin.type == 0x04 ){                                         // 扩展线性地址，修改起始地址
            data   = bin.data[0];                                       // 
            data <<= 8;                                                 // 
            data  += bin.data[1];                                       // 
            data <<= 16;                                                // 
            data_line_addr = data;                                      // 
            printf("地址：HEX记录 0x%04X 类型 04 扩展线性地址 0x%08X。\n",i,data_line_addr );
            continue;                                                   // 
        }                                                               // 
            
        length = bin.length;                                            // 
        data_addr = bin.addr + data_line_addr;                          // 
        if( data_addr < WORK_PROG_START_ADDR ) {                         // 
            printf("错误：HEX记录 0x04X 地址小于起始地址 0x%08X\n",i, WORK_PROG_START_ADDR );
            return HEX_ERROR;                                           // 
        }                                                               // 
        
        data_addr -= WORK_PROG_START_ADDR;                              // 
        for( k=0, j=data_addr+128; k<length; k++, j++ ) {               // 复制数据到 缓冲区，数据从地址128开始保存
            data_buff[j] = bin.data[k];                                 // 
            if( ( j >> 7 ) > pages ) {                                  // 
                pages = (unsigned short)( j>>7 );                               // 
                if( pages > MAX_PAGES ) {                               // 
                    printf("错误：HEX文件太大，程序区无法保存\n");      // 
                    return  HEX_ERROR;                                  // 
                }                                                       // 
            }                                                           // 
        }                                                               // 
        
    }                                                                   // 
    
    return HEX_SUCCESS;                                                 // 
}

//==========================================================================
// 函数名称：sub_encode_buff_data
// 函数功能：加密二进制程序文件
// 入口参数：无
// 出口参数：
// 程序版本：1.0
// 编写日期：2011-07-18
// 程序作者：
// 修改次数：
// 修改作者：
// 修改日期：
// 修改内容：
// 版本升级：
//==========================================================================
static  void   sub_encode_buff_data( void )
{
    unsigned char   encode;                                                     // 
    unsigned int  i;                                                          // 
    unsigned short   p;                                                         // 
    unsigned short   pages;                                                     // 
    
    pages   = data_buff[4];                                             // 
    pages <<= 8;                                                        // 
    pages  += data_buff[5];                                             // 
    
    for( i=0, p=0, encode = 0x00; i<0x80080 ; i++ ) {                   // 512K max
        if( ( i & 0x0000007F ) == 0x0000 ) {                            // 设置每页数据的起始加密量
            if( p > pages ) {                                           // 
                break;                                                  // 
            }                                                           // 
            encode = (unsigned char)p;                                          // 等于页号
            p++;                                                        // 128bytes 为一页
        }                                                               // 
        
        data_buff[i] ^= encode;                                         // 加密数据
        encode += 29;                                                   // 加密量变换，加质数
    }                                                                   // 
}                                                                       // 


//==========================================================================
// 函数名称：sub_get_prog_version
// 函数功能：从二进制文件中提取程序版本号，在程序中，数据格式为"version:xx"
// 入口参数：无
// 出口参数：返回取出的版本号
// 程序版本：1.0
// 编写日期：2011-07-18
// 程序作者：张孝龙
// 修改次数：
// 修改作者：
// 修改日期：
// 修改内容：
// 版本升级：
//==========================================================================
unsigned char   sub_get_prog_version( )
{
    unsigned int  i;                                                          // 
    unsigned short   p;                                                         // 
    unsigned short   pages;                                                     // 
    unsigned char   dProgVer[12];                                               // 
    
    for( i=0; i<10; i++ ) {                                             // 检测缓冲区初始化
        dProgVer[i] = 0x00;                                             // 
    }                                                                   // 

    pages   = data_buff[4];                                             // 
    pages <<= 8;                                                        // 
    pages  += data_buff[5];                                             // 

    for( i=0x00000080, p=0; i<0x80080 ; i++ ) {                         // 512K Bytes
        if( ( i & 0x0000007F ) == 0x00000000 ) {                        // 
            if( p > pages )     break;                                  // 
            p++;                                                        // 128bytes 为一页
        }                                                               // 
        
        dProgVer[0] = dProgVer[1];                                      // 
        dProgVer[1] = dProgVer[2];                                      // 
        dProgVer[2] = dProgVer[3];                                      // 
        dProgVer[3] = dProgVer[4];                                      // 
        dProgVer[4] = dProgVer[5];                                      // 
        dProgVer[5] = dProgVer[6];                                      // 
        dProgVer[6] = dProgVer[7];                                      // 
        dProgVer[7] = dProgVer[8];                                      // 
        dProgVer[8] = dProgVer[9];                                      // 
        dProgVer[9] = data_buff[i];                                     // 
        
        if( ( dProgVer[0] == 'v' ) &&                                   // 从二进制数据流中，提取 "version:"字符串 
            ( dProgVer[1] == 'e' ) &&                                   // 
            ( dProgVer[2] == 'r' ) &&                                   // 
            ( dProgVer[3] == 's' ) &&                                   // 
            ( dProgVer[4] == 'i' ) &&                                   // 
            ( dProgVer[5] == 'o' ) &&                                   // 
            ( dProgVer[6] == 'n' ) &&                                   // 
            ( dProgVer[7] == ':' )      ) {                             // 
                dVersion  = dProgVer[8];                                // 
                dHVersion = dProgVer[9];                                // 
                data_buff[1] = dVersion;                                // 保存版本号，这个为软件版本号，这部分为兼容老版本保留，2010-10-02
                data_buff[6] = dHVersion;                               // 新协议定义的硬件版本号，软件版本号，存放在 data[6] data[7]
                data_buff[7] = dVersion;                                // 
                return 0xFF;                                            // 
        }                                                               // 
    }                                                                   // 
    
    printf("\n错误：版本号获取失败。\n");                               // 
    return 0x00;                                                        // 如果提取版本号错误，返回0x00
    
}



//==========================================================================
// 函数名称：sub_save_updata_file
// 函数功能：保存升序数据文件
// 入口参数：无
// 出口参数：
// 程序版本：1.0
// 编写日期：2008-05-16
// 程序作者：
// 修改次数：
// 修改作者：
// 修改日期：
// 修改内容：
// 版本升级：
//==========================================================================
static  unsigned char   sub_save_updata_file( unsigned char * file_path )
{
    unsigned int  i;                                                          // 
    unsigned char   j;                                                          // 
    unsigned char   path[255];                                                  // 
    time_t  save_time;                                                  //
    struct  tm *stime;                                                  // 
    FILE    *fp;                                                        // 
    unsigned short  pages;                                                      // 
    unsigned short   p;                                                         // 
    unsigned int  crc32;                                                      // 

    
    if( sub_get_prog_version( ) == 0x00 ){                              // 从二进制文件中，提取程序版本号；
        return HEX_ERROR;                                               // 如果版本号提取错误，返回错误
    }                                                                   // 
    
    pages   = data_buff[4];                                             // 
    pages <<= 8;                                                        // 
    pages  += data_buff[5];                                             // 
    
    i = ( pages << 7 );                                                 // 计算 CRC32
    crc32 = sub_cal_crc32( (unsigned char*)(data_buff+128), i );                // 
    data_buff[ 8] = (unsigned char)((crc32>>24)&0x000000FF);                    // 
    data_buff[ 9] = (unsigned char)((crc32>>16)&0x000000FF);                    // 
    data_buff[10] = (unsigned char)((crc32>> 8)&0x000000FF);                    // 
    data_buff[11] = (unsigned char)((crc32>> 0)&0x000000FF);                    // 

    for( i=0; i<1024; i++ ) {                                           // 打印 1024 个字节
        if( ( i & 0x000F ) == 0x0000 )                                  // 
            printf("\n");                                               // 
        printf("%02X ", data_buff[i]);                                  // 
    } 
    
    sub_encode_buff_data();                                             // 加密程序
    printf("\n");                                                       // 
    for( i=0; i<1024; i++ ) {                                           // 
        if( ( i & 0x000F ) == 0x0000 )                                  // 
            printf("\n");                                               // 
        printf("%02X ", data_buff[i]);                                  // 
    } 

    i = strlen( file_path );
    if( i > 240 ) {                                                     // 判断路径字符串长度，不能超过240个字节
        printf("\n路径错误。\n");                                       //
        return HEX_ERROR;                                               // 
    }                                                                   // 
    
    path[i] = '\0';                                                     // 复制路径
    for( ; i != 0 ; i-- ){                                              // 
        path[ i-1] = file_path[i-1];                                    // 
    }                                                                   //        

    time( &save_time );                                                 // 获取当前系统时间
    stime = localtime( &save_time );                                    // 
    i = strlen( path );                                                 // 修改路径名后缀为 .dat，名字后面加时间
    for( ; i != 0; i-- ) {                                              // 
        
        if( path[i] == '.' ){                                           // 2010-10-03 硬件版本号添加到文件名中
            path[i++] = ' ';                                            // 
            path[i++] = 'H';                                            // 
            path[i++] = 'V';                                            // 
            j = dHVersion>>4;                                           // 
            if( j > 9 ) {                                               // 
                j -= 10;                                                // 
                j += 'A';                                               // 
            }                                                           // 
            else {                                                      // 
                j += '0';                                               // 
            }                                                           // 
            path[i++] = j;                                              // 
            path[i++] = '.';                                            // 
            j = dHVersion&0x0F;                                         // 
            if( j > 9 ) {                                               // 
                j -= 10;                                                // 
                j += 'A';                                               // 
            }                                                           // 
            else {                                                      // 
                j += '0';                                               // 
            }                                                           // 
            path[i++] = j;                                              // 
            
            path[i++] = ' ';                                            // 2100-10-03 软件版本号添加到文件名中
            path[i++] = 'S';                                            // 
            path[i++] = 'V';                                            // 
            j = dVersion>>4;                                            // 
            if( j > 9 ) {                                               // 
                j -= 10;                                                // 
                j += 'A';                                               // 
            }                                                           // 
            else {                                                      // 
                j += '0';                                               // 
            }                                                           // 
            path[i++] = j;                                              // 
            path[i++] = '.';                                            // 
            j = dVersion&0x0F;                                          // 
            if( j > 9 ) {                                               // 
                j -= 10;                                                // 
                j += 'A';                                               // 
            }                                                           // 
            else {                                                      // 
                j += '0';                                               // 
            }                                                           // 
            path[i++] = j;                                              // 
            
            path[i++] = ' ';                                            // 
            path[i++] = ( ((stime->tm_year - 100)/10) ) + '0';          // 年
            path[i++] = ( ((stime->tm_year - 100)%10) ) + '0';          // 
            path[i++] = ( ((stime->tm_mon  + 1  )/10) ) + '0';          // 月
            path[i++] = ( ((stime->tm_mon  + 1  )%10) ) + '0';          // 
            path[i++] = ( ((stime->tm_mday - 0  )/10) ) + '0';          // 日
            path[i++] = ( ((stime->tm_mday - 0  )%10) ) + '0';          // 
            path[i++] = '.';                                            // 
            path[i++] = 'd';                                            // 
            path[i++] = 'a';                                            // 
            path[i++] = 't';                                            // 
            path[i++] = '\0';                                           // 
            break;                                                      // 
        }                                                               // 
    }                                                                   // 
    if( i == 0 ){                                                       // 
        printf("\n路径错误，保存文件失败。\n");                         // 
        return HEX_ERROR;                                               // 
    }                                                                   // 
 
    if( ( fp = fopen(path,"wb+") ) == NULL ) {                          // 如果建立文件  
        printf("\n\n保存文件失败。");                                   // 文件建立失败，返回0
        printf("\n文件建立失败。");                                     // 
        printf("路径：%s", path);                                       // 
        return HEX_ERROR;                                               // 
    }
    memcpy(dat_path,path,sizeof(path));
    for( i=0, p=0; p<=pages ; p++ ) {                                   // 
        for( j=0; j<128; j++ ) {                                        // 
            fputc( data_buff[i], fp );                                  // 
            i++;                                                        // 
        }                                                               // 
    }                                                                   // 

    fclose(fp);                                                         // 关闭文件
    
    return HEX_SUCCESS;                                                 // 保存成功
}

//==========================================================================
// 函数名称：sub_hex_to_updata
// 函数功能：把HEX文件转换为升序数据文件
// 入口参数：file_path  HEX文件路径
// 出口参数：
// 程序版本：1.0
// 编写日期：2008-05-16 
// 程序作者：
// 修改次数：
// 修改作者：
// 修改日期：
// 修改内容：
// 版本升级：
//==========================================================================
extern  unsigned char   sub_hex_to_updata( unsigned char * file_path )
{
    unsigned char   flag;                                                       // 

    //printf("C print file_path function \"sub_hex_to_updata\" : %s\r\n",file_path);

    flag = sub_read_hex_file( file_path );                              // ¶ÁÈ¡Ö¸¶¨ HEX ÎÄ¼þ
    if( flag == HEX_ERROR )                                             // 
        return HEX_ERROR;                                               // 
    
    flag = sub_hex_to_data_buff();                                      // HEX文件的 ASCII数据 转换为 二进制数据
    if( flag == HEX_ERROR )                                             // 
        return HEX_ERROR;                                               // 

    flag = sub_save_updata_file( file_path  );                          // 加密二进制数据，提取版本号，把加密后的二进制数据保存到文件
    if( flag == HEX_ERROR )                                             // 
        return HEX_ERROR;                                               // 
    
    return HEX_SUCCESS;                                                 // 
}

//==========================================================================
// 函数名称：sub_cal_crc32
// 函数功能：计算输入数据的CRC32
// 入口参数：data 数据指针
//           len  数据长度
// 出口参数：unsigned int 返回的CRC32结果
// 程序版本：1.0
// 编写日期：2011-06-22
// 程序作者：张孝龙
// 修改次数：
// 修改作者：
// 修改日期：
// 修改内容：
// 版本升级：
//==========================================================================
unsigned int sub_cal_crc32( const unsigned char* data, unsigned int length )
{
    unsigned int  crc32 = 0x00000000;                                         // 
    unsigned int  i;                                                          // 
    unsigned char   j;                                                          // 
    unsigned char   cal_data;                                                   // 
    
    for( i=0; i<length; i++ ) {                                         // 
        cal_data = data[i];                                             // 
        crc32 ^= (((unsigned int)cal_data)<<24);                              // 
        for( j=0; j<8; j++ ) {                                          // 
	        if( crc32 & 0x80000000 ) {                                  // 
		        crc32 <<= 1;                                            // 
		        crc32 ^=  CRC32_CODE;                                   // 
            }                                                           // 
	        else crc32 <<=1 ;                                           // 
        }                                                               // 
    }                                                                   // 
    return crc32;                                                       // 
} 


char *get_dat_path(void)
{
    return dat_path;
}
