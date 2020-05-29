# import the necessary packages
from __future__ import print_function

from sklearn.metrics import accuracy_score

from sklearn.svm import SVC
import numpy as np
import argparse
import pickle
import h5py
from sklearn.model_selection import train_test_split

def load_dataset(path, datasetName):
    # open the database, grab the labels and data, then close the dataset
    db = h5py.File(path, "r")
    (labels, data) = (db[datasetName][:, 0], db[datasetName][:, 1:])
    db.close()
    # return a tuple of the data and labels
    return (data, labels)
# load the configuration file and the initial dataset
print("[INFO] loading dataset...")
(data, labels) = load_dataset("output/leaf/leaf_features.hdf5", "featured")

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=130)


# train the classifier
print("[INFO] training classifier...")
model = SVC(kernel="linear", C=0.01, probability=False, random_state=42)
model.fit(x_train, y_train)


# dump the classifier to file
print("[INFO] dumping classifier...")
f = open("output/leaf/model_with_hn.cpickle", "wb")
f.write(pickle.dumps(model))
f.close()

y_pred = model.predict(x_test)
print("Accuracy of SVM: %.2f %%" % (100 * accuracy_score(y_test, y_pred)))
