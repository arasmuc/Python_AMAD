import company


allEmpl = []

allEmpl.append(company.Employee("Arkadiusz","Borucki",100))
allEmpl.append(company.Employee("TTTTT","DDDDDD",200))
allEmpl.append(company.Employee("ZZZZZ","YYYYY"))
allEmpl.append(company.Employee("ddddd","vvvvv",200000))
allEmpl.append(company.Employee())

allEmpl.append(company.Employee())

for odj in allEmpl:
    print "---------------"
    odj.showEmployee()
    
#test=company.Employee.age
#test=999 
  
print "---------------"  
print "---------------" 
allEmpl[1].showEmployee()

print "---------------" 

print "---------------"  
allEmpl[0].showEmployee()
print "---------------"
allEmpl[0].lastName="TESTTEST"
allEmpl[0].showEmployee()

print "---------------"
print "---------------"
test=company.Employee
test.age=999

print test.age
