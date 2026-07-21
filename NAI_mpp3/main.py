import random
import sys

from perceptron import Perceptron
from utils import load_data, input_new_text


def main():
    if len(sys.argv) != 3:
        print("usage: python main.py <a> <language dir>")
        sys.exit(1)

    a = float(sys.argv[1])
    lang_data = load_data(sys.argv[2])

    languages = sorted(list(set(data[1] for data in lang_data)))
    perceptrons = {}

    for lang in languages:
        weights = [random.uniform(-1, 1) for _ in range(26)]
        threshold = random.uniform(-1, 1)
        perceptrons[lang] = Perceptron(weights, threshold)

    epochs = 10000
    epoch = 0
    accuracy = 0.0

    for i in range(0, epochs):
        random.shuffle(lang_data)
        epoch += 1

        for vector, correct_lang in lang_data:
            for lang, perceptron in perceptrons.items():
                d = 1 if lang == correct_lang else 0
                y = perceptron.calculate_net(vector)

                perceptrons[lang] = perceptron.apply_delta_rule(vector, d, y, a)

        correct = 0

        for vector, correct_lang in lang_data:
            predicted_language = None
            max_val = float("-inf")

            for lang, perceptron in perceptrons.items():
                value = perceptron.maximum_selector(vector)

                if value > max_val:
                    max_val = value
                    predicted_language = lang

            if predicted_language == correct_lang:
                correct += 1

        accuracy = correct / len(lang_data)

        if accuracy == 1.0:
            break

    if accuracy == 1.0:
        print(f"Sieć nauczyła się rozpoznawać języki w 100% w {epoch} epokach")
    else:
        print(f"W {epoch} epokach sieć nauczyła się rozpoznawać języki z dokładnością {round(accuracy * 100, 2)}%")

    input_new_text(perceptrons)


if __name__ == '__main__':
    main()
