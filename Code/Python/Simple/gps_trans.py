
import json
import urllib
import math
import tkinter
import tkinter.ttk

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方

def gcj02_to_bd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]


def bd09_to_gcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]


def wgs84_to_gcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)


def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)



def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret



def wgs84_to_nmea0183(lon,lat):
    tuple_lon = math.modf(lon)
    longitude = tuple_lon[1]*100 +tuple_lon[0]*60
    tuple_lat = math.modf(lat)
    latitude = tuple_lat[1]*100 +tuple_lat[0]*60
    return [longitude, latitude]

def nmea0183_to_wgs84(lon,lat):
    longitude = int(lon / 100) + (lon % 100 ) / 60
    latitude = int(lat / 100) + (lat % 100 ) / 60
    return [longitude, latitude]


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)

class Window(tkinter.Frame):
    def __init__(self,master = None):
        tkinter.Frame.__init__(self,master)
        self.type = tkinter.StringVar()
        self.input = tkinter.StringVar()
        self.pack()
        self.window_creat()
        self.window_layout()

    def window_creat(self):
        self.master.geometry('480x180')
        self.master.title('HPM坐标转化')
        self.inframe = tkinter.Label(self.master)
        self.outframe = tkinter.Label(self.master)
        self.select = tkinter.ttk.Combobox(self.inframe,width=10,textvariable=self.type, value = ('NMEA0183','WGS84','GCJ02','BD09'))
        # self.select['value'] = ['NMEA0183','WGS84']
        self.select.current(0)
        self.input = tkinter.Entry(self.inframe,textvariable=self.input)
        self.key = tkinter.Button(self.inframe, text = '转换',command = self.transform_callback)
        self.line1 = tkinter.Label(self.outframe)
        self.line2 = tkinter.Label(self.outframe)
        self.line3 = tkinter.Label(self.outframe)
        self.line4 = tkinter.Label(self.outframe)
        
        self.tip1 = tkinter.Label(self.line1,text = 'NMEA0183', anchor = tkinter.E, width=10, height=1)
        self.tip2 = tkinter.Label(self.line2,text = 'WGS84',anchor = tkinter.E, width=10, height=1)
        self.tip3 = tkinter.Label(self.line3,text = 'GCJ02',anchor = tkinter.E, width=10, height=1)
        self.tip4 = tkinter.Label(self.line4,text = 'BD09',anchor = tkinter.E, width=10, height=1)
        
        self.out1 = tkinter.Entry(self.line1, width = 35)
        self.out2 = tkinter.Entry(self.line2, width = 35)
        self.out3 = tkinter.Entry(self.line3, width = 35)
        self.out4 = tkinter.Entry(self.line4, width = 35)
        
        
    def window_layout(self):
        self.inframe.pack()
        self.outframe.pack()
        self.select.pack(side=tkinter.LEFT,padx=10)
        self.input.pack(side=tkinter.LEFT,padx=20)
        self.key.pack(side=tkinter.LEFT)

        self.line1.pack(side=tkinter.TOP)
        self.line2.pack(side=tkinter.TOP)
        self.line3.pack(side=tkinter.TOP)
        self.line4.pack(side=tkinter.TOP)
        
        self.tip1.pack(side=tkinter.LEFT,padx=30,ipadx=20)
        self.tip2.pack(side=tkinter.LEFT,padx=30,ipadx=20)
        self.tip3.pack(side=tkinter.LEFT,padx=30,ipadx=20)
        self.tip4.pack(side=tkinter.LEFT,padx=30,ipadx=20)
        
        self.out1.pack(side=tkinter.LEFT)
        self.out2.pack(side=tkinter.LEFT)
        self.out3.pack(side=tkinter.LEFT)
        self.out4.pack(side=tkinter.LEFT)
        
        
    
    def transform_callback(self):
        list = self.input.get().split(',',1)
        type = self.type.get()
        lon_in = float(list[0])
        lat_in = float(list[1])

        self.out1.delete(0,'end')
        self.out2.delete(0,'end')
        self.out3.delete(0,'end')
        self.out4.delete(0,'end')
        
        if 'NMEA0183' == type:
            list = nmea0183_to_wgs84(lon_in,lat_in)
            self.out1.insert('insert', self.input.get())
            self.out2.insert('insert', str(list[0]) + ',' + str(list[1]))
            lon_in = list[0]
            lat_in = list[1]
            list = wgs84_to_gcj02(lon_in,lat_in)
            self.out3.insert('insert', str(list[0]) + ',' + str(list[1]))
            lon_in = list[0]
            lat_in = list[1]
            list = gcj02_to_bd09(lon_in,lat_in)
            self.out4.insert('insert', str(list[0]) + ',' + str(list[1]))
        elif 'WGS84' == type:
            list = wgs84_to_nmea0183(lon_in,lat_in)
            self.out1.insert('insert', str(list[0]) + ',' + str(list[1]))
            self.out2.insert('insert', self.input.get())
            list = wgs84_to_gcj02(lon_in,lat_in)
            self.out3.insert('insert', str(list[0]) + ',' + str(list[1]))
            lon_in = list[0]
            lat_in = list[1]
            list = gcj02_to_bd09(lon_in,lat_in)
            self.out4.insert('insert', str(list[0]) + ',' + str(list[1]))
        elif 'GCJ02' == type:
            list = gcj02_to_wgs84(lon_in,lat_in)
            self.out2.insert('insert', str(list[0]) + ',' + str(list[1]))
            lon_in = list[0]
            lat_in = list[1]
            list = wgs84_to_nmea0183(lon_in,lat_in)
            self.out1.insert('insert', str(list[0]) + ',' + str(list[1]))
            list = wgs84_to_bd09(lon_in,lat_in)
            self.out4.insert('insert', str(list[0]) + ',' + str(list[1]))
            self.out3.insert('insert', self.input.get())
        elif 'BD09' == type:
            self.out4.insert('insert', self.input.get())
            list = bd09_to_gcj02(lon_in,lat_in)
            self.out3.insert('insert', str(list[0]) + ',' + str(list[1]))
            lon_in = list[0]
            lat_in = list[1]
            list = gcj02_to_wgs84(lon_in,lat_in)
            self.out2.insert('insert', str(list[0]) + ',' + str(list[1]))
            lon_in = list[0]
            lat_in = list[1]
            list = wgs84_to_nmea0183(lon_in,lat_in)
            self.out2.insert('insert', str(list[0]) + ',' + str(list[1]))

if __name__ == '__main__':
    win = Window()
    win.mainloop()

    
