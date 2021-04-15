'''

https://pandas.pydata.org/docs/user_guide/io.html#excel-files


Excel files


The read_excel() method can read Excel 2007+ (.xlsx) files using the openpyxl Python module.

Excel 2003 (.xls) files can be read using xlrd.

Binary Excel (.xlsb) files can be read using pyxlsb.

The to_excel() instance method is used for saving a DataFrame to Excel.

Generally the semantics are similar to working with csv data.

'''
import pandas as pd

# Load a comma separated file (CSV file) into a DataFrame:
df = pd.read_excel('Model-load-template.xlsx', na_values=["NA"], usecols="A:G")

print(df)

