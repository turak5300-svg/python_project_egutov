qqq = float(input('qqq = '))
www = int(input('www = '))
eee = 1.0
for _ in range(www):
    eee *= qqq
print('qqq^www =', eee)

@echo off title Zapysk program
echo Zapyskay...
start iexplore.exe
start notepad.exe
start calc.exe
echo Готово!
pause

@echo off
dir /b /a-d *.* > "&USERNAME&.txt"
echo Поиск завершён. Результат в файле "&USERNAME&.txt"
pause

@echo off
set "TEMP_DIR=%TEMP%"
dir "%TEMP_DIR%" > "%USERPROFILE%\Desktop\Temp_clean.txt"
del /q /f /s "%TEMP_DIR%\*.*"
echo VPEMPNNIE FAILI YDALENT. SPISOK v Temp_clean.txt
pause

@echo off
md "C:\\COLLEGE_OS\\laboratory_work\\LR_1"
md "C:\\COLLEGE_OS\\laboratory_work\\LR_2"
md "C:\\COLLEGE_OS\\laboratory_work\\LR_3"
md "C:\\COLLEGE_OS\\term papers\\1_ course"
md "C:\\COLLEGE_OS\\term papers\\2_ course"
md "C:\\COLLEGE_OS\\report"
echo Struktura sozdana!
pause