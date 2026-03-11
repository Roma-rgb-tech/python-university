def test():
    num = int(input("Номер з списку групи: "))
    if num > 0:
        for n in range(0, num):
            print(n * 10)
            

test()