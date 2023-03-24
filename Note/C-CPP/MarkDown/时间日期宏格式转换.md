### 1.  获取编译日期、时间：

这个很简单，直接使用两个宏`__DATE__`、`__TIME__`即可，代码如下：

```C
#include <stdio.h>
int main() {
    printf("%s\r\n%s\r\n",__DATE__,__TIME__);
    return 0;
}
```
程序运行结果如下：
> ```
> Sep  8 2021
> 17:41:37
> ```

---

### 2. 获取编译时的星期：

星期是无法直接获取到的，不过可以根据一个基准日期（xxxx年xx月xx日 星期x)，以及当前日期（`__DATE__`），算出当前星期。思考方式较简单，当然计算量相对稍大，此处不详细介绍。以下介绍一种更高级的方法，便是使用泰勒公式：

 泰勒公式：**`w=y+[y/4]+[c/4]-2c+[26(m+1）/10]+d-1`** 

   + w：星期； w对7取模得：0-星期日，1-星期一，2-星期二，3-星期三，4-星期四，5-星期五，6-星期六
   + c：世纪（注：一般情况下，在公式中取值为已经过的世纪数，也就是年份除以一百的结果，而非正在进行的世纪，也就是现在常用的年份除以一百加一；不过如果年份是公元前的年份且非整百数的话，c应该等于所在世纪的编号，如公元前253年，是公元前3世纪，c就等于-3）
   + y：年（一般情况下是后两位数，如果是公元前的年份且非整百数，y应该等于cMOD100+100）
   + m：月（m大于等于3，小于等于14，即在蔡勒公式中，某年的1、2月要看作上一年的13、14月来计算，比如2003年1月1日要看作2002年的13月1日来计算）
   + d：日
   + [ ]代表取整，即只要整数部分。

代码如下：

```C++
#include <stdio.h>
#include <stdint.h>
#include <string.h>
typedef struct time_struct {
	uint16_t year;
	uint8_t  month;
	uint8_t  day;
	uint8_t  week;
	uint8_t  hour;
	uint8_t  minute;
	uint8_t  second;
}TimeStructType;



void GetDateTime(TimeStructType *dt)
{
	char *date = __DATE__;
	char *time = __TIME__;

	dt->year = (date[7] - 48) * 1000 + \
		(date[8] - 48) * 100 + \
		(date[9] - 48) * 10 + \
		(date[10] - 48);

	if (0 == memcmp("Jan", date, 3))
		dt->month = 1;
	else if (0 == memcmp("Feb", date, 3))
		dt->month = 2;
	else if (0 == memcmp("Mar", date, 3))
		dt->month = 3;
	else if (0 == memcmp("Apr", date, 3))
		dt->month = 4;
	else if (0 == memcmp("May", date, 3))
		dt->month = 5;
	else if (0 == memcmp("Jun", date, 3))
		dt->month = 6;
	else if (0 == memcmp("Jul", date, 3))
		dt->month = 7;
	else if (0 == memcmp("Aug", date, 3))
		dt->month = 8;
	else if (0 == memcmp("Sep", date, 3))
		dt->month = 9;
	else if (0 == memcmp("Oct", date, 3))
		dt->month = 10;
	else if (0 == memcmp("Nov", date, 3))
		dt->month = 11;
	else if (0 == memcmp("Dec", date, 3))
		dt->month = 12;


	if (' ' != date[4])
		dt->day = (date[4] - 48) *10 ;
	else
		dt->day = 0;
	dt->day += (date[5] - 48);

	dt->week = dt->year + (dt->year / 4) + (26 * (dt->month + 1) / 10) + dt->day - 36;
	dt->week %= 7;

	dt->hour = (time[0] - 48) * 10 + \
		(time[1] - 48);
	dt->minute = (time[3] - 48) * 10 + \
		(time[4] - 48);
	dt->second = (time[6] - 48) * 10 + \
		(time[7] - 48);
}


int main(void)
{
	TimeStructType udt;
	GetDateTime(&udt);
	printf("%d-%d-%d %d %d:%d:%d", udt.year, udt.month, udt.day, udt.week, udt.hour, udt.minute, udt.second);
	return 0;
}
```

程序运行结果如下:

> `2021-9-8 3 17:51:55`


---



### 3. 使用宏定义将日期字符串转换为数值

