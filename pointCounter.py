#Program Purpose: Create a point tracker for kids camp
import sys
import pygame
pygame.display.init()
pygame.font.init()
display = pygame.display.set_mode((1000,500),pygame.RESIZABLE)
clock = pygame.time.Clock()
ranks = ["private", "specialist", "seargeant", "lieutenant", "general"]
#  team#:[points,rank,placement]
file = open ("teams.txt","r")
value = [""]
x = 0
teams = {}
for char in file.read():
    if char == ",":
        value.append("")
        x += 1
    elif char == ":":
        if value[1].isdigit():
            teams[value[0]] = [int(value[1])]
        else:
            teams[value[0]] = [value[1]]
        value = [""]
        x = 0
    else:
        value[x] += char
        

# potstick and red d decided to go on a walk
# on their walk they saw a flock and a man with a big red c

def screen(display, teams, amount, addRes):
        armyColors = [(84, 90, 44), (89, 68, 25), (135, 121, 34), (50, 58, 20), (69, 77, 50), (110, 124, 97), (55, 60, 39), (75, 50, 19), (178, 157, 105)]
        pygame.display.set_caption("Point Tracker")
        camo = pygame.image.load(r"C:\Users\yulia\OneDrive\Documents\Point Counter\camo.jpg")
        camo = pygame.transform.rotozoom(camo, 90, .8)
        display.blit(camo, (0, -5))
        font = pygame.font.SysFont("stencil", 40)
        teamy = 21
        ranky = 20
        barY = 15
        x = 0
        pygame.draw.rect(display, (108, 120, 46), [0, 0, 270, 1200])
        sortTms = sortTeams(teams)
        bars(teams)
        for team in sortTms:
            if amount[team] and not endRes[team]:
                endRes[team] = teams[team][0] + int(amount[team])
                amount[team] = ""
            if teams[team][0] < endRes[team] and addRes:
                teams[team][0] += 10
            score = teams[team][0]
            rank = teams[team][1]
            placement = teams[team][2]
            barLen = teams[team][3]
            pointOffset = teams[team][4]
            name = font.render(str(team), True, (0, 0, 0))
            points = font.render(str(score), True, (0, 0, 0))
            display.blit(name, (60, teamy))
            display.blit(rankImage(rank)[0], (10 + rankImage(rank)[1], ranky + rankImage(rank)[2]))
            pygame.draw.rect(display, (0, 0, 0), [270, barY - 5, barLen, 60])
            pygame.draw.rect(display, armyColors[x], [270, barY, barLen -5, 50])
            if len(str(score)) == 3 and score >= 250:
                display.blit(points, (pointOffset + 270 - 35, teamy))
            elif len(str(score)) == 4:
                display.blit(points, (pointOffset + 270 - 48, teamy))
                
            barY += 70
            teamy += 70
            ranky += 70
            x += 1
        pygame.display.update()
# from teams area to end of screen = 1010 pixels
# each rank should be 202 pixels apart
# 600 points = 202 pixels

def rankImage(rank):
    if rank == "private":
        private = pygame.transform.scale(pygame.image.load(r"C:\Users\yulia\OneDrive\Documents\Point Counter\private.png"), (35, 30))
        return [private, 0, 0]
    elif rank == "specialist":
        specialist = pygame.transform.scale(pygame.image.load(r"C:\Users\yulia\OneDrive\Documents\Point Counter\specialist.png"), (35, 40))
        return [specialist, 0, -4]
    elif rank == "sergeant":
        sergeant = pygame.transform.scale(pygame.image.load(r"C:\Users\yulia\OneDrive\Documents\Point Counter\sergeant.png"), (35, 40))
        return [sergeant, 0, -7]
    elif rank == "lieutenant":
        lieutenant = pygame.transform.scale(pygame.image.load(r"C:\Users\yulia\OneDrive\Documents\Point Counter\lieutenant.png"), (10, 30))
        return [lieutenant, 13, 0]
    elif rank == "general":
        general = pygame.transform.scale(pygame.image.load(r"C:\Users\yulia\OneDrive\Documents\Point Counter\general.svg"), (35, 35))
        return [general, 0, 0]
        
