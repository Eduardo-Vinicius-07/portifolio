def calc_media(v1,v2,v3):
    s=v1+v2+v3
    m=s/3
    return m

if __name__ == '__main__':
    a= float(input(f"digite um valor"))
    b= float(input(f"digite um valor"))
    c= float(input(f"digite um valor"))
    r = calc_media(a,b,c)
    print(r)
    