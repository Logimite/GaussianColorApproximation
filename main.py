import numpy as np
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
    rgb = np.clip(rgb, 0, 1)
    rgb_255 = (rgb * 255).astype(int)
    return rgb_255

def wavelengthToRGB(wavelength):
    xVal = 0
    yVal = 0
    zVal = 0
    for x in range (0, 2):
        xVal += alphaList[x]**((-1/2)*(wavelength-betaList[x])*((wavelength-betaList[x]) if gammaList[x] < 0 else deltaList[x]))**2
    for y in range (0, 1):
        yVal += alphaList[y]**((-1/2)*(wavelength-betaList[y+4])*((wavelength-betaList[y+4]) if gammaList[y+4] < 0 else deltaList[y+4]))**2
    for z in range (0, 1):
        zVal += alphaList[z]**((-1/2)*(wavelength-betaList[y+5])*((wavelength-betaList[y+5]) if gammaList[y+5] < 0 else deltaList[y+5]))**2
    return [xVal, yVal, zVal]

print(xyzToRGB(wavelengthToRGB(1700)))