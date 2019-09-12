
box_size = input("input maps size, for example 3,3:").split(',')
height = int(box_size[0])
width = int(box_size[1])
maps = []
for i in range(height+1):
    for j in range(width+1):
        maps.append((i,j))
print(maps)
