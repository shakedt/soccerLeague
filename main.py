import csv

#soccer_players.csv
#The functions take a csv file and returns a list of dictonarys with the propper deatils
def  intoDict(csvfile):
    file = open(csvfile)
    file_csv = csv.reader(file)
    lis = []
    for row in file_csv:
        lis.append({'Name': row[0],
                    'Height (inches)': row[1],
                    'Soccer Experience': row[2],
                    'Gurdian Name(s)': row[3]})

    del lis[0]
    return lis

#a function to find out how many players have experince
def hasExperince(listDicts):
    counter = 0 #counter for the item
    for item in listDicts: # a for loop to find out how many people with exprince are in the team
        if item['Soccer Experience'] == 'YES':
            counter += 1

    return counter

#the function take the list of players and the amount of people with experince
#the purpose of the function is to set them into 3 groups
def makeLeague(listPlayers):
    sharks = []
    dragons = []
    raptors = []
    league = []
    sCounter = 0
    dCounter = 0
    rCounter = 0
    newCounter= 0
    for player in listPlayers:
        if player['Soccer Experience'] == 'YES' and sCounter < 3:
            sharks.append(player)
            sCounter += 1
        elif player['Soccer Experience'] == 'YES' and dCounter < 3:
            dragons.append(player)
            dCounter += 1
        elif player['Soccer Experience'] == 'YES' and rCounter < 3:
            raptors.append(player)
            rCounter += 1
        else:
            if newCounter < 3:
                sharks.append(player)
                newCounter += 1
            elif newCounter < 6:
                dragons.append(player)
                newCounter += 1
            else:
                raptors.append(player)
    league.append(sharks)
    league.append(dragons)
    league.append(raptors)
    return league


#write letter functions
def write_letter(player,letter):
    #take the gurdian names of the player and add them into the string
    newLetter = letter.format(GurdianName = player['Gurdian Name(s)'], name = player['Name'], time = '10:45', location = 'amazing Location')
    return newLetter






#Write the Letter to disk and name the file the player name
def saveToDisk(player,letter):
    playerName = player['Name']    # taking the name of the player to user as file name
    playerName = playerName.replace(' ', '_')   #replacing space with underscore
    file = open(playerName + '.txt', 'w')
    file.write(letter)

    #close the file
    pass

#this function saves letters for each player **dependent on other functions
def saveLeagueLetters(playerDicts, letter):
    for player in playerDicts:
        fixed_letter = write_letter(player,letter)
        saveToDisk(player,fixed_letter)



#testing
league = (makeLeague(intoDict('soccer_players.csv')))
print(len(league[2]))
################3more testing
playerDict = intoDict('soccer_players.csv') #create a functional dictonary
#create propper fixed letter
letter = write_letter(playerDict[0],'hello {GurdianName}, please bring {name} arrive at the requested time: {time}, to this {location}')
#save 1 letter to disk
saveToDisk(playerDict[0], letter)
#save all players
letterx = 'hello {GurdianName}, please bring {name} arrive at the requested time: {time}, to this {location}'
saveLeagueLetters(playerDict, letterx)