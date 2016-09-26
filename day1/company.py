class Employee:

    number = 0

    def __init__(self,lastName="Bayern",firstName="Munich",employeeNum="none"):
        Employee.number=Employee.number+1
        self.lastName=lastName
        self.firstName=firstName
        self.employeeNum=employeeNum
        
 
   
        
    def showEmployee(self):
      
        print self.lastName
        print self.firstName
        print self.employeeNum
        print Employee.number
