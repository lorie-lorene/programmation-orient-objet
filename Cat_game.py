from os import system
import time
import random

d_row = [1, -1, 0, 0, 1, 1, -1, -1]    #The directions
d_column = [0, 0, 1, -1, 1, -1, 1, -1]

# A class to store the current location and distance, and will be used to fine the shortest distance from a point to another
class QItem:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

class Cat:
    def __init__(self, gender, pos, map): # The gender will either be 1 for male or 2 for female
        self.gender = gender
        self.pos = [pos[0],pos[1]]
        self.isAlive = True
        map[self.pos[0]][self.pos[1]] = self.gender
        self.TTL = 5      # this represents the life points of the cat
        self.Total_moves = 0
    
    # this fonction is used in minDistance fonction in order to see if a cell is valid
    def isValid(self, row, col, map, visited):
        result = False
        if row >= 0 and col >= 0 and row < len(map) and col < len(map) and visited[row][col] == False :
            if map[row][col] != 5 and map[row][col] != self.gender:
                result = True
        return result

    # Function to calculate the minimum distance from the current location to the nearest mouse
    def minDistance(self, grid, row, col):
        source = QItem(row, col, 0)
        queue = [source]
        visited = [[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False]]
        
        visited[source.row][source.col] = True
        while len(queue) > 0:
            p = queue.pop(0)

            if grid[p.row][p.col] == 3 or grid[p.row][p.col] == 4:
                return p.dist
            
            # move up
            if self.isValid(p.row - 1, p.col, grid, visited):
                queue.append(QItem(p.row-1, p.col, p.dist+1))
                visited[p.row-1][p.col] = True

            # move down
            if self.isValid(p.row + 1, p.col, grid, visited):
                queue.append(QItem(p.row+1, p.col, p.dist+1))
                visited[p.row+1][p.col] = True

            # move left
            if self.isValid(p.row, p.col - 1, grid, visited):
                queue.append(QItem(p.row, p.col-1, p.dist+1))
                visited[p.row][p.col-1] = True

            # move right
            if self.isValid(p.row, p.col + 1, grid, visited):
                queue.append(QItem(p.row, p.col+1, p.dist+1))
                visited[p.row][p.col+1] = True

        return -1

    def move(self,grid):
        if self.TTL == 0:
            grid[self.pos[0]][self.pos[1]] = 0
            self.isAlive = False
        
        if self.isAlive:
            dist = self.minDistance(grid, self.pos[0], self.pos[1])

            for i in range(4):
                row = self.pos[0] + d_row[i]
                column = self.pos[1] + d_column[i]

                if row < 0 or column < 0: continue
                if row >= len(grid) or column >= len(grid): continue
                if grid[row][column] == 5 or grid[row][column] == self.gender: continue

                if self.minDistance(grid, row, column) == dist-1:
                    grid[self.pos[0]][self.pos[1]] = 0
                    grid[row][column] = self.gender
                    self.pos[0] = row
                    self.pos[1] = column
                    self.TTL-=1
                    self.Total_moves+=1
                    break
    
    def eat(self, m):
        if self.isAlive:
            i=0
            while i < len(m):
                if self.pos[0] == m[i].pos[0] and self.pos[1] == m[i].pos[1] and m[i].isAlive:
                    m[i].isAlive = False
                    self.TTL+=4
                i+=1

    def reproduce(self, c, map):
        j = -1
        i = 0
        while i < len(c):
            if self.isAlive:
                if self.pos[0] == c[i].pos[0] and self.pos[1] == c[i].pos[1] and self.gender != c[i].gender and c[i].isAlive:
                    map[self.pos[0]][self.pos[1]] = 0
                    map[c[i].pos[0]][c[i].pos[1]] = 0
                    c.append(Cat(random.randint(1,2), self.pos, map))
                    row = self.pos[0]
                    column = self.pos[1]

                    for k in range(8):
                        x = row + d_row[k]
                        y = column + d_column[k]

                        if x < 0 or y < 0: continue
                        if x >= len(map) or y >= len(map): continue
                        if map[x][y] != 0: continue

                        self.pos[0] = x
                        self.pos[1] = y
                        break

                    for k in range(8):
                        x = row + d_row[k]
                        y = column + d_column[k]

                        if x < 0 or y < 0: continue
                        if x >= len(map) or y >= len(map): continue
                        if map[x][y] != 0: continue

                        c[i].pos[0] = x
                        c[i].pos[1] = y
                        break
                    j = i
                    break
            i+=1
        return j

