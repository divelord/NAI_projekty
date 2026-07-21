import math


class Perceptron:
    def __init__(self, weights: list, threshold: float):
        self.weights = weights
        self.threshold = threshold

    def calculate_net(self, input_vector: list):
        net = 0

        for i in range(len(input_vector)):
            net += self.weights[i] * input_vector[i]

        return 1 if net - self.threshold >= 0 else 0

    def apply_delta_rule(self, input_vector: list, d: int, y: int, alpha: float):
        new_weights = [0.0] * len(self.weights)
        weight_diff = d - y

        for i in range(len(input_vector)):
            new_weights[i] = self.weights[i] + weight_diff * alpha * input_vector[i]

        new_threshold = self.threshold - weight_diff * alpha

        return Perceptron(new_weights, new_threshold)

    def maximum_selector(self, input_vector: list):
        normalized_weights = self.normalize_vector(self.weights)
        normalized_input_vector = self.normalize_vector(input_vector)

        return sum(w * v for w, v in zip(normalized_weights, normalized_input_vector))

    @staticmethod
    def normalize_vector(vector: list):
        vector_length = math.sqrt(sum(x ** 2 for x in vector))

        if vector_length == 0.0:
            return vector

        return [x / vector_length for x in vector]
