import matplotlib.pyplot as plt
import pandas as pd


def read_fft_wht(path):
    data = pd.read_excel(path, sheet_name=0)
    print(data)
    var_x = data["n"].tolist()
    x = []
    for i in range(len(var_x)):
        x.append(pow(2, var_x[i]))
    y_fft_32 = data["ring-LPN(32-bit)"].tolist()
    y_fft_64 = data["ring-LPN(64-bit)"].tolist()
    y_fft_128 = data["ring-LPN(128-bit)"].tolist()
    y_wht_32 = data["QA-SD(32-bit)"].tolist()
    y_wht_64 = data["QA-SD(64-bit)"].tolist()
    y_wht_128 = data["QA-SD(128-bit)"].tolist()
    plt.plot(x, y_fft_64, marker='o', color='blue',label="FFT")
    #plt.plot(x, y_fft_64, marker='o', color='red',label="FFT(64bit)")
    #plt.plot(x, y_fft_128, marker='o', color='purple',label="FFT(128bit)")
    plt.plot(x, y_wht_64, marker='o', color='red', label="Walsh")
    #plt.plot(x, y_wht_64, marker='*', color='red', label="WHT(64bit)")
    #plt.plot(x, y_wht_128, marker='*', color='purple', label="WHT(128bit)")
    plt.xlabel("The number of evaluations")
    plt.xscale("log", base=2)
    plt.yscale("log")
    plt.ylabel("Runtime")
    plt.legend()
    # plt.title("The security parameter for c=4, n=20, t=16 and different field sizes")
    plt.show()


def read_VOLE(path):
    data = pd.read_excel(path, sheet_name=1)
    print(data)
    x = data["n"].tolist()
    y_ea_fast = data["EA(aggressive)"].tolist()
    y_ea_slow = data["EA(conservative)"].tolist()
    y_ec_fast = data["EC(aggressive)"].tolist()
    y_ec_slow = data["EC(conservative)"].tolist()
    y_qa_sd = data["QA-SD"].tolist()
    plt.plot(x, y_ea_fast, marker='o', color='blue',label="EA-aggressive")
    plt.plot(x, y_ea_slow, marker='*', color='c',label="EA-conservative")
    #plt.plot(x, y_fft_128, marker='o', color='purple',label="FFT(128bit)")
    plt.plot(x, y_ec_fast, marker='o', color='red', label="EC-aggressive")
    plt.plot(x, y_ec_slow, marker='*', color='m', label="EC-conservative")
    plt.plot(x, y_qa_sd, marker="o", color="g", label="QA-SD")
    #plt.plot(x, y_wht_128, marker='*', color='purple', label="WHT(128bit)")
    plt.xlabel("The number of variables")
    plt.yscale("log")
    plt.ylabel("Runtime")
    plt.legend()
    # plt.title("The security parameter for c=4, n=20, t=16 and different field sizes")
    plt.show()


if __name__ == "__main__":
    '''
    x = [128, 256, 512, 1024]
    goal = 80
    lis_vole = []
    lis_svole = []
    lis_vope = []
    lis_he = []
    for i in x:
        lis_vole.append(cost_naive_vole(i, goal)+other_cost(i))
        lis_svole.append(cost_subfield_vole(i, goal)+other_cost(i))
        lis_vope.append(cost_vope(i, goal)+other_cost(i))
        lis_he.append((i/128)*(i/128)*12.46)
    MBps = 1 * 1000/8
    print([i for i in lis_vole])
    print([i for i in lis_svole])
    print([i for i in lis_vope])
    print([i for i in lis_he])
    plt.xscale("log", base=2)
    plt.yscale("log")
    plt.plot(x, lis_vole, marker='o', label="naive VOLE", color='r')
    plt.plot(x, lis_svole, marker='o', label="subfield_VOLE", color='b')
    plt.plot(x, lis_vope, marker='o', label="our VOPE", color='g')
    plt.plot(x, lis_he, marker='o', label="HE", color='pink')
    plt.xlabel("Length ")
    plt.ylabel("Communication (MB)")
    plt.legend()
    plt.title("The communication of secure matrix multiplication ({}-bit security)".format(goal))
    plt.show()
    lis_x = [9, 11, 13, 17, 19, 23, 25, 27, 29, 31, 37, 41, 43, 49, 53, 59, 61, 67, 71, 73, 79, 81, 89, 97, 101]
    lis_y1_cons = [128.26, 129.4, 130.21, 131.4, 131.94, 131.97, 132.43, 132.86, 133.26, 133.47, 134.08, 134.51,
                   134.71, 134.98, 135.1, 135.26, 135.31, 135.44, 135.53, 135.57, 135.67, 135.7, 135.82, 135.94, 136
                   ]
    lis_y1 = [124.78, 125.96, 128.63, 130.28, 131.42, 132.3, 133.46, 134, 132.85, 133.14,
             133.4, 133.64, 133.84, 134.34,  134.62, 134.74, 134.98, 135.1]
    lis_y2 = [122.82, 128.24, 130.5, 129.34, 130.8, 132, 133.29, 133.84, 134.85, 135.08,
              135.27, 135.43, 135.54, 135.82, 135.96, 136.01, 136.16, 136.25]
    plt.plot(lis_x, lis_y1_cons, marker='o', color='blue')
    plt.xlabel("Field size ")
    plt.ylabel("Security parameter")
    #plt.title("The security parameter for c=4, n=20, t=16 and different field sizes")
    plt.show()
    '''
    read_fft_wht("QA-SD.xlsx")

