#loops
school = ["Hope", "Valley", "Brooke", "Copper"]
pupil = ["Klaus", "Kobe", "Shaq", "Bron"]

#hard way
print(f"{pupil[0]} goes to {school[0]} school")
print(f"{pupil[1]} goes to {school[1]} school")
print(f"{pupil[2]} goes to {school[2]} school")
print(f"{pupil[3]} goes to {school[3]} school")

#simpler ways-using loops
for pupil in pupil:
    print(f"Hello I am pupil {pupil}")
for school in school:
    print(f"I go to school {school}")
       



