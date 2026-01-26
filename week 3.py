name = input ('what is your name?')
print ('Hello ' + name)
age = int(input("what is your age?"))
#ask how many years to add
years = int(input("enter how many years to add"))
future_age = age + years
print("In " + str(years) + "years you will be " + str(future_age) + "years old")
# print then having it raise age doesnt work because print is just going to write whatever you said in the quotations
hours = float(input("enter the number of hours worked"))
wage = float(input("hourly wage, without $"))
pay = hours * wage
print("Your total pay for the week is $" + str(pay))