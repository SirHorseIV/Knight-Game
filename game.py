import random

class player:
    def __init__(self,name,health,pos,map=False,dam=10):
        self.name=name
        self.health=health
        self.dam=dam
        self.pos=pos
        self.map=map

class cell:
    def __init__(self,walls):
        self.walls=walls

class enemy:
    def __init__(self,name,health,dam):
        self.name=name
        self.health=health
        self.dam=dam

def battle(plyr,enemy):
    print("\nA",enemy.name,"appeared!")
    if enemy.health>20:
        print("It looks threatening and dangerous, and ready to attack!")
    elif enemy.health>10:
        print("It stares you down, assessing the situation.")
    else:
        print("It looks weak, an easy target.")
    battling=True
    print("f-fight, r-run")
    while battling:
        choice=input("\nWhat do you want to do? >>> ")
        if choice=="f":
            dam=plyr.dam-2+random.randint(0,4)
            enemy.health-=dam
            print("You dealt",str(dam),"damage!")
            if enemy.health<=0:
                print("You killed "+enemy.name+"!\n")
                drop=random.randint(1,10)
                if drop<3:
                    plyr.map=True
                    print("What's this? The enemy dropped a map!")
                elif 2<drop<4:
                    plyr.health+=15
                    print("What's this? The enemy dropped a health potion!")
                    print("You drank it, restoring some health")
                battling=False
                break
            dam=enemy.dam-2+random.randint(0,4)
            plyr.health-=dam
            print(enemy.name,"dealt",str(dam),"damage!")
            if plyr.health<=0:
                print("You died.\n")
                break
            elif plyr.health<=20:
                print("You start to feel weary.")
        elif choice=="r":
            run=random.randint(1,2)
            if run==1:
                print("You got away!")
                battling=False
                break
            else:
                print(enemy.name,"blocks the way.")
                dam=enemy.dam-2+random.randint(0,4)
                plyr.health-=dam
                print(enemy.name,"dealt",str(dam),"damage!")
                if plyr.health<=0:
                    print("You died.\n")
                    break
                elif plyr.health<=20:
                    print("You are feeling weary from battle.")
        else:
            print("Invalid choice")

def generating(maze):
    for row in maze:
        for column in row:
            if column.walls==[True]*4:
                return True
    return False

def dirMoved(pos,newPos):
    if pos[0]-newPos[0]>0:
        return 2
    elif pos[0]-newPos[0]<0:
        return 3
    elif pos[1]-newPos[1]>0:
        return 0
    else:
        return 1

def printMaze(maze,bossRoom):
    newMaze=[]
    for y,row in enumerate(maze):
        string=""
        lowerString=""
        for x,column in enumerate(row):
            if [x,y]==plyr.pos:
                string+="K"
            elif [y,x]==bossRoom:
                string+="B"
            else:
                string+="+"
            if column.walls[1]==False:
                string+="---"
            else:
                string+="   "
            if column.walls[3]==False:
                lowerString+="|   "
            else:
                lowerString+="    "
        newMaze.append(string)
        newMaze.append(lowerString)
    for row in newMaze[:-1]:
        print(row)

def printKnownMaze(maze,known,next):
    newMaze=[]
    for y,row in enumerate(maze):
        string=""
        lowerString=""
        for x,column in enumerate(row):
            if [x,y] in known:
                if [x,y]==plyr.pos:
                    string+="K"
                elif [y,x]==bossRoom:
                    string+="B"
                else:
                    string+="+"
                if column.walls[1]==False:
                    string+="---"
                else:
                    string+="   "
                if column.walls[3]==False:
                    lowerString+="|   "
                else:
                    lowerString+="    "
            elif [x,y] in next:
                string+="."
                if column.walls[1]==False and [x,y+1]!=plyr.pos:
                    string+="---"
                else:
                    string+="   "
                if column.walls[3]==False and [x+1,y]!=plyr.pos:
                    lowerString+="|   "
                else:
                    lowerString+="    "
            else:
                string+=".   "
                lowerString+="    "
        newMaze.append(string)
        newMaze.append(lowerString)
    for row in newMaze[:-1]:
        print(row)

