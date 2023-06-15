import sys

def AxisBefChk(house_map, row,col):
    colstr =""     
    for rowin in range(row-1,-1,-1):
        colstr += house_map[rowin][col]   
    RowBef,ColBef = "".join(house_map[row][:col]),colstr

    for point in reversed(RowBef):
        if point == "X":
            break
        if point == "p":
            return False
    for point in (ColBef):
        if point == "X":
            break
        if point == "p":
            return False
    return True

def AxisAftChk(house_map, row,col):
    colstr =""     
    for rowin in range(row+1,len(house_map)):
        colstr += house_map[rowin][col]   
    RowAft,ColAft = "".join(house_map[row][col+1:]),colstr

    for point in RowAft:
        if point == "X":
            break
        if point == "p":
            return False
    for point in ColAft:
        if point == "X":
            break
        if point == "p":
            return False
    return True

def NegDiagBefChk(house_map,row,col):
    i = row - 1
    j = col - 1
    while i >= 0 and j >=0:
        if house_map[i][j] == 'X':
            return True
        elif house_map[i][j] == 'p':
            return False
        else:
            i = i-1
            j = j-1
            continue
    return True
def NegDiagAftChk(house_map,row,col):
    i = row + 1
    j = col + 1
    while i < len(house_map) and j < len(house_map[0]):
        if house_map[i][j] == 'X':
            return True
        elif house_map[i][j] == 'p':
            return False
        else:
            i = i+1
            j = j+1
            continue
    return True

def PosDiagBefChk(house_map, row,col):
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(house_map[0]):
        if house_map[i][j] == 'X':
            return True
        elif house_map[i][j] == 'p':
            return False
        else:
            i = i-1
            j = j+1
            continue
    return True
def PosDiagAftChk(house_map, row,col):
    i = row + 1
    j = col - 1
    while i < len(house_map) and j >= 0:
        if house_map[i][j] == 'X':
            return True
        elif house_map[i][j] == 'p':
            return False
        else:
            i = i+1
            j = j-1
            continue
    return True

def IsValid(house_map, row,col):
    Rcnt = len(house_map)
    Ccnt = len(house_map[0])
    flag = True
    if row>=Rcnt or row<0 or col>=Ccnt or col<0: flag = False
    
    if house_map[row][col] in "pX": flag = False
    
    if not AxisBefChk(house_map, row,col): flag = False
    
    if not AxisAftChk(house_map, row,col): flag = False
    
    if not NegDiagBefChk(house_map, row,col): flag = False
    
    if not NegDiagAftChk(house_map, row,col): flag = False
    
    if not PosDiagBefChk(house_map, row,col): flag = False
    
    if not PosDiagAftChk(house_map, row,col): flag = False
    
    
    if flag: 
        return True
    else:
        return False
        
    
# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of agents on house_map
def count_agents(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-agently format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a agent to the house_map at the given position, and return a new house_map (doesn't change original)
def add_agent(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [ (add_agent(house_map, r, c)) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if (house_map[r][c] == '.' or house_map[r][c] == '@')]

def successor(house_map):
    return [ (r,c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if (house_map[r][c] == '.' or house_map[r][c] == '@')]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_agents(house_map) == k 

def solve(initial_house_map,k):
    global fringe
    fringe = [initial_house_map]
    ValidMarked =[]
    global new_house_map
    new_house_map = initial_house_map.copy()
    while len(fringe) > 0:
        for new_queen_loc in successor( fringe.pop() ):
        
            # if new_queen_loc in ValidMarked:
            #      continue
            if IsValid(new_house_map, new_queen_loc[0], new_queen_loc[1]):
                new_house_map = add_agent(new_house_map, new_queen_loc[0], new_queen_loc[1])
                print(printable_house_map(new_house_map),"\n")
                
                if is_goal(new_house_map,k):
                    return(new_house_map,True)
                
                #ValidMarked.append(new_queen_loc)
                fringe.append(new_house_map)
                print(fringe)
        
    return "",False
                
# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


