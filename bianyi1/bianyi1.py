print("begin------------1")
print("if   ------------2")
print("then ------------3")
print("else ------------4")
print("end  ------------5")
print("标志符------------6")
print("整型常数----------7")
print("+----------------8")
print("*----------------9")
print("**---------------10")
print("（---------------11")
print("）---------------12")
print("=========================================================")
input = input("please input your equation:")
input = input.split()
def kind(input):
    alphaall=[]

    def whatstring(string):
        temp = ''.join(string)
        if temp != "":
            if temp.isdigit():
                print("(7," + temp + ")")
            else:
                if temp not in alphaall:
                    alphaall.append(temp)
                alphaindex = str(alphaall.index(temp))
                print('(6,' + alphaindex + ")")
        string.clear()
        return string

    for x in input:
        if x=='if':
            print("(2,-)")
        elif x=='begin':
            print("(1,-)")
        elif x=='then':
            print("(3,-)")
        elif x=='else':
            print("(4,-)")
        elif x=='end':
            print("(5,-)")
        elif x.isdigit():
            print("(7,"+x+")")
        elif x.isalpha():
            if not x in alphaall:
                alphaall.append(x)
            alphaindex = str(alphaall.index(x))
            print('(6,'+alphaindex+")")
        else:
            string = ""
            temp = str(x)
            for xx in temp:
                if xx != '+' and xx != '*' and xx != "**" and xx != '(' and xx != ')':
                    string = ''.join(string)
                    string = string + xx
                    string = list(string)
                elif xx == '+':
                    whatstring(string)
                    print("(8,-)")
                elif xx == '*':
                    whatstring(string)
                    print("(9,-)")
                elif xx == '**':
                    whatstring(string)
                    print("(10,-)")
                elif xx == '(':
                    whatstring(string)
                    print("(11,-)")
                elif xx == ')':
                    whatstring(string)
                    print("(12,-)")
            if string!="":
                whatstring(string)


kind(input)