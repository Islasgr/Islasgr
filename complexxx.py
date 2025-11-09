import sys
print(sys.executable)
print(sys.version)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


#complex plane??
x = np.linspace (-2, 2, 1000)
y = np.linspace (2, -2, 1000) #flippp
X, Y = np.meshgrid(x, y)
Z = X + (1j * Y)

functions = {
    "f1(z) = z": lambda z: z,
    "f2(z) = 2z + 1": lambda z: 2*z + 1,
    "f3(z) = 1^z": lambda z: 1**z,
    "f4(z) = exp(z)": lambda z: np.exp(z),
    "f5(z) = (z^3)": lambda z: z**3,
} #just whats needed - more pics on phone of other functions?



def complex_to_color(fz):
    modulus = np.abs(fz)
    argument = np.angle(fz)

    # Anglke normalized from (−π, π) to (0, 1) so like 600 degrees becomes 240
    hue = (argument + np.pi) / (2 * np.pi)

    log_mod = np.log1p(modulus) # deals with large values -found on google and copypaste icl
    brightness = log_mod / np.max(log_mod) # ???

    #create HSV image- hue, saturation=1 ( as unspecified) , brightness=scaled modulus
    hsv_image = np.stack((hue, np.ones_like(brightness), brightness), axis=-1)

    #convert to RGB 
    rgb_image = mcolors.hsv_to_rgb(hsv_image)
    return rgb_image

# Generate and display plots for each function
for name, func in functions.items():
    fz = func(Z) #plot function values over grid
    rgb_image = complex_to_color(fz) #call subroutine

    #plot 
    plt.figure(figsize=(6, 6))
    plt.imshow(rgb_image, extent=(-2, 2, -2, 2))
    plt.title(name, fontsize=14)

plt.show() 
    
