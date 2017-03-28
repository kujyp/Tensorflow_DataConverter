import numpy as np


def labels_to_binary(labels):
    nOfLabels = max(labels)+1
    lengthOfLabels = labels.shape[0]
    binary_labels = np.zeros([lengthOfLabels,nOfLabels], dtype='uint8')
    binary_labels[range(lengthOfLabels), labels] = 1
    return binary_labels