class Calculator:
	def __init__(self, Input):
		Input = Input.replace(" ", "") #Removing spaces to make it less complicated. 
		inputList = [y for x,y in enumerate(Input)] #Making a list of all letters of the Input.. For Example 2+2 = ['2', '+', '2']
		self.numList = [] 
		self.opList = [] #op stands for operator 
		self.tempNum = ''
		self.N = ['1','2','3','4','5','6','7','8','9','0', '.'] #Accepted Characters for input as a number. 
		numList, opList = self.formNumber(inputList) # Splitting inputList into numList, opList for eg, 2+2, numList = ['2', '2'] opList = ['+']
		numList, opList = self.solve(numList, opList)
		while ('+' in opList) or ('-' in opList) or ('*' in opList) or ('/' in opList) or ('^' in opList):
			numList, opList = self.solve(numList, opList)
		self.result = numList[0]

	def solveBrackets(self, Input):
		inputList = [y for x,y in enumerate(Input)]
		numList, opList = [], []
		tempNum = ''
		for y,x in enumerate(inputList):
			if str(x) in self.N:
				tempNum += str(x)
			else:
				if tempNum != '':
					numList.append(float(tempNum))
				tempNum = ''
				opList.append(x)
			if y+1 is len(inputList):
				if tempNum != '':
					numList.append(float(tempNum))
				tempNum = ''
		numList, opList = self.solve(numList, opList)
		while ('+' in opList) or ('-' in opList) or ('*' in opList) or ('/' in opList) or ('^' in opList):
			numList, opList = self.solve(numList, opList)
		return numList[0]

	def formNumber(self, inputList):
		tempNum = ''
		numList = []
		opList = []
		brackets = False
		for y,x in enumerate(inputList):
			if str(x) is '(':
				brackets = True 
				continue 
			elif str(x) is ')':
				brackets = False 
				tempNum = self.solveBrackets(tempNum)
				numList.append(tempNum)
				continue
			if brackets:
				tempNum += str(x)
			else:
				if str(x) in self.N:
					tempNum = tempNum + str(x) 
				else:
					if tempNum != '':
						numList.append(float(tempNum))
					tempNum = ''
					opList.append(x)
				if y+1 is len(inputList):
					numList.append(float(tempNum))
					tempNum = ''
		return numList, opList 

	def solve(self, numList, opList):
		for x,y in enumerate(opList):
			if y is '^':
				numList[x] = float(numList[x]) ** numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		for x,y in enumerate(opList):
			if y is '/':
				numList[x] = float(numList[x]) / numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		for x,y in enumerate(opList):
			if y is '*':
				numList[x] = float(numList[x]) * numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		for x,y in enumerate(opList):
			if y is '+':
				numList[x] = float(numList[x]) + numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		for x,y in enumerate(opList):
			if y is '-':
				numList[x] = float(numList[x]) - numList[x+1]
				numList.remove(numList[x+1])
				opList.remove(y)
		return numList, opList 

while True:
	try:
		cal = Calculator(raw_input("Enter An Equation: ")) #You may need to change raw_input to input if you are using python 3
		print(cal.result)
	except:
		print("Sorry There's an error")
