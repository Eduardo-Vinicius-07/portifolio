n=float(input("digite uma distancia em metros:"))
cm=n*100
mm=n*1000
print("{} metros em centimetros são:{:.0f} cm\ne em milimetros são:{:.0f} mm"
      "\nem decimetros são:{:.0f}, e em kilometros são:{:.2f},\nem hectometros são:{:.1f}\ne em decametros sao:"
      "{:.1f}".format(n,cm,mm,(n*10),(n/1000),(n/100),(n/10)))
