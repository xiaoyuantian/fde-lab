1.这是一个用FastAPI+SQLLite演示【请求--代码--存储】最小链路实验项目
2.如何在本地运行起来
    先检查系统没有安装uv  可以用使用uv --version命令查看，如果出现uv的版本号说明安装成功
    如果未安装请自行搜索uv如何安装

    克隆代码到本地，命令终端计入本地目录，项见如下示例：
    C:\dev>git clone git@github.com:xiaoyuantian/fde-lab.git _verify  //克隆代码
    C:\dev>cd _verify                                                 //进入项目目录
    C:\dev\_verify>uv sync                                            //同步代码
    C:\dev\_verify>uv run uvicorn main:app --reload                   //启动项目
    即可在浏览器输入这个地址：http://127.0.0.1:8000/students进行验证
3.如何调试
    调试配置文件在这里.vscode\launch.json
    在vscode下可以直接按F5键进入调试模式
4.项目实现过程中踩过的坑可以参加doc\windows-pitfalls.md这个文件