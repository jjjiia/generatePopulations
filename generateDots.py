import random
import copy
import csv

totalPopulation = 500
blackBins = {
"educationOccupationB":{"category":["education","occupation"],
	"grade_school_or_less":{"white_collar_or_skilled":10,"semiskilled":13,"unskilled_domestic_and_personal_service":77,"total":146},
	"some_high_school":{"white_collar_or_skilled":16,"semiskilled":21,"unskilled_domestic_and_personal_service":63,"total":113},
	"high_school_graduate":{"white_collar_or_skilled":27,"semiskilled":24,"unskilled_domestic_and_personal_service":50,"total":59}
	},
"occupationSatisfactionInFieldB":{
	"category":["occupation","satisfactionInField"],
	"white_collar_or_skilled":{"poor":25,"hard_to_say":12,"fair":18,"good":45,"total":40},
	"semiskilled":{"poor":40,"hard_to_say":16,"fair":15,"good":29,"total":55},
	"unskilled_domestic_and_personal_service":{"poor":52,"hard_to_say":17,"fair":10,"good":21,"total":181}
	},
"occupationsatirsfactionInWorkplaceB":{
	"category":["occupation","satisfactionInWorkplace"],
	"white_collar_or_skilled":{"poor":37,"hard_to_say":21,"fair":11,"good":32,"total":40},
	"semiskilled":{"poor":53,"hard_to_say":15,"fair":17,"good":15,"total":55},
	"unskilled_domestic_and_personal_service":{"poor":57,"hard_to_say":16,"fair":11,"good":16,"total":181}
	},
"experienceExpectationsB":{
		"category":["pastExperience","expectations"],
		"biracial_living_experience":{"integration":11,"mutual_acomodation":69,"conflict":20,"total":193},
		"no_biracial_living_experience":{"integration":5,"mutual_acomodation":50,"conflict":45,"total":18}
		},
"evaluationOfHilltownB":{
	"category":["evaluationOfHilltown"],
	"favorable":93,
	"unfavorable":7,
	"total":432
	},
"evaluationOfPhysicalAmenitiesB":{
		"category":["evaluationOfPhysicalAmenities"],
		"favorable":97,
		"unfavorable":3,
		"total":314
	},
"evaluationOfCoResidentsB":{
		"category":["evaluationOfCoResidents"],
		"favorable":85,
		"unfavorable":15,
		"total":75
	},
"evaluationOfManagementB":{
		"category":["evaluationOfManagement"],
		"favorable":79,
		"unfavorable":21,
		"total":43
	},
"impressionOfFriendsB":{
		"category":["impressionOfFriends"],
		"favorable":60,
		"favorableAndUnfavorable":22,
		"noComments":4,
		"unfavorable":14,
		"total":356
	},
"transiencyB":{
		"category":["transiency"],
		"permanent":17,
		"asLongAsEligible":42,
		"neverThoughtAboutIt":17,
		"untilOwnHome":8,
		"untilBetterPlace":16,
		"total":356
	},
"attitudeAttitudeOfFriendB":{
		"category":["attitude","attitudeOfFriend"],
		"liberal":{"liberalFriend":87,"ambivalentFriend":13,"illiberalFriend":0,"total":218},
		"ambivalent":{"liberalFriend":79,"ambivalentFriend":21,"illiberalFriend":0,"total":28},
		"illiberal":{"liberalFriend":1,"ambivalentFriend":0,"illiberalFriend":0,"total":1}
	}
}

