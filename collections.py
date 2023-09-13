print("Collections")
print("Tuples, Lists, Dictionaries")

full_name = ("Dileep", "Ealapolu")
print(type(full_name))
scores = [10, 15, 16, 32]
print(type(scores))
score1 = scores[0]
score_last = scores[-1]
subset_scores = scores[1:3]
subset_scores_step = scores[0::2]
scores[1] = scores[1] + 1
scores[1:2] = []
scores.append(64)
scores.insert(0, 2)
print(scores)
scores.pop(1)
del scores[1]
print(scores)
scores.clear()

member_score = {"Dileep": 10, "Shashi": 16}
print(type(member_score))

len(full_name)
max(full_name)
min(full_name)
del full_name
member_score['harsh'] = 32

print([i for i in range(1, 20)])
print([i*j for i in range(1, 3) for j in range(1, 3)])

print({i : i for i in range(1, 10)})