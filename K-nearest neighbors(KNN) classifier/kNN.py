import math
def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1) - 1):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def get_neighbors(train, test, k):
    distances = []
    for train_row in train:
        dist = euclidean_distance(test, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = [dist[0] for dist in distances[:k]]
    return neighbors

def predict_class(neighbors):
    class_votes = {}
    for neighbor in neighbors:
        class_label = neighbor[-1]
        if class_label in class_votes:
            class_votes[class_label] += 1
        else:
            class_votes[class_label] = 1
    sorted_votes = sorted(class_votes.items(), key=lambda x: x[1], reverse=True)
    return sorted_votes[0][0]

def load_dataset(filename):
    dataset = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = lines[1:]
        for line in lines:
            line = line.strip()
            if not line:
                continue
            row = line.split(',')
            if len(row) == 4:  
                dataset.append([float(row[0]), float(row[1]), float(row[2]), row[3]])
    return dataset

dataset = load_dataset('/content/Height.txt')
test_point = [1.69,79,37] 
k = int(input());
neighbors = get_neighbors(dataset, test_point, k)
prediction = predict_class(neighbors)
print(f"The predicted class for the test point {test_point} is: {prediction}")
