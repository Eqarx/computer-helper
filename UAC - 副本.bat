@echo off
:获取管理员权限
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
:保持当前目录下运行
cd /d "%~dp0"

cd D:\