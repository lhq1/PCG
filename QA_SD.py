import math

def seed_size(c, n, t, security_parameter=128,field_size=128, d=2):
    N=math.pow(d, n)
    part1 = math.pow(c*t, 2) * (security_parameter * math.log(2*N/t, 2)+security_parameter+1+field_size)
    part2 = c*t* (math.log(N, 2)+field_size)
    return math.log((part1+part2)/field_size, 2)


if __name__=="__main__":
    c_set = [2, 3, 4]
    n_set = [20, 25]
    secpar_set = [80, 128]
    t_set = [[33, 57],
             [19, 24],
             [11, 15]]
    for i in range(len(c_set)):
        for j in range(len(secpar_set)):
            for k in range(len(n_set)):
                c = c_set[i]
                security_parameter=secpar_set[j]
                t = t_set[i][j]
                n = n_set[k]
                print("c={}, n={}, t={}, security paramter={}".format(c, n, t, security_parameter))
                size = seed_size(c,n,t, security_parameter)
                expand = math.pow(2, n-size+1)
                print("seed size is 2^{}, expand is {}".format(size, expand))