class Mouse:
    def __init__(self, gender, pos, map):
        self.gender = gender # the gender can either be 3 for male or 4 for female
        self.pos = [0,0]
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.isAlive = True
        map[self.pos[0]][self.pos[1]] = self.gender
        self.TTL = 5            # represents the life points of the mouse
        self.Total_moves = 0
    
    # fonction to check for the validity of a cell, will be used in finding the minimum distance
    def isValid(self, row, col, map, visited):
        result = False
        if row >= 0 and col >= 0 and row < len(map) and col < len(map) and visited[row][col] == False :
            if map[row][col] == 0 or map[row][col] == 5:
                result = True
        return result

    def minDistance(self, grid, row, col):
        source = QItem(row, col, 0)
        queue = [source]

        visited = [[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False]]
        
        visited[source.row][source.col] = True
        while len(queue) > 0:
            p = queue.pop(0)

            if grid[p.row][p.col] == 5:
                return p.dist
            
            # moving up
            if self.isValid(p.row - 1, p.col, grid, visited):
                queue.append(QItem(p.row-1, p.col, p.dist+1))
                visited[p.row-1][p.col] = True

            # moving down
            if self.isValid(p.row + 1, p.col, grid, visited):
                queue.append(QItem(p.row+1, p.col, p.dist+1))
                visited[p.row+1][p.col] = True

            # moving left
            if self.isValid(p.row, p.col - 1, grid, visited):
                queue.append(QItem(p.row, p.col-1, p.dist+1))
                visited[p.row][p.col-1] = True

            # moving right
            if self.isValid(p.row, p.col + 1, grid, visited):
                queue.append(QItem(p.row, p.col+1, p.dist+1))
                visited[p.row][p.col+1] = True

        return -1

    def move(self,grid):
        if self.TTL == 0:
            grid[self.pos[0]][self.pos[1]] = 0
            self.isAlive = False
        
        if self.isAlive:
            dist = self.minDistance(grid, self.pos[0], self.pos[1])

            for i in range(4):
                row = self.pos[0] + d_row[i]
                column = self.pos[1] + d_column[i]

                if row < 0 or column < 0: continue
                if row >= len(grid) or column >= len(grid): continue
                if grid[row][column] == 1 or grid[row][column] == self.gender or grid[row][column] == 2: continue

                if self.minDistance(grid, row, column) == dist-1:
                    grid[self.pos[0]][self.pos[1]] = 0
                    grid[row][column] = self.gender
                    self.pos[0] = row
                    self.pos[1] = column
                    self.TTL-=1
                    self.Total_moves+=1
                    break
    
    def eat(self, m):
        if self.isAlive:
            i=0
            while i < len(m):
                if self.pos[0] == m[i].pos[0] and self.pos[1] == m[i].pos[1] and m[i].isAlive:
                    m[i].isAlive = False
                    self.TTL+=4
                i+=1

    def reproduce(self, m, map):
        j = -1
        i = 0
        while i < len(m):
            if self.isAlive:
                if self.pos[0] == m[i].pos[0] and self.pos[1] == m[i].pos[1] and self.gender != m[i].gender and m[i].isAlive:
                    map[self.pos[0]][self.pos[1]] = 0
                    map[m[i].pos[0]][m[i].pos[1]] = 0
                    m.append(Cat(random.randint(3,4), self.pos, map))
                    row = self.pos[0]
                    column = self.pos[1]

                    for k in range(8):
                        x = row + d_row[k]
                        y = column + d_column[k]

                        if x < 0 or y < 0: continue
                        if x >= len(map) or y >= len(map): continue
                        if map[x][y] != 0: continue

                        self.pos[0] = x
                        self.pos[1] = y
                        break

                    for k in range(8):
                        x = row + d_row[k]
                        y = column + d_column[k]

                        if x < 0 or y < 0: continue
                        if x >= len(map) or y >= len(map): continue
                        if map[x][y] != 0: continue

                        m[i].pos[0] = x
                        m[i].pos[1] = y
                        break
                    j = i
                    break
            i+=1
        return j

