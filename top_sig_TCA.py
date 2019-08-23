import pandas 
import glob
import numpy as np

cpgs = "cpglist.csv"

cpg_list = []
with open(cpgs, 'r') as myfile:
	for line in myfile:
		cpg = line.split(",")[1].strip('\n').strip('"')
		cpg = cpg.replace('"','')
		cpg_list.append(cpg)

filelist = glob.glob('pvalct[1-6].csv')

celltypes = []


for file in filelist:
	final = []
	with open(file, 'r') as matrix:
		counter = 0
		for line in matrix:
			if counter != 0:
				line_split = line.strip('\n').split(',')
				pval = float(line_split[1])
				final.append(pval)
			counter += 1
	celltypes.append(final)


final_final = []
for celltype in celltypes:
	celltype_final = []
	counter = 0
	for pval in celltype:
		cpg = cpg_list[counter]
		celltype_final.append([cpg, pval])
		counter +=1
	final_final.append(celltype_final)




final = []
for celltype in final_final:
	mylist = celltype
	mylist.sort(key=lambda x: x[1])
	finalcelltype = mylist[:100]
	final.append(finalcelltype)

finalframes = []
for entry in final:
	newdf = pandas.DataFrame(entry)
	newdf = newdf.set_index(0)
	finalframes.append(newdf)

counter = 1
for entry in finalframes:
	entry.to_csv("celltype"+str(counter)+'top100significant_TCA.csv')
	cpgs = entry.index
	with open("celltype"+str(counter)+'top100significant_TCA_aslist.csv','w') as out:
		out.write('\n'.join(cpgs))
	out.close()
	counter += 1
