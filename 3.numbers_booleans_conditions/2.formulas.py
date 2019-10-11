from math import pi


def sphere_volume(radius):
    """
    Implements sphere volume formula: V = 4/3πr^3
    """
    return 4 / 3 * pi * radius ** 3


def stokes_law(dyn_visc, radius, flow_visc):
    """
    Implements Stokes' law: F = 6πμRv
    """
    return 6 * pi * dyn_visc * radius * flow_visc


def harmonic_mean(*args):
    """
    Implements harmonic mean formula: H = n/(1/x1 + 1/x2 + ... + 1/xn)
    """
    denominator = [1 / x for x in args]
    return len(args) / sum(denominator)


c = None
while c != '0':
    print("Select formula. Type '1', '2' or '3'. Enter '0' to escape.")
    c = input()
    if c == '1':
        print('1. Calculating volume inside a sphere.\nEnter sphere radius:')
        sr = float(input())
        print(f'Sphere volume: {sphere_volume(sr)}')
    elif c == '2':
        print("2. Calculate force of viscosity using Stokes' law.\nEnter dynamic viscosity:")
        dv = float(input())
        print('Enter object radius:')
        r = float(input())
        print('Enter flow viscosity:')
        fv = float(input())
        print(f'Frictional force: {stokes_law(dv, r, fv)}')
    elif c == '3':
        print('3. Calculate harmonic mean of a set of observations.\nEnter observations values, separated by spaces:')
        a = [float(x) for x in input().split()]
        print(harmonic_mean(*a))
    elif c == '0':
        print('Goodbye, cruel world.')
    else:
        print('Unknown command.')

