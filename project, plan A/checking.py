def inner_checker (t) :
    # ['abcd','abcd','abcd','abcd']
    if t[0][0] == t[1][0] == t[2][0] == t[3][0] != 'e':
        return True
    elif t[0][1] == t[1][1] == t[2][1] == t[3][1] != 'm':
        return True
    elif t[0][2] == t[1][2] == t[2][2] == t[3][2] != 'p':
        return True
    elif t[0][3] == t[1][3] == t[2][3] == t[3][3] != 't':
        return True
    return False

def check(t) :
    checker = []
    for i in range (4) :
        checker = []
        for j in range (4) :
            checker.append(t[j][i])
        if inner_checker(checker) :
            return True
        
    for i in range (4) :
        checker = []
        for j in range (4) :
            checker.append(t[i][j])
        if inner_checker(checker) :
            return True
    checker = []
    for i in range (4) :
        checker.append(t[i][i])
    if inner_checker(checker) :
        return True
    checker = []
    for i in range(4) :
        checker.append(t[i][3-i])
    if inner_checker(checker) :
        return True
    return False
