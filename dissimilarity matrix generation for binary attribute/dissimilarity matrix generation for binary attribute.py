import numpy as np
from scipy.spatial.distance import pdist, squareform
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import pandas as pd
data_frame=pd.read_csv("/content/DataSet1.csv")
print("data_frame")
print(data_frame)
data=data_frame.to_numpy()

print(data)
nominal_indices = [1]

onehot_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
nominal_data_encoded = onehot_encoder.fit_transform(data[:, nominal_indices])
print("nominal_data_encoded")
print(nominal_data_encoded)

ordinal_indices = [2]

ordinal_encoder = OrdinalEncoder()
ordinal_data_encoded = ordinal_encoder.fit_transform(data[:, ordinal_indices])
print("ordinal_data_encoded")
print(ordinal_data_encoded)

numeric_indices = [3]

numeric_data = data[:, numeric_indices].astype(float)

preprocessed_data = np.hstack((nominal_data_encoded, ordinal_data_encoded, numeric_data))
print("preprocessed_data")
print(preprocessed_data)


pairwise_distances = pdist(preprocessed_data, metric='euclidean')

dissimilarity_matrix = squareform(pairwise_distances)
print("dissimilarity_matrix")
print(dissimilarity_matrix)

