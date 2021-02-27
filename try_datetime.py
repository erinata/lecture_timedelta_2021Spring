import pandas
from datetime import datetime

import numpy

dataset = pandas.read_csv("chicago_crime_2018.csv")
dataset = dataset.sample(frac=0.1).reset_index(drop=True)

# print(dataset)

# print(dataset['Date'])

dataset['Date'] = pandas.to_datetime(dataset['Date'])

# print(dataset['Date'])

dataset['year'] = dataset['Date'].dt.year
dataset['month'] = dataset['Date'].dt.month
dataset['hour'] = dataset['Date'].dt.hour
dataset['minute'] = dataset['Date'].dt.minute

# print(dataset[['Date', 'year', 'month', 'hour']])


dataset['hour_slot'] = numpy.select([
	(dataset['hour'] < 4),
	(dataset['hour'] < 8),
	(dataset['hour'] < 12),
	(dataset['hour'] < 16),
	(dataset['hour'] < 20),
	(dataset['hour'] < 24)]
	, [0,1,2,3,4,5])


# print(dataset[['Date', 'hour', 'hour_slot']])


dataset['minute_slot'] = numpy.select([
	(dataset['minute'] < 15),
	(dataset['minute'] < 30),
	(dataset['minute'] < 45),
	(dataset['minute'] < 60)]
	, [0,1,2,3])

dataset['minutes_slot_in_day'] = dataset['hour']*4 + dataset['minute_slot'] 


# dataset['diff'] = dataset['Date'] - datetime(2018,1,24,0,0,0)

# print(dataset[['Date', 'diff']])

time_block_dataset=pandas.DataFrame()
time_block_dataset['time_in_day'] = numpy.arange(0,96,1)

print(time_block_dataset)

print(sum((    dataset['minutes_slot_in_day'] == 1      )*1))




