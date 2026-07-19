import random
import sys

from perceptron import Perceptron


def load_from_file(filename: str):
    data = []
    with open(filename, 'r', encoding="utf-8") as file:
        file.readline()
        for line in file:
            data.append(line.strip().split(","))
    return data


def input_new_vector(perceptron: Perceptron, species_dict: dict):
    print("\n---Testowy interfejs---\n")

    print("Podaj pojedyńczy wektor do klasyfikacji")
    print("Wartości muszą być oddzielone przecinkami")
    print("Aby zakończyć program wpisz 'q'")

    while True:
        vector_to_classify = input("\nPodaj wektor do klasyfikacji: ")

        if vector_to_classify == "q":
            break

        try:
            vector = [float(x) for x in vector_to_classify.split(",")]

            if len(vector) != perceptron.attr_count:
                print(f"Wektor powinien mieć {perceptron.attr_count} atrybutów")
                continue

            net = perceptron.calculate_net(vector)
            result = list(species_dict.keys())[net]
            print(f"Decyzja: {result}")

        except ValueError:
            print("[Error] Wprowadź poprawne dane")


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <a> <iris_train.csv> <iris_test.csv>")
        return

    a = float(sys.argv[1])
    train_set = load_from_file(sys.argv[2])
    test_set = load_from_file(sys.argv[3])

    unique_species = sorted(list(set(sp[-1] for sp in train_set)))
    species_dict = {unique_species[0]: 0, unique_species[1]: 1}

    attr_count = len(train_set[0]) - 1
    weights = [random.uniform(-1, 1) for _ in range(attr_count)]
    thresholds = random.uniform(-1, 1)

    perceptron = Perceptron(weights, thresholds)

    epochs = 1000

    for epoch in range(1, epochs + 1):
        random.shuffle(train_set)
        errors = 0

        for train_vector in train_set:
            input_vector = [float(x) for x in train_vector[:-1]]
            d = species_dict[train_vector[-1]]
            y = perceptron.calculate_net(input_vector)

            if d != y:
                perceptron = perceptron.apply_delta_rule(input_vector, d, y, a)
                errors += 1

        if errors == 0:
            print(f"Osiągnięto 100% poprawność w epoce {epoch}")
            break
    else:
        correct_prediction = 0

        for train_vector in train_set:
            input_vector = [float(x) for x in train_vector[:-1]]
            d = species_dict[train_vector[-1]]
            y = perceptron.calculate_net(input_vector)

            if d == y:
                correct_prediction += 1

        train_accuracy = (correct_prediction / len(train_set)) * 100
        print(f"Ukończono trenowanie z poprawnością {train_accuracy:.2f}%")

    correct = 0
    correct_for_species = {sp: {"correct": 0, "total": 0} for sp in unique_species}

    for test_vector in test_set:
        input_vector = [float(x) for x in test_vector[:-1]]
        d = species_dict[test_vector[-1]]
        y = perceptron.calculate_net(input_vector)

        label = test_vector[-1]
        correct_for_species[label]["total"] += 1

        if d == y:
            correct += 1
            correct_for_species[label]["correct"] += 1

    accuracy = correct / len(test_set) * 100
    print(f"Dokładność: {accuracy:.2f}%")

    for sp in correct_for_species:
        species_accuracy = (correct_for_species[sp]["correct"] / correct_for_species[sp]["total"]) * 100
        print(f"Dokładność dla {sp}: {species_accuracy:.2f}%")

    input_new_vector(perceptron, species_dict)


if __name__ == "__main__":
    main()
