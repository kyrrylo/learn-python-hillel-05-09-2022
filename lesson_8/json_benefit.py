import json

with open('new_file', 'w') as fp:
    fp.write(str([5, 6, 7, 8]))

with open('new_file', 'r') as fp:
    x = fp.read()
    print(type(x), x)

x = json.load(open('new_file', 'r'))
print(type(x), x)
x.append(9)
print(x)