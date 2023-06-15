# Problem 1: Traversing the Maze to reach the final location 

The problem skeleton provided already does a great job in traversing the maze and only fails because there is no tracking/marking for visited places.

To figure the above out I spent around 4 hours. Mainly because all the logic seemed fine. 

After figuring that out I started by mutating the map itself by replacing the '.' with 'V' and added a checking condition for 'V' and the default code converged with dist = solution distance - 1 which I figured was due to not adding the last moves distance and rectified that.

Now I have a working map solver but the main challenge was to print the path. I initially made the function to translate the move int 'UDRL' by calculating the difference of the current row and col with prev row and col. But realized that it was printing the stray nodes too.

For this I tried modifying the path solver to not take the stray nodes into account however, I couldn't get it to work. After going through various sources for BFS and DFS the other most common way used to denote the travel pathway was to use "Backtracking". 

Further, since I wasn't using either DFS or BFS (although the code generally follows BFS behavior by default) I tried using Backtracking for which I used a dictionary to store the current location tuple as the key to store the next move location as it value so the key-value pair will store all the moves performed but by printing in reverse using while loop by referencing key-value pair in the reverse order I was able to get the path traversal string. 

Since this is in the reverse order I reversed the 'UDRL' order by interchanging the labels and then performing the search which is how I have submitted the code with

# Problem 2: arranging given number of agent(P) on the provided maps

Immediately as soon as I started looking at the code I know I needed another function to check if the move is valid hence the IsValid function. Went through a lot of different iterations for checking the diagonal and currently I do have the confidence that at least the IsValid function is correctly implemented

I'm using a modified successors function called successor (not a great name I know) that only returns the tuple of locations plausible for the map in the solve function.
This is where all my efforts start. in the solve function, I wanted to implement it in such a way that I mark the invalid locations invalid and valid places valid after placing an agent and then push it into fringe for revaluation and re-calculation of the new state matrix and so on.

But since we are already in a function and a while loop, I'm not able to figure out how to redo such a calculation (Brute forcing instead of DFS BFS). 
I spent all the time till now but was unable to get the prog to work beyond a certain limit as the search is not resetting. 

