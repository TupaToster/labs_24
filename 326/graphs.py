import matplotlib.pyplot as plt
import numpy as np

def graph(x, y, x_name, y_name, function='none'):
    time = x
    tok_mkA = y
    aprox = 0
    if function == 'exp':
        model = np.poly1d(np.polyfit(time, np.log(tok_mkA), deg = 1))
        aprox = f'{str(np.exp(model[0]))[:8]}*exp({str(model[1])[:8]}x)'

    if function == 'linear':
        model = np.poly1d(np.polyfit(time, tok_mkA, deg = 1))
        aprox = f'{str(model[1])[:8]}x+({str(model[0])[:8]})'
        k = float(model[1])
        b = float(model[0])
        print ('k = ' + str(k))
        print ('b = ' + str(b))
        minx = min(time)
        maxx = max(time)
        v = [minx + i*(maxx - minx)/100 for i in range(1, 101)]
        u = [k*t + b for t in v]
        v = np.linspace (0, maxx, 100)
        plt.plot(v, k*v + b, '--', color = 'orange', label = 'y = ' + str (k) + ' * x + ' + str(b))

    if aprox:
        plt.scatter(time, tok_mkA, color = 'green')
        # plt.scatter(time, tok_mkA, label = y_name + '(' + x_name +')' + f'\n aproximation: \n y = (12.68 ± 0.94) + (1.99 ± 0.014)·x', color = 'green')
    else:
        plt.plot(time, tok_mkA, label = y_name + '(' + x_name +')', color = 'green')
        plt.scatter(time, tok_mkA, label = y_name + '(' + x_name +')', color = 'red')
        coord = y[0] / 2.71
        plt.plot(x, [coord]*len(x), label = "y = lmax/e")

    plt.grid()
    # plt.title(y_name + '(' + x_name +')')
    plt.xlabel (x_name)
    plt.ylabel (y_name)
    # plt.xlabel(r'$10^{-9} * (Ro + R)^2$ Ом$^2$')
    # plt.ylabel(r'$1/\Theta^2$')
    plt.legend()
    # '''plt.xlim(min(time)*0.95, max(time)*1.05)
    # plt.ylim(min(tok_mkA)*0.95, max(tok_mkA)*1.05)'''
    plt.show()

i = [107.3482428,
95.18413598,
82.69073011,
62.26065473,
49.92570579,
41.67011162,
35.75736077,
31.31407269,
27.85299807
]
x = [225        ,202        ,178        ,138        ,113       ,96         ,84         ,75         ,66]
graph (x, i, "x, мм", "I, нА", "linear")

# R = [0.64,0.83,1.04,1.28,1.55,1.84,2.49,3.25,4.11,5.06]
# th11 = [0.27	,0.36	,0.37	,0.50	,0.56	,0.64	,0.87	,1.12	,1.23	,1.55]
# graph(R, th11, "", "", "linear")

# x = [0.019811788, 0.021903406,	0.024488796,	0.027766209,	0.032056419,	0.037914692,	0.046392948,	0.059755004,
#      	0.083927822,	0.141342756,	0.43956044,	0.164068909,	0.196270854,	0.244200244,	0.323101777,	0.388349515]
# y = [220,	213,	210,	208,	200,	191,	178,	161,	144,	113,	55,	100,	87,	81,	68,	61]
# x.sort()
# y.sort(reverse=True)
# graph(x, y, "1/(R+Ro), 1/кОм", "lmax, мм")