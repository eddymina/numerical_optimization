
#https://en.wikipedia.org/wiki/Assignment_problem#Algorithms_and_generalizations

def factorial(input):
	#n!= n * (n-1) * (n-2) * (n-3) ... * 1 
    sol=1 
    for i in range(1,input+1): sol*=i
    return sol 


def permutation(n,r):
	#order maters (AB!=BA)
	return int(factorial(n)/factorial(n-r))


def combination(n,r):
	### Order does not matter (therefore a smaller number since AB==BA)
	return int(factorial(n)/(factorial(r)*factorial(n-r)))


class gale_shapley:

	def __init__(self,guyprefers,galprefers):

		assert(type(guyprefers)== dict)
		assert(type(galprefers)== dict)

		self.guyprefers = guyprefers
		self.galprefers = galprefers
		self.guys = sorted(guyprefers.keys())
		self.gals = sorted(galprefers.keys())


	def match(self,verbose=False):
		guysfree = self.guys[:]
		engaged  = {}
		guyprefers2 = self.guyprefers
		galprefers2 = self.galprefers

		while guysfree:
		    guy = guysfree.pop(0) #Lets look at the first guy thats free
		    guyslist = self.guyprefers[guy] #who does that guy like 

		    gal = guyslist.pop(0) #get the first gal her likes
		    fiance = engaged.get(gal) #she taken? 

		    if verbose == True: print("Candidate Guy:",guy,"\nCurrent Girl:",gal)
		    
		    if not fiance: #if bride is not taken 
		        engaged[gal] = guy #set it up --> gal with guy 

		    else: #if bride is taken 
		 
		        galslist = self.galprefers[gal] #does she like the guy she is with? 

		        if galslist.index(fiance) > galslist.index(guy): #if current guy is ranked higher (lower number)
		            # She prefers new guy
		            engaged[gal] = guy
		            if verbose == True: print("%s dumped %s for %s" % (gal, fiance, guy))
		            if self.guyprefers[fiance]: 
		                # Ex has more girls to try
		                guysfree.append(fiance) #add the dumped guy to free 
		        else:
		            # She likes this guy more 
		            if guyslist:
		                # Look again
		                guysfree.append(guy) #send candidate guy to trash
		    if verbose == True: print('Engaged so far:', engaged,'\n')
		return engaged


	def check(self):

		engaged= self.match()
		inverseengaged = dict((v,k) for k,v in engaged.items())
		for she, he in engaged.items():
		    shelikes = self.galprefers[she]
		    shelikesbetter = shelikes[:shelikes.index(he)]
		    helikes = self.guyprefers[he]
		    helikesbetter = helikes[:helikes.index(she)]
		    for guy in shelikesbetter:
		        guysgirl = inverseengaged[guy]
		        guylikes = self.guyprefers[guy]
		        if guylikes.index(guysgirl) > guylikes.index(she):
		            print("%s and %s like each other better than "
		                  "their present partners: %s and %s, respectively"
		                  % (she, guy, he, guysgirl))
		            return False
		    for gal in helikesbetter:
		        girlsguy = engaged[gal]
		        gallikes = self.galprefers[gal]
		        if gallikes.index(girlsguy) > gallikes.index(he):
		            print("%s and %s like each other better than "
		                  "their present partners: %s and %s, respectively"
		                  % (he, gal, she, girlsguy))
		            return False
		return True


def sample_data():
	guyprefers = {
	'abe':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
	'bob':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
	'col':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
	'dan':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
	'ed':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
	'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
	'gav':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
	'hal':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
	'ian':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
	'jon':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']}
	galprefers = {
	'abi':  ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
	'bea':  ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
	'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
	'dee':  ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
	'eve':  ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
	'fay':  ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
	'gay':  ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
	'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
	'ivy':  ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
	'jan':  ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']}

	return guyprefers,galprefers


class hungarian:

	def __init__(self,usr_pref,pref_weights=None):
		assert(type(usr_pref)== dict)
		self.usr_pref= usr_pref
		self.usrs = list(usr_pref.keys())
	
		self.pref_order =list(set([item for sublist in list(usr_pref.values()) for item in sublist]))

		if pref_weights == None:
			self.pref_weights = {i:(i+1.1) /float(len(self.pref_order))for i in range(len(self.pref_order))}
		else: 
			assert(type(pref_weights )== dict)
			self.pref_weights = pref_weights 


	def diff(self,li1, li2): 
	   return [i for i in li1 + li2 if i not in li1 or i not in li2] 

	def weight_matrix(self,print_matrix=False):
		matrix= [] 
		for usr,prfs in self.usr_pref.items():
			prfs.extend(self.diff(self.pref_order,prfs))
			list_dic = {k: v for v, k in enumerate(prfs)}
			matrix.append([self.pref_weights[list_dic[e]] for e in self.pref_order])
		if print_matrix: 
			print(self.pref_order)
			for i,val in enumerate(matrix): print(self.usrs[i],val)
		return matrix

	def solve(self,print_matrix=False):

		matrix = self.weight_matrix()
		iterate = range(len(self.pref_order))
		
		for i in iterate: matrix[i][:] = [val - min(matrix[i][:]) for val in matrix[i][:]] #row minima
		for i in iterate: matrix[:][i] = [val - min(matrix[:][i]) for val in matrix[:][i]] #col minima
		
		
		self.hungarian_matrix= matrix

		if print_matrix: 
			print(self.pref_order)
			for i,val in enumerate(matrix): print(self.usrs[i],val)
			print('')

		return dict(zip([self.usrs[i] for i in iterate], [self.pref_order[matrix[i].index(0.)] for i in iterate]))



if __name__ == '__main__':
	# guyprefers,galprefers = sample_data()
	# gale_shapley(guyprefers,galprefers).match(True)


	usr_pref = {'userA' :["backcatcher", "center field", "short stop"],
	'userB':["pitcher", "backcatcher", "center field"],
	'userC':["pitcher", "center field", "short stop"],
	'userD': ["short stop", "backcatcher", "pitcher"]}

	h= hungarian(usr_pref)

	print('weighted preferences:', h.pref_weights,'\n')

	h.weight_matrix(print_matrix= True)
	print('')
	print('Results:', h.solve(print_matrix= True))










