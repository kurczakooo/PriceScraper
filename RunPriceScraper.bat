@echo off
conda activate PriceScraper
python main.py
if %errorlevel% neq 0 (
    echo There was an error running the script.
) else (
    echo Script executed successfully.
)
pause
conda deactivate
