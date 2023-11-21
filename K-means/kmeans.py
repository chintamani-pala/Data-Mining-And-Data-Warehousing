import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('/content/iris.csv')  

features = data[['sepal_length', 'sepal_width']]

k = 3

kmeans = KMeans(n_clusters=k, random_state=42)
data['cluster'] = kmeans.fit_predict(features)

plt.figure(figsize=(10, 6))

colors = ['blue', 'green', 'purple']

for cluster in range(k):
    cluster_data = data[data['cluster'] == cluster]
    plt.scatter(cluster_data['sepal_length'], cluster_data['sepal_width'], label=f'Cluster {cluster + 1}', color=colors[cluster])

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=200, color='red', label='Centroids')
plt.title('K-means Clustering')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()

sse = kmeans.inertia_

print(f"Sum of Squared Errors (SSE): {sse}")
