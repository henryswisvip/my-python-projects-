import random

lisst = "python"
print (lisst)
inpuut = input("欢迎来到猜词小游戏\n你有9词机会来猜单词，但是你一次只能输入一个字母。按任意键开始\n ")

count = 9

while 1 +1 == 2:
    if count <1:
        exit()
    inpuut = input("输入一个字母 ")
    i = 0
    if i > 0:
        exit()

    randomchoice = random.choice(lisst)
    lissst = list (randomchoice)
    n = lisst[i]
    if inpuut == lisst[i]:

        i = i + 1
        break
    else:

        count = count - 1

        print ("打错了继续加油你还有{}次机会".format(count))




while 0<count<=9:

    inpuut = input("答对了你还有两个，你现在是{}".format(str(n)))
    randomchoice = random.choice(lisst)
    lissst = list(randomchoice)

    if inpuut == lisst[i]:
        k = lisst[i]
        print("答对了你还有一个，你现在是{}".format(str(n)+str(k)))
        break
    else:
        print("打错了继续加油你还有7次机会")
        break
while 0<count<=8:










