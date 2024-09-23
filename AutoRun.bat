@echo off

REM 运行 RUN 目录中的 prepare.py 文件
python "%~dp0RUN\prepare.py"

REM 读取 RUN 目录中的 filename.txt 文件内容
set /p jar_file=<"%~dp0RUN\filename.txt"

REM 运行 Java 程序，并传入读取的参数
java -jar "%~dp0%jar_file%"