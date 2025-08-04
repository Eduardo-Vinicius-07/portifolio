def calc_imc(m,h):
    imc=m/(h**2)
    return imc
if __name__ == '__main__':
    for i in range(2):
        v1=float(input(f"digite o peso em kg:"))
        v2=float(input(f"digite a altura em metros:"))
        print(f"o imc dessa pessoa é:{calc_imc(v1,v2):.2f}")