def bars(teams):
    for team in teams:
        score = teams[team][0]
        pixels = score//(1/(252.5/750))
        if len(teams[team]) > 3:
            teams[team][3] = pixels
        else:
            teams[team].append(pixels)

def placement(teams):
    dispTeams = []
    for team in teams.keys():
        dispTeams.append(team)
    x = 1

    while dispTeams:
        highest = 0
        for team in dispTeams:
            score = teams[team][0] 
            if int(score) > int(highest):
                highest = score
        for team in teams:
            score = teams[team][0] 
            if int(score) == int(highest):
                if len(teams[team]) < 3:
                    teams[team].append(x)
                else:
                    teams[team][2] = (x)
                dispTeams.remove(team)
        x += 1

def chooseRank(teams):
    for team in teams:
        score = teams[team][0]
        rank = int(score) / 600
        if len(teams[team]) < 2:
            if rank < 1:
                teams[team].append("private")
            elif rank >= 1 and rank < 2:
                teams[team].append("specialist")
            elif rank >= 2 and rank < 3:
                teams[team].append("sergeant")
            elif rank >= 3 and rank < 4:
                teams[team].append("lieutenant")
            elif rank >= 4:
                teams[team].append("general")
        else:
            if rank < 1:
                teams[team][1] = "private"
            elif rank >= 1 and rank < 2:
                teams[team][1] = "specialist"
            elif rank >= 2 and rank < 3:
                teams[team][1] = "sergeant"
            elif rank >= 3 and rank < 4:
                teams[team][1] = "lieutenant"
            elif rank >= 4:
                teams[team][1] = "general"
        
            
def sortTeams(teams):
    dispTeams = []
    for team in teams.keys():
        dispTeams.append(team)
    teamL = []
    while dispTeams:
        x = [0]
        group = []
        for team in dispTeams:
            if int(teams[team][0]) > int(x[0]):
                x = [teams[team][0]]
                group = [team]
            elif int(teams[team][0]) == int(x[0]):
                group.append(team)
        for team in group:
            dispTeams.remove(team)
        teamL.append(group)
    tempTeams = teamL
    teamL = []
    for team in tempTeams:
        while team:
            teamL.append(team[0])
            team.remove(team[0])
    return teamL


def dispScore(teams):
    for team in teams:
        teamL = teams[team]
        scoreX = teamL[3]/2
        if len(teamL) > 4:
            teams[team][4] = scoreX
        else:
            teams[team].append(scoreX)
def checkButtons(pos):
    button = False
    x, y = pos
    if x >= 200 and x <= 280:
        if y >= 10 and y <= 40:
            button = True
            return button, "FAST"
        elif y >= 45 and y <= 75:
            button = True
            return button, "Bravo Co."
        elif y >= 80 and y <= 110:
            button = True
            return button, "BMW"
        elif y >= 115 and y <= 145:
            button = True
            return button, "G.I.Joes"
        elif y >= 150 and y <= 180:
            button = True
            return button, "SWAT"
        elif y >= 185 and y <= 215:
            button = True
            return button, "Cupcakes"
        elif y >= 220 and y <= 250:
            button = True
            return button, "CIA"
        elif y >= 255 and y <= 285:
            button = True
            return button, "Light"
        elif y >= 290 and y <= 320:
            button = True
            return button, "SOAR"
    if not button:
        return button, None
    
    
#to open menu click within the top left corner: 50 by 50 pixels
def openMenu():
    click = False
    if pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[0] <= 50 and pygame.mouse.get_pos()[1] >= 0 and pygame.mouse.get_pos()[1] <= 50:
        click = True
    return click
def openScreen():
    click = False
    if pygame.mouse.get_pos()[0] >= 160 and pygame.mouse.get_pos()[0] <= 220 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[1] <= 360:
        click = True
    return click
    

