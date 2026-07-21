# Specyfikacja programu "Jednowarstwowa sieć neuronowa":

Dane wejściowe (należy samemu przygotować):

1. Stworzyć zadany katalog na dane.

2. W zadanym katalogu tworzymy kilka (K=3) podkatalogów 
nazwanych nazwami języków (np. czeski, slowacki, ...)

3. W każdym z nich umieszczamy po kilka tekstów
trenujących ściągniętych np. z Wikipedii w odpowiednich językach (w alfabetach łacińskich).
(Z praktyki wynika, że wystarcza nawet mniej niż 10 tekstów uczących dla każdego języka, 
ale długości chociaż ze 2 akapity)

4. W momencie uruchomienia sieć perceptronów będzie używała tych tekstów jako danych trenujących.

## Opis programu:

Użyjemy 1-warstwowej sieci neuronowej do klasyfikowania języków
naturalnych tekstów.

Bierzemy dokument w dowolnym języku (w alfabecie łacińskim) z pliku ".txt",
wyrzucamy wszystkie znaki poza literami alfabetu angielskiego (ASCII) i
przerabiamy na 26-elementowy wektor proporcji liter (czyli: jaka jest
proporcja 'a', 'b', etc.)

Okazuje się, że taki wektor rozkładu znaków wystarcza do rozróżniania
języka naturalnego dokumentu tekstowego, nawet dla tak podobnych języków,
jak np. czeski i słowacki.

Tworzymy więc 1 warstwę K perceptronów (gdzie K to liczba języków) 
i uczymy każdy perceptron rozpoznawania "jego" języka.

Uczenie perceptronów przebiega jak w poprzednim projekcie, tzn. z dyskretną (0-1) funkcją aktywacji.

Mając wyuczony każdy z perceptronów, klasyfikacji do jednej z K klas dokonujemy, używając maximum selector 
(zdjąć dyskretną funkcję aktywacji) i normalizować zarówno wektor wag, jak i wejść.

UWAGA: przy normalizacji można użyć miary euklidesowej. 
Normalizując wektor wag, nie dokładamy do niego parametru progu (theta).

Zapewnić okienko tekstowe do testowania: po nauczeniu wklejamy dowolny
nowy tekst w danym języku i sprawdzamy, czy sieć prawidłowo go klasyfikuje.

Oczywiście w momencie pisania programu nie powinno być wiadome ile i jakie
będą języki. 




