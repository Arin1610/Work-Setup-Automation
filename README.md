# Work-Setup-Automation
Work Setup Automation - DevOps
A Python script that automates the opening of essential DevOps tools and platforms (AWS, Jenkins, GitHub, Slack, etc.) in Google Chrome. Customize the list of URLs to match your workflow. The project also includes instructions for converting the script into a standalone .exe file for quick execution using PyInstaller.

## Overview

This project automates the process of opening multiple web applications essential for a DevOps professional. By running the script, it automatically opens a list of frequently-used websites in Google Chrome, making the work setup process faster and more efficient.

## Features

- Automatically launches multiple work-related web applications.
- Configurable URLs: Easily customize the URLs based on your work environment.
- Uses `PyInstaller` to convert the script into a `.exe` for instant execution.

## Requirements

- Python 3.x installed on your machine.
- Google Chrome browser installed.
- `PyInstaller` for converting the Python script into an executable.

The script automatically opens the following URLs in Google Chrome:
- YouTube
- GitHub
- AWS Management Console
- Jenkins
- Slack
- Terraform

### Converting to an Executable (.exe)

1. Use `PyInstaller` to convert the Python script into an executable file:
    ```bash
    pyinstaller --onefile work_setup_automation.py
    ```

2. After running the above command, the `.exe` file will be created in the `dist/` directory of your project folder.

3. You can now double-click the `.exe` file to instantly open all your required URLs in Google Chrome.


- Once the script is converted to an `.exe` file, you can open it instantly without needing to run the Python script each time.
- Double-click the `.exe` file, and all your work-related websites will open automatically in Google Chrome.

