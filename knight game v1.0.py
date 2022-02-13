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
    for row in maze:
        string=""
        lowerString=""
        for column in row:
            if column.walls[1]==False:
                string+="+---"
            else:
                string+="+   "
            if column.walls[3]==False:
                lowerString+="|   "
            else:
                lowerString+="    "
        newMaze.append(string)
        newMaze.append(lowerString)
    for row in newMaze:
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
mazeSize=5

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
plyr=player(input("Who is the hero of this story? >>> ").strip(),random.randint(50,100),[0,0])
if plyr.health<67:
    print(plyr.name,"enters the dungeon, feeling a little worn out.")
elif plyr.health<84:
    print(plyr.name,"enters the dungeon, sights set on victory.")
else:
    print(plyr.name,"enters the dungeon, feeling fresh and ready to battle.")
