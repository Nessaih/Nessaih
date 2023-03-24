//==========================================================================
// 文件名称: HEX_To_Data.H
// 程序功能: 将 STM32 的 HEX 程序文件转换为 程序升级的数据文件
// 微控制器: 
// 系统时钟: 
// 版权所有: 深圳市友讯达科技发展有限公司  保留所有版权
// 编辑软件: UE13.0
// 编译环境：Windows XP SP2 + Visual Studio C++ 6.0
// 编写时间: 2011-07-18
// 程序版本: 1.0
// 程序作者: 张孝龙 
// 程序修改: 雍林
// 修改日期: 2013-07-05
// 修改内容: 增大了页数量，STM32F103ZE的FLASH为512K
//==========================================================================

#define HEX_ERROR   0
#define HEX_SUCCESS 1

#define WORK_PROG_START_ADDR    (0x08002000L)
#define CRC32_CODE              (0x04C11DB7L)

// HEX文件记录格式
struct  hex_format {                                                    // 该结构保存文件读入数据，ASCII码字符
            unsigned char   start;                                              // :
            unsigned char   length[2];                                          // LL   数据长度
            unsigned char   addr[4];                                            // AAAA 起始地址
            unsigned char   type[2];                                            // TT   记录类型
            unsigned char   data[64][2];                                        // DD   实际数据，一般HEX文件每条记录最大32字节，定义为 64bytes ，留一定余量
            unsigned char   sum[2];                                             // CC   校验数据
            unsigned char   end[2];                                             //      回车换行
        };                                                              // 
        
struct  bin_data {                                                      // 该结构保存二进制数据
            unsigned char   length;                                             // 数据长度
            unsigned short  addr;                                               // 其实地址
            unsigned char   type;                                               // 记录类型
            unsigned char   data[64];                                           // 数据，一般HEX每条记录最大32bytes，定义64bytes，留一定余量
            unsigned char   sum;                                                // 校验
        };                                                              // 

#define MAX_PAGES   (3840)                                              //原来是(1792)  ， STM32F103ZE flash为512K， 雍林修改                                              // 
#define MAX_RECORD  (40000)                                             // 
struct  hex_format  hex_data[MAX_RECORD];                               // 假设平均每条记录16bytes，那么对于STM32，HEX最大 32768 条记录
unsigned char   data_buff[512*1024];                                            // 二进制程序数据缓冲区，STM32 最大容量 512 Kbytes
                                                                        // 第一页（前128bytes） data[0] = 总页数低字节  data[1] = 软件版本号
                                                                        // data[4] = 总页数高字节，data[5] = 总页数低字节，data[6] = 硬件版本号，data[7]=软件版本号
                                                                        // data[8] data[9] data[10] data[11] = CRC32
unsigned char   dVersion;                                                       // 软件版本号
unsigned char   dHVersion;                                                      // 硬件版本号


// 内部函数
static  unsigned char   sub_read_hex_file( unsigned char *  file_path );                // 读取HEX文件
static  unsigned char   sub_hex_to_bin(  struct  hex_format   hex,
                                 struct  bin_data   * bin );            // 把一条HEX记录转换为二进制数据
static  unsigned char   sub_hex_to_data_buff( void );                           // 把HEX文件转为二进制数据，保存到缓冲区
static  void    sub_encode_buff_data( void );                           // 加密缓冲区数据
static  unsigned char   sub_get_prog_version( void );                           // 从二进制文件中，提取版本号信息，程序中数据格式："version：vv"
static  unsigned char   sub_save_updata_file( unsigned char * file_path );              // 保存升序数据文件
static  unsigned char   sub_ascii_to_hex( unsigned char ch1, unsigned char ch0, unsigned char *hex );   // 
static  unsigned int  sub_cal_crc32( const unsigned char *data, unsigned int length );      // 函数原型

// 外部函数
extern  unsigned char   sub_hex_to_updata( unsigned char *file_path );                  // 把HEX文件转换为升级数据



