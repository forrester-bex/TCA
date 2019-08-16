import pandas
import glob
import numpy as np

rankedlist = 'data_cleaned_v2.refactor.rankedlist.txt'
ranked = []

with open(rankedlist, 'r') as r:
	for line in r:
		cpg = line.strip('\n')
		ranked.append(cpg)

# create a list of the top 100 discriminatory cpgs
top = ranked[:100]

filelist = glob.glob('ct[1-6].csv')


celltypes = []


for file in filelist:
	final = []
	with open(file, 'r') as matrix:
		counter = 0
		for line in matrix:
			if counter != 0:
				line_split = line.strip('\n').split(',')
				data = line_split[1:]
				cpg = line_split[0].strip('"')
				data = [float(i) for i in data]
				mean = np.mean(data)
				if cpg in top:
					final.append([cpg, mean])
			counter += 1
	celltypes.append(final)

finalframes = []
for entry in celltypes:
	newdf = pandas.DataFrame(entry)
	newdf = newdf.set_index(0)
	finalframes.append(newdf)

counter = 1
for entry in finalframes:
	entry.to_csv("celltype"+str(counter)+'top100.csv')
	counter += 1