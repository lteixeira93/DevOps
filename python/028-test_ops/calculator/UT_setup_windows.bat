@echo off

REM Run the tests with coverage
python -m coverage run -m unittest discover

REM Generate the coverage report
python -m coverage html --omit=DisplayViewer.py,test_*.py,main.py

REM Automatically open the report on default browser
start "" htmlcov\index.html
