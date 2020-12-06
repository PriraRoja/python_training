row = int(input("Enter the no of rows:")) 
col = int(input("Enter the no of columns:")) 
 
mat = [] 
print("Enter the numbers:")   
for i in range(row):          
    a =[] 
    for j in range(col):      
         a.append(int(input())) 
    m.append(a)  
for i in range(row): 
    for j in range(col): 
        print(mat[i][j], end = " ") 
    print()