def matrix(number):
    print("구구단을 출력합니다. \n")
    for x in range(2, number+1):
        print("------- [" + str(x) + "단] ----------")
        for y in range(1,10):
            print(x, "X", y ,"=", x*y)
    print("-----------")

a = input("몇단까지 출력할까요? : ")
b = int(a)
result = matrix(b)
print(result)
