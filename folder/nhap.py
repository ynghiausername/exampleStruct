lst_pair = [['p', 'q'], ['p', 'r'], ['p', 's'], ['p', 't'], ['p', 'u'], ['q', 'r'], ['q', 's'], ['q', 't'], ['q', 'u'], ['r', 's'], ['r', 't'], ['r', 'u'], ['s', 't'], ['s', 'u'], ['t', 'u']]
#res = 0: win, 1: lose, 2: draw
#win: 3 points, draw: 1 point, lose: 0 point
#check(matches history): check if the matches history follow these conditions: p has 13 points, q has 7 points, r has 9 points, t has 1 point, u has 6 points
#check(matches history): return True if all the team have below point of the condition, otherwise return False
def check(matches_history):
    dct = {
    'p' : 0,
    'q' : 0,
    'r' : 0,
    's' : 0,
    't' : 0,
    'u' : 0
    }    
    #dct2: number of win, draw, lose of each team
    dct2 = {
        'p': [0, 0, 0],
        'q': [0, 0, 0],
        'r': [0, 0, 0],
        's': [0, 0, 0],
        't': [0, 0, 0],
        'u': [0, 0, 0]
    }
    draw_count = 0
    for i in range(len(matches_history)):
        if matches_history[i] == '0':
            dct[lst_pair[i][0]] += 3
            dct2[lst_pair[i][0]][0] += 1
            dct2[lst_pair[i][1]][2] += 1
        elif matches_history[i] == '1':
            dct[lst_pair[i][0]] += 1
            dct[lst_pair[i][1]] += 1
            dct2[lst_pair[i][0]][1] += 1
            dct2[lst_pair[i][1]][1] += 1
            draw_count += 1
        else:
            dct[lst_pair[i][1]] += 3
            dct2[lst_pair[i][1]][0] += 1
            dct2[lst_pair[i][0]][2] += 1
    if dct['p'] == 13 and dct['q'] == 7 and dct['r'] == 9 and dct['t'] == 1 and dct['u'] == 6 and len(matches_history) == 15:
        # print(matches_history)
        print(dct)
        print(draw_count)
        for(key, value) in dct2.items():
            print(key, value)
    if dct['p'] > 13 or dct['q'] > 7 or dct['r'] > 9 or dct['t'] > 1 or dct['u'] > 6:
        return False
    return True
    
def dequy(depth, matches_history):
    if depth == 14:
        check(matches_history)
        return
    if(not check(matches_history)):
        return
    dequy(depth + 1, matches_history + '0')
    dequy(depth + 1, matches_history + '1')
    dequy(depth + 1, matches_history + '2')

dequy(0, "0")
dequy(0, "1")
dequy(0, "2")