whiteBins = {
	"educationOccupationW":{"category":["education","occupation"],
		"grade_school_or_less":{"white_collar_or_skilled":45,"semiskilled":13,"unskilled_domestic_and_personal_service":27,"total":124},
		"some_high_school":{"white_collar_or_skilled":51,"semiskilled":31,"unskilled_domestic_and_personal_service":18,"total":78},
		"high_school_graduate":{"white_collar_or_skilled":58,"semiskilled":32,"unskilled_domestic_and_personal_service":10,"total":85}
	},
	"occupationSatisfactionInFieldW":{
		"category":["occupation","satisfactionInField"],
		"white_collar_or_skilled":{"poor":34,"hard_to_say":5,"fair":15,"good":46,"total":114},
		"semiskilled":{"poor":39,"hard_to_say":13,"fair":18,"good":30,"total":74},
		"unskilled_domestic_and_personal_service":{"poor":40,"hard_to_say":11,"fair":18,"good":31,"total":45}
	},
	"occupationsatisfactionInWorkplaceW":{
		"category":["occupation","satisfactionInWorkplace"],	
		"white_collar_or_skilled":{"poor":36,"hard_to_say":6,"fair":14,"good":44,"total":114},
		"semiskilled":{"poor":46,"hard_to_say":7,"fair":22,"good":25,"total":74},
		"unskilled_domestic_and_personal_service":{"poor":47,"hard_to_say":9,"fair":22,"good":22,"total":45}
	},
	"experienceExpectationsW":{
		"category":["pastExperience","expectations"],
		"biracial_living_experience":{"integration":9,"mutual_acomodation":72,"conflict":19,"total":115},
		"no_biracial_living_experience":{"integration":5,"mutual_acomodation":39,"conflict":56,"total":90}
	},
	"evaluationOfHilltownW":{
		"category":["evaluationOfHilltown"],
		"favorable":68,
		"unfavorable":32,
		"total":503
	},
	"evaluationOfPhysicalAmenitiesW":{
		"category":["evaluationOfPhysicalAmenities"],
		"favorable":80,
		"unfavorable":20,
		"total":317
	},
	"evaluationOfCoResidentsW":{
		"category":["evaluationOfCoResidents"],
		"favorable":40,
		"unfavorable":60,
		"total":137
	},
	"evaluationOfManagementW":{
		"category":["evaluationOfManagement"],
		"favorable":41,
		"unfavorable":59,
		"total":48
	},
	"impressionOfFriendsW":{
		"category":["impressionOfFriends"],
		"favorable":46,
		"favorableAndUnfavorable":13,
		"noComments":7,
		"unfavorable":34,
		"total":357
	},
	"transiencyW":{
		"category":["transiency"],
		"permanent":17,
		"asLongAsEligible":27,
		"neverThoughtAboutIt":14,
		"untilOwnHome":16,
		"untilBetterPlace":26,
		"total":358
	},
	"attitudeAttitudeOfFriendW":{
		"category":["attitude","attitudeOfFriend"],
		"liberal":{"liberalFriend":45,"ambivalentFriend":45,"illiberalFriend":10,"total":82},
		"ambivalent":{"liberalFriend":34,"ambivalentFriend":48,"illiberalFriend":18,"total":108},
		"illiberal":{"liberalFriend":20,"ambivalentFriend":56,"illiberalFriend":24,"total":50}
	}
}





def makeDots(bins,group):
	dots = []
	#print bins["category"]
	if len(bins["category"])==1:
		cat1 = bins["category"][0]
		for b in bins:
			if b!="category" and b!="total":
				count = int(round(bins[b]*.01*bins["total"]))
				for c in range(count):
					did = {cat1:b,"group":group}
					dots.append(did)
		missingEntries = totalPopulation-len(dots)
		#print missingEntries, "missing"
		for m in range(missingEntries):
			did = {cat1:"NA"}
			dots.append(did)
				
	elif len(bins["category"])==2:
		cat1 = bins["category"][0]
		cat2 = bins["category"][1]
	
		for b in bins:
			if b!="category":
				for g in bins[b]:
					if g!="total":
						count = int(round(bins[b][g]*.01*bins[b]["total"]))
						for c in range(count):
							did = {cat1:b,cat2:g,"group":group}
							dots.append(did)
		
		missingEntries = totalPopulation-len(dots)
		#print missingEntries, "missing"
		for m in range(missingEntries):
			did = {cat1:"NA",cat2:"NA","group":group}
			dots.append(did)
							
	shuffledDots = sorted(dots, key=lambda k: random.random())
	return shuffledDots

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z
	
