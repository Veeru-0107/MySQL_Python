def alphanum_sort(ls):
    Nls = []
    Sls = []
    for x in ls:

        if (isinstance(x, int)):
            Nls.append(x)
        else:
            Sls.append(x)

    Nls.sort()
    Sls.sort()
    print(Nls)
    print(Sls)
    Tls = Sls + Nls
    print(Tls)

