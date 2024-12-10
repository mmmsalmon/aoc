with open("input/10", "r") as f:
    lines = f.read().splitlines()

def findscore(x,y,n) -> int:
    tile, score = {}, 0
    if 0 < x-1 < len(lines[0]):
        tile['left'] = lines[y][x-1]
    if 0 < x+1 < len(lines[0]):
        tile['right'] = lines[y][x+1]
    if 0 < y-1 < len(lines):
        tile['up'] = lines[y-1][x]
    if 0 < y+1 < len(lines):
        tile['down'] = lines[y+1][x]

    tile = {k:v for k,v in tile if v == n+1}
    for k,v in tile:
        if n < 9:
            findscore(x,y,n)
        else:
            score = 1
    n += 1
    return score


res = 0
for y in lines:
    for x in y:
        if x == '0':
            res += findscore(x,y,0)

print(f'part 1: {res}')
