import csv
import json


for i in range(0,14):
	csvReader = csv.reader(open("pop_all_"+str(i)+".csv","r"))
	for row in csvReader:
		header = row
		break
	
	pop = {}
	#csvReader.next()
	for row in csvReader:
		#print row
		uid = row[0]
		entry = {}
		for h in range(len(header)):
			#print header[h],row[h]
			if h!=0:
				entry[header[h]]=row[h]
		pop[uid]=entry
				
	print pop.keys()[3], pop[pop.keys()[3]]
		#break
		
	with open("pop_"+str(i)+".json", "w") as outfile:
	    json.dump(pop, outfile)