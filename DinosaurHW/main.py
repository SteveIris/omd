import pandas as pd

URL = "https://raw.githubusercontent.com/kjanjua26/jurassic-park/main/data/data.csv"
data = pd.read_csv(URL, header=0)
cols = [0, 1, 3]
relevant_data = data[data.columns[cols]]
print(relevant_data.head())