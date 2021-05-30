#Decision tree algorithm
from sklearn import tree
# Rough 1 # Smooth 0 # Tennis 1 # Cricket 2

def MarvellousDecision(weight,surface):
	Features=[[35,1],[40,1],[90,0],[100,0],[20,1],[36,1],[99,0],[110,0]]
	
	Label=[1,1,2,2,1,1,2,2]
	
	dobj=tree.DecisionTreeClassifier()
	
	dobj.fit(Features,Label)
	
	Result=dobj.predict([[weight,surface]])
	
	if Result==1:
		print("Your object is Tennis ball")
	else:
		print("Your object is cricket ball")
	
def main():
	print("Enter weight of ball")
	weight=int(input())
	
	print("Enter surface of ball")
	surface=input()
	
	if surface.lower() == "rough":
		surface=1
	elif surface.lower() == "smooth":
		surface=0
	else:
		print("Invalid input")
		return
	MarvellousDecision(weight,surface)
	
if __name__=="__main__":
	main()