#add even no. to list

list = []
even = []
for i in range(1,11):
	x = int(input('input no. :- '))
	
	list.append(x)
	
for i in list:
	if i%2 ==0:
		even.append(i)

print(even)