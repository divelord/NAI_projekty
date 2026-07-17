import sys

import knnClassification


def load_from_file(filename: str):
    data = []
    with open(filename, "r", encoding="utf-8") as file:
        file.readline()
        for line in file:
            data.append(line.strip().split(","))
    return data


def input_new_vector(knn: knnClassification.KNN):
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

            if len(vector) != knn.attr_count:
                print(f"Wektor powinien mieć {knn.attr_count} atrybutów")
                continue

            result = knn.classify(vector)
            print(f"Decyzja: {result}")

        except ValueError:
            print("[Error] Wprowadź poprawne dane")


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <K> <iris_train.csv> <iris_test.csv>")
        return

    k = int(sys.argv[1])
    train_set = load_from_file(sys.argv[2])
    test_set = load_from_file(sys.argv[3])

    knn = knnClassification.KNN(k, train_set)
    accuracy, poprawne = knn.calculate_accuracy(test_set)

    print(f"Poprawnie sklasyfikowano {poprawne}/{len(test_set)} ({accuracy:.2f}%)")

    input_new_vector(knn)


if __name__ == "__main__":
    main()