x = 200
rects = {"FAST":[False, [x, 10, 80, 30]], "Bravo Co.":[False, [x, 45, 80, 30]], "BMW":[False, [x, 80, 80, 30]],  "G.I.Joes":[False,[x, 115, 80, 30]], "SWAT":[False, [x, 150, 80, 30]], "Cupcakes":[False,[x, 185, 80, 30]], "CIA":[False,[x, 220, 80, 30]], "Light":[False,[x, 255, 80, 30]], "SOAR":[False,[x, 290,80, 30]]}
amount = {"FAST": "", "Bravo Co.": "", "BMW": "", "G.I.Joes": "", "SWAT": "", "Cupcakes": "", "CIA": "", "Light": "", "SOAR": ""}
endRes = {"FAST": 0, "Bravo Co.": 0, "BMW": 0, "G.I.Joes": 0, "SWAT": 0, "Cupcakes": 0, "CIA": 0, "Light": 0, "SOAR": 0}
def menu(teams, rects, amount):
    display.fill((255, 255, 255))
    teamWrd = pygame.font.SysFont("georgia", 25)
    buttons = pygame.font.SysFont("georgia", 15)
    y = 10
    for team in teams:
        for rect in rects:
             val = rects[rect]
             if val[0]:
                 pygame.draw.rect(display, (230, 230, 230), val[1], 5)
             elif not val[0]:
                 pygame.draw.rect(display, (50, 50, 50), val[1], width = 1)
        pygame.draw.rect(display, (0, 0, 0), [158, 338, 64, 24])
        pygame.draw.rect(display, (200, 200, 200), [160, 340, 60, 20])
        add = buttons.render("add", True, (0, 0, 0))
        name = teamWrd.render(str(team), True, (0, 0, 0))
        numFont = pygame.font.SysFont("georgia", 20)
        num = numFont.render(amount[team], True, (0, 0, 0))
        display.blit(name, (10, y))
        display.blit(add, (175, 340))
        display.blit(num, (rects[team][1][0] + 5, rects[team][1][1]))
        y += 35
    click, button = checkButtons(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
        if pygame.mouse.get_pressed()[0] and not disp:
            if click:
                rects[button][0] = True
            for rect in rects:
                x, y = pygame.mouse.get_pos()
                specs = rects[rect]
                if specs[0] and not (x >= specs[1][0] and x <= specs[1][0] + 80 and y >= specs[1][1] and y <= specs[1][1] + 30):
                    rects[rect][0] = False
        
        sumthin = False
        for rect in rects:
            if rects[rect][0]:
                sumthin = True
                break
        for rect in rects:
            vals = rects[rect]
            if vals[0] and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    amount[rect] += "0"
                elif event.key == pygame.K_1:
                    amount[rect] += "1"
                elif event.key == pygame.K_2:
                    amount[rect] += "2"
                elif event.key == pygame.K_3:
                    amount[rect] += "3"
                elif event.key == pygame.K_4:
                    amount[rect] += "4"
                elif event.key == pygame.K_5:
                    amount[rect] += "5"
                elif event.key == pygame.K_6:
                    amount[rect] += "6"
                elif event.key == pygame.K_7:
                    amount[rect] += "7"
                elif event.key == pygame.K_8:
                    amount[rect] += "8"
                elif event.key == pygame.K_9:
                    amount[rect] += "9"
                elif event.key == pygame.K_BACKSPACE:
                    amount[rect] = amount[rect][0:-1]
    pygame.display.update()
    return amount

    
disp = True
stop = False
addRes = False
while not stop:
    clock.tick(120)
    chooseRank(teams)
    placement(teams)
    bars(teams)
    dispScore(teams)

    if disp:
        screen(display, teams, amount, addRes)
    else:
        amount = menu(teams, rects, amount)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
        if pygame.mouse.get_pressed()[0] and openMenu() and disp:
            endRes = {"FAST": 0, "Bravo Co.": 0, "BMW": 0, "G.I.Joes": 0, "SWAT": 0, "Cupcakes": 0, "CIA": 0, "Light": 0, "SOAR": 0}
            addRes = False
            display = pygame.display.set_mode((300,370))
            disp = False
        if pygame.mouse.get_pressed()[0] and openScreen() and not disp:
            display = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
            disp = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                addRes = True
        
    
    

#Closing the Program (saving team data, stopping the display, exiting the program)
store = ""
for key in teams:
    store += key
    for value in teams[key]:
        store += "," + str(value)
        break
    store += ":"
file = open("teams.txt","w")
file.write(store)
file.close()
pygame.display.quit()
sys.exit()