def joinCombinedDots(dots1,dots2,joinByCats,newDots):
	counter = 0
	for d in dots1:
		for d2 in dots2:
			#print d2
			match = True
			for cat in joinByCats:
				if d[cat]!=d2[cat] and d[cat]!="NA" and d2[cat]!="NA":
					counter +=1
					match = False
					
			#print match, d,d2
			if match == True:
				newDot = merge_two_dicts(d, d2)
				dots1.remove(d)
				dots2.remove(d2)
				newDots.append(newDot)
				if len(dots1)<1 or len(dots2)<1:# or counter>10^10:
					return {"joined":newDots,"unmatched1":dots1,"unmatched2":dots2}
				else:
					joinCombinedDots(dots1,dots2,joinByCats,newDots)
				#print len(dots1),len(dots2),len(newDots)
	return {"joined":newDots,"unmatched1":dots1,"unmatched2":dots2}




def joinWithNoCommonCat(dots1,dots2,newDots):	
	d = dots1[0]
	dots1.remove(d)
	for d2 in dots2:
		newDot = merge_two_dicts(d, d2)	
		dots2.remove(d2)
		newDots.append(newDot)
		#print newDot
		
		if len(dots1)>0 and len(dots2)>0:
			joinWithNoCommonCat(dots1,dots2,newDots)
		else:
			break
	return {"joined":newDots,"unmatched1":dots1,"unmatched2":dots2}
				
def combineBins(cats1,cats2,dots1, dots2):
	joinByCats = []
	newDots = []	
	for cat in cats1:
		if cat in cats2:
			joinByCats.append(cat)
	if len(joinByCats)>0:	
		print "join with common category"
		joined=joinCombinedDots(dots1,dots2,joinByCats,newDots)
	else:
		print "join with NO common category"
		joined= joinWithNoCommonCat(dots1,dots2,newDots)
	return joined
	

def generatePopulation(csvWriter,allBins,group,isheader):
	keys = allBins.keys()
	
	combinedCats= allBins[keys[0]]["category"]
	
	allDots = makeDots(allBins[keys[0]],group)
	
	for i in range(1,len(keys)):
		#print i
		newCats = allBins[keys[i]]["category"]
		#print newCats
		newDots = makeDots(allBins[keys[i]],group)
		results = combineBins(combinedCats,newCats,allDots,newDots)
		combinedCats = list(set(combinedCats)|set(allBins[keys[i]]["category"]))
		allDots = results["joined"]

	headers = allDots[0].keys()
	if isheader == True:
		#print "headers", headers
		csvWriter.writerow(["id","group"]+headers)
		#print "added headers", ["id"]+headers
	pid = 0
	
	for d in allDots:
		pid+=1
		row = []
		for c in headers:
			row.append(d[c])
		#print
		#print "data",row
		#print "added data",[str(pid)]+row
		csvWriter.writerow([str(pid)+"_"+group,group]+row)
	return allDots


	
	
for k in range(1,15):
	#print blackBins.keys()
	print whiteBins.keys()
	
	csvWriter = csv.writer(open("pop_all_"+str(k)+".csv","w"))
	
	
	
	bPop = generatePopulation(csvWriter,blackBins,"b",True)
	wPop = generatePopulation(csvWriter,whiteBins,"w",False)
	
	
	
	#combinedWriter = csv.writer(open("web/populations/pop_all_"+str(k)+".csv","w"))
	#combinedWriter.writerow(shuffledAllPop[0].keys())
	
	#for i in shuffledAllPop:
	#	print shuffledAllPop[0].keys()
	#	combinedWriter.writerow(i.values())
	#	
	break






