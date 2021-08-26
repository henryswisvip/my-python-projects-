def ABC(bian):
    B = bian*bian
    return B




print("press A to start")

A = input()



if A == 'A':


    X = 2

    while X == 2:
        Q = input("输入边长:")
        if Q == "u":
            break
        else:

            area = ABC(float(Q))
            print("你的面积是%d" % (area))














