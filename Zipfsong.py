import sys

def quicksort(target):
	left = []
	right = []
	if(len(target)<=1):
		return target
	pivot = int(len(target)/2)
	pivotVal = target[pivot]
	target.pop(pivot)
	for x in range(0, len(target)):
		if(target[x][2]<pivotVal[2]):
			left.append(target[x])
		elif(target[x][2]==pivotVal[2]):
			if(target[x][3]<pivotVal[3]):
				right.append(target[x])
			else:
				left.append(target[x]) 
		else:
			right.append(target[x])
	return quicksort(left)+[pivotVal]+quicksort(right)

inBuffer = []

n, m = [int(x) for x in sys.stdin.readline().split()]

for counter in range(0, n):
	newLine = sys.stdin.readline().split()

	freq = int(newLine[0])
	name = newLine[1]
	q = float(freq)/(float(1)/float(counter+1))
	inBuffer.append([freq, name, q, counter])

inBuffer = quicksort(inBuffer)

for x in range(0, m):
	print(inBuffer[len(inBuffer)-x-1][1])





