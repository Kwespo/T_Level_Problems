ListOfMessage = [] #Makes a List of the message objects

LenOfMessageInput = int(input("lENGTH OF YOUR MESSAGE ")) #Makes an input for the length of your message

##Get the Words to append to the list
for i in range(LenOfMessageInput): ##loops the length of the message
  MessageInput = input("Message Word ") #Gets an input for the words in the message
  ListOfMessage.append(MessageInput) #Adds the words to the list


#Get the length of the List
ListOfMessageLength = len(ListOfMessage) 

#Getting length of the longest word
for i in range(ListOfMessageLength): #Loops though the list 
  LenList = [] #Makes a list of the length of the words
  BiggestWordLength = len(ListOfMessage[i]) #Gets the length of the words
  LenList.append(BiggestWordLength)#adds the length of the words to the length list
  LenList.sort()#Sorts the list by size, smallest to largest
  BiggestWordLength = int(LenList[-1])#Gets the largest word length
  print(LenList) #prints the lenth of the word

##Get all words to the same length
for x in range(len(LenList)):#loops though the amount of words there are
  if i  < LenList[-1]:#if a length is smaller than the end word
    DiffrenceBetweenWords = LenList[-1] - x#Varable where it finds the difference between the largest and the current word.

##Print the Words
print("* " * (BiggestWordLength))#Prints the top astrics
for word in ListOfMessage:#Loops throught the list of words and if the length is equal to largest it does not print the astriks
  if len(word) == BiggestWordLength:
    print("*", word, "*")
  else: #if its not as long as the longest it will print the atriks with the spacers
    for x in range(len(LenList)):
      DiffrenceBetweenWord = BiggestWordLength - len(word)
      print("*", word, " " * DiffrenceBetweenWord + "*")
print("* " * (BiggestWordLength))#prints the bottom border