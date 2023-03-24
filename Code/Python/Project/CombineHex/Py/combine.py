
import os.path
import sys
import datetime
import tkinter.filedialog
import tkinter.messagebox


def get_version(path):
    file = open(path,encoding='utf-8')
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

def read_file(path):
    file = open(path,encoding='utf-8')
    lines =  file.readlines()
    return lines

#def resourcepath():
#    if hasattr(sys,'_MEIPASS'):
#        return sys._MEIPASS

def write_file(boot_path,app_path,boot_val,ver_head):
    #p = resourcepath()
    #print(p)
    app_complete = ':020000040801F1\n:04DFFC005A5A5A5AB9\n'
    date = datetime.datetime.now().strftime('%Y%m%d')
    version = get_version(app_path)
    if boot_val == 1 :
        #boot_file_name = '\\SDAU_BL_SV11.hex'
        ba_file_name = '\\FC-686B1JQ_HK32_ALL_HVB1'+version[2:]+'_SV'+ver_head
    else :
        #boot_file_name = '\\SDAU_BL_SV12.hex'
        ba_file_name = '\\FC-686B1ZX_HK32_ALL_HVB1'+version[2:]+'_SV'+ver_head
    file_path = os.path.dirname(os.path.realpath(sys.argv[0])) + ba_file_name + version[0:2] + '_' + date + '.hex'
    lines = read_file(boot_path)
    file = open(file_path,'w')
    for x in range(0,len(lines)-2):
        file.write(lines[x])
    lines = read_file(app_path)
    x = 0 
    for x in range(0,len(lines)):
        if x == len(lines)-2 :
            file.write(app_complete)
            file.write(lines[x])
        else:
            file.write(lines[x])
    file.close()

top = tkinter.Tk()
top.geometry('200x120')
top.title('hex文件自动拼接1.1')
boot_path = tkinter.StringVar()
app_path = tkinter.StringVar()
boot_val = tkinter.IntVar()
ver_head = tkinter.StringVar()
ver_head.set('55')

def selectbootfileCallback(path):
    path = tkinter.filedialog.askopenfilename()
    boot_path.set(path)
    
def selectappfileCallback(path):
    path = tkinter.filedialog.askopenfilename()
    app_path.set(path)

def combineCallback(boot_path,app_path,boot_val,ver_head):
    write_file(boot_path,app_path,boot_val,ver_head)
    tkinter.messagebox.showinfo('提示','成功!')

l1 = tkinter.Label(top,text = '软件版本高位字节:',font=("Microsoft YaHei Mono", 10))
l1.grid(row = 0,column = 0,sticky = tkinter.S)
e1 = tkinter.Entry(top,width = 6,textvariable = ver_head)
e1.grid(row = 0,column = 1,sticky = tkinter.S)
a1 = tkinter.Radiobutton(top,text = '钜泉',variable = boot_val, value = 1)
a1.grid(row = 1,column = 0,sticky = tkinter.S)
a2 = tkinter.Radiobutton(top,text = '智芯',variable = boot_val, value = 2)
a2.grid(row = 1,column = 1,sticky = tkinter.S)
b1 = tkinter.Button(top, text ="选择BOOT文件", command = lambda:selectbootfileCallback(boot_path))
b1.grid(row = 2,column = 0,padx = 7,sticky = tkinter.N,ipadx = 5, pady = 2)
b2 = tkinter.Button(top, text ="选择APP文件", command = lambda:selectappfileCallback(app_path))
b2.grid(row = 3,column = 0,padx = 7,sticky = tkinter.N,ipadx = 11, pady = 2)
b3 = tkinter.Button(top, text ="开始合并", command = lambda:combineCallback(boot_path.get(),app_path.get(),boot_val.get(),ver_head.get()))
b3.grid(row = 2,column = 1, sticky = tkinter.N+tkinter.S,rowspan=2,ipadx = 7, padx = 4)


top.mainloop()
