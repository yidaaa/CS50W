people = [
    {"name": "naruto", "team": "7"},
    {"name": "saskue", "team": "7"},
    {"name": "sakura", "team": "7"},
    {"name": "hinata", "team": "10"},
    {"name": "itachi", "team": "akastuki"},
]

people.sort(key=lambda person:person["name"])
print(people)

people.sort(key=lambda person:person["team"])
print(people)
