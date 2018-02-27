from prettytable import PrettyTable
import global_list
import copy
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

def g_clear():
    global_list.g_string = []
    global_list.g_count = 0
    global_list.g_chr = 65
    global_list.g_m = 0

def simp(x,qe):
    qe.add_row(["<" + global_list.g_string[x] + "," + global_list.g_string[x - 1] + "," +
                global_list.g_string[x + 1] + "," + chr(global_list.g_chr) + ">"])
    global_list.g_string[x - 1] = global_list.g_string[x] = global_list.g_string[x + 1] = chr(global_list.g_chr)
    global_list.g_chr = global_list.g_chr + 1
    global_list.g_count = global_list.g_count - 1

def set_up(bg,ed,qe):
    for x in range(bg,ed+1):
        if global_list.g_string[x] == '^':
           simp(x,qe)

def set_mul(bg,ed,qe):
    for x in range(bg,ed+1):
        if global_list.g_string[x] == '*':
            simp(x, qe)

def set_add(bg,ed,qe):
    for x in range(bg,ed+1):
        if global_list.g_string[x] == '+':
            simp(x, qe)

def cul(ed,qe):
    for x in range(0,ed-1):
        if global_list.g_string[x] == '^':
            simp(x, qe)
    for x in range(0, ed - 1):
        if global_list.g_string[x] == '*':
            simp(x, qe)
    for x in range(0, ed - 1):
        if global_list.g_string[x] == '+':
            sig = 0
            for xx in range(0, x):
                if global_list.g_string[xx] == '+' or global_list.g_string[xx]  == '^' or global_list.g_string[xx]  == '*' or global_list.g_string[xx] == 'i':
                    sig = 1
                    break
                else:
                    continue
            if sig == 0:
                for xx in range(0, x):
                    global_list.g_string[xx] = chr(global_list.g_chr-1)
            simp(x, qe)


while True:
    print("\n************************************\n")
    psc = list((input("Input characters to be reduced(With the end of '#' ):")))# 输入栈
    table = PrettyTable(["Step", "Stack Characters", "Priority Relationship", "Current Character", "Remainder Characters", "Move Or Reduction"])
    qe = PrettyTable(["Quaternary Expressions"])
    p = ['#']  # 分析栈
    j = 1
    q = ""
    flag = 0
    n = 1
    k = 0
    x = 0
    c = -1
    index = []
    m = -1
    global_list.g_string = copy.deepcopy(psc)
    for var in global_list.g_string:
        m = m + 1
        if var == '*' or var == '+' or var == '^':
            global_list.g_count = global_list.g_count + 1
        if var == '(':
            c = c + 1
            index.append(m)
        if var == ')':
            ed = m
            set_up(index[c],ed,qe)
            set_mul(index[c],ed,qe)
            set_add(index[c],ed,qe)
            global_list.g_chr = global_list.g_chr - 1
            global_list.g_string[index[c]] = global_list.g_string[ed] = chr(global_list.g_chr)
            c = c - 1
            global_list.g_chr = global_list.g_chr + 1

        if var == '#':
            break
    cul(m, qe)
    if global_list.g_count == 0:
        qe.add_row(["Successful"])
    else:
        qe.add_row(["Wrong"])
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
                for y in p:
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
                print(qe)
                table.clear_rows()
                qe.clear_rows()
                g_clear()
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