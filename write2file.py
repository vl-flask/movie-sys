# Just open file and write to it

with open('mydump.txt', 'r') as f:
    print(f.readline())
# with open('mydump.txt', 'w') as f:
#     f.write("Hello world")
