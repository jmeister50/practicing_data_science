import matplotlib.pyplot as plt

def plot_line_graph(input_values, squares, style, title, x_label, y_label):
	"""Simple example of ploting line graph"""

	plt.style.use(style)
	fig, ax = plt.subplots()
	ax.plot(input_values, squares, linewidth=3)

	# Set chart title and label axes.
	ax.set_title(title, fontsize=24)
	ax.set_xlabel(x_label, fontsize=14)
	ax.set_ylabel(y_label, fontsize=14)

	# Set size of tick labels.
	ax.tick_params(axis='both', labelsize=14)

	plt.show()

def plot_scatter():
	"""Simple example of ploting a scatter plot"""

	x_values = [1, 2, 3, 4, 5, 6]
	y_values = [2, 3, 4, 5, 6, 7]

	plt.style.use('seaborn-darkgrid')
	fig, ax = plt.subplots()
	ax.scatter(x_values, y_values, s=100)

	#Set chart title and label axes.
	ax.set_title("Square Numbers", fontsize=25)
	ax.set_xlabel("Value", fontsize=14)
	ax.set_ylabel("Square of Values", fontsize=14)

	#Set size of tick labels.
	ax.tick_params(axis='both', which='major', labelsize=14)

	plt.show()

if __name__ == "__main__":
	plot_line_graph(
		[1, 2, 3, 4, 5],
		[1, 4, 9, 16, 25],	
		'fivethirtyeight',
		'Square Numbers',
		'Square of Value',
		'Value')
	#plot_scatter()
