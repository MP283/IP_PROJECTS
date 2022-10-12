#printing grades
marks = int(input('Pls input your marks'))

if (marks<= 100 and marks >= 80):
	print('Your grade is A')
	
elif(marks < 80 and marks >= 60):
	print('Your grade is B')
	
elif(marks < 60 and marks >= 40):
	print('Your grade is C')
	
else:
	print('Fail, Better luck next time')
	
print('	',marks)