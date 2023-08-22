import pandas as pd
data=pd.read_csv("/content/Toyota.csv",usecols = ['Price','Age','KM'])
print(data)


copy_data = data.copy()
copy_data.fillna(0, inplace=True)


#replace all string data objects to iteger bject
from sklearn.preprocessing import LabelEncoder

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Iterate through columns and apply label encoding to each string column
for column in copy_data.columns:
    if copy_data[column].dtype == 'object':  # Check if the column contains strings
        copy_data[column] = label_encoder.fit_transform(copy_data[column])




# apply normalization techniques
def normalize_column(column):
    min_val = column.min()
    max_val = column.max()
    normalized_column = (column - min_val) / (max_val - min_val)
    return normalized_column

# view normalized data
copy_data["Price"]=normalize_column(copy_data["Price"]);
copy_data["Age"]=normalize_column(copy_data["Age"]);
copy_data["KM"]=normalize_column(copy_data["KM"]);
display(copy_data)







copy_data2 = data.copy()
copy_data2.fillna(0, inplace=True)

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
for column in copy_data2.columns:
    if copy_data2[column].dtype == 'object':
        copy_data2[column] = label_encoder.fit_transform(copy_data2[column])


def decimal_scaling(column):
    max_val = column.max()
    j = len(str(max_val))
    normalized_column = column / (10 ** j)
    return normalized_column

copy_data2["Price"]=decimal_scaling(copy_data2["Price"]);
copy_data2["Age"]=decimal_scaling(copy_data2["Age"]);
copy_data2["KM"]=decimal_scaling(copy_data2["KM"]);
display(copy_data2)



copy_data3 = data.copy()
copy_data3.fillna(0, inplace=True)

import statistics as st
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
for column in copy_data3.columns:
    if copy_data3[column].dtype == 'object':
        copy_data3[column] = label_encoder.fit_transform(copy_data3[column])

def z_score(column):
    mean = st.mean(column)
    std_dev = st.stdev(column)
    normalized_column = abs(column - mean) / std_dev
    return normalized_column

copy_data3["Price"]=z_score(copy_data3["Price"]);
copy_data3["Age"]=z_score(copy_data3["Age"]);
copy_data3["KM"]=z_score(copy_data3["KM"]);
display(copy_data3)