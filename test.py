import csv

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}
names = {}
names["kevin bacon"] = {"1"}
print(names)

with open('/Users/manuelheller/Documents/GitHub Repositories/degrees/small/people.csv') as f:

    # Create a generator object for the file: gen_file
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
        people[row["id"]] = {
            "name": row["name"],
            "birth": row["birth"],
            "movies": set()
        }
        if row["name"].lower() not in names:
            names[row["name"].lower()] = {row["id"]}
        else:
            names[row["name"].lower()].add(row["id"])

print('end of code')
print(people)
print(names)