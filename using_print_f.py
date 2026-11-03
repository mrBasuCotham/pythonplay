name = "Mr Basu"
job = "Teacher"
years = 56
pay = 52385

print (name + " is a "+job+". He is "+str(years)+" years old and he is paid £"+str(pay)+".00")

print(f"{name} is a {job}. He is {years} years old and he is paid £{pay:.2f}")

def payHim(n,j,y,p):
   print(f"{n} is a {j}. He is {y} years old and he is paid £{p:.2f}") 

payHim("Mr Penny","Headteacher",48,104059)