# PP2

## struktura opinni w serwisie ceneo.pl :   https://www.ceneo.pl/ 
| składowa opinni |selektor|nazwa zmiennej|typ danych|
|-----------------|--------|--------------|----------|
|opinia|div.js_product-review|opinion||
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id||
|autor opinii|span.user-post__author-name|author||
|rekomendacja autora|span.user-post__author-recomendation > em|recomendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opininii|div.user-post__text|content||
|lista zalet|div\[class$=positives\] ~ div.review-feature__item|pros||
|lista wad|div\[class$=negatives\] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|button.vote-yes > span|useful||
|dla ilu osób nieprzydatna|button.vote-no > span|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)\["datetime"\]|published||
|data zakupu produktu|span.user-post__published > time:nth-child(2)\["datetime"\]|purchased||

## Etapy pracy nad projektem  strukturalnym
1. Pobranie elementów pojedyńczej opinii do niezależnych zmiennych
2. Zapisanie wszystkich elementów pojeduńczej opinnii do jednej zmiennej \(słownink\)
3. Pobranie wszystkich opinii z pojedyńczej strony do słowników i dodanie ich do listy
4. Pobranie wszystkich opinii z wszystkich stron i zapisanie ich do pliku .json
5. Dodanie możliwości podania id produktu przez użytkownika za pomocą klawiatury 
6. Refaktoryzacja \(optymalizacja\) kodu:
    a. utworzenie funkcji do pobierania składowych strony html
    b. utworzenie słownika opisującego strukturą opinii wraz z selektorami poszczególnych elementów
    c.zamiana instrukcji pobierającyc składowe opinii do pojedynczych zmiennych i tworzących z nich słownik na wyrażenie słownikowe \(dictionary comprehension\)
    tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów
7. analiza opinii o wybranym produkcie
    1. wczytanie wszystkich opinii o wskazanym produkcie do obiektu dataframe
    2. wyliczenie podstawowych statystyk na podstawie opinii
        1. liczba wszystkich opinii o produkcie 
        2. liczba opinii z zaletami 
        3. liczba opinii z wadami 
        4. średnia ilość gwiazdek
    3. przygotowanie wykresów na podstawie zawartośći opinii 
        1. udział poszczególnymh rekomendacji w ogólnej liczbie opinii
        2. histogram częstości występowania poszczególnych ocen (liczby gwiazdek)
