import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# peoplenames dictionary would Map peoplenames to a set of corresponding person_ids
peoplenames = {}

# People dictionary would map person_ids to a dictionary of: name, birth, assign_movie_values (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
assign_movie_values = {}




def load_dataset(directory):
    """
    Load data from CSV files into memory.

    """
    # Load people
    with open(f"{directory}/actorpeople.csv", encoding="utf-8") as file_data:
        reader = csv.DictReader(file_data)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "assign_movie_values": set() #set() function creates a set object. The items in a set list are unordered, so it will appear in random order. 
            }#Below loading the content onto the people dictionary for the processing. 
            if row["name"].lower() not in peoplenames:
                peoplenames[row["name"].lower()] = {row["id"]}
            else:
                peoplenames[row["name"].lower()].add(row["id"])

    # Load assign_movie_values dictionary with movie values from the csv file
    with open(f"{directory}/movieslist.csv", encoding="utf-8") as file_data:
        reader = csv.DictReader(file_data)
        for row in reader:
            assign_movie_values[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars data set into the stars set
    with open(f"{directory}/peoplestars.csv", encoding="utf-8") as file_data:
        reader = csv.DictReader(file_data)
        for row in reader:
            try:
                people[row["person_id"]]["assign_movie_values"].add(row["movie_id"])
                assign_movie_values[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
 
    if len(sys.argv) > 2:
        sys.exit("Usage: python calculate-shortpath-kb.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "D:\Documents\ML Projects\Pranitha-ML\large\large"
    # Load data from files into memory
    print("Loading data...")
    load_dataset(directory)
    print("Data loaded.")
    #reading user input for running the BFS algorithm to find out the path
    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_possible_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.") # printing the degrees of seperation based on the availability of the actors relation to the path
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = assign_movie_values[path[i + 1][0]]["title"] #calculating and assigning the movies that the actors have worked on 
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_possible_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # TODO - BFS
    explored = set([])
    frontier = [source]
    parents = {}
    while len(frontier) > 0:
        person = frontier.pop(0)
        if person == target: #come out of loop if this is the target
            break
        explored.add(person)
        for (m, p) in neighbors_for_person(person):
            if not p in frontier and not p in explored: 
                frontier.append(p) #add if he is not explored yet but is a neighbor
                parents[p] = (m, person) #as p is neighbor of person as they both star in same movie m
    if not target in parents:
        return None
    path = []
    person = target #now mostly this last person is our target
    while person != source: #to make sure its not the source
        m, p = parents[person]
        path.append((m, person))
        person = p
    path = path[::-1]
    return path


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(peoplenames.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["assign_movie_values"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in assign_movie_values[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
