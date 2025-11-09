import numpy as np
import matplotlib.pyplot as plt

#Part1
lynx = np.array([
[209.7,368.4],[157.6,332.1],[118.8,284.2],[80.9,224.6],[43.1,244.4],[20.4,266.7],
[-4.3,293.6],[2.4,263.2],[-20.4,292.4],[-39.3,299.4],[-21.3,259.7],
[-50.7,267.8],[-39.3,242.1],[-55.4,240.9],[-100.8,300.6],[-149.1,345.0],
[-172.8,361.4],[-189.8,300.6],[-192.7,225.7],[-181.3,145.0],[-168.1,104.1],
[-184.1,66.7],[-187.0,31.6],[-183.2,3.5],[-208.8,-4.7],[-197.4,-29.2],
[-182.2,-44.4],[-203.1,-43.3],[-172.8,-92.4],[-131.1,-126.3],[-101.8,-147.4],
[-74.3,-163.7],[-110.3,-224.6],[-143.4,-287.7],[-161.4,-240.9],[-282.6,-221.1],
[-388.6,-205.9],[-370.7,-301.8],[-339.4,-397.7],[18.5,-397.7],[345.1,-400.0],
[359.3,-378.9],[367.8,-342.7],[347.0,-362.6],[363.1,-302.9],[357.4,-243.3],
[348.9,-266.7],[336.6,-201.2],[290.2,-135.7],[240.0,-118.1],[258.9,-164.9],
[258.0,-228.1],[252.3,-271.4],[256.1,-333.3],[247.6,-359.1],[230.5,-307.6],
[194.6,-238.6],[160.5,-181.3],[120.7,-149.7],[165.2,-132.2],[201.2,-100.6],
[183.2,-99.4],[221.1,-73.7],[253.3,-24.6],[222.0,-23.4],[251.4,-1.2],
[262.7,24.6],[234.3,25.7],[214.4,42.1],[202.1,60.8],[220.1,101.8],
[234.3,160.2],[240.0,230.4],[232.4,317.0]
])

def plot_shape(points, title):
    plt.plot(points[:,0], points[:,1])
    plt.title(title)
    plt.axis('equal')
    plt.show()

def stretch(X, a, b):
    A = np.array([[a,0],
                  [0,b]])
    print("Stretch A =\n", A)
    return X @ A.T

def shear(X, a, b):
    A = np.array([[1,a],
                  [b,1]])
    print("shear A =\n", A)

    return X @ A.T

def rotate(X, deg):
    t = np.radians(deg)
    A = np.array([[np.cos(t),-np.sin(t)],
                  [np.sin(t),np.cos(t)]])
    print("rotate A =\n", A)
    return X @ A.T

def reflect_xy(X):
    A = np.array([[0,1],[1,0]])
    print("Reflection (y=x) A =\n", A)
    return X @ A.T

orig = lynx
st = stretch(lynx, 1.2, 0.8)
sh = shear(lynx, 0.3, 0)
rot=rotate(lynx, 30)
ref= reflect_xy(lynx)
comp= rotate(shear(stretch(lynx,1.2,0.8),0.3,0), 30)

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
plots = [(orig, "Original", "gray"),
    (st, "Stretch (1.2, 0.8)","lightblue"),
    (sh,"Shear (0.3, 0)", "lightpink"),
    (ref,"Reflection (line y=x)","lightgreen"),
    (rot,"Rotation (30°)","plum"),
    (comp,"Composition\n(Stretch→Shear→Rotate)","purple")
]
for ax, (pts, title, color) in zip(axes.ravel(), plots):
    ax.plot(pts[:,0], pts[:,1], color=color)
    ax.fill(pts[:,0], pts[:,1], color=color, alpha=0.3)
    ax.set_title(title)
    ax.axis('equal')
    ax.axis('off')
plt.tight_layout()
plt.show()


#Part2
comp1 = rotate(shear(stretch(lynx, 1.2, 0.8), 0.3, 0), 30)
comp2 = rotate(stretch(shear(lynx, 0.3, 0), 1.2, 0.8), 30)
comp3 = stretch(shear(rotate(lynx, 30), 0.3, 0), 1.2, 0.8)

plt.figure(figsize=(6,6))
plt.fill(lynx[:,0], lynx[:,1], color='gray',alpha=0.25)
plt.plot(lynx[:,0], lynx[:,1], color='gray', label='Original')

plt.fill(comp1[:,0], comp1[:,1], color='blue',alpha=0.25)
plt.plot(comp1[:,0], comp1[:,1], color='blue', label='Stretch-Shear-Rotate')

plt.fill(comp2[:,0], comp2[:,1], color='lightcoral',alpha=0.25)
plt.plot(comp2[:,0], comp2[:,1], color='lightcoral', label='Shear-Stretch-Rotate')

plt.fill(comp3[:,0], comp3[:,1], color='green',alpha=0.25)
plt.plot(comp3[:,0], comp3[:,1], color='green', label='Rotate-Shear-Stretch')

plt.title("Different Orders of Transformations", fontsize=11)
plt.legend(fontsize=8)
plt.axis('equal')
plt.show()