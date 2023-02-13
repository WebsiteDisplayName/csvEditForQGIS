

# import csv file
# delete second row
# create additional column
from tkinter import filedialog as fd
import pandas as pd
filename = fd.askopenfilename(
    title="Select file", filetypes=(("CSV Files", "*.csv"),))

lines = open(filename, 'r').readlines()
lines.pop(1)
open(filename, 'w').writelines(lines)

csvFile = pd.read_csv(filename)
# csvFile["GEO_ID2"] = csvFile["GEO_ID"].str.split("US")[1]
csvFile["GEO_ID2"] = csvFile["GEO_ID"].apply(
    lambda x: pd.Series(str(x).split("US")[1]))
csvFile = csvFile.loc[:, ~csvFile.columns.str.match("Unnamed")]
csvFile.to_csv(filename, index=False)
