# Deep Eutectic Solvent (DES) Polarity and pH Prediction System - Installation and User Guide
============================================================

## Important Notes
This software only supports the Windows x64 operating system.
Python 3.12 must be installed (as the core algorithms have been compiled specifically for this version).

## Step 1: Environment Setup
Ensure that Python 3.12 is installed on your computer.  
Download link: https://www.python.org/downloads/  
Be sure to check the box "Add Python to PATH" during installation

Install the required dependencies using the following packages:

```plaintext
# Core framework
streamlit

# Common machine learning libraries
numpy
pandas
scikit-learn
xgboost

# Deep learning libraries (based on your .pth files)
torch
torchvision

# For plotting (if used in the project)
matplotlib
```

## Step 2: Run the Software

### Required Files
Download all project files, including:
- app.py
- predictor.cp312-win_amd64.pyd
- model_utils.cp312-win_amd64.pyd
- *.pth / *.pkl (model weight and serialized files)

### Execution Steps
1. Hold down the Shift key and right-click in the project folder, then select "Open PowerShell window here" or "Open CMD window here".
2. Enter the command:  
   ```bash
   streamlit run app.py
   ```