class Maize:
    def __init__(self, pos, map):
        self.pos = [pos[0], pos[1]]
        self.isAlive = True
        map[self.pos[0]][self.pos[1]] = 5

# function to draw a line depending on the size given as parameter, will be used in drawing the environment
def print_line(size):
    i = 0
    while i < size * 4.2:
        print("-", end='')
        i+=1
    print()

# function to draw the environment
def print_map(tab, c, m):
    system('clear')
    print("\n\t\t",end='')
    print_line(len(tab))
    i = 0

    while i < len(tab):
        print("\t\t|",end='')
        j = 0
        while j < len(tab):
            if tab[i][j] == 0:
                print("   |", end='')
            elif tab[i][j] == 1:
                print(" O |", end='')
            elif tab[i][j] == 2:
                print(" o |", end='')
            elif tab[i][j] == 3:
                print(" x |", end='')
            elif tab[i][j] == 4:
                print(" × |", end='')
            elif tab[i][j] == 5:
                print(" . |", end='')
            j+=1
        print("\n\t\t",end='')
        print_line(len(tab))
        i+=1
    
    print("\nKey: ")
    print("\t'O' = male cat, 'o' = female cat, 'x' = male mouse, '×' = female mouse, '.' = maize")
    print("\n\n")

    i = 0
    while i < len(c):
        if(c[i].isAlive):
            print("cat",i+1," TTL = ", c[i].TTL, "\t", end='')
        i+=1
    
    print("\n\n")
    i = 0
    while i < len(m):
        if(m[i].isAlive):
            print("mouse",i+1," TTL = ", m[i].TTL, "\t", end='')
        i+=1
    print("\n")
    time.sleep(0.4)


""" The main program """
grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
map_size = 10
m = []
cat = []
mais = []
pos = [0,0]

i = 0

while i < 5:
    pos[0] = random.randrange(0, map_size-1)
    pos[1] = random.randint(0, map_size-1)

    while(grid[pos[0]][pos[1]] != 0):
        pos[0] = random.randint(0, map_size-1)
        pos[1] = random.randint(0, map_size-1)   

    cat.append(Cat(random.randint(1,2),pos,grid))
    i+=1

i = 0
while i < 5:
    pos[0] = random.randint(0, map_size-1)
    pos[1] = random.randint(0, map_size-1)

    while(grid[pos[0]][pos[1]] != 0):
        pos[0] = random.randint(0, map_size-1)
        pos[1] = random.randint(0, map_size-1)   

    m.append(Mouse(random.randint(3,4),pos,grid))
    i+=1

i = 0
while i < 5:
    pos[0] = random.randint(0, map_size-1)
    pos[1] = random.randint(0, map_size-1)

    while(grid[pos[0]][pos[1]] != 0):
        pos[0] = random.randint(0, map_size-1)
        pos[1] = random.randint(0, map_size-1)   

    mais.append(Maize(pos,grid))
    i+=1

while True:
    i = 0
    while i < len(cat):
        if cat[i].isAlive:
            cat[i].move(grid)
            cat[i].eat(m)
            print_map(grid, cat, m)
            j = -1
            j = cat[i].reproduce(cat,grid)
            print_map(grid,cat,m)
            if j != -1:
                grid[cat[i].pos[0]][cat[i].pos[1]] = cat[i].gender
                grid[cat[j].pos[0]][cat[j].pos[1]] = cat[j].gender
                print_map(grid, cat, m)

        i+=1

    i = 0
    while i < len(m):
        if m[i].isAlive:
            m[i].move(grid)
            m[i].eat(mais)
            print_map(grid, cat, m)
            j = -1
            j = m[i].reproduce(m,grid)
            print_map(grid,cat,m)
            if j != -1:
                grid[m[i].pos[0]][m[i].pos[1]] = m[i].gender
                grid[m[j].pos[0]][m[j].pos[1]] = m[j].gender
                print_map(grid, cat, m)
        i+=1