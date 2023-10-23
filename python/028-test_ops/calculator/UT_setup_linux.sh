#!/bin/bash

# Run the tests with coverage
python -m coverage run -m unittest discover

# Generate the coverage report
python -m coverage html --omit=DisplayViewer.py,test_*.py,main.py


# Automatically open the report on default browser
open htmlcov/index.html