# Randomised Depth First Search Maze Generation Algorithm
def genMaze(mazeSize):
    maze=[]
    for row in range(mazeSize):
        maze.append([])
        for column in range(mazeSize):
            maze[row].append(cell([True]*4))
    stack=[]
    y,x=0,0
    max=len(stack)
    while generating(maze):
        valid=[]
        if x==0:
            if y==0:
                for i in range(2):
                    if maze[y+i][x-i+1].walls==[True]*4:
                        valid.append((y+i,x-i+1))
            elif y==mazeSize-1:
                for i in range(2):
                    if maze[y+i-1][x+i].walls==[True]*4:
                        valid.append((y+i-1,x+i))
            else:
                for i in range(3):
                    if maze[y+i-1][x-i**2+2*i].walls==[True]*4:
                        valid.append((y+i-1,x-i**2+2*i))
        elif x==mazeSize-1:
            if y==0:
                for i in range(2):
                    if maze[y+i][x+i-1].walls==[True]*4:
                        valid.append((y+i,x+i-1))
            elif y==mazeSize-1:
                for i in range(2):
                    if maze[y-i][x+i-1].walls==[True]*4:
                        valid.append((y-i,x+i-1))
            else:
                for i in range(3):
                    if maze[y+i-1][x+i**2-2*i].walls==[True]*4:
                        valid.append((y+i-1,x+i**2-2*i))
        elif y==0:
            for i in range(3):
                if maze[y-i**2+2*i][x+i-1].walls==[True]*4:
                    valid.append((y-i**2+2*i,x+i-1))
        elif y==mazeSize-1:
            for i in range(3):
                if maze[y+i**2-2*i][x+i-1].walls==[True]*4:
                    valid.append((y+i**2-2*i,x+i-1))
        else:
            for i in range(4):
                if i<2:
                    if maze[int(y+(i*(i-1.5)*(i-3)))][x+i-1].walls==[True]*4:
                        valid.append((int(y+(i*(i-1.5)*(i-3))),x+i-1))
                else:
                    if maze[int(y+(i*(i-1.5)*(i-3)))][x+i-2].walls==[True]*4:
                        valid.append((int(y+(i*(i-1.5)*(i-3))),x+i-2))
        if len(valid)>0:
            curCell=valid[random.randint(0,len(valid)-1)]
            maze[y][x].walls[dirMoved([y,x],curCell)]=False
            maze[curCell[0]][curCell[1]].walls[dirMoved(curCell,[y,x])]=False
            y,x=curCell[0],curCell[1]
            stack.append(curCell)
            if len(stack)>max:
                max=len(stack)
                bossRoom=list(curCell)
        else:
            stack.pop()
            y,x=stack[-1][0],stack[-1][1]
    return maze,bossRoom

def readSave():
    with open("save.txt","r") as save:
        file=save.read()
    file=file.split(",")
    if file[4]=="True":
        map=True
    else:
        map=False
    plyr=player(file[0],int(file[1]),[int(file[2]),int(file[3])],map)
    maze=file[5]
    bossRoom=[int(file[6]),int(file[7])]
    mazeSize=(round(len(maze)/4))**0.5
    newMaze=[]
    for i in range(0,len(maze),4):
        newMaze.append(maze[i:i+4])
    maze=newMaze
    newMaze=[]
    for i,c in enumerate(maze):
        walls=[]
        for b in c:
            if b=="0":
                walls.append(False)
            else:
                walls.append(True)
        maze[i]=walls
    for i,c in enumerate(maze):
        if i%mazeSize==0:
            newMaze.append([])
        newMaze[-1].append(cell(c))
    maze=newMaze
    known=file[8]
    newKnown=[]
    for i in range(0,len(known),2):
        newKnown.append(known[i:i+2])
    known=[]
    for c in newKnown:
        known.append([int(c[0]),int(c[1])])
    return plyr,maze,bossRoom,known

def writeSave(plyr,maze,bossRoom,known):
    mazeSize=len(maze)
    mazeString=""
    for row in maze:
        for column in row:
            for wall in column.walls:
                if wall:
                    mazeString+="1"
                else:
                    mazeString+="0"
    knownString=""
    for c in known:
        for coord in c:
            knownString+=str(coord)
    with open("save.txt","w") as save:
        save.write(str(plyr.name)+","+str(plyr.health)+","+str(plyr.pos[0])+","+
        str(plyr.pos[1])+","+str(plyr.map)+","+mazeString+","+str(bossRoom[0])+","+
        str(bossRoom[1])+","+knownString)

