import os
import os.path
import sys
import datetime
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import ctypes 

def resource_path(relative):
    """ Gets the resource's absolute path.

    :param relative: the relative path to the resource file.
    :return: the absolute path to the resource file.
    """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)

    abspath = os.path.abspath(os.path.join(__file__, ".."))
    abspath = os.path.dirname(abspath)
    return os.path.join(abspath, relative)

class Window(tkinter.Frame):
    def __init__(self,master = None):
        tkinter.Frame.__init__(self,master)
        self.tsBootPath = tkinter.StringVar()
        self.tsAppPath = tkinter.StringVar()
        self.tsVerHead = tkinter.StringVar()
        self.tiTypeVer = tkinter.IntVar()
        self.tsVerHead.set('55')
        self.grid()
        self.cratewindow()

    def cratewindow(self):
        self.master.geometry('200x120')
        self.master.title('Hex文件拼接2.0')
        self.master.iconbitmap(resource_path('hex.ico'))
        self.l1 = tkinter.Label(self.master,text = '软件版本高位字节:',font=("Microsoft YaHei Mono", 10))
        self.l1.grid(row = 0,column = 0,sticky = tkinter.S)
        self.e1 = tkinter.Entry(self.master,width = 6,textvariable = self.tsVerHead)
        self.e1.grid(row = 0,column = 1,sticky = tkinter.S)
        self.a1 = tkinter.Radiobutton(self.master,text = '钜泉',variable = self.tiTypeVer, value = 1)
        self.a1.grid(row = 1,column = 0,sticky = tkinter.S)
        self.a2 = tkinter.Radiobutton(self.master,text = '智芯',variable = self.tiTypeVer, value = 2)
        self.a2.grid(row = 1,column = 1,sticky = tkinter.S)
        self.b1 = tkinter.Button(self.master, text ="选择BOOT文件", command = lambda:self.selectbootfileCallback(self.tsBootPath))
        self.b1.grid(row = 2,column = 0,padx = 7,sticky = tkinter.N,ipadx = 5, pady = 2)
        self.b2 = tkinter.Button(self.master, text ="选择APP文件", command = lambda:self.selectappfileCallback(self.tsAppPath))
        self.b2.grid(row = 3,column = 0,padx = 7,sticky = tkinter.N,ipadx = 11, pady = 2)
        self.b3 = tkinter.Button(self.master, text ="开始合并", command = lambda:self.combineCallback(self.tsBootPath.get(),self.tsAppPath.get(),self.tiTypeVer.get(),self.tsVerHead.get()))
        self.b3.grid(row = 2,column = 1, sticky = tkinter.N+tkinter.S,rowspan=2,ipadx = 7, padx = 4)
    
    #选择Boot.hex文件
    def selectbootfileCallback(self,path):
        path = tkinter.filedialog.askopenfilename()
        self.tsBootPath.set(path)
    
    #选择App.hex文件
    def selectappfileCallback(self,path):
        path = tkinter.filedialog.askopenfilename()
        self.tsAppPath.set(path)

    
    #合并Boot.hex、App.hex文件
    def combineCallback(self,boot_path,app_path,type_val,ver_head):
        hexfile_obj = HexFile(boot_path,app_path,type_val,ver_head)
        hexfile_obj.combine_hex()
        hexfile_obj.generate_dat()
        tkinter.messagebox.showinfo('提示','成功!')



class HexFile(object):
    def __init__(self, bfp:str, afp:str, nt:int, vh:str):
        self.path = {
            'boot_full_path':bfp,
            'boot_dir_path':'',
            'boot_name':'',
            'app_full_path':afp,
            'app_dir_path':'',
            'app_name':'',
            'name_type':nt,
            'ver_head':vh,
            'target_dir':'',
            'target_name_without_extension':'',
            'app_complete_str':':020000040801F1\n:04DFFC005A5A5A5AB9\n'
        }
        (self.path['boot_dir_path'],self.path['boot_name']) = os.path.split(bfp)
        (self.path['app_dir_path'],self.path['app_name']) = os.path.split(afp)
        self.path['target_dir'] = self.path['app_dir_path']
        self.path['target_name_without_extension'] = self.generate_nanme()
        
        
        
    def get_version(self) ->list:
        file = open(self.path['app_full_path'],encoding='utf-8')
        lines =  file.readlines()
        for line in lines:
            if '76657273696F6E3A' in line:
                break
        for x in range(0, len(line) - 3):
            if line[x] == '6' and line[x+1] == 'E' and line[x+2] == '3' and line[x+3] == 'A' :
                version = line[x+4:x+8]
                break
            else :
                version = ['0','0','0','0']
        version = "".join(version)
        return version
    
    def generate_nanme(self) -> str:
        date = datetime.datetime.now().strftime('%Y%m%d')
        version = self.get_version()
        if self.path['name_type'] == 1 :
            name = '\\FC-686B1JQ_HK32_ALL_HVB1'
        else :
            name = '\\FC-686B1ZX_HK32_ALL_HVB1'
        name += version[2:]+'_SV' + self.path['ver_head'] + version[0:2] + '_' + date
        return name
        
    def read_file(self,path):
        file = open(path,encoding='utf-8')
        lines =  file.readlines()
        return lines

    def combine_hex(self):
        #生成拼接文件的全路径
        file_path = self.path['app_dir_path'] + self.path['target_name_without_extension'] + '.hex'
        #读取Boot.hex并创建写入拼接文件
        lines = self.read_file(self.path['boot_full_path'])
        file = open(file_path,'w')
        for x in range(0,len(lines)-2):
            file.write(lines[x])
        #读取App.hex并写入拼接文件，加入程序程序完整性标志
        lines = self.read_file(self.path['app_full_path'])
        x = 0 
        for x in range(0,len(lines)):
            if x == len(lines)-2 :
                file.write(self.path['app_complete_str'])
                file.write(lines[x])
            else:
                file.write(lines[x])
        file.close()

    def generate_dat(self):
        #输入相对路径，获取资源文件绝对路径
        path = resource_path('hextodata_32.dll')
        #相对路径不存在此文件，改用绝对路径
        if not os.path.exists(path):
            path = "D:\\ProgramCode\\Python\\test\\PyRunC\\03-HexToDat\\pyhtd\\hextodata_32.dll"
        #调用资源文件
        htdpy = ctypes.cdll.LoadLibrary(path)
        #将string转为byte类型再传入，如果直接是字符串可以这么转： b'my string'
        htdpy.sub_hex_to_updata(bytes(self.path['app_full_path'],encoding='gbk'))#实际传入的路径可能包含中文，utf-8编码C无法识别，改为gbk
        file =htdpy.get_dat_path()          #获取C返回的字符串首地址
        file = ctypes.c_char_p(file).value  #将字符串转为c_char_p类型，并取其值
        file = str(file,encoding='gbk')   #将bytes型字符串转为str类型（传回的路径编码需要和传入的保持一致）
        newfile =  os.path.split(file)[0] + self.path['target_name_without_extension'] + '.dat'
        if not os.path.exists(newfile):
            os.rename(file, newfile)
        else:
            os.unlink(newfile)
            os.rename(file, newfile)
        print('\n数据转换成功。')


win = Window()
win.mainloop()
