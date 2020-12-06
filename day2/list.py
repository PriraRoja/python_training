lst = {1: [1, "Ram", 18000],
2: [2, "Sam", 50000],
3: [3, "Lavan", 21000]}
print ("{:<5} {:<5} {:<5} {:<5}".format('Sno','id','Name','Salary'))
for k, i in lst.items():
    id, name, salary = i
    print ("{:<5} {:<5} {:<5} {:<5}".format(k, id, name, salary))