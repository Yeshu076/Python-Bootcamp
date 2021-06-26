# create and import module
import Day11_MYMODULE as m

m.mymodule("Vjn")

# _____________________________________________________________________________________________________________________
# install panda and and import it
pip install pandas
import pandas as pd
print("installed pandas version:", pd.__version__)

# ---------------------------------------------------------------------------------------------------------------------
# program to print random number using module
import random as r

print("random number between 1 to 100 :", r.randint(1, 100))

# -----------------------------------------------------------------------------------------------------------------------
# import sys package and find python path
import sys

for p in sys.path:
    print(p)
# ----------------------------------------------------------------------------------------------------------------
# unistall pandas using pip
pip uninstall pandas

# ----------------------------------------------------------------------------------------------------------------
