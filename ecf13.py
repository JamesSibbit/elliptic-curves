#Tool for checking number of solutions to elliptic curve mod prime p

def ec_soln(p,a1,a3,a2,a4,a6):
    card = 1
    for x in range(p):
        rhs = (x**3+a2*(x**2)+a4*x+a6)%p
        print('f('+str(x)+')='+str(rhs))
        for y in range(p):
            if (y**2 + a1*x*y + a3*y)%p == rhs:
                print(x,y)
                card+=1
    print("Cardinality WITH pt at infinity = " + str(card))


ec_soln(7,0,0,0,0,5)
