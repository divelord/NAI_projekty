# Projekt programistyczny 1

Celem jest napisanie programu, który pobiera następujące argumenty:

- K – dodatnia liczba naturalna będąca parametrem k-NN. 
- Train-set – nazwa pliku zawierającego zbiór treningowy w postaci CSV. 
- Test-set – nazwa pliku zawierającego zbiór testowy w postaci CSV. 

Program ma dokonać klasyfikacji k-NN wszystkich obserwacji z pliku test-set na podstawie pliku 
train-set, a także podać dokładność (accuracy) tej klasyfikacji. 

Program ma też dostarczać testowy interfejs (niekoniecznie graficzny), który umożliwia podawanie 
przez użytkownika pojedynczych wektorów do klasyfikacji i podaje ich etykietę k-NN na podstawie 
train-set. 

Należy przetestować program na danych iris, po uprzednim podzieleniu go na 105 treningowych 
irysów (po 35 z każdej klasy) oraz 45 testowych.