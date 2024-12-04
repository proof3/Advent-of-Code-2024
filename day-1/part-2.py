import fileinput

left = list()
right = dict()

# Using fileinput.input() method
for line in fileinput.input(files =('input.txt')):
    list = line.split()
    left.append(int(list[0]))
    right[int(list[1])] = right.get(int(list[1]), 0) + 1

total_simmilarity = 0
for i in range(len(left)):
    simmilarity = left[i] * right.get(left[i], 0)
    print(left[i], right.get(left[i], 0), simmilarity)
    total_simmilarity += simmilarity

print(total_simmilarity)
