@echo off
chcp 65001 >nul
title CyberGuard Expert - Build EXE
where py >nul 2>nul
if errorlevel 1 (
  echo Python غير مثبت. ثبته من https://www.python.org/downloads/windows/ ثم أعد تشغيل الملف.
  pause
  exit /b 1
)
py -m pip install --upgrade pyinstaller
pyinstaller --noconfirm --clean --onefile --windowed --name CyberGuard_Expert --add-data "knowledge_base.json;." main.py
if errorlevel 1 (
  echo حدث خطأ أثناء البناء.
  pause
  exit /b 1
)
echo تم إنشاء الملف: dist\CyberGuard_Expert.exe
pause
