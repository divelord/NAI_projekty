import sys


def load_from_file(filename: str):
    data = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            data.append(line.strip())
    return data


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <knapsack.txt>")
        sys.exit(1)

    knapsack_data = load_from_file(sys.argv[1])

    k, n = [int(x) for x in knapsack_data[0].split()]
    values = [int(x) for x in knapsack_data[1].split(",")]
    weights = [int(x) for x in knapsack_data[2].split(",")]

    binary_vector = [0] * n

    best_value = float("-inf")
    best_vector = list(binary_vector)

    total_combinations = 2 ** n
    log_frequency = max(1, total_combinations // 20)

    for i in range(total_combinations):
        current_value = 0
        current_weight = 0

        for j in range(n):
            if binary_vector[j] == 1:
                current_value += values[j]
                current_weight += weights[j]

        if current_weight <= k and current_value > best_value:
            best_value = current_value
            best_vector = list(binary_vector)

            print(f"Znaleziono nowy najlepszy wektor")
            print(f" - Wartość: {best_value}")
            print(f" - Wektor: {best_vector}")
            print()

        if i % log_frequency == 0 and i > 0:
            print(f"Sprawdzono {round(i / total_combinations * 100, 2)}% wszystkich kombinacji \n")

        for j in range(n - 1, -1, -1):
            if binary_vector[j] == 0:
                binary_vector[j] = 1
                break
            else:
                binary_vector[j] = 0

    print(f"Najlepszy znaleziony wektor:\n{best_vector}")
    print(f" - Wartość: {best_value}")
    print(f" - Waga: {sum(weights[x] for x in range(n) if best_vector[x] == 1)}")


if __name__ == "__main__":
    main()
