import sys

inBuffer = []

n, m = [int(x) for x in sys.stdin.readline().split()]

for counter in range(0, n):
	newLine = sys.stdin.readline().split()

	freq = int(newLine[0])
	name = newLine[1]
	q = float(freq)/(float(1)/float(counter+1))
	inBuffer[]

	inBuffer.append([freq, name, q])

for i in range(0, m):
	maxIndex = i
	maxValue = inBuffer[i][2]
	for j in range(i+1, n):
		if(inBuffer[j][2]>maxValue):
			maxIndex = j
			maxValue = inBuffer[j][2]
	temp = inBuffer[i]
	inBuffer[i]=inBuffer[maxIndex]
	inBuffer[maxIndex]=temp
	print inBuffer[i][1]





