tempList = []                   #Creates a list for temporary storing the current input values
progressionList = []            #Creates a list for storing all the progression outcomes
exitChoice = "y"                #This is to start the loop

#The counts are for keeping count of how many times each is calculated
progressCount = 0
trailingCount = 0
retreiverCount = 0
excludedCount = 0

#The credits are to keep count of the entered credits
passCredit = 0
deferCredit = 0
failCredit = 0

count = 0           #Creates a count for where to store the current input values






##Main Version
def calculateProgression(passCredit, deferCredit, failCredit):      #Initialises the function and carries the arguments
    total = passCredit + deferCredit + failCredit                   #Adds up the credits and stores it in total

    if total > 120 or total <=0:                        #Checks to see if the total is above 120
        print("Total incorrect")                        #If total is above 120 then output incorrect
    elif passCredit == 120:                             #Checks to see if the pass credit is 120
        print("Progress")                               #Outputs progress if the passcredit is 120
    elif passCredit == 100:                             #Checks to see if the passcredit is 1005
        print("Progress (module trailer)")              #Outputs if the passcredit is 100
    elif failCredit >= 80:                              #Checks to see if the fail credit is equal to or greater than 80
        print("Exclude")                                #If it is then it outputs exclude
    elif deferCredit <= 120:                            #Checks to see if the defercredit is less than or equal to 120
        print("Do not Progress - module retriever")     #If it is then output this

##SATRT OF PROGRAM
try:                                    #Start of the try except statement this is to ensure that the program takes in a non integer and outputs an error
    passCredit = 0                      #Sets the passcredit to 0
    deferCredit = 0                     #Sets the defer credit to 0
    failCredit = 0                      #Sets the fail credit to 0

    passCredit = int(input("Enter your credits at pass: "))         #Inputs the pass credit
    if passCredit % 20 == 0:                                        #Checks to see if the input is in the range 0,20,40,60,80,100,120
        deferCredit = int(input("Enter your credits at defer: "))   #Input defer credit
        if deferCredit % 20 == 0:
            failCredit = int(input("Enter your credits at fail: "))
            if failCredit % 20 == 0:
                calculateProgression(passCredit, deferCredit, failCredit)   #calls the function and passes the arguments so that the progression can be calculated
            else:
                print("Out of range")       #If the input for passcredit is out of range it will print out of range
        else:
            print("Out of range")           #If the input for defercredit is out of range it will print out of range
    else:
        print("Out of range")               #If the input for fail credit is out of range it will print out of range

except ValueError:                          #This checks to see if the input is not an integer
    print("Integer required")               #This will output if the input for any credit is not an integer







##Staff Version
##START OF  PROGRAM
while exitChoice == "y":        #Will keep the program looping until the user does not want to continue

    passCredit = 0              #Sets the passCredit to 0 to reset everytime it loops
    deferCredit = 0             #Sets the deferCredit to 0 to reset everytime it loops
    failCredit = 0              #Sets the failCredit to 0 to reset everytime it loops
    try:                        #Start of the try except statement this is to ensure that the program takes in a non integer and outputs an error
        passCredit = int(input("Enter your credits at pass: "))         #Inputs the pass credit        
        if passCredit % 20 == 0:                                        #Checks to see if the input is in the range 0,20,40,60,80,100,120
            tempList.append(passCredit)                                 #Stores the passcredit into the templist
            
            deferCredit = int(input("Enter your credits at defer: "))   #Input defer credit     
            if deferCredit % 20 == 0:
                tempList.append(deferCredit)#stores the defercredit into the templist
                
                failCredit = int(input("Enter your credits at fail: ")) 
                if failCredit % 20 == 0:
                    tempList.append(failCredit)#stores the failcredit into the templist
                    
                    total = passCredit + deferCredit + failCredit       #Adds up the credits and stores it in total
                    
                    if total > 120 or total <=0::                       #Checks to see if the total is above 120
                        print("Total incorrect")                        #If total is above 120 then output incorrect
                        
                    elif passCredit == 120:                             #Checks to see if the pass credit is 120
                        print("Progress")                               #Outputs progress if the passcredit is 120
                        progressCount = progressCount + 1               #Adds
                        tempList.insert(0,("Progress - "))
                        
                    elif passCredit == 100:                             #Checks to see if the passcredit is 1005
                        print("Progress (module trailer)")              #Outputs if the passcredit is 100
                        trailingCount = trailingCount + 1
                        tempList.insert(0,("Progress (module trailer) - "))
                        
                    elif failCredit >= 80:                              #Checks to see if the fail credit is equal to or greater than 80
                        print("Exclude")                                #If it is then it outputs exclude
                        excludedCount = excludedCount + 1               
                        tempList.insert(0,("Exclude - "))               
                        
                    elif deferCredit <= 120:                            #Checks to see if the defercredit is less than or equal to 120
                        print("Do not Progress - module retriever")     #if it is then output this
                        retreiverCount = retreiverCount + 1
                        tempList.insert(0,("Retriever - "))
                else:
                    print("Out of range")                       #If the input for passcredit is out of range it will print out of range
            else:
                print("Out of range")                           #If the input for defercredit is out of range it will print out of range
        else:
            print("Out of range")                               #If the input for fail credit is out of range it will print out of range

    except ValueError:                                          #This checks to see if the input is not an integer
        print("Integer required")                               #This will output if the input for any credit is not an integer
        

    progressionList.append(tempList)                    #Takes all the items in templist and stores them into the permanent list
    tempList = []                                       #Then clears the templist to use for the next set of data
    count = count + 1                                   #Keeps count of how long the list wwill be by counting the times it loops
    
    print("")
    print("Would you like to enter another set of data?")
    exitChoice = input("Enter 'y' for yes or 'q' to quit and view results: ")
    print("")
