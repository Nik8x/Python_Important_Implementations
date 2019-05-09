# check whether a package is present, if not install
x = !pip list
if any(str(x == 'xgboost')):
    pass
else:
    !pip install xgboost

## or

# to automatically check package & install if not present
import sys
import types
import pip

if pip.__version__ >= "10.0.0":
    from pip._internal.utils.misc import get_installed_distributions
else:
    from pip import get_installed_distributions
    
if not('xgboost' in [package.project_name for package in get_installed_distributions()]):
    !pip install xgboost -q
