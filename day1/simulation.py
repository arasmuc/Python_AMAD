import company2

allEmpl = []
allEmpl.append(company2.Employee1("Arkadiusz","Borucki",100))
allEmpl.append(company2.Employee1())
allEmpl.append(company2.Employee1("A","B",111))

print allEmpl[0]

print "--------------------"
allEmpl[0].showEmployee()
print "--------------------"
allEmpl[1].showEmployee()
print "--------------------"
allEmpl[2].showEmployee()
print "--------------------"

print "------ LOOP --------------"

for odj in allEmpl:
    print "---------------"
    odj.showEmployee()
    
print "--------------------"    
print allEmpl[0] < allEmpl[1]
print "--------------------"


if allEmpl[0] < allEmpl[1]:
    print "true eq"
else:
    print " not eq"
        
        
print "--------------------"
print allEmpl[0] + allEmpl[1] 
