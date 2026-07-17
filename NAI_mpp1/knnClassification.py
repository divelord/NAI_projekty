class KNN:
    def __init__(self, k: int, train_set: list):
        self.k = k
        self.train_set = train_set
        self.attr_count = len(train_set[0]) - 1

    def calculate_distance(self, v1: list, v2: list):
        distance = 0

        for i in range(self.attr_count):
            distance += (float(v1[i]) - float(v2[i])) ** 2

        return distance

    def classify(self, test_vector: list):
        distances = []

        for train_vector in self.train_set:
            distance = self.calculate_distance(test_vector, train_vector)
            species = train_vector[-1]
            distances.append((distance, species))

        distances.sort(key=lambda x: x[0])
        nearest_neighbours = distances[:self.k]

        votes = {}

        for _, species in nearest_neighbours:
            votes[species] = votes.get(species, 0) + 1

        return max(votes, key=votes.get)

    def calculate_accuracy(self, test_set: list):
        correct = 0

        for i in test_set:
            predicted_species = self.classify(i)
            real_species = i[-1]

            if predicted_species == real_species:
                correct += 1

        accuracy = (correct / len(test_set)) * 100

        return accuracy, correct
