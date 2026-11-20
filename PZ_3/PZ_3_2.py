year = int(input('Введите год:'))
if year % 400 == 0: #Проверка на високосный год если делится на 400 (2000, 1600)
    days = 366
elif year % 100 == 0: #Проверка на не високосный год если делится на 100 (1900, 2100)
    days = 365
elif year % 4 == 0: #Проверка на високосный год если делится на 4 (2024, 2028)
    days = 366
else: # а астальное это вор всех остальных случаях
    days = 365
print(f"B {year} году {days} дней")

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