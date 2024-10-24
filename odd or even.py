arr = [1, 7, 8, 4, 5, 16, 2]  
n = len(arr) 

even = 0 
odd = 0  

for i in range(0, n):
    if arr[i] % 2 == 0: 
        even += 1
    else: 
        odd += 1
print("Even number count:", even)
print("Odd number count:", odd)
