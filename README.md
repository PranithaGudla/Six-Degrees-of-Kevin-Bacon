<h2>Problem Definition</h2> 

<p align="justify">The game of "Six Degrees of Kevin Bacon" is essentially a graph theory issue. 
Every actor is given a vertex, and if two actors have worked together before in a 
film, an edge is put between them. Finding the shortest path between two vertices 
in graph theory thus solves the challenge of connecting a particular actor to Kevin 
Bacon in the fewest number of steps. Numerous shortest path algorithms could 
be used to solve this issue. Of all the traversal algorithms we have chosen BFS 
algorithm.</p>

<h4>Illustration of the problem statement – </h4>

![image](https://github.com/PranithaGudla/Six-Degrees-of-Kevin-Bacon/assets/172133526/dc533a9d-8131-4c76-9a14-48475ee77215)

<p align = "justify">For instance, let the above figure be a graph connecting 4 actors A, B, C, and D. 
Let A be the source and D be the destination. Then, the shortest path between 
actor A and Actor D is AB – BC – CD. According to the concept of degrees of 
separation, the degree of Actor D corresponding to Actor A and vice versa is 3. 

From the above illustration, 
Degree of an actor = Number of Vertices – 1  
              Or 
= Number of Edges in between 

However, Degree = Number of Edges can only be considered if the graph involved 
is Singly Connected Graph. 

Only in the case of Singly Connected Graph, Number of Edges = Number of 
Vertices – 1. 

Thus, Degree = Number of Vertices – 1 is a mathematically unambiguous way to 
find the degree of an actor. 

Based on our Problem Statement, we have made a system model using Data Flow 
Diagram. It is as follows –</p>

![image](https://github.com/PranithaGudla/Six-Degrees-of-Kevin-Bacon/assets/172133526/2f869394-fd88-4482-9d9a-3fcd5fd19ae5)

<p align = "justify">Few assumptions we have made before proceeding to the solution were as follows – </p>

<p align="justify">➢ Since we are trying to make an application that would work on systems 
used daily (lower configuration systems), we have reduced the size of the 
dataset by cleansing the data almost 10x times than the original IMDB 
Dataset. Due to this there might be cases – </p>

<p align="justify">• Person Not Found: Since the dataset has only a part of the original 
dataset values, there is a chance that an actor/actress is not present 
in the dataset. </p>

<p align="justify">• Not Connected: Since the dataset is cleansed, there is a chance that 
the source and destination are not connected due to the absence of 
data that can connect them. </p>

<p align="justify">➢ We assumed that there would be no use of using the source and target 
terminology since swapping the source and target names would not have 
any impact on the degree value. Thus, we prompt the user to enter the 
name for both inputs instead of prompting source and target.</p>

<h2>Solution</h2>

<p align="justify">→ Firstly, we have chosen the following simulation settings –  </p>

    IDE – Visual Studio Code 

    Programming Language – Python 

    Dataset Resource – IMDB 

    Dataset File Format – csv

<p align="justify">→ Then, we moved on to the algorithm part. Initially we have looked for better data structure than a graph. However, though there are other 
data structures using which current problem can be solved it turned out 
that graph is the best possible data structure for this problem. </p>

<p align="justify">→ Later, we started working on deciding upon an algorithm. We found 
Dijkstra’s algorithm and BFS are competitive enough. But Dijkstra’s 
algorithm would require weighted graph with only positive weights. Thus, BFS seemed efficient.</p> 

<p align="justify">→ Since all the required concepts for moving ahead into implementation are finalised, we started off from datasets. We downloaded datasets 
from IMBD. They were too large and were in a bizarre file format. We 
converted them into a feasible dataset of format .csv.  </p>

<p align="justify">→ Then we started actual implementation part. We initiated dictionaries into which the dataset values will be loaded. </p>

<p align="justify">→ We have taken three datasets –   </p>

    Actorpeople – Consists of the data regarding actors and actresses 
  
    Movielist – Consists of the data regarding movies 
  
    Peoplestars – Used to relate actors and movies. 

<p align="justify">→ Then the names of the source and target will be prompted. Once the 
input is given it would be verified over the datasets. If the actor is not 
found in the dataset or if there is a typo in the input it would return 
person not found. If there are multiple records with the same actor’s 
name then the user would be prompted to enter the id number of the 
actor. </p>

<p align="justify">→ After the source and target names are locked, BFS algorithm would run over all the neighbours of the source. The BFS algorithm would stop 
upon reaching the target node. It would return the path to the target. </p>

<p align="justify">→ The path would be returned to the main method excluding the target 
node name. </p>

<p align="justify">→ The length of the path after excluding the target is the degree of the actor corresponding to the other target. </p>

<p align="justify">This is how we have made a step-by-step implementation guide to our 
problem.</p>

<h4>Formal Time Complexity Analysis – 
Practical Illustration -</h4>


