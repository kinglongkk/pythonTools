# pythonTools

需求来源：
研究微博最新登陆密码加密方式为rsa2，python里面需要装rsa模块才能用。
安装rsa模块，需要用easy_install安装。
要用easy_install，就要装setuptools。
概念简介：
setuptools
是 Python Enterprise Application Kit（PEAK）的一个副项目，可以让程序员更方便的创建和发布 Python 包。
easy_install
当需要安装第三方python包时，可能会用到easy_install命令。easy_install是由PEAK(Python Enterprise 
Application 
Kit)开发的setuptools包里带的一个命令，所以使用easy_install实际上是在调用setuptools来完成安装模块的工作。
安装：
windows下：
下载ez_setup.py
调用相应版本的python ez_setup.py执行。
我装了两个版本python，2.7和3.2，都set了环境变量中的path。
当我用python27 ez_setup.py，则自动在该版本安装目录下产生Scripts 目录，并将安装的东西放在那。
用python32 ez_setup.py，则在32版本的目录下产生安装文件。
linux下：
比如ubuntu系列的
复制代码
代码如下:
# apt-get install 
python-setuptools
使用：
安装模块：
复制代码
代码如下:
easy_install package-name
卸载模块：
复制代码
代码如下:
easy_install -m package-name
但卸载后还要手动删除遗留文件
安装rsa-3.1.1-py2.7.egg：
下载rsa-3.1.1-py2.7.egg
切换目录
执行命令：
复制代码
代码如下:
easy_install.exe rsa-3.1.1-py2.7.egg

安装xlrd-1.0.0
C:\Python27\Excel\xlrd-1.0.0>python setup.py install
