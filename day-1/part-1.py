import fileinput

left = list()
right = list()

# Using fileinput.input() method
for line in fileinput.input(files =('input.txt')):
    list = line.split()
    left.append(int(list[0]))
    right.append(int(list[1]))

left.sort()
right.sort()

total_diff = 0

for i in range(len(left)):
    diff = abs(left[i] - right[i])
    total_diff += diff

print(total_diff)