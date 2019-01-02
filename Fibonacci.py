'''Fibonacci
Rule: Xn = Xn-1 + Xn-2
'''


def Fibonacci():
	x = 0
	Nterm1 = 1 
	Nterm2 = 1
	while x < 20:
		CurrentTerm = Nterm1+Nterm2
		Nterm1 = CurrentTerm
		Nterm2 = Nterm1-Nterm2
		x +=1
		print CurrentTerm
Fibonacci()