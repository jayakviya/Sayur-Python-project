for row in range(0,8):
    for colume in range(0,8):
        if colume % 2 == 0 :
            print("\u25A0",end=" ")
        else :
            print("\u25A1",end=" ")
    print()
