import matplotlib.pyplot as plt

def calculateAndShowGraph(s:float,sigma:float,y0:float,T:int):
        tt = T
        Y = [0 for i in range(tt)]
        C = [0 for i in range(tt)]
        I = [0 for i in range(tt)]
        S = [0 for i in range(tt)]
        DK = [0 for i in range(tt)]
        b1 = [0 for i in range(tt)]
        b2 = [0 for i in range(tt)]
        b3 = [0 for i in range(tt)]
        Y.insert(0, y0)
        C.insert(0, (1-s)*y0)
        for i in range(T):           
            S.insert(i, s*Y[i])
            I.insert(i, S[i])
            DK.insert(i+1, I[i])
            Y.insert(i+1, Y[i] + sigma*DK[i+1])
            C.insert(i+1, (1-s)*Y[i+1])
            b1.insert(i, sigma * DK[i+1]/Y[i])
            b2.insert(i, ((1-s)*Y[i+1]-C[i])/C[i])
            b3.insert(i, (s*Y[i+1]-s*Y[i])/I[i])

        plt.axis([1,T, None, None])
        plt.plot(Y, label='Y(t)')
        plt.plot(C, label='C(t)')
        plt.plot(I, label='I(t)')

        plt.xlabel(r'$x$', fontsize=16)
        plt.ylabel(r'$t$', fontsize=16)

        plt.title('Графики Y(t), C(t), I(t)')
        plt.legend(fontsize=14)
        plt.show()

        plt.show()       
calculateAndShowGraph(s=0.72, sigma=1.57, y0=80, T=10)