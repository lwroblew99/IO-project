
# Serwis wspomagający pracę trenera personalnego

Nazwa skrócona: Trainer Track

Nazwa pełna: Serwis wspomagający pracę trenera personalnego

Opis: Trainer Track wspiera trenerów personalnych w analizie danych treningowych klientów
poprzez obliczanie Training Stress Score (TSS) oraz monitorowanie czasu spędzanego w
poszczególnych strefach tętna. Aplikacja oferuje wizualizacje danych oraz rekomendacje,
umożliwiające optymalizację planów treningowych.

## Prawa autorskie

Autorzy: Łucja Wróblewska, Marek Michalak

Licencja: Licencja MIT, Licencja API Strava
## Specyfikacja wymagań

Priorytet:1

Identyfikator: LM1

Logowanie

Opis: Użytkownik musi zalogować się do aplikacji za pomocą linku wygenerowanego przez ngrok.

Kategoria: Funkcjonalne

Identyfikator: LM2

Autoryzacja API Strava

Opis: Użytkownik musi zaakceptować dostęp do swoich danych z API Strava.

Kategoria: Funkcjonalne

Identyfikator: LM3 Analiza danych
(HRmax).

Kategoria: Funkcjonalne

Opis: System oblicza Training Stress Score (TSS) oraz monitoruje czas spędzony w strefach tętna

Identyfikator: LM4 Wizualizacje danych

Opis: Użytkownik otrzymuje graficzne przedstawienie wyników analizy TSS i HRmax.

Kategoria: Funkcjonalne

Identyfikator: LM5 Personalizacja planu treningu

Opis: System generuje rekomendacje na podstawie zależności między TSS a HRmax, aby pomóc
trenerowi w optymalizacji planu treningowego.

Kategoria: Funkcjonalne

Identyfikator: LM7
Historia aktywności

Opis: Przechowywanie danych o aktywnościach w MongoDB dla przyszłej analizy i wglądu.

Kategoria: Funkcjonalne

Priorytet: 2

Identyfikator: LM8
Responsywność interfejsu

Opis: Aplikacja działa poprawnie na urządzeniach mobilnych i desktopowych.

Kategoria: Pozafunkcjonalne

Priorytet: 3

Identyfikator: LM9 Wydajność 

Opis: Czas oczekiwania na odpowiedź serwera przy analizie danych nie może przekroczyć 1 sekundy

Kategoria: Pozafunkcjonalne

#Architektura systemu/oprogramowania

Architektura rozwoju

Stos technologiczny oraz narzędzia wykorzystywane podczas rozwoju aplikacji:

Nazwa technologii: Python

Przeznaczenie: Backend - obsługa serwera aplikacji (pobieranie danych dla trenera
personalnego), przetwarzanie zdarzeń webhooka. Frontend - analiza pobranych danych

Numer wersji: Python 3.10.12

Nazwa technologii: Flask

Przeznaczenie: Tworzenie API i obsługa żądań HTTP

Numer wersji: Flask 2.2.5

Nazwa technologii: MongoDB

Przeznaczenie: Przechowywanie danych użytkowników, aktywności i komentarzy

Numer wersji: MongoDB 5.0

Przykładowy punkt końcowy: /webhook

Przeznaczenie: Nasłuchiwanie zdarzeń Strava (np. nowych aktywności, usuniętych aktywności).

Narzędzia programistyczne:

PyCharm 2024.2 (Community Edition)

Postman (do testowania API oraz punktów końcowych webhook)

Ngrok (do udostępniania lokalnego serwera webhookowi podczas testów)

Debugger Flask (do monitorowania logów przy obsłudze zdarzeń webhooka)

Przeznaczenie: Nasłuchiwanie zdarzeń Strava (np. nowych aktywności, usuniętych aktywności).


Architektura uruchomieniowa

Stos technologiczny oraz narzędzia wymagane podczas działania aplikacji:

Nazwa technologii: Flask

Przeznaczenie: Hostowanie aplikacji webowej

Numer wersji: Flask 2.2.5

Nazwa technologii: webhook

Przeznaczenie: Udostępnianie lokalnego serwera w Internecie

Numer wersji: ngrok 3.1.1

Nazwa technologii: ngrok

Przeznaczenie: Udostępnianie lokalnego serwera w Internecie

Numer wersji: ngrok 3.1.1

Nazwa technologii: MongoDB

Przeznaczenie: Przechowywanie i zarządzanie danymi

Numer wersji: MongoDB 5.0

Narzędzia uruchomieniowe:

Serwer HTTP (serwer wbudowany Flask - )

Środowisko produkcyjne (macOS - Sequoia 15.1)
 
Klient Strava API (do interakcji z zewnętrznym API)

Przykładowy punkt końcowy /webhook

Żądanie POST (do odbierania zdarzeń od Strava).

Przetwarzanie danych: Każde zdarzenie jest zapisywane w bazie MongoDB (wczytanie nowej
aktywności użytkownika).
