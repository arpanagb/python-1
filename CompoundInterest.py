#Compound Interest
p=float(input(" Enter Principle amount = "))
t=float(input(" Enter term = " ))
r=float(input(" Enter rate of interest = "))
ci=p*(pow((1+r/100),t))
print("Compound Interest = ",ci)
