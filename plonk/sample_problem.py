from .copy_constraint import find_permutation
from .constraint import add_mul_constraint, add_add_constraint, add_constant_constraint

def gen_witness():
    a = [3, 3, 9, 9, 16]
    b = [4, 4, 16, 4, 9]
    c = [5, 25, 5, 5, 25]
    return (a, b, c)

def is_satisfied_witness(a, b, c):
    assert a[0] == 3
    assert b[0] == 4
    assert c[0] == 5
    assert a[1] * b[1] == c[1]  # 3 * 4 = 12
    assert a[2] + b[2] == c[2]  # 9 + 16 = 25
    assert a[3] == 9
    assert b[3] == 4
    assert c[3] == 5
    assert a[4] == 16
    assert b[4] == 9
    assert c[4] == 25

def add_add_constraint(Ql, Qr, Qm, Qo, Qc):
    Ql.append(1)   # Coefficient for the first term (a)
    Qr.append(1)   # Coefficient for the second term (b)
    Qm.append(0)   # No multiplication term
    Qo.append(-1)  # Coefficient for the output term (c), which is subtracted
    Qc.append(0)   # No constant term here

    return Ql, Qr, Qm, Qo, Qc

def gen_constraints():
    # Initialize constraints
    Ql = []
    Qr = []
    Qm = []
    Qo = []
    Qc = []

    # Example constraints for proving (3, 4, 5) satisfies the equation a^2 + b^2 = c^2
    Ql, Qr, Qm, Qo, Qc = add_constant_constraint(Ql, Qr, Qm, Qo, Qc, 9)   # 3^2
    Ql, Qr, Qm, Qo, Qc = add_constant_constraint(Ql, Qr, Qm, Qo, Qc, 16)  # 4^2
    Ql, Qr, Qm, Qo, Qc = add_constant_constraint(Ql, Qr, Qm, Qo, Qc, 25)  # 5^2
    Ql, Qr, Qm, Qo, Qc = add_add_constraint(Ql, Qr, Qm, Qo, Qc)           # 9 + 16 - 25 = 0

    return (Ql, Qr, Qm, Qo, Qc)

def gen_copy_constraints():
    copy_constraints = [0, 1, 2, 3, 4]
    eval_domain = range(0, len(copy_constraints))

    x_a_prime = find_permutation(copy_constraints[0:2], eval_domain[0:2])
    x_b_prime = find_permutation(copy_constraints[2:4], eval_domain[2:4])
    x_c_prime = find_permutation(copy_constraints[4:], eval_domain[4:])

    return (x_a_prime, x_b_prime, x_c_prime, copy_constraints)

def setup():
    Ql, Qr, Qm, Qo, Qc = gen_constraints()
    perm_x, perm_y, perm_z, copy_constraints = gen_copy_constraints()

    return (Ql, Qr, Qm, Qo, Qc, perm_x, perm_y, perm_z, copy_constraints)
