import cairosvg
import os

inputFolder = "D:/Code/Python/Svg2Png/input"    #输入的文件夹，里面有svg
outputFolder = "D:/Code/Python/Svg2Png/output"  #输出的文件夹，将把结果放到此文件夹中

for root, dirs, files in os.walk(inputFolder):#遍历所有的文件
	for f in files:
		svgFile = os.path.join(root,f)  #svg文件名
		if f[-3:] == "svg":#确保是svg
			pngFile = outputFolder + "/" + f.replace("svg","png") #png文件名
			try: 
				cairosvg.svg2png(url=svgFile, write_to=pngFile, dpi=1900)
			except:
				print('error =>' + pngFile)
			finally:
				print('file => ' + pngFile)
