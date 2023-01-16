import pandas as pd
import numpy as np

#a)
html_data = pd.read_html('https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table')

#b)
#print(len(html_data))

#c)
#print(html_data[2])

#d)
#data_table = pd.DataFrame(html_data[2])
#print(data_table)

#e)
data_table = pd.DataFrame(html_data[2])
top20 = pd.DataFrame(data_table.head(20))
print(top20)