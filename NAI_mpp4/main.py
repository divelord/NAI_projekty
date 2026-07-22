import sys


def load_from_file(filename: str):
    data = []
    with open(filename, 'r', encoding="utf-8") as file:
        file.readline()
        for line in file:
            data.append(line.strip().split(";"))
    return data


def train(train_data: list):
    all_observations = len(train_data)
    decision_counts = {}

    for obs in train_data:
        decision = obs[-1]
        decision_counts[decision] = decision_counts.get(decision, 0) + 1

    num_of_attr = len(train_data[0]) - 1
    unique_attr = [set() for _ in range(num_of_attr)]

    for obs in train_data:
        for attr in range(num_of_attr):
            unique_attr[attr].add(obs[attr])

    return all_observations, decision_counts, num_of_attr, unique_attr


def classify(obs: list, train_data: list, all_observations: int, decision_counts: dict, num_of_attr: int, unique_attr: list):
    probabilities = {}

    for current_class, class_count in decision_counts.items():
        probability = class_count / all_observations

        for i in range(num_of_attr):
            attr_count = 0

            for train_obs in train_data:
                if train_obs[i] == obs[i] and train_obs[-1] == current_class:
                    attr_count += 1

            unique_values = len(unique_attr[i])

            if attr_count == 0:
                probability *= 1 / (class_count + unique_values)
            else:
                probability *= attr_count / class_count

        probabilities[current_class] = probability

    return max(probabilities, key=probabilities.get)


def input_new_data(train_data: list, all_observations: int, decision_counts: dict, num_of_attr: int, unique_attr: list):
    print("\n---Testowy interfejs---\n")

    print(f"Podaj wartości atrybutów do klasyfikacji (liczba atrybutów do podania: {num_of_attr})")
    print("Wartości muszą być oddzielone przecinkami")
    print("Aby zakończyć program wciśnij 'q'")

    while True:
        user_input = input("Wprowadź dane: ")

        if user_input == "q":
            break

        if not user_input:
            print("Wprowadź poprawne dane")
            continue

        obs = [attr.strip() for attr in user_input.split(",")]

        if len(obs) != num_of_attr:
            print(f"Podaj {num_of_attr} dane")
            continue

        decision = classify(obs, train_data, all_observations, decision_counts, num_of_attr, unique_attr)
        print(f"{obs[:num_of_attr]}: {decision}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <bayes_train.csv> <bayes_test.csv>")
        sys.exit(1)

    train_data = load_from_file(sys.argv[1])
    test_data = load_from_file(sys.argv[2])

    all_observations, decision_counts, num_of_attr, unique_attr = train(train_data)

    for obs in test_data:
        decision = classify(obs, train_data, all_observations, decision_counts, num_of_attr, unique_attr)
        print(f"{obs[:num_of_attr]}: {decision}")

    input_new_data(train_data, all_observations, decision_counts, num_of_attr, unique_attr)


if __name__ == '__main__':
    main()
