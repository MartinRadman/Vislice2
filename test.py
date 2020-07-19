for i in range(2, 201):
    preskoci = False
    j = 2
    while j ** 2 <= i:
        if i % j == 0:
            preskoci = True
            break
        j += 1
    if not preskoci:
        print(i)