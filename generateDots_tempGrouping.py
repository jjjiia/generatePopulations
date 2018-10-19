import random
import copy
import csv
import json
from pprint import pprint

totalPopulation = 501

bins1 = {"category":["education","occupation"],
	"gradeSchoolOrLess":{"whiteColorSkilled":10,"semiSkilled":13,"unskilledDomesticPersonalService":77,"total":146},
	"someHighSchool":{"whiteColorSkilled":16,"semiSkilled":21,"unskilledDomesticPersonalService":63,"total":113},
	"highSchoolGraduate":{"whiteColorSkilled":27,"semiSkilled":24,"unskilledDomesticPersonalService":50,"total":59},
}

bins2 = {
	"category":["occupation","satisfactionInField"],
	"whiteColorSkilled":{"poor":25,"hardToSay":12,"fair":18,"good":45,"total":40},
	"semiSkilled":{"poor":40,"hardToSay":16,"fair":15,"good":29,"total":55},
	"unskilledDomesticPersonalService":{"poor":52,"hardToSay":17,"fair":10,"good":21,"total":181}
}

bins3 = {
	"category":["occupation","satisfactionInWorkplace"],
	"whiteColorSkilled":{"poor":37,"hardToSay":21,"fair":11,"good":32,"total":40},
	"semiSkilled":{"poor":53,"hardToSay":15,"fair":17,"good":15,"total":55},
	"unskilledDomesticPersonalService":{"poor":57,"hardToSay":16,"fair":11,"good":16,"total":181}
}
bins4 = {
	"category":["transiency"],
	"permanent":17,
	"asLongAsEligible":42,
	"neverThoughtAboutIt":17,
	"untilOwnHome":8,
	"untilBetterPlace":16,
	"total":356
}

bins5 = {
	"category":["evaluationOfHilltown"],
	"favorable":93,
	"unfavorable":7,
	"total":432
}
bins6 = {
	"category":["evaluationOfPhysicalAmenities"],
	"favorable":97,
	"unfavorable":3,
	"total":314
}
bins7 = {
	"category":["evaluationOfCoResidents"],
	"favorable":85,
	"unfavorable":15,
	"total":75
}
bins8 = {
	"category":["evaluationOfManagement"],
	"favorable":79,
	"unfavorable":21,
	"total":43
}
bins9 = {
	"category":["pastExperience","expectations"],
	"biracialLivingExperience":{"integration":11,"mutualAcomodataion":69,"conflict":20,"total":193},
	"noBiracialLivingExperience":{"integration":5,"mutualAcomodataion":50,"conflict":45,"total":18}
}
bins10 = {
	"category":["impressionOfFriends"],
	"favorable":60,
	"favorableAndUnfavorable":22,
	"noComments":4,
	"unfavorable":14,
	"total":356
}
bins11={
	"category":["attitude","attitudeOfFriend"],
	"liberal":{"liberalFriend":87,"ambivalentFriend":13,"illiberalFriend":0,"total":218},
	"ambivalent":{"liberalFriend":79,"ambivalentFriend":21,"illiberalFriend":0,"total":28},
	"illiberal":{"liberalFriend":1,"ambivalentFriend":0,"illiberalFriend":0,"total":1}
}

tempGroupBins = {
	"category":["group"],
	"A":50,
	"B":50,
	"total":totalPopulation
}
	
def makeDots(bins):
	dots = []
	#print bins["category"]
	if len(bins["category"])==1:
		cat1 = bins["category"][0]
		for b in bins:
			if b!="category" and b!="total":
				count = int(round(bins[b]*.01*bins["total"]))
				for c in range(count):
					did = {cat1:b}
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
							did = {cat1:b,cat2:g}
							dots.append(did)
		
		missingEntries = totalPopulation-len(dots)
		#print missingEntries, "missing"
		for m in range(missingEntries):
			did = {cat1:"NA",cat2:"NA"}
			dots.append(did)
							
	shuffledDots = sorted(dots, key=lambda k: random.random())
	return shuffledDots

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z
	
def joinCombinedDots(dots1,dots2,joinByCats,newDots):
	for d in dots1:
		for d2 in dots2:
			#print d2
			match = True
			for cat in joinByCats:
				if d[cat]!=d2[cat]:
					match = False
			#print match, d,d2
			if match == True:
				newDot = merge_two_dicts(d, d2)
				dots1.remove(d)
				dots2.remove(d2)
				newDots.append(newDot)
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
		#print "join with common category"
		joined=joinCombinedDots(dots1,dots2,joinByCats,newDots)
	else:
		#print "join with NO common category"
		joined= joinWithNoCommonCat(dots1,dots2,newDots)
	return joined
	

def generatePopulation(fileName):
	allBins = [bins1,bins4,bins11,tempGroupBins]
	
	combinedCats= allBins[0]
	allDots = makeDots(allBins[0])
	for i in range(1,len(allBins)):
		newCats = allBins[i]["category"]
		newDots = makeDots(allBins[i])
		results = combineBins(combinedCats,newCats,allDots,newDots)
		combinedCats = list(set(combinedCats)|set(allBins[i]["category"]))
		allDots = results["joined"]

	pid = 0
	populationDictionary = {}
	for d in allDots:
		pid+=1
		idDigits = str(pid)
		while len(str(idDigits))<len(str(totalPopulation)):
			idDigits = "0"+ idDigits
			
		idName = "_"+str(idDigits)
		
		populationDictionary[idName]=d
		
	with open(fileName, "w") as outfile:
	    json.dump(populationDictionary, outfile)
		
		
#keys = {
#	"group": ["A","B"],
#	"education": ["NA","gradeSchoolOrLess","someHighSchool","highSchoolGraduate"],
#	"occupation": ["NA", "whiteColorSkilled","semiSkilled","unskilledDomesticPersonalService"],
#	"attitude":["NA", "illiberal", "liberal", "ambivalent"],
#	"attitudeOfFriend": ["NA","liberalFriend","ambivalentFriend","illiberalFriend"],
#	"transiency": ["NA", "permanent", "asLongAsEligible", "neverThoughtAboutIt", "untilOwnHome", "untilBetterPlace"]
#}


#for k in range(100):
#	generatePopulation("temp_populations/temp_pop_"+str(k)+".json")
#
#
#with open("temp_populations/temp_pop_14.json") as checkInput:
#	data = json.load(checkInput)
#	pprint(data["_059"])
#
#with open("temp_populations/temp_pop_12.json") as checkInput:
#	data = json.load(checkInput)
#	pprint(data["_059"])
