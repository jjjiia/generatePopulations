import random
import copy
import csv

totalPopulation = 500

def generateNetwork(fileName):
	csvReader = csv.reader(open(fileName,"r"))
	csvReader.next()
	
	print fileName.replace("pop_","links_")
	csvWriter = csv.writer(open(fileName.replace(".csv","_links.csv"),"w"))
	csvWriter.writerow(["source","target","Weight"])
	nodes = []
	checked = []
	for row in csvReader:
		nodes.append(row)

	for node1 in nodes:
		id1 = node1[0]
		for node2 in nodes:
			id2 = node2[0]
			if id1!=id2 and [id1,id2].sort not in checked:
				linkStrength = checkPair(node1,node2)
				checked.append([id1,id2].sort)
				if linkStrength >2:
					csvWriter.writerow(["_"+str(id1),"_"+str(id2),linkStrength])
		
		
def checkPair(node1,node2):
	
	matches = 0
	for i in range(len(node1)):
		
		if node1[i]==node2[i] and node1[i]!="NA" and node2[i]!="NA":
			matches+=1
	
	return matches
			
		
	
generateNetwork("web/populations/pop_0.csv")






