import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def read_off(path):
    with open(path, "r") as f:
        if f.readline().strip() != "OFF":
            raise ValueError("Not a valid OFF header")
        n_verts, n_faces, _ = map(int, f.readline().split())
        verts = [list(map(float, f.readline().split())) for _ in range(n_verts)]
        faces = [list(map(int, f.readline().split()[1:])) for _ in range(n_faces)]
    return np.array(verts, dtype=float), faces

def rotate_xy(X, theta_deg):
    θ = np.radians(theta_deg)
    R = np.array([
        [np.cos(θ), -np.sin(θ), 0],
        [np.sin(θ),  np.cos(θ), 0],
        [0,          0,         1]
    ])
    return X.copy() @ R.T, R

def rotate_yz(X, theta_deg):
    θ = np.radians(theta_deg)
    R = np.array([
        [1, 0, 0],
        [0, np.cos(θ), -np.sin(θ)],
        [0, np.sin(θ),  np.cos(θ)]
    ])
    return X.copy() @ R.T, R

def rotate_xz(X, theta_deg):
    θ = np.radians(theta_deg)
    R = np.array([
        [ np.cos(θ), 0, np.sin(θ)],
        [ 0,         1, 0        ],
        [-np.sin(θ), 0, np.cos(θ)]
    ])
    return X.copy() @ R.T, R

def plot_off(ax, vertices, faces, title):
    mesh = Poly3DCollection(
        [vertices[face] for face in faces],
        alpha=0.3, edgecolor='k'
    )
    ax.add_collection3d(mesh)
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=2, c='r')
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])

path = r"C:\Users\tanya\Downloads\meta40\airplane_0628.off\airplane_0628.off"
vertices, faces = read_off(path)

verts_xy, Rxy = rotate_xy(vertices, 45)
verts_yz, Ryz = rotate_yz(vertices, 45)
verts_xz, Rxz = rotate_xz(vertices, 45)

#матриці
print("Rotation XY (Z-axis):\n", Rxy)
print("\nRotation YZ (X-axis):\n", Ryz)
print("\nRotation XZ (Y-axis):\n", Rxz)

fig = plt.figure(figsize=(12, 10))
ax1 = fig.add_subplot(221, projection='3d')

plot_off(ax1, vertices, faces, "Original model")

ax2 = fig.add_subplot(222, projection='3d')
plot_off(ax2, verts_xy, faces, "Rotate XY (45°)")

ax3 = fig.add_subplot(223, projection='3d')
plot_off(ax3, verts_yz, faces, "Rotate YZ (45°)")

ax4 = fig.add_subplot(224, projection='3d')
plot_off(ax4, verts_xz, faces, "Rotate XZ (45°)")

plt.tight_layout()
plt.show()

#part2
R_total1 = Ryz @ Rxy @ Rxz
verts_total1 = vertices @ R_total1.T
print("\nR_total1 (YZ-XY-XZ) =\n", R_total1)

R_total2 = Rxz @ Ryz @ Rxy
verts_total2 = vertices @ R_total2.T
print("\nR_total2 (XZ-YZ-XY) =\n", R_total2)

fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1, projection='3d')
plot_off(ax1, verts_total1, faces, "Combined 1 (YZ-XY-XZ)")

ax2 = fig.add_subplot(1,2,2, projection='3d')
plot_off(ax2, verts_total2, faces, "Combined 2 (XZ-YZ-XY)")

plt.tight_layout()
plt.show()