print("""
 _   __      _       _     _   _          ___
| | / /     (_)     | |   | | ( )        |_  |
| |/ / _ __  _  __ _| |__ | |_|/ ___       | | ___  _   _ _ __ _ __   ___ _   _
|    \| '_ \| |/ _` | '_ \| __| / __|      | |/ _ \| | | | '__| '_ \ / _ \ | | |
| |\  \ | | | | (_| | | | | |_  \__ \  /\__/ / (_) | |_| | |  | | | |  __/ |_| |
\_| \_/_| |_|_|\__, |_| |_|\__| |___/  \____/ \___/ \__,_|_|  |_| |_|\___|\__, |
                __/ |                                                      __/ |
               |___/                                                      |___/

""")
running=True
menu=True
while running:
    if menu:
        print("""1. New Game
2. Load Game
        """)
        inputting=True
        while inputting:
            choice=input(">>> ")
            if choice=="1":
                menu=False
                inputting=False
                game=True
                newSave=True
                break
            elif choice=="2":
                try:
                    plyr,maze,bossRoom,known=readSave()
                    menu=False
                    inputting=False
                    game=True
                    newSave=False
                    break
                except:
                    print("Save file does not exist")
            else:
                print("Invalid choice")
    elif game:
        playing=True
        next=[]
        mazeSize=7
        if newSave:
            print("""
The beautiful princess has been stolen from the royal palace.
A plentiful reward is offered to anyone who can save her,
But standing between our hero and the princess,
Is a deadly dungeon, brimming with traps and monsters.
Our hero stands at the entrance, ready to conquer!
Remember, enemies may be carrying useful items.
            """)
            plyr=player(input("Who is the hero of this story? >>> ").strip(),random.randint(50,100),[0,0])
            if plyr.health<67:
                print(plyr.name,"enters the dungeon, feeling a little worn out.\n")
            elif plyr.health<84:
                print(plyr.name,"enters the dungeon, sights set on victory.\n")
            else:
                print(plyr.name,"enters the dungeon, feeling fresh and ready to battle.\n")
            maze,bossRoom=genMaze(mazeSize)
            known=[]
            newSave=False
        print("To move, type in l-left, r-right, u-up, d-down")
        while playing:
            dirs=""
            validDir=[False]*4
            if not maze[plyr.pos[1]][plyr.pos[0]].walls[0]:
                dirs+=" left,"
                validDir[0]=True
            if not maze[plyr.pos[1]][plyr.pos[0]].walls[1]:
                dirs+=" right,"
                validDir[1]=True
            if not maze[plyr.pos[1]][plyr.pos[0]].walls[2]:
                dirs+=" up,"
                validDir[2]=True
            if not maze[plyr.pos[1]][plyr.pos[0]].walls[3]:
                dirs+=" down,"
                validDir[3]=True
            known.append([plyr.pos[0],plyr.pos[1]])
            if validDir[0]:
                next.append([plyr.pos[0]-1,plyr.pos[1]])
            if validDir[2]:
                next.append([plyr.pos[0],plyr.pos[1]-1])
            if plyr.map:
                printMaze(maze,bossRoom)
            else:
                printKnownMaze(maze,known,next)
            print("You can move"+dirs[:-1]+".")
            inputting=True
            while inputting:
                move=input("What do you want to do? >>> ")
                if move=="l" and validDir[0]:
                    plyr.pos[0]-=1
                    inputting=False
                elif move=="r" and validDir[1]:
                    plyr.pos[0]+=1
                    inputting=False
                elif move=="u" and validDir[2]:
                    plyr.pos[1]-=1
                    inputting=False
                elif move=="d" and validDir[3]:
                    plyr.pos[1]+=1
                    inputting=False
                else:
                    print("Invalid choice")
            writeSave(plyr,maze,bossRoom,known)
            if plyr.pos==bossRoom[::-1]:
                battle(plyr,enemy("goblin king",40,9))
                if plyr.health>0:
                    print("""
You return to the palace, with the princess.
Awaiting you are the riches of the kingdom!
You Win!
""")
                playing=False
                game=False
                menu=True
                break
            elif random.randint(1,5)==5:
                battle(plyr,enemy("goblin",random.randint(7,25),random.randint(4,8)))
                if plyr.health<=0:
                    playing=False
                    game=False
                    menu=True
                    break
