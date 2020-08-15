class Person:
    def _init_(self, age = 0):
        if age<0:  #check the condition if age is negative then print below statement. 
            print('Age is not valid')
            self.age=0    #set age as zero
        else:
            self.age = age
    def amIOld(self):
        if self.age <=11:
            print('You are young')
        elif self.age > 11 and self.age <=19:
            print('you are teenager')
        else:
            print('You are old')
    def yearPasses(self):
        print('Year passed')
def func():        
    p = Person(16)
    p.amIOld()
    p.yearPasses()
func()








