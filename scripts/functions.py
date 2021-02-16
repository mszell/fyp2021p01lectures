def barplot(data, field_name, field_categories):
	"""Make a bar plot of a categorical variable, given as a field field_name in the
	structured array data. Field categories and their names are given in the dict field_categories.
	"""

	categories, counts = np.unique(data[field_name], return_counts=True)

	fig = plt.figure(figsize=(4, 3))
	axes = fig.add_axes([0, 0, 1, 1]) # left, bottom, width, height (range 0 to 1)
	axes.bar(range(len(categories)), counts, fc="gray") # fc is the face color

	axes.set_xlabel("")
	axes.set_ylabel('Count')
	axes.set_title(field_name)
	fig.autofmt_xdate(rotation=45)

	axes.set_xticks(range(len(categories)))
	axes.set_xticklabels(field_categories.values());

print("Loaded functions.\n")