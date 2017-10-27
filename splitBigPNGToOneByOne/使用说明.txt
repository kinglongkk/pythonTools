1、准备
	1、安装 TexturePacker
	2、安装python
	3、安装Pillow-2.1.0.win-amd64-py2.7.exe 

2、PVR转PNG.bat的使用
	把 xx.plist和xx.pvr.ccz 文件放在工具目录下，直接双击“PVR转PNG.bat”
	批处理文件，如果成功的话，在当前目录下就会生成相应的.png文件，这个批处理
	可同时转化很多对（xx.plist和xx.pvr.ccz）文件，当然，也有可能失败，
	如果失败，我们可以使用另一种方式转化，直接使用TexturePacker工具。
3、使用TexturePacker工具把xx.plist和xx.pvr.ccz转化为.png
    1. TexturePacker中有个PVR Viewer工具，我们可以直接使用这个工具
       进行转化。
    2. 使用PVR Viewer工具打开我们要转化的文件，然后点击File下的Save As，
    保存为.png文件即可，保存时把文件的后缀名添加上.png即可。
4、使用split.py脚本 - 将Texture Packer制作的.pvr.ccz和.plist文件还原为多个原图
    1. split.py脚本只能通过.png和.plist文件还原，而不能直接通过.pvr.ccz和.plist文件，
    所以需要根据2和3中的方法把xx.plist和xx.pvr.ccz转化为.png
    2. 在Dos命令行模式下，进入脚本存放目录，同时需要把.png和.plist文件也放在这个
    目录下，而且要确保.png和.plist文件的文件名相同(例：mm.png和mm.plist),
    然后执行split.py脚本，传入参数(例：上面的mm),然后执行即可。
    3. 当然也有可能不成功，因为split.py脚本是通过分析.plist文件，然后对
     .png文件进行切割，保存，如果失败，可以检查一下.plist文件是否正确。