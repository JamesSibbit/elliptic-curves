def solve(b1,a,b2):
    run = 0
    for w in range(100):
        for u in range(100):
            for v in range(100):
                if (w**2 == b1*u**4 + a*(u*v)**2 + b2*(v**4)) and (u+v+w != 0):
                    print(u,v,w)
                    break
                else:
                    run += 1

solve(7,-10,7)
