1.在Windows环境下中文字符编码问题，python默认是GBK编码，我们统一成UTF-8模式，可以适配各种操作系统环境，可以用如下命令永久配置用户级别的UTF-8格式：
[Environment]::SetEnvironmentVariable("PYTHONUTF8", "1", "User")
可以用如下命令监测是否配置成功（注意是 getdefaultencoding，末尾不是 enconding）：
python -c "import sys;print(sys.getdefaultencoding())"
如果输出：utf-8
说明配置成功

2.在Windows环境下路径分隔符的问题
任何时候不要尝试用转义符去拼接路径字符串，非常容易出错，统一直接使用pathlib,如：
from pathlib import Path

DB_PATH=`Path(__file__).parent / "lab.db"`

（注：`__file__` 两边是**两个下划线**，写成 `_file_` 会报 NameError。在 Markdown 里必须用反引号包起来，否则双下划线会被渲染成粗体，显示成 file。）

3.在Windows环境下不要尝试在终端直接发中文请求，会因为编码问题导致出错，直接用页面上的/docs里面的按钮发送请求

4.发现服务端口被占用的时候请尝试如下命令找到占用端口的进程：
netstat -ano | findstr :8000
显示结果的最后一列就是进程的PID
用如下命令杀掉这个进程即可释放端口：
taskkill /F /PID <PID> 

5.在Windows环境下，**文件系统（NTFS）**对大小写不敏感，但是在linux环境下（ext4等）是敏感的。
这里要说准确：这不是python的特性。python本身按字符串精确比较大小写，`Foo` 和 `foo` 是两个完全不同的模块名。
真实机制是 NTFS 在查找文件时不区分大小写，所以你把文件名的大小写写错了也能找到；一旦换到 linux 就会 ModuleNotFoundError。
为了避免代码跨平台运行时出现不必要的错误，从现在开始，约定编码规范，文件名全部小写，import 严格对照真实大小写，不依靠IDE自动补全掩盖错误。