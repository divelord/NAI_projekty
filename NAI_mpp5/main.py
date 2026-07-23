import random
import sys


def load_from_file(filename: str):
    data = []
    with open(filename, "r", encoding="utf-8") as file:
        file.readline()
        for line in file:
            obs = line.strip().split(",")
            num_list = [float(x) for x in obs[:-1]]
            data.append(num_list)
    return data


def calculate_distance(v1: list, v2: list):
    distance = 0
    for i in range(len(v1)):
        distance += (v1[i] - v2[i]) ** 2
    return distance


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <k> <iris.csv>")
        sys.exit(1)

    k = int(sys.argv[1])
    iris_data = load_from_file(sys.argv[2])

    centroids = random.sample(iris_data, k)

    print("Początkowe centroidy: ")
    for c in centroids:
        print(f" - {c}")
    print()

    iteration = 0

    while True:
        iteration += 1
        sum_of_squared_distances = 0.0
        clusters = [[] for _ in range(k)]

        for point in iris_data:
            distances = [calculate_distance(point, c) for c in centroids]
            min_distance = min(distances)

            cluster_id = distances.index(min_distance)
            clusters[cluster_id].append(point)

            sum_of_squared_distances += min_distance

        print(f"Iteracja: {iteration}")
        print(f" Suma kwadratów odległości: {round(sum_of_squared_distances, 2)}")
        for i in range(len(clusters)):
            cluster = clusters[i]
            print(f" - Grupa {i + 1}: {len(cluster)} punktów")
        print()

        new_centroids = []

        for cluster in clusters:
            if len(cluster) > 0:
                new_centroid = []

                for i in range(len(cluster[0])):
                    point_sum = 0.0

                    for point in cluster:
                        point_sum += point[i]

                    new_centroid.append(point_sum / len(cluster))

                new_centroids.append(new_centroid)
            else:
                new_centroids.append(centroids[len(new_centroids)])

        if new_centroids == centroids:
            print(f"Przydzielono na {k} grupy")
            break
        else:
            centroids = new_centroids


if __name__ == "__main__":
    main()
