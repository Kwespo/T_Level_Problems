#list of the speed of the people based on their sex.
men = []
women = []
sex= [men, women]
ListOfRacers = []

while True:
  AmountOfRacers = input("Ammount of racers: ") #get the amount of racers
  
  try:
    AmountOfRacers = int(AmountOfRacers) #trys to conver the amount of racers to an integer
    if AmountOfRacers <= 8 and AmountOfRacers >= 4: #checks the amount if valid
      break #breaks the loop
  except: #if the conditions are not met
    print("Amount of racers must be between 4 and 8.") #print this line and start again

for i in range(AmountOfRacers): #Loops though the amount of racers there are. This later is added to a list.
  sex = input("Men or Women? ")
  if sex == "Men":
    time = int(input("Time? "))
    men.extend([time])
    men.sort(reverse=True)
  elif sex == "Women":
    time = int(input("Time? "))
    women.extend([time])
    women.sort(reverse=True)
  else:
    print(f"Please enter Men or Women")

#printing the list
print(f"Mens results sorted by time", men)
print(f"Womens results sorted by time", women)



