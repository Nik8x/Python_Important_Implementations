# check whether a package is present, if not install
x = !pip list
if any(str(x == 'xgboost')):
    pass
else:
    !pip install xgboost
