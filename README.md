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

![image](https://github.com/PranithaGudla/Six-Degrees-of-Kevin-Bacon/assets/172133526/1d687d97-5f91-4015-99a6-e6105a31d02b)

Basic Operation : Traversing the graph using BFS 

The time complexity of BFS algorithm on the above graph is the number of 

Steps taken to traverse through all the nodes of the graph – 

Part – 01: Creating Adjacency List 

A – {B,E} 

B – {C} 

C – {D,F} 

D – {} 

E – {C} 

F – {} 

Part – 02: 

Step – 01: Traversing through the graph using BFS 

Enqueue – A 

Step – 02: 

Enqueue – B 

Step – 03: 

Enqueue – C 

Step – 04: 

Dequeue – A 

Step – 05: 

Enqueue – D 

Step – 06: 

Dequeue – B 

Step – 07: 

Dequeue – C 

Step – 08: 

Enqueue – E 

Step – 9: 

Enqueue – F 

Step – 10: 

Dequeue – D 

Step – 11: 

Dequeue – E 

Step – 12: 

Dequeue - F 

Basic Operation Count = Total Number of Steps = 12 

= Number of Vertices + Number of Edges = 6 + 6 = O(V+E) 

<h4>Mathematical Analysis – </h4>

Let N represent the typical quantity of edges that occur at each node (N = E / V). 

As a result, queue operations take O(N) time on each node. 

The entire runtime is O(V) O(N) = O(V) O (E / V) = O because there are V nodes 
(E). 

The problem is that, strangely enough, we can't state that O(V) O(E / V) = O in 
this case (E).  O (E / V) represents the average effort per node. As a result, the 
amount of work completed asymptotically is constrained from above by a certain 
multiple of E / V. 

<p align = "justify">When we consider what BFS does, the work done per node probably looks more like c1 + c2E / V because there is some baseline work done per node (establishing loops, checking fundamental conditions, etc.), which is what is accounted for by the c1 term, as well as some amount of work proportional to the number of edges 
visited (E / V, times the work done per edge). This is equal to that if we multiply 
it by V. </p>

V · (c1 + c2E / V) 

= c1V + c2E 

= Θ(V + E) 

These lower-order concepts that big-O so neatly allows us to ignore are significant 
in our situation, so we cannot just easily dismiss them. So, at least 
mathematically, that is what is happening. 

Regardless of how many edges are present in the graph, each node still requires 
a certain amount of work that is independent of the edges. This is the setup 
needed to execute the main if statements and create local variables, among other 
things.
