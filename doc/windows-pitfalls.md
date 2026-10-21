1.在Windows环境下中文字符编码问题，python是默认是GBK根式，我们统一成UTF-8模式，可以适配各种操作系统环境，可以用如下命令永久配置用户级别的UTF-8格式：
[Environment]::SetEnvironmentVariable("PYTHONUTF8", "1", "User")
可以用如下命令监测是否配置成功：
python -c "import sys;print(sys.getdefaultenconding())"
如果输出：utf-8
说明配置成功

2.在Windows环境下路径分隔符的问题
任何时候不要尝试用转义符去拼接路径字符串，非常容易出错，统一直接还用pathlib,如：
from pathlib import Path

DB_PATH=Path(_file_).parent / "lab.db"

3.在Windows环境下不要尝试在终端直接发中文请求，会因为编码问题导致出错，直接用页面上的/docs里面的按钮发送请求

4.发现服务端口被占用的时候请尝试如下命令找到占用端口的进程：
netstat -ano | findstr :8000
显示结果的最后一列就是进程的PID
用如下命令杀掉这个进程即可释放端口：
taskkill /F /PID 

5.在Windows环境下,python对大小写不敏感，但是在linux环境下是敏感，为了避免代码跨平台运行时出现不必要的错误，从现在开始，约定编码规范，文件名全部小写，import 严格对照真实大小写，不依靠IDE自动补全掩盖错误。