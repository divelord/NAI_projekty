# Projekt programistyczny 7 

Celem jest stworzenie programu, który jako argument przyjmie lokalizację pliku o następującej 
strukturze: 

n

v1 v2 d 

v1 v3 d 

… 

vn-1 vn d 

gdzie: 

n – liczba miast 

v1 v2 d – odległość d pomiędzy miastami v1 i v2. 

Następnie program powinien wykorzystać algorytm wspinaczki, aby rozwiązać problem 
komiwojażera dla danych z pliku. Jako odpowiedź powinna zostać wyświetlona kolejność 
odwiedzonych miast (np. dla n=5 odpowiedzią może być 02431) oraz łączna długość tej drogi. Należy 
też w miarę działania programu, wypisywać informacje dotyczące postępu – liczba iteracji, najlepsza 
znaleziona dotąd droga itp.

UWAGA! Dopuszczalna złożoność pamięciowa wynosi O(n^2). 