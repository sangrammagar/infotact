import numpy as np

def compute_ndvi(nir, red):
    # nir, red: numpy arrays of same shape
    # Avoid division by zero
    denom = (nir + red).astype(float)
    denom[denom == 0] = 1e-6
    ndvi = (nir - red) / denom
    return ndvi

if __name__ == '__main__':
    # demo synthetic arrays
    nir = np.random.randint(1,255,(100,100))
    red = np.random.randint(1,255,(100,100))
    ndvi = compute_ndvi(nir, red)
    print('NDVI sample:', ndvi.mean())