```C
#include <stdio.h>

#define BUILDTM_YEAR (\
    __DATE__[7] == '?' ? 1900 \
    : (((__DATE__[7] - '0') * 1000 ) \
    + (__DATE__[8] - '0') * 100 \
    + (__DATE__[9] - '0') * 10 \
    + __DATE__[10] - '0'))

#define BUILDTM_MONTH (\
    __DATE__ [2] == '?' ? 1 \
    : __DATE__ [2] == 'n' ? (__DATE__ [1] == 'a' ? 1 : 6) \
    : __DATE__ [2] == 'b' ? 2 \
    : __DATE__ [2] == 'r' ? (__DATE__ [0] == 'M' ? 3 : 4) \
    : __DATE__ [2] == 'y' ? 5 \
    : __DATE__ [2] == 'l' ? 7 \
    : __DATE__ [2] == 'g' ? 8 \
    : __DATE__ [2] == 'p' ? 9 \
    : __DATE__ [2] == 't' ? 10 \
    : __DATE__ [2] == 'v' ? 11 \
    : 12)

#define BUILDTM_DAY (\
    __DATE__[4] == '?' ? 1 \
    : ((__DATE__[4] == ' ' ? 0 : \
    ((__DATE__[4] - '0') * 10)) + __DATE__[5] - '0'))


int main() {
    printf("string:%s\nnumber:%4d%2d%2d",__DATE__,BUILDTM_YEAR,BUILDTM_MONTH,BUILDTM_DAY);
    return 0;
}
```

程序运行结果如下:

> `string:Sep  8 2021`
> `number:2021 9 8`

---

### 4. 使用函数将宏转换为数值

```C
#include <stdio.h>
#include <string.h>
#include <time.h>

time_t cvt_TIME(char const *time) {
    char s_month[5];
    int month, day, year;
    struct tm t = {0};
    static const char month_names[] = "JanFebMarAprMayJunJulAugSepOctNovDec";

    sscanf(time, "%s %d %d", s_month, &day, &year);

    month = (strstr(month_names, s_month)-month_names)/3;

    t.tm_mon = month;
    t.tm_mday = day;
    t.tm_year = year - 1900;
    t.tm_isdst = -1;

    return mktime(&t);
}

int main() {

    time_t     tv;
    struct tm *pt;

    tv = cvt_TIME(__DATE__);
    pt = gmtime(&tv);
    printf("string:%s\r\n",__DATE__);
    printf("%ld-%d-%d\r\n",pt->tm_year+1900,pt->tm_mon,pt->tm_mday);
    printf("time:%lld",tv);
    return 0;
}
```
程序运行结果如下:

> `string:Sep  8 2021`
> `2021-8-7`
> `time:1631030400`

---

### 5. 使用宏定义格式化日期格式



```C
#include <stdio.h>

#define DATE_CODE  (\
    (char const[]){\
    __DATE__[7]  ,                                                           \
    __DATE__[8]  ,                                                           \
    __DATE__[9]  ,                                                           \
    __DATE__[10] , (                                                         \
    __DATE__[0] == 'O' ||                                                    \
    __DATE__[0] == 'N' ||                                                    \
    __DATE__[0] == 'D' ) ? '1':'0', (                                        \
    __DATE__[2] == '?' ? '1'                                               : \
    __DATE__[2] == 'n' ? (__DATE__ [1] == 'a' ? '1' : '6')                 : \
    __DATE__[2] == 'b' ? '2'                                               : \
    __DATE__[2] == 'r' ? (__DATE__ [0] == 'M' ? '3' : '4')                 : \
    __DATE__[2] == 'y' ? '5'                                               : \
    __DATE__[2] == 'l' ? '7'                                               : \
    __DATE__[2] == 'g' ? '8'                                               : \
    __DATE__[2] == 'p' ? '9'                                               : \
    __DATE__[2] == 't' ? '0'                                               : \
    __DATE__[2] == 'v' ? '1' : '2'),                                         \
    __DATE__[4] == ' ' ? '0' : __DATE__[4],                                  \
    __DATE__[5],                                                             \
    '\0' })

int main() {
    printf("%s \r\n",__DATE__);
    printf("%s \r\n",DATE_CODE);
    return 0;
}
```

程序运行结果如下：

> `Sep  8 2021`
> `20210908`

---
