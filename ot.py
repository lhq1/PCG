import lpn
import math

def ole_vole(m, goal=80):
    t = lpn.choose_weight(2*m, goal)
    return m*m*t

def ole_vope(m, goal=80):
    t = lpn.choose_weight(2*m, goal)
    t0 = lpn.choose_weight(m, goal)
    return m*t*t0

def ot_pprf_subfield(m, goal=80):
    t = lpn.choose_weight(2*m, goal)
    num_ot = m * t * (int(math.log2(8*m/t))+1)
    return num_ot

def ot_pprf_naive(m, goal=80):
    return m*ot_pprf_subfield(m, goal)

def ot_pprf_vope(m, goal=80):
    t = lpn.choose_weight(2 * m, goal)
    t0 = lpn.choose_weight(m, goal)
    len_ot = int(math.log2(8*m/t))+1
    len_ot0 = int(math.log2(4*m/t0))+1
    num_ot = m * (t * len_ot + t0 * len_ot0)
    return num_ot

if __name__=='__main__':
    for i in (128, 256, 512, 1024):
        print("-----------length={}---------".format(i))
        print("Naive VOLE: number of OLE: {}, number of pprf-OT: {}".format(ole_vole(i), ot_pprf_naive(i)))
        print("Subfield VOLE: number of OLE: {}, number of pprf-OT: {}".format(ole_vole(i), ot_pprf_subfield(i)))
        print("Naive VOLE: number of OLE: {}, number of pprf-OT: {}".format(ole_vope(i), ot_pprf_vope(i)))
        print('\n')
