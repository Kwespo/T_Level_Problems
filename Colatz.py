Number = int(input("What is your number? "))
loopnum = 0
while True:
  if Number % 2 == 0:
    Number = Number / 2
    loopnum = loopnum + 1
    print(Number ," Loop number ", loopnum)
  elif Number == 1:
    print(Number , "It took", loopnum, "Loops to get to ONE")
    break
  else:
    Number = Number * 3 + 1
    loopnum = loopnum + 1
    print(Number ," Loop number ", loopnum)