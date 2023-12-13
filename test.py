import scipy.stats, math
# print(scipy.stats.norm.ppf(0.1))
tAlpha = abs(scipy.stats.t.ppf(0.05/2, 29))
r=-0.655
t = r/math.sqrt((1-(r**2))/(29-2))
if abs(r) >= tAlpha:
    print("Significant")