import csv
import matplotlib.pyplot as plt 
from datetime import datetime


filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	for index, column_header in enumerate(header_row):
		print(index,column_header)

	# Get high temperatures, dates and lows from this file.
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		low = int(row[6])
		dates.append(current_date)
		highs.append(high)
		lows.append(low)

	#Plot the high temps and low temps.
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(dates, highs, c='red',alpha=.5)
	ax.plot(dates, lows, c='blue',alpha=.5)
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)
	ax.plot(dates, highs, c='red')
	ax.plot(dates, lows, c='blue')

	#Format Plot.
	plt.title("Daily High and Low Temperatures-2018", fontsize=24)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.tick_params(axis='both', which='major',labelsize=16)

	plt.show()

