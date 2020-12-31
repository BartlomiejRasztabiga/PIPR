# Zadania przed laboratorium

## 1. Dad's jokes

Napisz program z prostym interfejsem który umożliwi pobieranie losowych dad jokes'ów oraz dopisywanie najlepszych - wybranych przez użytkownika do bazy danych.

- Interfejs powinien wyświetlać losowy dad jokes pobrany za pomocą api [https://icanhazdadjoke.com/api](https://icanhazdadjoke.com/api), a następnie pytać czy żart jest na odpowiednim poziomie i powinien zostać dopisany do bazy. 
- Bazę żartów proszę zrealizowana jako plik tekstowy. Proszę dopisywać od nowej linijki tylko treść tekstową żartu wyciągniętą z odpowiedzi zapytania. 
- Proszę zwrócić uwagę na to żeby po ponownym uruchomieniu aplikacji, nowe żarty nie nadpisywały tych poprzednich. (Podpowiedź - tryb otwierania pliku append "a+")

Przykładowe zapytanie do API:
```
curl -H "Accept: application/json" https://icanhazdadjoke.com/
```

Dla zainteresowanych, polecam zabawę z innymi publicznie dostępnymi API. Ich spis mogą Państwo znaleźć tutaj: [link](https://github.com/public-apis/public-apis)

## 2. Histogram

Napisz funkcję która obliczy i wyświetli histogram wartości podanych w liście. Proszę zadbać o to żeby wykres był generowany w sposób czytelny, posiadał odpowiednią liczbę "kubełków", opis osi oraz tytuł.

Do generowania histogramów w bibliotece matplotlib służy funkcja [hist](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.hist.html).

Poprawność generowania histogramu mogą Państwo sprawdzić wizualizując rozkład znanych funkcji (np. rozkład normalny z różnymi wartościami *mu* i *sigma* czy jednostajny z zadanego przedziału). Do generowania odpowiednich danych proszę wykorzystać generator z modułu *random*. 

Przykład generowania danych:

```
n_samples = 100
uniform_data = [random.uniform(-3, 3) for _ in range(n_samples)]
gauss_data = [random.gauss(2, 3) for _ in range(n_samples)]
```
