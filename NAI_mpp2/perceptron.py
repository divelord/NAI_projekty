class Perceptron:
    def __init__(self, weights: list, threshold: float):
        self.weights = weights
        self.threshold = threshold
        self.attr_count = len(self.weights)

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
