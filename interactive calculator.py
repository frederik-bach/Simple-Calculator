#Eingabezeile

calculations = []


def addingfunc(number1, number2):
    print("Das Ergebnis ihrer Rechnung ist:")
    result=float(number1) + float(number2)
    calchlist =["Addition:",str(number1), "+", str(number2), "=",result]
    calculations.extend(calchlist)
    print(result)


def subractfunc (number1,number2):
    print("Das Ergebnis ihrer Rechnung ist:")
    result= float(number1) - float(number2)
    calchlist =["Substraktion:",str(number1), "-", str(number2), "=",result]
    calculations.extend(calchlist)
    print(result)

def multiplyfunc (number1,number2):
    print("Das Ergebnis ihrer Rechnung ist:")
    result= float(number1) * float(number2)
    calchlist =["Multiplikation:",str(number1), "*", str(number2), "=",result]
    calculations.extend(calchlist)
    print(result)

def dividingfunc(number1, number2):
    print("Das Ergebnis ihrer Rechnung ist")
    result=float(number1) / float(number2)
    calchlist =["Division:",str(number1), "/", str(number2), "=",result]
    calculations.extend(calchlist)
    print(result)

def historyfunc(calculations) :
    calculations.append(result)

n=3
i=2



while i < n:

    OperationenListe = ["add", "subtract", "multiply" ,"divide","history"]
    operation = input ("Geben Sie ein, welche Rechenoperation ausgeführt werden soll (add/subtract/multiply/divide/end/history)")

    if (operation == "end" or operation not in OperationenListe) :
            exit()
        
    if (operation =="history"):
        for j in calculations:
            print(j)
            i=2 
    else:
            
            number1= input ("Geben Sie die erste Nummer ein")
            number2= input ("Geben Sie die zweiter Nummer ein")
            
    if operation not in OperationenListe:
        exit()
    
        
    if (operation == "add"):
            
        addingfunc(number1, number2)
        
        i=2    
            
    if (operation == "subtract"):
            
        subractfunc(number1,number2)
        i=2
        
    if (operation == "multiply"):
            
        multiplyfunc(number1,number2)
        i=2
        
    if (operation == "divide"):
            
        dividingfunc(number1, number2) 
        i=2
    
     

       




