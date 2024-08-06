# import subprocess
# import sys

# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# # List of required packages
# required_packages = [
#     'numpy==1.21.2',
#     'pandas==1.3.3',
#     'scikit-learn==0.24.2'
# ]

# # Install packages
# for package in required_packages:
#     try:
#         __import__(package.split('==')[0])
#     except ImportError:
#         install(package)


import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font
filepath = 'Samplefile.xlsx'
wb = load_workbook(filepath)
sheet = wb.active

