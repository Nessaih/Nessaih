/*******************************************************************************
Copyright 2008 - 2016 深圳市信盈达电子有限公司. All rights reserved.
文件名:        bluetooth.h
描述   : 
作者   :       Jahol Fan
版本   :       V1.0
修改   :   
完成日期：
信盈达官网：http://www.edu118.com/
信盈达网校：http://www.edu118.cn/
Notice    :本程序只供学习使用，未经作者许可，不得用于其它任何用途。版权所有，盗版必究。
*******************************************************************************/
#ifndef BLUETOOTH_H
#define BLUETOOTH_H

#ifdef __cplusplus
extern "C"
{
#endif

/*********************************************************************
 * INCLUDES
 */
#include "stm32f4xx.h"
/*********************************************************************
 * TYPEDEFS
 */
/*********************************************************************
*  EXTERNAL VARIABLES
*/

/*********************************************************************
 * CONSTANTS
 */
#define BLUE_TOOTH_CONNECTED         1
#define BLUE_TOOTH_DIS_CONNECTED     0
/*********************************************************************
 * MACROS
 */

/*********************************************************************
 *PUBLIC FUNCTIONS DECLARE
 */

u8 BT_init(void);
u8 BT_enable(void);
u8 BT_disable(void);
u8 BT_getStatus(void);
void Bluetooth_Show(void);
/*********************************************************************
*********************************************************************/

#ifdef __cplusplus
}
#endif

#endif /* BLUETOOTH_H */
