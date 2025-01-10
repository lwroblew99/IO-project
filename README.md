
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
