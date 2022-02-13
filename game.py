import random

class player:
    def __init__(self,name,health,pos,exp=0):
        self.name=name
        self.health=health
        self.exp=exp
        self.pos=pos

class cell:
    def __init__(self):
        self.used=False
        self.walls=[True]*4
        self.contain=[]

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

def printMaze(maze):
    newMaze=[]
    for y,row in enumerate(maze):
        string=""
        lowerString=""
        for x,column in enumerate(row):
            if [x,y]==plyr.pos:
                string+="K"
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
                if column.walls[1]==False:
                    string+="---"
                else:
                    string+="   "
                if column.walls[3]==False:
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

# Depth First Search Maze Generation Algorithm
def genMaze(mazeSize):
    maze=[]
    for row in range(mazeSize):
        maze.append([])
        for column in range(mazeSize):
            maze[row].append(cell())
    stack=[]
    y,x=0,0
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
        else:
            stack.pop()
            y,x=stack[-1][0],stack[-1][1]
    return maze

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
                break
            else:
                print("Invalid choice")
    elif game:
        playing=True
        print("""
The beautiful princess has been stolen from the royal palace.
A plentiful reward is offered to anyone who can save her,
But standing between our hero and the princess,
Is a deadly dungeon, brimming with traps and monsters.
Our hero stands at the entrance, ready to conquer!
        """)
        plyr=player(input("Who is the hero of this story? >>> ").strip(),random.randint(50,100),[0,0])
        if plyr.health<67:
            print(plyr.name,"enters the dungeon, feeling a little worn out.\n")
        elif plyr.health<84:
            print(plyr.name,"enters the dungeon, sights set on victory.\n")
        else:
            print(plyr.name,"enters the dungeon, feeling fresh and ready to battle.\n")
        mazeSize=5
        maze=genMaze(mazeSize)
        known=[]
        next=[]
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
