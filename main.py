import random
import pyttsx3
#note: remove all puctuation before mixing up, it causes delays cause commas etc. are read as a pause
inputFileLines = open("input", "r").readlines()

#x = text.split() and now x is equal to the list of the words

wordList = []

for x in inputFileLines:
    splitLine = x.split()   #splitLine is now the list of words

    for y in splitLine:
        wordList.append(y)



#len(list) gets the not starting at zero list length

#mix them up by making a new list
outputList = []

firstRandom = 0 #this will be the first swap location
secondRandom = 0    #this will be the second swap location

numberOfTimesToSwap = 1000   #set the number of this based on the length of the words list so I don't have to custom set it every time
#set it as a fractions of the length like a quarter, half, up to 100% and 200%

for x in range(numberOfTimesToSwap):
    firstRandom = random.randint(0, len(wordList)-1)
    secondRandom = random.randint(0, len(wordList)-1)

    firstWord = wordList[firstRandom]
    secondWord = wordList[secondRandom]
    wordList[firstRandom] = secondWord
    wordList[secondRandom] = firstWord



engine = pyttsx3.init() # object creation
#now put them on a file
outputFile = open("output", "w")

wordsBeforeNewLine = 10
number = 0
stringToSay = " "

for z in wordList:
    number += 1
    outputFile.write(z+" ")
    stringToSay += z+"   "
    if number == wordsBeforeNewLine:
        outputFile.write("\n")
        number = 0

outputFile.close()
#engine.setProperty('volume',1.0)
#engine.setProperty('rate', 60)
#engine.say(stringToSay)
#engine.runAndWait()

#myfile.write(string)

#voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#engine.say('My current speaking rate is ' + str(rate))
#engine.save_to_file(stringToSay, 'test.mp3')
#engine.runAndWait()
engine.stop()