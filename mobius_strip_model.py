import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import simpson

class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=100):
       
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._generate_mesh()

    def _generate_mesh(self):
       
        U, V = self.U, self.V
        R = self.R
        X = (R + V * np.cos(U / 2)) * np.cos(U)
        Y = (R + V * np.cos(U / 2)) * np.sin(U)
        Z = V * np.sin(U / 2)
        return X, Y, Z

    def plot(self):
        
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='k', alpha=0.8)
        ax.set_title("Möbius Strip")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()
        plt.show()

    def compute_surface_area(self):
        
        def partials(u, v):
            dx_du = -np.sin(u) * (self.R + v * np.cos(u / 2)) - (v / 2) * np.sin(u / 2) * np.cos(u)
            dx_dv = np.cos(u) * np.cos(u / 2)
            dy_du = np.cos(u) * (self.R + v * np.cos(u / 2)) - (v / 2) * np.sin(u / 2) * np.sin(u)
            dy_dv = np.sin(u) * np.cos(u / 2)
            dz_du = (v / 2) * np.cos(u / 2)
            dz_dv = np.sin(u / 2)
            E = dx_du**2 + dy_du**2 + dz_du**2
            F = dx_du * dx_dv + dy_du * dy_dv + dz_du * dz_dv
            G = dx_dv**2 + dy_dv**2 + dz_dv**2
            return np.sqrt(E * G - F**2)

        integrand = np.zeros((self.n, self.n))
        for i, u in enumerate(self.u):
            for j, v in enumerate(self.v):
                integrand[j, i] = partials(u, v)

        return simpson(simpson(integrand, x=self.v, axis=0), x=self.u, axis=0)

    def compute_edge_length(self):
        
        u_vals = self.u
        v_edge = self.w / 2
        x = (self.R + v_edge * np.cos(u_vals / 2)) * np.cos(u_vals)
        y = (self.R + v_edge * np.cos(u_vals / 2)) * np.sin(u_vals)
        z = v_edge * np.sin(u_vals / 2)
        dx = np.gradient(x)
        dy = np.gradient(y)
        dz = np.gradient(z)
        ds = np.sqrt(dx**2 + dy**2 + dz**2)
        return np.sum(ds)

# Usage example
if __name__ == "__main__":
    mobius = MobiusStrip(R=1.0, w=0.3, n=200)
    print("Surface Area of Mobius Strip:", mobius.compute_surface_area())
    print("Edge Length of Mobius Strip:", mobius.compute_edge_length())
    mobius.plot()
