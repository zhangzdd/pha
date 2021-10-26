echo off
rem RunS2.bat
rem 同时并行运行多个程序
set cmd1=usb_c.exe
set cmd2=python3 logic.py
start %cmd1%
start %cmd2%