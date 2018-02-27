from prettytable import PrettyTable
def find(a,b):
    table = [
        [1 ,-1, -1, -1, -1, 1, 1],
        [1 , 1, -1, -1, -1, 1, 1],
        [1 , 1, -1, -1, -1, 1, 1],
        [1 , 1,  1,  2,  2, 1, 1],
        [-1,-1, -1, -1, -1, 0, 2],
        [1 , 1,  1,  2,  2, 1, 1],
        [-1,-1, -1, -1, -1, 2, 0]
    ]
    return table[a-1][b-1]

def in_vt(n):
    return {
    '+': 1,
    '*': 2,
    '^': 3 ,
    'i': 4 ,
    '(': 5 ,
    ')': 6 ,
    '#': 7 ,
    }.get(n,'0')#'0'为默认值

def tem(p):
    tem = -1
    while int(int(in_vt(p[tem - 1])) + int(in_vt(p[tem]))) == 0:
        tem = tem - 1
    tem = len(p) + tem + 1
    return tem
#p为分析栈列表，psc为输入栈列表,k为栈顶指针

def judge(p,k,psc):
    if psc[-1] != '#':
        print("\nChracters must be end of \" # \" \n")
    if k == 0 and p[k] == '#' and (psc[0] == '+' or psc[0] == '*' or psc[0] == '^' ):
        print("\nThere is no operand in front of the operator\n")
        return 0
    if (psc[0] == '+' or psc[0] == '*' or psc[0] == '^' ) and  (psc[1] == '+' or psc[1] == '*' or psc[1] == '^' ):
        print("\nContiguous operation symbols\n")
        return 0
    if len(psc)!=1:
        if psc[-1] == '#' and(psc[-2] == '+' or psc[-2] == '*' or psc[-2] == '^' ):
            print("\nThere is no operand behind the operator\n")
            return 0
    return 1

while True:
    print("\n************************************\n")
    psc = list((input("Input characters to be reduced(With the end of '#' ):")))# 输入栈
    table = PrettyTable(["Step", "Stack Characters", "Priority Relationship", "Current Character", "Remainder Characters", "Move Or Reduction"])
    p = ['#']  # 分析栈
    j = 1
    q = ""
    flag = 0
    n = 1
    k = 0

    while True:
        if judge(p,k,psc) == 0:
            print("\nError!\n")
            break
        j = k
        while int(in_vt(p[j])) == 0:
            j = j - 1
        flag = find(in_vt(p[j]),in_vt(psc[0]))
        if flag == 1 : #如果p[j] > 当前输入字符
            while True:
                q = p[j]
                j = j-1
                while int(in_vt(p[j])) == 0:
                    j = j - 1
                if find(int(in_vt(p[j])),int(in_vt(q))) == -1:
                    break
            k = j + 1
            while int(in_vt(p[k])) == 0:
                k = k + 1
            table.add_row([n,"".join(p[0:tem(p)]),">",psc[0],"".join(psc[1:]),"Reduction"])
            n = n + 1
            p[k] = "S"
            #若最后一个符号为终结符，则意味着此终结符之前有与它为 "=" 关系的字符 , 这些相等字符是在p[k：]的范围，因此要全部归约为"S"
            if p[-1] != "S":
                count = -1
                for x in p:
                    count = count + 1
                    if count > k:
                        p[count] = "S"
                    else:
                        continue
            p = p[0:tem(p)]
            k = len(p) - 1
            continue
        elif flag == -1:
            k = k + 1
            table.add_row([n, "".join(p), "<", psc[0], "".join(psc[1:]), "Move"])
            n = n + 1
            p.append(psc[0])
            del psc[0]
            continue
        elif flag == 0:
            if p[j] == '#':
                table.add_row([n, "".join(p[0:2]), "=", psc[0], "".join(psc[1:]), "Reduction"])
                n = n + 1
                table.add_row([n,"S","","","","Receive"])
                table.align["Stack Characters"]="l"
                table.align["Remainder Characters"]="l"
                print(table)
                print("Success Of Reduction！ ")
                table.clear_rows()
                break
            else:

                table.add_row([n, "".join(p), "=", psc[0], "".join(psc[1:]), "Move"])
                n = n + 1
                p.append(psc[0])
                k = len(p) - 1
                del psc[0]
                continue
        else:
            table.add_row([n, "".join(p), "None", psc[0], "".join(psc[1:]), "Error!"])
            n = n + 1
            print("\nError! Please input characters again.\n")
            break