class Employee1(object):

    __slots__ = ['__lastName','__firstName','__employeeNum']

    number = 0
    
    def __init__(self,lastName="Bayern",firstName="Munich",employeeNum="none"):
        Employee1.number=Employee1.number+1
        self.setLastName(lastName)
        self.setFirstName(firstName)
        self.setEmployeeNum(employeeNum)
        
    
    def getLastName(self):
        return self.__lastName
        
    def setLastName(self,newName):
            self.__lastName=newName
            
    def getFirstName(self):
        return self.__firstName
        
    def setFirstName(self,newLast):
            self.__firstName=newLast   

    def getEmployeeNum(self):
        return self.__employeeNum
        
    def setEmployeeNum(self,newNum):
            self.__employeeNum=newNum           
        
        
    def __str__(self):
            return "call " + self.__lastName + self.getLastName()
            
    def showEmployee(self):
      
        print self.getLastName()
        print self.getFirstName()
        print self.getEmployeeNum()
        
    def __lt__(self,other):
            return self.__lastName < other.__lastName
            
    def __add__(self,other):   
            return self.__lastName + other.__lastName
            
