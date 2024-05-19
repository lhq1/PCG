import lpn
import math
# This function use OLE from ring-lwe to compute base VOLE
# The plaintext is only 120-bit and each OLE requires 420 bits


def from_bit_to_mb(n):
    return n/(8*1024*1024)


def base_vole_from_ole(len, num):
    return len * num * 420


def ot(num, kappa):
    return num * kappa


def cost_naive_vole(m, goal=128, bit_len=128):
    t = lpn.choose_weight(2*m, goal)
    cost_base_vole = base_vole_from_ole(1, m * m * t)
    num_ot = m * m * t * math.log2(8*m/t)
    cost_ot = ot(num_ot, 128)
    cost_com = 2 * m * m * t * bit_len
    return from_bit_to_mb(cost_base_vole + cost_ot + cost_com)


def cost_subfield_vole(m, goal=128, bit_len=128):
    t = lpn.choose_weight(2 * m, goal)
    cost_base_vole = base_vole_from_ole(m, m * t)
    num_ot = m * t * math.log2(8 * m / t)
    cost_ot = ot(num_ot, 128)
    cost_com = (1 + m) * m * t * bit_len
    return from_bit_to_mb(cost_base_vole + cost_ot + cost_com)


def cost_vope(m, goal=128, bit_len=128):
    t = lpn.choose_weight(2 * m, goal)
    t0 = lpn.choose_weight(m, goal)
    cost_base_vole = base_vole_from_ole(t, m * t0)
    num_ot = m * (t * math.log2(8 * m / t) + t0 * math.log2(4 * m / t0))
    cost_ot = ot(num_ot, 128)
    cost_com = m * (t * (1+m) + t0 * (1 + t)) * bit_len
    return from_bit_to_mb(cost_base_vole + cost_ot + cost_com)


def other_cost(m,bit_len=128):
    cost_vole = 16 * m*m*bit_len
    cost_sacrifice = 2* m * m * bit_len
    return from_bit_to_mb(cost_vole + cost_sacrifice)


if __name__ == "__main__":
   for i in (128, 256, 512, 1024):
        print("The cost of VOLE and sacrifce: {} MB".format(other_cost(i)))
        for j in (80, 128):
            print("Naive VOLE: Length: {}, Security: {}, Com cost: {:.2f} MB".format(i, j, cost_naive_vole(i, j)))
            print("Subfield VOLE: Length: {}, Security: {}, Com cost: {:.2f} MB".format(i, j, cost_subfield_vole(i, j)))
            print("Our VOPE: Length: {}, Security: {}, Com cost: {:.2f} MB".format(i, j, cost_vope(i, j)))
        print("\n")
