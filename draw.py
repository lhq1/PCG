from vole import *
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = [128, 256, 512, 1024, 2048]
    goal = 128
    lis_vole = []
    lis_svole = []
    lis_vope = []
    lis_he = []
    for i in x:
        lis_vole.append(cost_naive_vole(i, goal)+other_cost(i))
        lis_svole.append(cost_subfield_vole(i, goal)+other_cost(i))
        lis_vope.append(cost_vope(i, goal)+other_cost(i))
        lis_he.append((i/128)*(i/128)*12.46)
    plt.xscale("log",base=2)
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
