@echo off
cd /d %~dp0ecommerce
echo === Lab 5: Ecommerce - Start ===
echo.
echo [1/4] Installing required packages...
py -m pip install pillow --quiet
echo.
echo [2/4] Running migrations...
py manage.py makemigrations store
py manage.py migrate
echo.
echo [3/4] Loading sample data (5 categories, 11 products)...
py manage.py shell < load_data.py
echo.
echo [4/4] Starting server...
echo Open browser: http://127.0.0.1:8000/
echo Admin panel:  http://127.0.0.1:8000/admin/
echo (Superuser: run "py manage.py createsuperuser" once if you need admin)
echo.
py manage.py runserver
pause
