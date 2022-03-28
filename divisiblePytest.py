def divisible_5(num):
    if num%5==0:
        return True
    else:
        return False

def divisible_7(num):
    if num%7==0:
        return True
    else:
        return False

def divisible_9(num):
    if num%9==0:
        return True
    else:
        return False

def divisible_10(num):
    if num%10==0:
        return True
    else:
        return False

if __name__=="__main__":
    num=int(input("Enter Number :"))
    div5=divisible_5(num)
    print(div5)

    div7 = divisible_7(num)
    print(div7)

    div9 = divisible_9(num)
    print(div9)

    div10 = divisible_10(num)
    print(div10)