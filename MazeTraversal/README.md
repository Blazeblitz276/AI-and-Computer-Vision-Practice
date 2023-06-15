# Problem 1: Traversing the Maze to reach the final location

The problem skeleton provided already does a great job in traversing the maze and only fails because there is no tracking/marking for visited places.

To figure the above out I spent around 4 hours. Mainly because all the logic seemed fine. 

After figuring that out I started by mutating the map itself by replacing the '.' to 'V' and added checking condition for 'V' and the default code converged with dist = solution distance - 1 which i figured was due to not adding the last moves distance and rectified that.

Now i have a working map solver but the main challenge was to print the path. I initially made the function to translate the move int 'UDRL' by calculating the difference of current row and col with prev row and col. But realised that it was printing the stray nodes too.

For her on i tried modifying the path solver to not take the stray nodes into account however i couldn't get it to work. After going through various sources for BFS and DFS the other most common way used to denote the travel pathway was to use "Backtracking". 

Further more since i wasn't really using either DFS or BFS (althought the code generally follows BFS behavour by default) i tried using Backtracking for which i used a dictionary to store the current location tuple as the key to store the next move location as it value so the key value pair will store all the moves performed but by printing in reverse using while loop by refrenceing key value pair in the reverse order i was able to get the path traversal string. 

Since this is in the reverse order i reversed the 'UDRL' order by interchanging the labels and then performing the search which is how i have submitted the code with

# Problem 2: arranging given number of agent(P) on the provided maps

Let me begin by saying what a complete rollercoaster of emotions I had to go through for this code. I am still not done but im close to giving up.
I understand the problem, i get the theory that goes behind solving it and also the approach i want to go for BUT i couldn't code it.

Immediately as soon as i started looking at the code i know i need another fucntion to check if the move is valid hence the IsValid function. Went through al lot of different iterations for checking the diagonal and currently i do have the confidence that atleast the IsValid function is correctly implemented

Im using a modified successors function called successor (not a great name i know) that only return the tuple of locations plausible for the map in the solve function.
This is where all my efforts start. in the solve function i wanted to implement in such a way the i mark the invalid locations invalid and valid places valid after placing a agent and then pushing it into fringe for revaluation and re calculation of the new state matrix and so on.

But since we are already in a function and in a while loop im not able to figure out how to redo such a calculation (Brute forcing instead of DFS BFS). 
I spent all the time till not but unable to get the prog to work beyond a certain limit as the search is not resetting. 

I discussed with TAs etc but due to the nature of my code I'm unable to get the desired results. it does work and doesnt go into infinite loop but it shows false for agents.

