@echo off
:: 检查 Python 是否安装
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [错误] Python 未安装或未添加到系统 PATH 环境变量！
    pause
    exit /b
)

:: 使用格式化的 PowerShell 代码创建 GUI 窗口
for /f "tokens=* delims=" %%a in ('powershell -command ^"
    # 加载程序集
    Add-Type -AssemblyName System.Windows.Forms;
    Add-Type -AssemblyName Microsoft.VisualBasic;
    
    # 创建主窗体
    $form = New-Object System.Windows.Forms.Form;
    $form.Text = '创建 Python 虚拟环境';
    $form.Width = 500;
    $form.Height = 220;
    $form.FormBorderStyle = 'FixedDialog';
    $form.StartPosition = 'CenterScreen';
    
    # 虚拟环境名称标签和输入框
    $label1 = New-Object System.Windows.Forms.Label;
    $label1.Text = '虚拟环境名称:';
    $label1.Location = New-Object System.Drawing.Point(20, 30);
    $label1.Width = 120;
    $form.Controls.Add($label1);
    
    $textbox1 = New-Object System.Windows.Forms.TextBox;
    $textbox1.Location = New-Object System.Drawing.Point(150, 30);
    $textbox1.Width = 300;
    $form.Controls.Add($textbox1);
    
    # 存放路径标签和输入框
    $label2 = New-Object System.Windows.Forms.Label;
    $label2.Text = '存放路径:';
    $label2.Location = New-Object System.Drawing.Point(20, 80);
    $label2.Width = 120;
    $form.Controls.Add($label2);
    
    $textbox2 = New-Object System.Windows.Forms.TextBox;
    $textbox2.Location = New-Object System.Drawing.Point(150, 80);
    $textbox2.Width = 250;
    $form.Controls.Add($textbox2);
    
    # 浏览按钮（尺寸调小）
    $button = New-Object System.Windows.Forms.Button;
    $button.Text = '浏览...';
    $button.Location = New-Object System.Drawing.Point(410, 80);
    $button.Width = 60;  # 宽度从80减小到60
    $button.Height = 24; # 设置固定高度
    $button.Add_Click({
        $folder = New-Object System.Windows.Forms.FolderBrowserDialog;
        $folder.Description = '选择存放路径';
        if ($folder.ShowDialog() -eq 'OK') { 
            $textbox2.Text = $folder.SelectedPath;
        }
    });
    $form.Controls.Add($button);
    
    # 确定按钮（尺寸调小）
    $okButton = New-Object System.Windows.Forms.Button;
    $okButton.Text = '确定';
    $okButton.Location = New-Object System.Drawing.Point(200, 130);
    $okButton.Width = 80;  # 宽度从100减小到80
    $okButton.Height = 24; # 设置固定高度
    $okButton.DialogResult = 'OK';
    $form.AcceptButton = $okButton;
    $form.Controls.Add($okButton);
    
    # 显示对话框并返回结果
    if ($form.ShowDialog() -eq 'OK') { 
        Write-Output ($textbox1.Text + '|' + $textbox2.Text);
    } else { 
        Write-Output 'cancel|cancel';
    }
"') do (
    set "user_input=%%a"
)

:: 剩余部分保持不变...
:: 检查用户是否取消
if "%user_input%"=="cancel|cancel" (
    echo [错误] 操作已取消！
    pause
    exit /b
)

:: 分割输入结果
for /f "tokens=1,2 delims=|" %%A in ("%user_input%") do (
    set "venv_name=%%A"
    set "venv_path=%%B"
)

:: 检查名称是否为空
if "%venv_name%"=="" (
    echo [错误] 未输入虚拟环境名称！
    pause
    exit /b
)

:: 检查路径是否为空
if "%venv_path%"=="" (
    echo [错误] 未选择存放路径！
    pause
    exit /b
)

:: 组合完整路径
set "full_path=%venv_path%\%venv_name%"

:: 检查路径是否已存在
if exist "%full_path%" (
    echo [错误] 路径 "%full_path%" 已存在！
    pause
    exit /b
)

:: 创建虚拟环境
echo [信息] 正在创建虚拟环境 "%venv_name%"...
python -m venv "%full_path%"

if not exist "%full_path%" (
    echo [错误] 虚拟环境创建失败！
    pause
    exit /b
)

:: 检查 requirements.txt 是否存在（当前目录下）
set "requirements_path=requirements.txt"
if not exist "%requirements_path%" (
    echo [警告] 未找到 "%requirements_path%"，跳过依赖安装。
    goto :env_created
)

:: 安装依赖
echo [信息] 正在安装依赖库...
call "%full_path%\Scripts\activate.bat" && pip install -r "%requirements_path%"

:env_created
echo [成功] 虚拟环境 "%venv_name%" 已创建并配置完成！
echo 路径: "%full_path%"
pause