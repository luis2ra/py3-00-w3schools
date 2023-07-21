# @author: https://github.com/luis2ra from https://www.w3schools.com/python/pandas/pandas_getting_started.asp

import pandas as pd

mydataset = {
	'cars': ["BMW", "Volvo", "Ford"],
	'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
