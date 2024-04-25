
import pandas as pd
import matplotlib.pyplot as plt



data_read = pd.read_excel('test.xls', usecols=['col1', 'col2'])
print(data_read)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
plt.plot(x, data_read["col1"])
plt.plot(x, data_read["col2"])
plt.show()