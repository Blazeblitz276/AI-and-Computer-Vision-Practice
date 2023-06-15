import sys

def movestr(CurRow,CurCol,NexRow,NexCol):
    #Labels are reversed since we will be backtracking
    if (CurRow - NexRow == 1) and (CurCol - NexCol == 0): 
        return "D"
    elif(CurRow - NexRow == -1) and (CurCol - NexCol == 0):
        return "U"
    elif (CurRow - NexRow == 0) and (CurCol - NexCol == 1): 
        return "R"
    elif(CurRow - NexRow == 0) and (CurCol - NexCol == -1):
        return "L"
    else:
        "nothing"


# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(map,pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m and (map[pos[0]][pos[1]] in ".@" )
    
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))
        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(map, move, len(map), len(map[0]))]


def search(house_map):
        # Find agent start position
        
        agent_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        end_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="@"][0]
        fringe=[(agent_loc,0)]
        TravelMap = dict()
        res = ""
        while fringe:
            (curr_move, curr_dist)=fringe.pop()
            #traversing through all moves
            for move in moves(house_map, *curr_move):
                    if house_map[move[0]][move[1]]=="@":
                        curr_dist += 1
                        TravelMap[(move)] = curr_move
                        while True:
                            InterMov = TravelMap[end_loc]
                            if InterMov == agent_loc:
                                #Using the 
                                house_map[InterMov[0]][InterMov[1]] = movestr(end_loc[0],end_loc[1],InterMov[0],InterMov[1])
                                res = movestr(end_loc[0],end_loc[1],InterMov[0],InterMov[1]) + res
                                break
                            house_map[InterMov[0]][InterMov[1]] = movestr(end_loc[0],end_loc[1],InterMov[0],InterMov[1])
                            res = movestr(end_loc[0],end_loc[1],InterMov[0],InterMov[1]) + res
                            end_loc = InterMov
                        return (curr_dist, res)
                    elif move in TravelMap:
                        continue
                    else:
                        fringe.append((move, curr_dist + 1))
                        TravelMap[(move)] = curr_move


        return (-1,"No solution possible")
    
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])