
#todo: how to handle multiple conditions + conditions from different streams
#todo: improve algorithm
def identifyFilterContainment(containment):
    query_one = containment[0].split(' ')
    query_two = containment[1].split(' ')

    op1 = query_one[1]
    op2 = query_two[1]

    a = query_one[2]
    b = query_two[2]

    if op1 == '==':
        if op2 == '==' and int(b) == int(a):
            return [0,1]
        elif (op2 == '<'and int(b) > int(a)) or (op2 == '<='and int(b) >= int(a)) or (op2 == '>'and int(b) < int(a)) or (op2 == '>='and int(b) <= int(a)) or (op2 == '!='and int(b) != int(a)):
            return [1,0]
    elif op1 == '>=':
        if op2 == '>':
            if int(b) < (int(a) - 1):
                return [1,0]
            else:
                return [0,1]
        elif op2 == '>=':
            if int(b) < int(a):
                return [1,0]
            else:
                return [0,1]
        elif op2 == '==':
            if int(b) >= int(a):
                return [0,1]
        elif op2 == '!=':
            if int(b) < int(a):
                return [1,0]
    elif op1 == '>':
        if op2 == '>':
            if int(b) < int(a):
                return [1,0]
            else:
                return [0,1]
        elif op2 == '>=':
            if int(b) >= int(a):
                return [1,0]
            else:
                return [0,1]
        elif op2 == '==':
            if int(b) > int(a):
                return [0,1]
        elif op2 == '!=':
            if int(b) <= int(a):
                return [1,0]
    elif op1 == '<=':
        if op2 == '<':
            if int(b) > (int(a) + 1):
                return [1,0]
            else:
                return [0,1]
        elif op2 == '<=':
            if int(b) > int(a):
                return [1,0]
            else:
                return [0,1]
        elif op2 == '==':
            if int(b) <= int(a):
                return [0,1]
        elif op2 == '!=':
            if int(b) > int(a):
                return [1,0]
    elif op1 == '<':
        if op2 == '<':
            if int(b) > int(a):
                return [1,0]
            else:
                return [0,1]
        elif op2 == '<=':
            if int(b) >= int(a):
                return [1,0]
            else:
                return [0,1]
        elif op2 == '==':
            if int(b) < int(a):
                return [0,1]
        elif op2 == '!=':
            if int(b) >= int(a):
                return [1,0]
    elif op1 == '!=':
        if op2 == '<' and int(a) >= int(b):
            return [0, 1]
        elif op2 == '<=' and int(a) > int(b):
            return [0, 1]
        elif op2 == '>' and int(a) <= int(b):
            return [0, 1]
        elif op2 == '>=' and int(a) < int(b):
            return [0, 1]
        elif op2 == '==' and int(b) != int(a):
            return [0, 1]
        elif op2 == '!=' and int(b) == int(a):
            return [0, 1]
    return [0,0]
