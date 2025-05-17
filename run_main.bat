@echo off
:: 检查Python是否安装
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [错误] Python未安装或未添加到系统PATH环境变量！
    pause
    exit /b
)

:: 检查source/main.py是否存在
if not exist "Source\main.py" (
    echo [错误] 未找到 source\main.py 文件！
    pause
    exit /b
)

:: 运行Python脚本
echo [信息] 正在运行 main.py...
python "Source\main.py"

:: 检查执行结果
if %errorlevel% neq 0 (
    echo [错误] main.py 执行失败！
) else (
    echo [成功] main.py 执行完成
)
pause