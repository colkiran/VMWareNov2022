
players = {
    'sachin':[250, 345, 409, 320, 380],
    'sourav':[182, 280, 340, 375, 310],
    'sehwag':[325, 410, 458, 385, 140],
    'rahul':[225, 310, 350, 375, 290],
    'yuvraj':[156, 185, 265, 215, 195],
    'laxman':[250, 340, 198, 275, 185]
}

print(f"players :{players}")
print("-" * 40)

print(f"sachin :{players['sachin']}")
print("-" * 40)

print(f"sachin :{sum(players['sachin'])}")
print("-" * 40)

scores = {k: sum(v) for k, v in players.items()}
print(f"scores :{scores}")
print("-" * 40)

scores = {k: (lambda score: sum(score) / len(score))(v)
for k, v in players.items()}
print(scores)
print("-" * 40)

def avg_scr(score):
    return sum(score) / len(score)

scores = {k :avg_scr(v) for k, v in players.items()}
print(scores)
print("-" * 40)

vals = {(lambda par: par * 10)(k): (lambda par: par * par)(v)
for k, v  in {1:1, 2: 2, 3: 3, 4: 4, 5: 5}.items()}
print(vals)
print("-" * 40)

players = {
    'sachin':[250, 345, 409, 320, 380],
    'sourav':[182, 280, 340, 375, 310],
    'sehwag':[325, 410, 458, 385, 140],
    'rahul':[225, 310, 350, 375, 290],
    'yuvraj':[156, 185, 265, 215, 195],
    'laxman':[250, 340, 198, 275, 185]
}

scores = [score for score in players.values()]
print(scores)
print("-" * 40)
# convert it into a one dimension array and values greater than 200

scores = [scr for score in players.values() for scr in score]
print(scores)
print("-" * 40)

scores = [scr for score in players.values() for scr in score if scr >= 200]
print(scores)
print("-" * 40)

ply_scores = {name: [scr for scr in score if scr >= 200]
              for name, score in players.items()}
print(ply_scores)

