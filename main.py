# Question 1 
case = int(input("cases of Hep A in Hillsborough County: "))
popu = float(input("population(in millions): "))
new = int(input("new cases: "))
died = int(input("people who died: "))
time = float(input("time for incidence(in years): "))
avgage = int(input("Average age of death: "))
ageone = int(input("age of 1 person: "))
agetwo = int(input("age of 2nd person: "))


# Prevalance 
p = case/popu
print("Prevalence = ", p)

# Incidence
i = new/(popu*time)
print("incidence = ", i)

# Mortailty Rate
mr = (died/popu) * 100000 
print("Mortality rate = ", mr)

# Potential life lost
ypll = avgage - ageone
print("Years of Potential life lost = ", ypll)
yplltwo = avgage - agetwo
print("Years of Potential life lost for person two = ", yplltwo)


# Question 2
print("")
print("")
print("Question 2")
print("")

case2 = int(input("cases of Salmonella in Miami-Dade: "))
pop2 = float(input("Population(in millions): "))
time2 = float(input("time for incidence(in years): "))
new_cases = int(input("new cases in Salmonella: "))
died2 = int(input("Number of people who died in Salmonella: "))

p2 = case2/pop2
print("Prevalence for Salmonella: ", p2)

i2 = new_cases / (pop2*time2)
print("incidence for Salmonella: ", i2)

mr2 = (died2/pop2) * 100000
print("Mortality rate for Salmonella: ", mr2)


# Question 3
print("")
print("")
print("Question 3")
print("")

case3 = int(input("cases of influenza: "))
pop3 = float(input("Population(in millions): "))
time3 = float(input("time for incidence(in years): "))
new_cases3 = int(input("new cases in influenza: "))
died3  = int(input("Number of people who died in influenza: "))

p3 = case3/pop3
print("Prevalence for influenza: ", p3)

i3 = new_cases3 / (pop3*time3)
print("incidence for influenza: ", i3)

mr3 = (died3/pop3) * 100000
print("Mortality rate for influenza: ", mr3)


# Question 4 

print("")
print("")
print("Question 4")
print("")
case4 = int(input("cases of Chlamydia: "))
pop4 = float(input("Population(in millions): "))
time4 = float(input("time for Chlamydia(in years): "))
new_cases4 = int(input("new cases of Chlamydia: "))
died4  = int(input("Number of people who died in Chlamydia: "))
age1 = int(input("age of 1 person: "))
age2 = int(input("age of 2 person: "))
age3 = int(input("age of 3 person: "))
age4 = int(input("age of 4 person: "))
age5 = int(input("age of 4 person: "))
avgage4 = avgage = int(input("Average age of death: "))

p4 = case4/pop4
print("Prevalence for Chlamydia: ", p4)

i4 = new_cases4 / (pop4*time4)
print("incidence for influenza: ", i4)

mr4 = (died4/pop4) * 100000
print("Mortality rate for influenza: ", mr4)

# Potential life lost
ypll1 = avgage4 - age1
print("Years of Potential life lost = ", ypll1)

ypll2 = avgage4 - age2
print("Years of Potential life lost for person 2 = ", ypll2)

ypll3 = avgage4 - age3
print("Years of Potential life lost for person two = ", ypll3)

ypll4 = avgage4 - age4
print("Years of Potential life lost for person two = ", ypll4)

ypll5 = avgage4 - age5
print("Years of Potential life lost for person two = ", ypll5)









