# Write Code to print 1 to 10 no. in ascending order using for loop

#Initialize array     
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]; 

temp = 0;    
     
#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(arr)):   

    print(arr[i], end=" ");    
     
#Sort the array in ascending order  
  
for i in range(0, len(arr)):

    for j in range(i+1, len(arr)):  

        if(arr[i] > arr[j]):    

            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
     
#Displaying elements of the array after sorting    
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    