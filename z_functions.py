from math import sqrt, sin, cos, acos, exp


# ----------------------------------------------------------------------------------------------------
# CONSTANTS

h_centre = 20.955  # [m], height of the roof at the radius of the Reading Room
h_edge = 19.71  # [m], height of the edge of the rectangle

a = 22.245  # [m], radius of Reading Room circle
b = 36.625  # [m], distance from left or right side of rectangle to centre of Reading Room circle
c = 46.025  # [m], distance from top of rectangle to centre of Reading Room circle
d = 51.125  # [m], distance from bottom of rectangle to centre of Reading Room circle
lambda_ = 0.5
mu = 14.0


# ----------------------------------------------------------------------------------------------------
# METHODS

def calculate_polar_coord(x: float, y: float) -> float:
    '''r'''
    return sqrt(x**2 + y**2)

def _calculate_eta(x: float, y: float) -> float:
    '''Function for level change
    η
    '''
    r = calculate_polar_coord(x, y)
    if r == 0:
        return 0
    numerator = _calculate_psi(x, y)
    denominator = (1 - (a*x)/(r*b)) * (1 + (a*x)/(r*b)) * (1 - (a*y)/(r*c)) * (1 + (a*y)/(r*d))
    return numerator / denominator if denominator != 0 else 0

def _calculate_psi(x: float, y: float) -> float:
    '''Function for finite curvature at corners - part 1
    ψ
    '''
    if x == b or x == -b or y == c or y == -d:
        return 0
    return (1 - x/b) * (1 + x/b) * (1 - y/c) * (1 + y/d)

def _calculate_alpha(x: float, y: float) -> float:
    '''Function for finite curvature at corners - part 2
    α
    '''
    r = calculate_polar_coord(x, y)
    if r == 0:
        return 0
    psi = _calculate_psi(x, y)
    return ((r/a) - 1) * psi

def calculate_theta(x: float, y: float) -> float:
    '''θ'''
    r = calculate_polar_coord(x, y)
    if r == 0:
        return 0
    return acos(x/r)

def _calculate_beta(x: float, y: float) -> float:
    '''Function for conical corners
    β
    '''
    r = calculate_polar_coord(x, y)
    if r == 0 or x == b or x == -b or y == c or y == -d:
        return 0
    numerator = 1 - a/r
    denominator_1 = sqrt((b - x)**2 + (c - y)**2) / ((b - x) * (c - y))
    denominator_2 = sqrt((b - x)**2 + (d + y)**2) / ((b - x) * (d + y))
    denominator_3 = sqrt((b + x)**2 + (c - y)**2) / ((b + x) * (c - y))
    denominator_4 = sqrt((b + x)**2 + (d + y)**2) / ((b + x) * (d + y))
    denominator = denominator_1 + denominator_2 + denominator_3 + denominator_4
    return numerator / denominator if denominator != 0 else 0

def _calculate_z_1(x: float, y: float) -> float:
    eta = _calculate_eta(x, y)
    return (h_centre - h_edge)*eta + h_edge

def _calculate_z_2(x: float, y: float) -> float:
    r = calculate_polar_coord(x, y)
    psi = _calculate_psi(x, y)
    theta = calculate_theta(x, y)
    alpha = _calculate_alpha(x, y)
    first_term = (35 + 10*psi) * 0.5 * (1 + cos(2*theta)) + 12*(0.5*(1 - cos(2*theta)) + sin(theta)) + (7.5 + 12*psi) * (0.5*(1 - cos(2*theta)) - sin(theta)) - 1.6
    second_term = 5 * (1 + cos(2*theta))
    third_term = 10 * (0.5 * (0.5 * (1 - cos(2*theta)) + sin(theta)))**2 * (1 - 3*alpha)
    fourth_term = 2.5 * (0.5 * (0.5 * (1 - cos(2*theta)) - sin(theta)))**2 * (r/a - 1)**2
    return alpha * ((1-lambda_)*first_term - second_term + third_term + fourth_term)

def _calculate_z_3(x: float, y: float) -> float:
    beta = _calculate_beta(x, y)
    theta = calculate_theta(x, y)
    first_term = 1.75 * (1 + cos(2*theta)) + 1.5 * (1 - cos(2*theta)) + 0.3 * sin(theta)
    second_term = 1.05 * (exp(-mu*(1 - x/b)) + exp(-mu*(1 + x/b))) * (exp(-mu*(1 - y/c)) + exp(-mu*(1 + y/d)))
    return beta * ((lambda_ * first_term) + second_term)

def calculate_z(x: float, y: float) -> float:
    z_1 = _calculate_z_1(x, y)
    z_2 = _calculate_z_2(x, y)
    z_3 = _calculate_z_3(x, y)
    z = z_1 + z_2 + z_3
    return round(z, 4)