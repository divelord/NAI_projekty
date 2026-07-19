# Projekt programistyczny 2 

Celem jest napisanie programu, który pobiera następujące argumenty: 

- a – stała uczenia. 
- Train-set – nazwa pliku zawierającego zbiór treningowy w postaci CSV. 
- Test-set – nazwa pliku zawierającego zbiór testowy w postaci CSV. 

Należy zaimplementować perceptron, który wykorzystując podany train-set oraz stałą uczenia, 
nauczy się rozpoznawać irysy. Po nauce, program powinien podać procent poprawnie rozpoznanych 
kwiatów z test-setu. Należy również wypisać procenty dla poszczególnych gatunków. 

Program ma też dostarczać testowy interfejs (niekoniecznie graficzny), który umożliwia (zapętlone) 
podawanie przez użytkownika pojedynczych wektorów do klasyfikacji. 

UWAGA! Program powinien działać poprawnie dla dowolnej liczby atrybutów. 

Przetestować program na danych iris, pomniejszonych o jeden gatunek (należy wybrać który) tak, aby 
zostało 100 kwiatów – po 50 z każdego pozostałego gatunku. Dane te należy podzielić na zbiór 
treningowy oraz testowy (35 do zbioru treningowego, a 15 do zbioru testowego z każdego gatunku).