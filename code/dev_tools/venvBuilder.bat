@echo off

REM This script is used to create a virtual environment for the project

REM Check if Python is installed
where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed
    exit /b
)

REM Check if the venv module is available
python -c "import venv" >nul 2>nul
if errorlevel 1 (
    echo The venv module is not installed
    exit /b
)

REM Check if the venv directory exists
if exist "venv" (
    echo venv directory already exists
    :ask_activate_venv
    set /p activate_venv="Do you want to activate the virtual environment? (y/n): "
    if /i "%activate_venv%"=="y" (
        call venv\Scripts\activate
        exit /b
    ) else if /i "%activate_venv%"=="n" (
        echo Exiting without activating the virtual environment.
        exit /b
    ) else (
        echo Please answer yes (y) or no (n).
        goto ask_activate_venv
    )
    exit /b
)

REM Create the virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Ask user if they want to install the requirements
:ask_install_requirements
set /p install_requirements="Do you want to install the requirements? (y/n): "
if /i "%install_requirements%"=="y" (
    pip install -r requirements.txt
) else if /i "%install_requirements%"=="n" (
    echo Requirements not installed.
) else (
    echo Please answer yes (y) or no (n).
    goto ask_install_requirements
)
