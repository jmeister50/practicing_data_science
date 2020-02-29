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

def plot_scatter(x_lower_bound, x_upper_bound, plt_style, title, x_label, y_label):
	"""Simple example of ploting a scatter plot"""

	x_values = range(x_lower_bound, x_upper_bound)
	y_values = [x**2 for x in x_values]

	plt.style.use(plt_style)
	fig, ax = plt.subplots()
	ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, s=10)

	#Set chart title and label axes.
	ax.set_title(title, fontsize=25)
	ax.set_xlabel(x_label, fontsize=14)
	ax.set_ylabel(y_label, fontsize=14)

	#Set size of tick labels.
	ax.axis([0, 1000, 0, 1100000])

	plt.show()

if __name__ == "__main__":
	"""plot_line_graph(
		[1, 2, 3, 4, 5],
		[1, 4, 9, 16, 25],	
		'fivethirtyeight',
		'Square Numbers',
		'Square of Value',
		'Value')"""
	plot_scatter(
	1,1000,'seaborn-darkgrid',
	'Square Numbers','Square of Value',
	'Value')