#Horizontal Histogram
print("----------------------------------------------------------------------")
print("Horizontal Histogram")
print("")
print("Progress", progressCount, " : ", end = ' ')          #The "end = ' '" is to make sure the stars get printed onto the same line
for x in range(progressCount):                              #Loops the amount of times progress was calculated
    print("*", end = ' ')                                   #Prints a star on the same line

print("")
print("Trailer", trailingCount, " : ", end = ' ')
for x in range(trailingCount):                              #Loops the amount of times trailing was calculated
    print("*", end = ' ')
    
print("")
print("Retreiver", retreiverCount, " : ", end = ' ')   
for x in range(retreiverCount):                             #Loops the amount of times retreiver was calculated
    print("*", end = ' ')

print("")
print("Excluded", excludedCount, " : ", end = ' ')
for x in range(excludedCount):                              #Loops the amount of times excluded was calculated
    print("*", end = ' ')

print("")
outcomeTotal = progressCount + trailingCount + retreiverCount + excludedCount   #Adds up all the counts and stores in outcometotal
print(outcomeTotal, "outcomes in total.")                   #Prints outcometotal

##VerticalHistogram
##Reference for vertical histogram = https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
#The referenced code has been modified slihtly to work with the program
print("Vertical Histogram")
header = ["Progress", "Trailing", 'Retriever', 'Excluded']                              #Creates a header where the stars will go under
print(" ".join(header))
for x in range(max(progressCount, trailingCount, retreiverCount, excludedCount)):       #Will loop printing stars until the range of the highest number in the counts variables
    print("   {0}         {1}       {2}         {3}".format(                                                    #It will print a star in the positions 0,1,2,3
        "*" if x < progressCount else " ",                                              #Prints a star of the progress count is greater than x else it will print nothing
        "*" if x < trailingCount else " ",
        "*" if x < retreiverCount else " ",
        "*" if x < excludedCount else " "))
    
outcomeTotal = progressCount + trailingCount + retreiverCount + excludedCount           #Adds up the total entries together
print(outcomeTotal, "outcomes in total.")                                               #Prints out ther toal number of entries


#Part 3
print("----------------------------------------------------------------------")
for x in range(count):                              #Loops till the end of the list
    print(progressionList[x][0], end = "")          #Prints the first item of the list the prediction
    print(progressionList[x][1], ", ", end = "")    #Prints the passcredit of the current prediction
    print(progressionList[x][2], ", ", end = "")    #Prints the defercredit for the current prediction
    print(progressionList[x][3])                    #Prints the failcredit for the current prediction




#Part 4
x = 0           #Resets the variable x to 0
with open("w1824056.txt", "w") as f:             #Opens a testfile in the dame directory as the script(in order to test this the w1824056.txt must be in the same place as the python script)
    for x in range(count):                                  #Loops for however many items there are in the progressionlist
        f.write(str(progressionList[x][0]) + "")            #Writes the prediction to the txt file
        f.write(str(progressionList[x][1]) + ", ")          #Writes the passcredit to the txt file
        f.write(str(progressionList[x][2]) + ", ")          #Writes the defercredit to the txt file
        f.write(str(progressionList[x][3]))                 #Writes the failcredit to the txt file
        f.write("\n")                                       #Writes "\n" tio the txt file to keep spaces invbetween each entry
        
with open("w1824056.txt", "r") as f:        #then open the text file where everything is written down
    contents = f.read()                     #read the contents of the txt file
    print(contents)                         #print the content of the txt file

