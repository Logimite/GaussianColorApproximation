import numpy as np
import matplotlib.pyplot as plt

RGB = []
alphaList = [0.362, 1.056, -0.065, 0.821, 0.286, 1.217, 0.681]
betaList = [442.0, 599.8, 501.1, 568.8, 530.9, 437.0, 459.0]
gammaList = [0.0624, 0.0264, 0.0490, 0.0213, 0.0613, 0.0845, 0.0385]
deltaList = [0.0374, 0.0323, 0.0382, 0.0247, 0.0322, 0.0278, 0.0725]

def xyzToRGB(xyz):
    transformation_matrix = np.array([
        [3.2406, -1.5372, -0.4986],
        [-0.9689, 1.8758, 0.0415],
        [0.0557, -0.2040, 1.0570]
    ])
    rgb = np.dot(transformation_matrix, xyz)
    whited = np.dot(rgb, [0.94811, 1, 1.08883])
    return whited

def wavelengthToRGB(wavelength):
    xVal = 0
    yVal = 0
    zVal = 0
    for x in range (2):
        xVal += alphaList[x]*np.exp((-1/2)*(wavelength-betaList[x])*((wavelength-betaList[x]) if gammaList[x] < 0 else deltaList[x]))**2
    for y in range (1):
        yVal += alphaList[y+3]*np.exp((-1/2)*(wavelength-betaList[y+3])*((wavelength-betaList[y+3]) if gammaList[y+3] < 0 else deltaList[y+4]))**2
    for z in range (1):
        zVal += alphaList[z+5]*np.exp((-1/2)*(wavelength-betaList[z+5])*((wavelength-betaList[z+5]) if gammaList[z+5] < 0 else deltaList[z+6]))**2
    return [xVal, yVal, zVal]

plt.style.use('dark_background')

wavelengths = np.linspace(380, 720, 340)
colors = []

for wl in wavelengths:
    xyz = wavelengthToRGB(wl)
    rgb_linear = xyzToRGB(xyz)
    rgb_srgb = rgb_linear**2.2
    colors.append(np.clip(rgb_srgb, 0, 1))

plt.figure(figsize=(10, 2))
plt.imshow([colors], aspect='auto', extent=[380, 780, 0, 1])
plt.xlabel('Wavelength (nm)')
plt.yticks([])
plt.title('Colors (1nm intervals) vs. Wavelength')
plt.show()

print(xyzToRGB(wavelengthToRGB(395)))