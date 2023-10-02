import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.linear_model import LinearRegression

data = pd.read_csv('austin_cleaned.csv')

X = data.drop(['PrecipitationSumInches'], axis=1)

Y = data['PrecipitationSumInches']
Y = Y.values.reshape(-1, 1)

day_index = 798
days = [i for i in range(Y.size)]

clf = LinearRegression()
clf.fit(X, Y)

input = np.array([[74], [60], [45], [67], [49], [43], [33], [45],
                  [57], [29.68], [10], [7], [2], [0], [20], [4], [31]])

input = input.reshape(1, -1)

print('The precipitation in inches for the input is:', clf.predict(input))
print('The precipitation trend graph: ')

plt.scatter(days, Y, color='b')
plt.scatter(days[day_index], Y[day_index], color='r')
plt.title('Precipitation level')
plt.xlabel('Days')
plt.ylabel('Precipitation in inches')

plt.show()      # Graph of precipitation level vs days

x_f = X.filter(['TempAvgF', 'DewPointAvgF', 'HumidityAvgPercent',
                'SeaLevelPressureAvgInches', 'VisibilityAvgMiles',
                'WindAvgMPH'], axis=1)

print('Precipitation vs selected attributes graph: ')
for i in range(x_f.columns.size):
    plt.subplot(3, 2, i + 1)
    plt.scatter(days, x_f[x_f.columns.values[i][:100]], color='b')
    plt.scatter(days[day_index], x_f[x_f.columns.values[i]]
                [day_index], color='r')
    plt.title(x_f.columns.values[i])

plt.show()      # Graph of precipitation level vs selected attributes
