import os


def process_text(text: str):
    text_lower = text.lower()
    letter_list = [0] * 26
    letters_count = 0

    for ch in text_lower:
        if "a" <= ch <= "z":
            index = ord(ch) - ord("a")
            letter_list[index] += 1
            letters_count += 1

    if letters_count > 0:
        for i in range(len(letter_list)):
            letter_list[i] /= letters_count

    return letter_list


def load_data(data_dir: str):
    train_data = []
    languages = [main_dir for main_dir in os.listdir(data_dir)]

    for lang in languages:
        lang_dir = os.path.join(data_dir, lang)

        for file_name in os.listdir(lang_dir):
            if file_name.endswith(".txt"):
                file_path = os.path.join(lang_dir, file_name)

                with open(file_path, "r", encoding="utf-8") as file:
                    vector = process_text(file.read())
                    train_data.append((vector, lang))

    return train_data


def input_new_text(perceptrons: dict):
    print("\n---Testowy interfejs---\n")

    print("Podaj tekst do rozpoznania")
    print("Aby zakończyć program wpisz 'q'")

    while True:
        text = input("Wprowadź tekst: ")

        if text == "q":
            break

        if not text:
            print("Tekst nie może być pusty")
            continue

        vector = process_text(text)
        predicted_language = None
        max_val = float("-inf")

        for lang, perceptron in perceptrons.items():
            value = perceptron.maximum_selector(vector)

            if value > max_val:
                max_val = value
                predicted_language = lang

        print(f"Rozpoznany język: {predicted_language}")
