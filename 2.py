f = open('2.txt', 'r').readlines()

p1 = [0, 'B X', 'C Y', 'A Z', 'A X', 'B Y', 'C Z', 'C X', 'A Y', 'B Z']
p2 = [0, 'B X', 'C X', 'A X', 'A Y', 'B Y', 'C Y', 'C Z', 'A Z', 'B Z']

for line in f:
    p1[0] += p1.index(line.strip());

print(p1[0])

for line in f:
    p2[0] += p2.index(line.strip())

print(p2[0])
