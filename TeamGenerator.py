import random
#Tank/Main/Off - DPS - Heals/Main/Off


TankMain = [['Jesse',9],['Tim',8],['Lachlan',7],['Daniel',3],['Josh',3],['Sarah',2]]
TankOff = [['Lachlan',10],['Jesse',9],['Jarrod',5],['Aidan',5],['Josh',3],['Sarah',2]]
DpsHitscan = [['Lachlan',9],['Jesse',7],['Tim',6],['Ben',5],['Aidan',2]]
DpsProj = [['Rusti',9],['Lachlan',8],['Tim',5],['Joseph',4],['Jarrod',4]]
HealsMain = [['Tim',9],['Mitch',8],['Joseph',7],['Ben',5],['Sam',4]]
HealsOff = [['Sam',8],['Aidan',6]]

Players = [TankMain,TankOff,DpsHitscan,DpsProj,HealsMain,HealsOff]

Roles = ['TankMain','TankOff','DpsHitscan','DpsProj','HealsMain','HealsOff']


#Generates 12 Unique Players, Each from a Certain Role
def Generate_Teams():
    teams = []
    while len(teams) < 12:
        #Add Random Role to Team
        rand =(random.randint(0,len(Players)-1))
        #Add Random Player from that Role
        subrand = random.randint(0,len(Players[rand])-1)
        #check if player has been added to a team already
        if (unique_player(teams,[rand,subrand])):
            teams.append([rand,subrand])
    return (teams[0:6],teams[6:12])

#Checks if a player has been used already
def unique_player(team,player):
    player_name = Players[player[0]][player[1]]
    for x in team:
        team_player_name = Players[x[0]][x[1]]
        if player_name[0] == team_player_name[0]:
            return False
    return True

#Prints player Names for a Team and their Role
def printteam(team):
    for x in team:
        print(str(Players[(x[0])][(x[1])]) +"-" +  str(Role(x[0])))

def printteamsafe(team):
    for x in team:
        print(str(Players[(x[0])][(x[1])][0]) +" - " +  str(Role(x[0])))
#Returns the Role when given a interger
def Role(x):
    return Roles[x]

#Checks if the team Composition follows the rules
"""
        Min Max
T	    1	4
Main	0	2
Off	    0	3
D	    1	3
H	    2	2
Main	1	2
Off	    0	1
"""
def check_valid(team1):
    R = count_roles(team1)
    MT = R[0]
    OT = R[1]
    DH = R[2]
    DP = R[3]
    HM = R[4]
    HO = R[5]
    #Checks Tank Counts are Valid
    if (MT + OT)<1 | MT+OT > 4:
        return False
    if (MT >2):
        return False
    if (OT >3):
        return False
    #Checks DPS Counts are Valid
    if (DH+DP)<1 | (DH+DP)>3:
        return False
    #Checks Heal Counts are Valid
    if(HM + HO) != 2:
        return False
    if(HM)<1 | (HM > 2):
        return False
    if HO > 1:
        return False
    return True

#counts what roles a team has
def count_roles(team):
    teamroles = []
    roles_count = [0,0,0,0,0,0]
    for x in team:
        roles_count[x[0]] += 1
    return (roles_count)

#Caculated difference between SR of the two teams
def Teams_Difference(team1, team2):
    return abs(Teams_Worth(team1)-Teams_Worth(team2))
#Caculates the SR of a particular team
def Teams_Worth(Team):
    sums = 0
    for x in Team:
        Player = Players[x[0]][x[1]]
        sums += Player[1]
    return abs(sums)

#Generates Many Possible Teams
def Generate_Lots():
    List_of_Teams = []
    for i in range(0,1000):
        team1, team2 = Generate_Teams()
        if (check_valid(team1)) &(check_valid(team2)):
            List_of_Teams.append([team1,team2,Teams_Difference(team1,team2)])
    return List_of_Teams

#Sorts the Teams based on their Absolute Difference
def Sort_Teams(Teams):
    Teams.sort(key=lambda x: int(x[2]))
    return Teams

Teams = Generate_Lots()
Teams = Sort_Teams(Teams)

#Prints Top 5 Teams
for x in range(0,5):
    print("Team 1")
    printteamsafe(Teams[x][0])
    print("-----------------------")
    print("Team 2")
    printteamsafe(Teams[x][1])
    print("Difference")
    print(Teams[x][2])
    print("____________________")
    print("____________________")
    print("")



