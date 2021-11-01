"""
Analysis of rock stresses using Mohr stress circle (2D).

Author: Daniel Kadaso

Date: October 2021
"""

# Necessary modules
import numpy as np
import matplotlib.pyplot as plt


# Class mohr_circle for visualization of stresses using a 2D Mohr stress circle
class mohr_stress_circle:
    """Determine 2D rock stresses using Mohr Stress Circle."""

    # Initialization of variables
    def __init__(self, sigmax, sigmay, shear_stress):
        self.sigmax = sigmax
        self.sigmay = sigmay
        self.shear_stress = shear_stress
        self.initial_values = {"sigma x": self.sigmax,
                               "sigma y": self.sigmay,
                               "shear stress": self.shear_stress}
        
        self.stress_state()         # calls a function stress_state to compute stress state values of the component
        self.disp_stress_state()    # calls a function disp_stress_state to display the computed stress state values of the component
        self.plot_msc()               # plots a Mohr stress circle for the given stress element

        
    def stress_state(self):
        """
        Determine the center and radius of the Mohr stress circle.
        Also, determine the principal normal stresses and the maximum shear stress.
        
        Input: Uses values (sigmax, sigmay, and shear stress) initially set by the user.

        Return: Center of the MSC (array)
                Radius of the MSC (array)
                Maximum normal stress (array)
                Minimum normal stress (array)
                Maximum shear stress (array)
        """

        # Calculate the center and radius of the circle
        # self.center = ((self.sigmax + self.sigmay) / 2)
        self.center = np.array([((self.sigmax + self.sigmay) / 2), 0])
        self.radius = np.sqrt((((self.sigmax - self.sigmay) / 2)**2) + (self.shear_stress**2))

        # Calculate principal normal stresses and maximum shear stress
        self.max_normal_stress = np.add(self.center[0], self.radius)
        self.min_normal_stress = np.subtract(self.center[0], self.radius)
        self.max_shear_stress = self.radius.copy()

        self.stress_state_values = {"Center": self.center,
                                    "Radius": self.radius,
                                    "Maximum normal stress": self.max_normal_stress,
                                    "Minimum normal stress": self.min_normal_stress,
                                    "Maximum shear stress": self.max_shear_stress}


    def disp_stress_state(self):
        """Display stress state values."""

        print("\nInitial stress state of a point:")
        for k, v in self.initial_values.items():
            print(f"{k.title()}: {round(v, 2)}")
        
        print("\nStress values for the given stress element are:")
        for k, v in self.stress_state_values.items():
            print(f"{k}: {np.round(v, 2)}")
    

    def plot_msc(self):
        """
        Plot 2D Mohr stress circle.
        
        Return: A 2D Mohr stress circle.
        """

        # Initialization of local variables for plotting a circle
        radians = np.linspace(0, 360, 361) * (2 * np.pi / 360)
        sigmapts = self.center[0] + self.radius * np.cos(radians)           # normal stress coordinates for plotting a circle
        taupts = self.radius * np.sin(radians)                           # shear stress coordinates for plotting a circle

        # Creating a Figure canvas and Axes
        figure = plt.figure(num="2D Mohr stress circle", figsize=(5.5, 5), dpi=100)
        axes = figure.add_subplot(111)
        
        axes.plot(sigmapts, taupts, "#497DD1")  # plot a circle
        axes.plot([self.sigmax, self.center[0], self.sigmay], [self.shear_stress, self.center[1], -self.shear_stress], color="red", marker=".")
        
        # customizing the plot
        font = {
            "family": "Times New Roman",
            "size": 11,
            "color": "black"
        }

        axes.grid()
        axes.set_xlabel(r"$\sigma$", fontdict=font)
        axes.set_ylabel(r"$\tau$", fontdict=font)
        axes.set_title("Mohr stress circle", fontdict=font, fontsize=12)
        
        
        # locating principal normal stresses and maximum shear stress on the Mohr circle
        offset = 1
        axes.text(self.max_normal_stress + offset, self.center[1], fr"$\sigma_1$ = {np.round(self.max_normal_stress, 2)}", fontdict=font)
        axes.text(self.min_normal_stress + offset, self.center[1], fr"$\sigma_2$ = {np.round(self.min_normal_stress, 2)}", fontdict=font)
        axes.text(self.center[0], self.max_shear_stress + offset, r"$\tau_{max}$ = " + str(np.round(self.max_shear_stress, 2)), fontdict=font)
        axes.text(self.center[0], self.center[1] + offset, f"C({int(self.center[0])}, {int(self.center[1])})", ha="center", fontdict=font)

        plt.tight_layout()
        plt.show()
        plt.close(fig="all")



"""
Example:

Plot a 2D Mohr stress circle for a stress element with normal stresses of 90 MPa and -60 MPa
in the horizontal and vertical directions respectively, and a shear stress of 20 MPa.
"""

circle = mohr_stress_circle(90, -60, 20)