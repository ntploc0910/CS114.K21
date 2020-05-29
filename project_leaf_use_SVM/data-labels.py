import numpy as np
import skimage
from skimage import feature
from imutils import paths

import random
import cv2
import h5py

class HOG:
    def __init__(self, orientations=12, pixelsPerCell=(4, 4), cellsPerBlock=(2, 2), normalize=True):
        # store the number of orientations, pixels per cell, cells per block, and
        # whether normalization should be applied to the image
        self.orientations = orientations
        self.pixelsPerCell = pixelsPerCell
        self.cellsPerBlock = cellsPerBlock
        self.normalize = normalize

    def describe(self, image):
        # compute Histogram of Oriented Gradients features for scikit-image < 0.13
        if int(skimage.__version__.split(".")[1]) < 13:
            
            hist = feature.hog(image, orientations=self.orientations, pixels_per_cell=self.pixelsPerCell,
                               cells_per_block=self.cellsPerBlock, transform_sqrt=self.normalize)

        # otherwise comput Histogram of Oriented Gradients features for scikit-image >= 0.13
        else:
            hist = feature.hog(image, orientations=self.orientations, pixels_per_cell=self.pixelsPerCell,
                               cells_per_block=self.cellsPerBlock, transform_sqrt=self.normalize, block_norm="L1")

        hist[hist < 0] = 0

        # return the histogram
        return hist
# hàm lưu lại đặc trưng và nhãn vào 1 file
class PROJECT:
def save_featured_labels(data, labels, path, datasetName, writeMethod="w"):
    # open the database, create the dataset, write the data and labels to dataset,
    # and then close the database
    db = h5py.File(path, writeMethod)
    dataset = db.create_dataset(datasetName, (len(data), len(data[0]) + 1), dtype="float")
    dataset[0:len(data)] = np.c_[labels, data]
    db.close()
def load_dataset(path, datasetName):
    # open the database, grab the labels and data, then close the dataset
    db = h5py.File(path, "r")
    (labels, data) = (db[datasetName][:, 0], db[datasetName][:, 1:])
    db.close()

    # return a tuple of the data and labels
    return (data, labels)

arr_featured = []
arr_labels = []
#load dataset
trnPaths = list(paths.list_images("dataset"))
trnPaths = random.sample(trnPaths, int(len(trnPaths)))
hog = HOG(orientations=12, pixelsPerCell=(4, 4), cellsPerBlock=(2, 2), normalize=True)
for i in trnPaths:
    IMG = cv2.imread(i, 0)
    IMG = cv2.resize(src=IMG, dsize=(232, 413))
    featured = hog.describe(IMG)
    imageID = i[i.rfind("_") + 1:].replace(".jpg", "")
    imageID = int(imageID)
    arr_labels.append(int(imageID/20) + 1)
    arr_featured.append(featured)
save_featured_labels(arr_featured, arr_labels, "output/leaf/leaf_features.hdf5","featured")
        
