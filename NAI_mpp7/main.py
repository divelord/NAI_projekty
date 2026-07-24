import random
import sys


def load_from_file(filename: str):
    data = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            data.append(line.strip())
    return data


def calculate_distance(route: list, graph: list):
    distance = 0
    for i in range(len(route)):
        current_point = route[i]
        next_point = route[(i + 1) % len(route)]
        distance += graph[current_point][next_point]
    return distance


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <traveling_salesman.txt>")
        sys.exit(1)

    tsp_data = load_from_file(sys.argv[1])

    n = int(tsp_data[0])

    graph = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for i in tsp_data[1:]:
        parts = i.split()
        v1 = int(parts[0])
        v2 = int(parts[1])
        d = int(parts[2])
        graph[v1][v2] = d
        graph[v2][v1] = d

    current_route = list(range(n))
    random.shuffle(current_route)
    current_distance = calculate_distance(current_route, graph)

    print(f"Trasa początkowa: {current_route}")
    print(f"Długość: {current_distance}")
    print()

    while True:
        best_route = current_route[:]
        best_distance = current_distance

        for i in range(n):
            for j in range(i + 1, n):
                route = current_route[:]
                route[i], route[j] = route[j], route[i]
                route_distance = calculate_distance(route, graph)

                if route_distance < best_distance:
                    best_distance = route_distance
                    best_route = route

        if best_distance < current_distance:
            current_distance = best_distance
            current_route = best_route

            print(f"Znaleziono lepszą trasę: {current_route}")
            print(f"Długość: {current_distance}")
            print()
        else:
            print("Osiągnięto lokalne optimum\n")
            print(f"Najlepsza trasa: {current_route}")
            print(f"Długość: {current_distance}")
            break


if __name__ == "__main__":
    main()
