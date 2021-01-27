#This file is created for the sole purpose of helping out


#Homework Assignment 3 is based on IF Statements

a = 4
b = 5
c = "4"
print(type(c)) #Checking Variable C's Datatype
def EqualityTest(a,b,c):
    if a == int b or a == int(c) or  b == int(c): #USING INT FUNCTION TO CONVERT VALUE OF C(STRING) TO INT
        print(True)
    else:
        print(False)
    
EqualityTest(a,b,c)
