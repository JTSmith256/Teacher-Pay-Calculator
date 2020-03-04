Sal = (float(input("What is the teacher's Starting Salary?")))
Inc = (float(input("What is the Annual Increase percentage?")))
Term = (int(input("How many years will the teacher be earning a salary?")))
Year = 0

while Year < Term:
    Sal += Sal * Inc / 100
    Sal = round (Sal, 2)
    Year += 1
    print ("Year:", Year, ";   Ending Salary: $", Sal)


