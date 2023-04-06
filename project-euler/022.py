
import data022

sort_allpeople = sorted(data022.allPeople)


def nameScore(name):
    score = 0
    for i in name:
        score += ord(i)-ord("A") +1
    return score

total = 0
count = 1

for name in sort_allpeople:
    total += nameScore(name) * count
    count+=1
print(total)


