from random import choice

def game_size():
    gs = int(input('what size u wanna play 3x3, 4x4,.... etc. Enter 3, 4,........: '))
    v1 = list(range(1,gs**2))
    v1.append([])
    return v1

def print_board():
    for i in range(len(b)):
        if i > 9 : print(b[i], end = '   ')
        else: print(' ',b[i], end = '   ')
        if (i+1) % (len(b))**0.5 == 0:
            print()
        
def move():
    while True:
        c = int(input('enter a number to move it: '))
        if c > 0 and c < (len(b)):
            a = b.index([])
            d = b.index(c)
            if (d == a-1  and a%(len(b))**0.5 != 0) or (d == a+1 and (a+1)%(len(b))**0.5 != 0) or d == a+(len(b)**0.5) or d == a-(len(b)**0.5):
                b[a] = c
                b[d] = []
                break
            else: print('invalid entry, try again!')
        else:
            print('invalid entry, try again!')
            continue

def correct():
    n2 = list(range(1,len(b)))
    n2.append([])
    if b == n2:
        return True

def randomize():
    for i in range(12):
        r, l, t, bo, a = b.index([])+1, b.index([])-1, b.index([])-(len(b))**0.5, b.index([])+(len(b))**0.5, b.index([])
        options = [r,l,t,bo]
        if a% (len(b)**0.5) == 0: del options[1]
        if a+1% (len(b)**0.5) == 0: del options[0]
        valid_options = []
        for k in options:
            if k > -1 and k <= (len(b)-1):
                valid_options.append(int(k))
        c = choice(valid_options)
        v_o_nums = [x+1 for x in valid_options]
        m = b[c]
        b[c] = []
        b[a] = m

b = game_size()
randomize()
print_board()

while True:
    move()
    print_board()
    if correct() == True:
        print('u win!!')
        break
