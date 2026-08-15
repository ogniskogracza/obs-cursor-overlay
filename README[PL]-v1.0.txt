======================================================================
                         OBS Cursor Overlay
              Niestandardowy kursor myszy dla OBS
======================================================================

Copyright (c) 2026 Rafał Modzelewski
Licensed under — see LICENSE.txt
Autor: Rafal Modzelewski
Kontakt: ogniskogracza@gmail.com
Wersja: 1.0
Obsługiwane systemy: Windows, macOS i Linux
OBS: Windows / macOS / Linux
Zaprojektowane dla: OBS Studio
Python: 3.10+
Połączenie: Lokalny WebSocket (localhost)
Uwierzytelnianie: Wyłączone
======================================================================


1. CZYM JEST OBS CURSOR OVERLAY?
======================================================================

OBS CURSOR OVERLAY to niewielka lokalna aplikacja, która wyświetla
niestandardowy kursor myszy wewnątrz źródła typu Browser Source w OBS.

Jest to przydatne podczas nagrywania lub streamowania:

    - rozgrywki na PlayStation
    - rozgrywki na PC
    - poradników
    - aplikacji desktopowych
    - prezentacji
    - demonstracji oprogramowania
    - treści edukacyjnych
    - dowolnych innych treści, w których chcesz, aby widz wyraźnie
      widział, gdzie wskazuje mysz


System działa w następujący sposób:

    1. Wykrywa system operacyjny.

    2. Odczytuje pozycję myszy komputera.

    3. Wykrywa wymiary pulpitu komputera.

    4. Konwertuje współrzędne myszy na skonfigurowaną
       rozdzielczość wyjściową OBS.

    5. Wysyła współrzędne przez lokalne połączenie WebSocket.

    6. Źródło Browser Source w OBS odbiera te współrzędne.

    7. pointer.html wyświetla wybrany kursor SVG.

    8. Kursor automatycznie znika, gdy mysz przestaje się poruszać.


Kursor widoczny dla widza jest całkowicie niezależny od zwykłego
kursora myszy systemu operacyjnego.

Zmiana pliku SVG NIE zmienia zatem normalnego kursora myszy w
Windows, macOS ani Linux.


======================================================================
2. WSPARCIE WIELOPLATFORMOWE
======================================================================

OBS CURSOR OVERLAY został zaprojektowany do działania na:

    Windows
    macOS
    Linux


Ten sam plik pointer.py jest używany na wszystkich obsługiwanych
systemach operacyjnych.

Aplikacja automatycznie wykrywa system operacyjny.

Kod Python NIE wymaga osobnych wersji, takich jak:

    pointer_windows.py
    pointer_macos.py
    pointer_linux.py


Zamiast tego pointer.py wybiera odpowiednią metodę właściwą dla
danego systemu operacyjnego podczas uruchamiania.


----------------------------------------------------------------------
2.1 WEJŚCIE MYSZY
----------------------------------------------------------------------

Wejście myszy jest obsługiwane za pomocą:

    pynput


pynput zapewnia wieloplatformowy interfejs do odczytu pozycji myszy.

Główny kod śledzenia myszy jest więc współdzielony pomiędzy
Windows, macOS i Linux.


----------------------------------------------------------------------
2.2 WYKRYWANIE EKRANU
----------------------------------------------------------------------

Wymiary ekranu komputera są wykrywane za pomocą metody właściwej
dla danego systemu operacyjnego.

Windows korzysta z API wyświetlania Windows.

macOS korzysta z dostępnych informacji o pulpicie macOS.

Linux korzysta z dostępnych informacji o pulpicie/wyświetlaczu wraz
z wieloplatformowym rozwiązaniem awaryjnym (fallback).


Wykryte wymiary ekranu są następnie używane do konwersji pozycji
myszy na rozdzielczość wyjściową OBS.


----------------------------------------------------------------------
2.3 WYŚWIETLACZE RETINA W macOS
----------------------------------------------------------------------

Wyświetlacze Retina w macOS mogą ujawniać rozróżnienie pomiędzy
logicznymi punktami wyświetlacza a fizycznymi pikselami.

Z tego powodu niektóre konfiguracje Retina mogą wymagać dodatkowego
testowania lub dostosowania.

Aplikacja została zaprojektowana tak, aby korzystać z systemu
współrzędnych udostępnianego przez system operacyjny, zamiast
stosować logikę DPI specyficzną dla Windows w systemie macOS.


Jeśli konkretna konfiguracja Retina powoduje nieprawidłowe
skalowanie lub przesunięcia, można to naprawić w kodzie wykrywania
ekranu specyficznym dla macOS, bez zmiany całej architektury.


======================================================================
3. JAK ZBUDOWANY JEST SYSTEM
======================================================================

Projekt składa się z kilku oddzielnych części.


    pointer.py
        Wieloplatformowy serwer śledzenia myszy.

        Wykrywa system operacyjny, odczytuje pozycję myszy,
        określa wymiary ekranu, konwertuje współrzędne na
        rozdzielczość wyjściową OBS i wysyła je do Browser Source.

        Normalnie NIE powinieneś edytować tego pliku.


    pointer.html
        Wizualny kursor wyświetlany przez OBS.

        Odbiera współrzędne myszy oraz konfigurację z pointer.py
        i wyświetla wybrany kursor SVG.

        Normalnie NIE powinieneś edytować tego pliku.


    cursor_config.json
        KONFIGURACJA KURSORA UŻYTKOWNIKA.

        To jest główny plik, który edytujesz, gdy chcesz:

            - zmienić aktywny kursor
            - zmienić kolor poświaty (glow)
            - zmienić intensywność poświaty
            - zmienić prędkość poświaty
            - zmienić styl poświaty (domyślnie "blur", można też
              ustawić "halo"); jeśli parametr jest pominięty,
              przyjmowany jest wybór "blur"
            - skonfigurować zachowanie poświaty dla poszczególnych
              kursorów

Przykład:
"pointers/skeleton_hand.svg": {
    "color": "rgba(49, 239, 44, 0.9)",
    "min": "40px",
    "max": "250px",
    "speed": "5s",
    "style": "halo",
    "trough": 0.55,
    "trough_opacity": 0
}


    pointer_config.json
        OGÓLNA KONFIGURACJA WSKAŹNIKA (POINTERA).

        Kontroluje:

            - szerokość wskaźnika
            - wysokość wskaźnika
            - czas trwania zanikania (fade)
            - opóźnienie automatycznego ukrywania
            - szerokość wyjściową OBS
            - wysokość wyjściową OBS
            - pozycję X czubka kursora
            - pozycję Y czubka kursora


    start_pointer.py
        Skrypt pomocniczy Python dla OBS.

        OBS ładuje ten skrypt automatycznie, a on uruchamia
        pointer.py.

        Oznacza to, że normalnie nie musisz ręcznie uruchamiać
        pointer.py przed otwarciem OBS.


    README.txt
        Ta dokumentacja.


    pointers/
        Folder zawierający pliki SVG kursorów.


======================================================================
4. WYMAGANA STRUKTURA FOLDERÓW
======================================================================

Cały projekt powinien być przechowywany razem w jednym folderze.

Przykład:

    OBS-Cursor-Overlay/


Wewnątrz tego folderu:

    OBS-Cursor-Overlay/
    |
    +-- pointer.py
    |
    +-- pointer.html
    |
    +-- cursor_config.json
    |
    +-- pointer_config.json
    |
    +-- start_pointer.py
    |
    +-- README.txt
    |
    +-- pointers/
         |
         +-- crystal_blue_sword.svg
         +-- arrow.svg
         +-- staff.svg
         +-- skeleton_hand.svg


WAŻNE:

Nie przenoś pojedynczych plików poza ten folder, chyba że wiesz,
która konfiguracja się do nich odwołuje.

Projekt został zaprojektowany tak, aby był PRZENOŚNY (portable).


----------------------------------------------------------------------
4.1 ŚCIEŻKI PRZENOŚNE
----------------------------------------------------------------------

Aplikacja Python nie zawiera na stałe zapisanej (hard-coded) ścieżki
do katalogu projektu.

Pliki konfiguracyjne są zlokalizowane względem pointer.py.

Na przykład cały projekt można umieścić w:

    C:\OBS-Cursor-Overlay\

lub:

    D:\Streaming\OBS-Cursor-Overlay\

lub:

    C:\Users\Someone\Desktop\OBS-Cursor-Overlay\


Na macOS:

    /Users/Someone/OBS-Cursor-Overlay/


Na Linuksie:

    /home/someone/OBS-Cursor-Overlay/


Cały folder można skopiować na inny komputer.

Same pliki projektu nie muszą być edytowane tylko dlatego, że
katalog projektu został przeniesiony.


UWAGA:

Źródło Browser Source w OBS nadal musi wskazywać na prawidłową
lokalizację pointer.html na nowym komputerze.


======================================================================
5. INSTALACJA PYTHONA
======================================================================

OBS CURSOR OVERLAY wymaga Pythona w wersji 3.10 lub nowszej.

Pythona można pobrać ze strony:

    https://www.python.org/


Zalecana jest aktualna wersja Python 3.


----------------------------------------------------------------------
5.1 WINDOWS
----------------------------------------------------------------------

Pobierz Pythona dla Windows.

Podczas instalacji zaznacz opcję:

    Add Python to PATH


jeśli jest ona dostępna.


----------------------------------------------------------------------
5.2 macOS
----------------------------------------------------------------------

Zainstaluj aktualną wersję Python 3 odpowiednią dla Twojego Maca.

Po instalacji otwórz Terminal i sprawdź:

    python3 --version


W zależności od instalacji Pythona, komenda może być również:

    python --version


----------------------------------------------------------------------
5.3 LINUX
----------------------------------------------------------------------

Zainstaluj Python 3 za pomocą standardowego menedżera pakietów
Twojej dystrybucji Linuksa, jeśli nie jest jeszcze zainstalowany.

Następnie sprawdź:

    python3 --version


======================================================================
6. SPRAWDZANIE PYTHONA
======================================================================

Komenda używana do sprawdzenia Pythona zależy od systemu
operacyjnego.


Windows:

    python --version


Jeśli to nie zadziała:

    py --version


macOS:

    python3 --version


Linux:

    python3 --version


Powinieneś zobaczyć coś podobnego do:

    Python 3.10.x

lub:

    Python 3.11.x

lub:

    Python 3.12.x


Zalecany jest Python 3.10 lub nowszy.


======================================================================
7. INSTALACJA WYMAGANYCH PAKIETÓW PYTHON
======================================================================

OBS CURSOR OVERLAY wymaga dwóch zewnętrznych pakietów Python:

    pynput
    websockets


----------------------------------------------------------------------
7.1 WINDOWS
----------------------------------------------------------------------

Otwórz Wiersz polecenia (Command Prompt).

Przejdź do folderu OBS-Cursor-Overlay.

Aby sprawdzić gdzie aktualnie się znajdujesz i jakie foldery są ci dostepne wpisz:

  dir

Przykład aby przemieścić się do folderu pod konkretną ścieżką:

    cd C:\OBS-Cursor-Overlay

Następnie zainstaluj:

    python -m pip install pynput websockets


Alternatywnie:

    python -m pip install pynput

    python -m pip install websockets


----------------------------------------------------------------------
7.2 macOS
----------------------------------------------------------------------

Otwórz Terminal.

Przejdź do folderu OBS-Cursor-Overlay.

Aby sprawdzić listę folderów dostępnych w lokacji w której się znajdujesz wpisz:

    ls -la

Przykład komendy która pozwoli ci dojść do poszukiwanego folderu:

    cd /Users/Someone/OBS-Cursor-Overlay


Zainstaluj:

    python3 -m pip install pynput websockets


----------------------------------------------------------------------
7.3 LINUX
----------------------------------------------------------------------

Otwórz Terminal.

Przejdź do folderu OBS-Cursor-Overlay.

Przykład:

    cd /home/someone/OBS-Cursor-Overlay


Zainstaluj:

    python3 -m pip install pynput websockets


======================================================================
8. TESTOWANIE SERWERA WSKAŹNIKA (POINTER SERVER)
======================================================================

Przed skonfigurowaniem OBS zaleca się ręczne przetestowanie
serwera.

Potwierdza to, że Python, pynput, websockets oraz wykrywanie
myszy/ekranu działają poprawnie.


----------------------------------------------------------------------
8.1 WINDOWS
----------------------------------------------------------------------

Otwórz Wiersz polecenia.

Przejdź do folderu projektu:

    cd C:\OBS-Cursor-Overlay


Uruchom:

    python pointer.py


----------------------------------------------------------------------
8.2 macOS / LINUX
----------------------------------------------------------------------

Otwórz Terminal.

Przejdź do folderu projektu:

    cd /path/to/OBS-Cursor-Overlay


Uruchom:

    python3 pointer.py


----------------------------------------------------------------------
8.3 OCZEKIWANY WYNIK
----------------------------------------------------------------------

Powinieneś zobaczyć coś podobnego do:

    ========================================
     OBS CURSOR OVERLAY Mouse Server
    ========================================

    Operating system: Windows

    Screen: 1920 x 1080
    OBS output: 1920 x 1080

    Scale X: 1.0000
    Scale Y: 1.0000

    Listening ONLY on: 127.0.0.1:8765

    Authentication: DISABLED

    Server is restricted to localhost.
    It is NOT accessible from other
    computers on your network.

    Configuration:
      Cursor: pointers/crystal_blue_sword.svg
      Cursor config: ...
      Pointer config: ...

    Press Ctrl+C to stop.


Dokładna nazwa systemu operacyjnego, wymiary ekranu i wartości
skalowania będą zależeć od komputera.


Jeśli to widzisz, serwer działa poprawnie.


Aby zatrzymać serwer:

    Naciśnij Ctrl+C


======================================================================
9. BEZPIECZEŃSTWO / POŁĄCZENIE LOKALNE
======================================================================

Serwer WebSocket nasłuchuje na:

    127.0.0.1:8765


127.0.0.1 oznacza:

    "ten komputer"


Serwer NIE nasłuchuje na:

    0.0.0.0


i w związku z tym nie jest przeznaczony do akceptowania połączeń
z innych komputerów w sieci.


Uwierzytelnianie jest celowo wyłączone.

Jest to akceptowalne, ponieważ usługa jest ograniczona do
localhost.


Browser Source łączy się z:

    ws://127.0.0.1:8765


WebSocket jest używany wyłącznie do komunikacji pomiędzy:

    pointer.py

a:

    pointer.html


Żaden zewnętrzny serwer nie jest wymagany.


======================================================================
10. JAK DZIAŁA POZYCJA MYSZY
======================================================================

OBS CURSOR OVERLAY automatycznie wykrywa system operacyjny komputera.


Ogólny proces przebiega następująco:

    Fizyczny pulpit
          |
          v
    System operacyjny
          |
          v
    Pozycja myszy z pynput
          |
          v
    Konwersja współrzędnych
          |
          v
    Rozdzielczość wyjściowa OBS
          |
          v
    Browser Source


Na przykład fizyczny pulpit może mieć:

    2560 x 1440


podczas gdy OBS może używać:

    1920 x 1080


Aplikacja proporcjonalnie konwertuje:

    Pulpit X -> OBS X

    Pulpit Y -> OBS Y


Pozwala to kursorowi dotrzeć do właściwych krawędzi i narożników
płótna (canvas) OBS.


Docelowa rozdzielczość OBS jest kontrolowana przez:

    pointer_config.json


Na przykład:

    "output_width": 1920,
    "output_height": 1080


Konwersja odbywa się automatycznie.

Użytkownicy NIE powinni ręcznie kompensować skalowania
wyświetlacza Windows.


======================================================================
11. KONFIGURACJA WSKAŹNIKA (POINTERA)
======================================================================

Ogólne zachowanie wskaźnika jest kontrolowane poprzez:

    pointer_config.json


Domyślny plik wygląda tak:

    {
        "pointer_width": 90,
        "pointer_height": 90,

        "fade_duration": "0.45s",

        "hide_delay": 5.0,

        "output_width": 1920,
        "output_height": 1080,

        "tip_x": 8,
        "tip_y": 8
    }


Poniżej opisano poszczególne wartości.


----------------------------------------------------------------------
11.1 SZEROKOŚĆ WSKAŹNIKA (POINTER WIDTH)
----------------------------------------------------------------------

Przykład:

    "pointer_width": 90


Kontroluje szerokość kontenera kursora w pikselach.


Na przykład:

    "pointer_width": 120


tworzy szerszy kontener wskaźnika.


Grafika SVG jest skalowana tak, aby wypełnić ten kontener.


----------------------------------------------------------------------
11.2 WYSOKOŚĆ WSKAŹNIKA (POINTER HEIGHT)
----------------------------------------------------------------------

Przykład:

    "pointer_height": 90


Kontroluje wysokość kontenera kursora.


Na przykład:

    "pointer_height": 120


tworzy wyższy kontener wskaźnika.


Zazwyczaj:

    pointer_width

oraz:

    pointer_height


powinny być równe, chyba że celowo chcesz rozciągnąć kursor.


----------------------------------------------------------------------
11.3 CZAS ZANIKANIA (FADE DURATION)
----------------------------------------------------------------------

Przykład:

    "fade_duration": "0.45s"


Kontroluje, jak szybko kursor pojawia się i zanika.


Szybciej:

    "fade_duration": "0.2s"


Wolniej:

    "fade_duration": "1s"


Wartość używa notacji czasu CSS.


----------------------------------------------------------------------
11.4 OPÓŹNIENIE UKRYCIA (HIDE DELAY)
----------------------------------------------------------------------

Przykład:

    "hide_delay": 5.0


Jest to liczba sekund od ostatniego ruchu myszy, po której kursor
znika.


Na przykład:

    "hide_delay": 3.0


oznacza, że kursor znika po około 3 sekundach.


Wartość:

    "hide_delay": 10.0


sprawia, że pozostaje widoczny przez około 10 sekund.


----------------------------------------------------------------------
11.5 SZEROKOŚĆ WYJŚCIOWA (OUTPUT WIDTH)
----------------------------------------------------------------------

Przykład:

    "output_width": 1920


Określa szerokość systemu współrzędnych wyjścia/płótna (canvas) OBS.


Dla standardowej konfiguracji OBS w Full HD:

    1920


jest zazwyczaj odpowiednie.


----------------------------------------------------------------------
11.6 WYSOKOŚĆ WYJŚCIOWA (OUTPUT HEIGHT)
----------------------------------------------------------------------

Przykład:

    "output_height": 1080


Dla standardowej konfiguracji OBS w Full HD:

    1080


jest zazwyczaj odpowiednie.


WAŻNE:

Wymiary Browser Source powinny odpowiadać tym wartościom.


Na przykład:

    pointer_config.json:

        "output_width": 1920,
        "output_height": 1080


Browser Source w OBS:

        Width: 1920
        Height: 1080


----------------------------------------------------------------------
11.7 TIP X / TIP Y
----------------------------------------------------------------------

Przykład:

    "tip_x": 8,
    "tip_y": 8


Te wartości definiują lokalizację rzeczywistego czubka kursora
myszy wewnątrz grafiki SVG.


System pozycjonuje kontener SVG tak, aby:

    tip_x
    tip_y


trafiały dokładnie w rzeczywistą współrzędną myszy.


Dla dostarczonej grafiki kursorów standardowa konwencja to:

    X = 8
    Y = 8


Pozwala to na wymianę różnych projektów kursorów bez zmiany
systemu śledzenia myszy.


======================================================================
12. KONFIGURACJA KURSORA
======================================================================

Wybór kursora i ustawienia poświaty są kontrolowane poprzez:

    cursor_config.json


Przykład:

    {
        "active_cursor": "pointers/crystal_blue_sword.svg",

        "default_glow": {
            "color": "rgba(70, 190, 255, 0.8)",
            "min": "3px",
            "max": "10px",
            "speed": "2.6s"
        },

        "cursors": {
            ...
        }
    }


======================================================================
13. ZMIANA AKTYWNEGO KURSORA
======================================================================

Otwórz:

    cursor_config.json


Znajdź:

    "active_cursor"


Przykład:

    "active_cursor": "pointers/crystal_blue_sword.svg"


Aby użyć strzałki:

    "active_cursor": "pointers/arrow.svg"


Aby użyć laski/kostura (staff):

    "active_cursor": "pointers/staff.svg"


Aby użyć szkieletowej dłoni:

    "active_cursor": "pointers/skeleton_hand.svg"


Zapisz plik.


======================================================================
14. ZASTOSOWANIE ZMIANY KURSORA
======================================================================

NIE musisz:

    - restartować OBS
    - restartować pointer.py
    - restartować start_pointer.py


Po zmianie cursor_config.json:

    1. Zapisz cursor_config.json.

    2. Wróć do OBS.

    3. Kliknij prawym przyciskiem myszy na Browser Source OBS
       Pointer.

    4. Wybierz:

           Refresh (Odśwież)


Browser Source ponownie ładuje pointer.html.

Nowa konfiguracja jest wtedy ładowana.


Konfiguracja kursora jest celowo ładowana z pominięciem
mechanizmów cache'owania (cache-busting, cache wyłączony), dzięki
czemu OBS/Chromium nie powinien ponownie użyć starej wersji
konfiguracji JSON.


======================================================================
15. ZMIANA POŚWIATY (GLOW)
======================================================================

Ustawienia poświaty są również kontrolowane poprzez:

    cursor_config.json


Każdy kursor może mieć swoje własne:

    color
    min
    max
    speed


Przykład:

    "pointers/crystal_blue_sword.svg": {

        "color": "rgba(70, 190, 255, 0.8)",
        "min": "3px",
        "max": "10px",
        "speed": "2.6s"

    }


======================================================================
16. KOLOR POŚWIATY (GLOW COLOR)
======================================================================

Kolor jest zapisywany za pomocą notacji CSS rgba.


Przykład:

    rgba(70, 190, 255, 0.8)


Pierwsze trzy liczby reprezentują:

    Czerwony (Red)
    Zielony (Green)
    Niebieski (Blue)


Ostatnia liczba reprezentuje:

    Nieprzezroczystość (Opacity)


Przykłady:


Niebieski:

    rgba(70, 190, 255, 0.8)


Czerwony:

    rgba(255, 60, 60, 0.8)


Zielony:

    rgba(80, 255, 120, 0.8)


Biały:

    rgba(255, 255, 255, 0.8)


Fioletowy:

    rgba(180, 80, 255, 0.8)


======================================================================
17. MINIMALNA POŚWIATA (MINIMUM GLOW)
======================================================================

Przykład:

    "min": "3px"


To najmniejsza poświata podczas animacji.


Mniejsza:

    "min": "1px"


oznacza bardziej subtelną poświatę początkową.


Większa:

    "min": "6px"


oznacza, że kursor zawsze ma silniejszą poświatę.


======================================================================
18. MAKSYMALNA POŚWIATA (MAXIMUM GLOW)
======================================================================

Przykład:

    "max": "10px"


Kontroluje, jak duża staje się poświata w szczytowym momencie
animacji.


Przykład:

    "max": "5px"


tworzy bardzo subtelny efekt.


Przykład:

    "max": "15px"


tworzy znacznie silniejszy efekt.


======================================================================
19. PRĘDKOŚĆ POŚWIATY (GLOW SPEED)
======================================================================

Przykład:

    "speed": "2.6s"


Kontroluje długość jednego pełnego cyklu pulsowania poświaty.


Mniejsza wartość:

    "speed": "1.5s"


oznacza szybsze pulsowanie.


Większa wartość:

    "speed": "4s"


oznacza wolniejsze pulsowanie.


Dla spokojnego, subtelnego efektu zalecane jest w przybliżeniu:

    2,5 - 4 sekundy


======================================================================
20. DOMYŚLNA POŚWIATA (DEFAULT GLOW)
======================================================================

cursor_config.json zawiera również:

    "default_glow"


Przykład:

    "default_glow": {

        "color": "rgba(70, 190, 255, 0.8)",
        "min": "3px",
        "max": "10px",
        "speed": "2.6s"

    }


Ta konfiguracja jest używana, gdy dany kursor nie ma własnej
konfiguracji poświaty.


Pozwala to nowym kursorom działać bez konieczności posiadania
dedykowanego wpisu poświaty.


======================================================================
21. DODAWANIE NOWEGO KURSORA
======================================================================

Aby dodać nowy kursor:


    1. Utwórz lub zdobądź plik SVG.


    2. Umieść SVG wewnątrz:

           pointers/


    3. Upewnij się, że SVG spełnia wymagania dotyczące
       wskaźnika (pointer requirements).


    4. Dodaj jego ścieżkę do cursor_config.json.


Przykład:

    pointers/my_new_cursor.svg


Następnie dodaj:

    "pointers/my_new_cursor.svg": {

        "color": "rgba(255, 255, 255, 0.8)",
        "min": "3px",
        "max": "10px",
        "speed": "2.6s"

    }


Następnie ustaw go jako aktywny:

    "active_cursor": "pointers/my_new_cursor.svg"


Zapisz plik.


Odśwież Browser Source.


======================================================================
22. WYMAGANIA DOTYCZĄCE KURSORA SVG
======================================================================

Każdy kursor SVG powinien być zgodny ze wspólną konwencją
współrzędnych.


SVG powinno używać:

    viewBox="0 0 90 90"


Czubek kursora powinien znajdować się zazwyczaj w:

    X = 8
    Y = 8


Ten punkt jest traktowany jako rzeczywista pozycja myszy.


Reszta grafiki jest rysowana wokół tego punktu.


Na przykład miecz skierowany w górny lewy róg powinien mieć swoje
ostrze/czubek wyrównane z punktem (8,8).


Ta konwencja pozwala na wymianę zupełnie różnych projektów kursorów
bez zmiany pointer.py ani pointer.html.


======================================================================
23. ROZMIAR KURSORA
======================================================================

Domyślny kontener wskaźnika to:

    90 x 90 pikseli


Jest to kontrolowane poprzez:

    pointer_config.json


Na przykład:

    "pointer_width": 90,
    "pointer_height": 90


Grafika SVG wypełnia ten kontener.


Dlatego grafika SVG powinna być zazwyczaj zaprojektowana w
granicach:

    0 - 90 X
    0 - 90 Y


Pozycja myszy jest zakotwiczona w punkcie:

    (8,8)


chyba że tip_x i tip_y zostały celowo zmienione w
pointer_config.json.


======================================================================
24. POŚWIATA SVG VS ZEWNĘTRZNA POŚWIATA OBS CURSOR OVERLAY
======================================================================

Kursor może mieć dwa różne rodzaje poświaty.


----------------------------------------------------------------------
24.1 POŚWIATA WBUDOWANA W SVG (BAKED-IN)
----------------------------------------------------------------------

Samo SVG może zawierać:

    gradienty
    filtry
    cienie (drop shadows)
    efekty poświaty


Ta poświata należy do samej grafiki.


Na przykład kryształowo-niebieski miecz może mieć niebieską
poświatę bezpośrednio wokół ostrza.


----------------------------------------------------------------------
24.2 ZEWNĘTRZNA POŚWIATA OBS CURSOR OVERLAY
----------------------------------------------------------------------

pointer.html dodaje kolejną animowaną poświatę wokół kursora.


Jest ona kontrolowana przez:

    cursor_config.json


Oba efekty mogą więc działać razem.


Na przykład:

    SVG:
        niebieska poświata wokół ostrza miecza

    HTML:
        miękka, "oddychająca" niebieska poświata wokół całego
        miecza


Pozwala to, aby każdy kursor miał swój własny charakter
wizualny.


======================================================================
25. ODPOWIEDZIALNOŚCI PLIKÓW KONFIGURACYJNYCH
======================================================================

Projekt celowo dzieli konfigurację na dwa pliki JSON.


----------------------------------------------------------------------
25.1 cursor_config.json
----------------------------------------------------------------------

Kontroluje:

    - aktywny kursor
    - poświatę specyficzną dla kursora
    - domyślną poświatę


To jest plik, który większość użytkowników będzie edytować.


----------------------------------------------------------------------
25.2 pointer_config.json
----------------------------------------------------------------------

Kontroluje:

    - szerokość wskaźnika
    - wysokość wskaźnika
    - czas zanikania
    - opóźnienie ukrycia
    - szerokość wyjściową
    - wysokość wyjściową
    - X czubka kursora
    - Y czubka kursora


Ten plik jest przeznaczony dla użytkowników, którzy chcą
dostosować ogólne zachowanie wskaźnika.


----------------------------------------------------------------------
25.3 DLACZEGO DWA PLIKI?
----------------------------------------------------------------------

Oba pliki konfiguracyjne mają różne odpowiedzialności.


cursor_config.json odpowiada na pytanie:

    "Jaki kursor powinienem wyświetlić i jak powinien się
    świecić?"


pointer_config.json odpowiada na pytanie:

    "Jak powinien zachowywać się sam system wskaźnika?"


Zapobiega to mieszaniu się codziennej konfiguracji wizualnej z
techniczym kodem śledzenia myszy.


======================================================================
26. KONFIGURACJA JEST WYSYŁANA PRZEZ LOKALNY WEBSOCKET
======================================================================

Gdy pointer.html łączy się z pointer.py, serwer najpierw wysyła
informacje konfiguracyjne.


Browser Source otrzymuje:

    konfigurację kursora

oraz:

    konfigurację wskaźnika


Następnie otrzymuje w sposób ciągły współrzędne myszy.


Ogólna sekwencja komunikacji wygląda tak:

    Browser Source łączy się
             |
             v
        pointer.py
             |
             v
       konfiguracja
             |
             v
       współrzędne myszy
             |
             v
       pointer.html


Oznacza to, że pointer.html nie musi zawierać na stałe zapisanych
wartości konfiguracyjnych.


======================================================================
27. OBSŁUGA BŁĘDÓW KONFIGURACJI
======================================================================

Jeśli cursor_config.json nie może zostać poprawnie wczytany,
pointer.html zgłasza opisowy błąd w konsoli Browser Source.


Możliwe przyczyny to:

    - brakujący plik JSON
    - nieprawidłowy JSON
    - brakujące active_cursor
    - nieprawidłowa ścieżka kursora
    - nieprawidłowo sformułowana konfiguracja poświaty


Błąd jest celowo wyświetlany w konsoli Browser Source, zamiast
zawodzić w sposób niewidoczny (cichy błąd).


======================================================================
28. KONFIGUROWANIE PYTHONA W OBS
======================================================================

OBS musi wiedzieć, gdzie zainstalowany jest Python.


Otwórz OBS Studio.


Przejdź do:

    Tools (Narzędzia)
        ->
    Scripts (Skrypty)


Powinieneś zobaczyć okno skryptowania OBS.


Przejdź do sekcji Python Settings.


Wybierz katalog instalacji Pythona.


Przykład na Windows:

    C:\Users\USERNAME\AppData\Local\Programs\Python\Python310


WAŻNE:

Wybierz folder instalacyjny Pythona, a nie plik python.exe, chyba
że Twoja wersja OBS wyraźnie prosi o plik wykonywalny.


OBS powinien zgłosić coś podobnego do:

    Loaded Python version 3.10


Dokładne sformułowanie zależy od wersji OBS.


======================================================================
29. DODAWANIE SKRYPTU AUTOMATYCZNEGO URUCHAMIANIA DO OBS
======================================================================

W OBS:

    Tools
        ->
    Scripts


Kliknij:

    +


Wybierz:

    start_pointer.py


Skrypt powinien wygenerować komunikaty podobne do:

    ========================================
     OBS CURSOR OVERLAY
    ========================================

    Python:
    C:\Users\USERNAME\AppData\Local\Programs\Python\Python310\python.exe

    Script:
    C:\OBS-Cursor-Overlay\pointer.py

    OBS CURSOR OVERLAY: pointer.py started


Oznacza to, że OBS pomyślnie uruchomił pointer.py.


NIE powinieneś ręcznie uruchamiać pointer.py w tym samym czasie.


Jeśli to OBS odpowiada za uruchamianie pointer.py, pozwól OBS
nim zarządzać.


======================================================================
30. AUTOMATYCZNE URUCHAMIANIE
======================================================================

Po dodaniu start_pointer.py do OBS, OBS załaduje skrypt przy
starcie OBS.


Skrypt pomocniczy automatycznie uruchamia pointer.py.


Dlatego normalny przebieg pracy wygląda tak:


    Uruchom OBS
        |
        v
    OBS ładuje start_pointer.py
        |
        v
    start_pointer.py uruchamia pointer.py
        |
        v
    pointer.py wykrywa system operacyjny
        |
        v
    pointer.py rozpoczyna śledzenie myszy
        |
        v
    Browser Source łączy się z localhost
        |
        v
    Konfiguracja jest wysyłana
        |
        v
    Niestandardowy kursor pojawia się przy ruchu myszy


Nie powinieneś potrzebować otwierać Wiersza polecenia ani
Terminala i ręcznie uruchamiać pointer.py podczas normalnego
użytkowania.


======================================================================
31. DODAWANIE BROWSER SOURCE
======================================================================

Otwórz OBS Studio.


Wybierz scenę, w której chcesz mieć niestandardowy kursor.


W panelu Sources (Źródła):

    Add (Dodaj)
        ->
    Browser


Utwórz nowe źródło Browser Source.


Nadaj mu nazwę, na przykład:

    OBS CURSOR OVERLAY


Ustaw URL na lokalny plik pointer.html.


Przykład dla Windows:

    file:///C:/OBS-Cursor-Overlay/pointer.html


Kolejny przykład dla Windows:

    file:///D:/Streaming/OBS-Cursor-Overlay/pointer.html


Przykład dla macOS:

    file:///Users/Someone/OBS-Cursor-Overlay/pointer.html


Przykład dla Linuksa:

    file:///home/someone/OBS-Cursor-Overlay/pointer.html


Użyj poprawnej ścieżki dla swojego komputera.


Ustaw wymiary Browser Source zgodnie z:

    pointer_config.json


Dla domyślnej konfiguracji:

    Width: 1920
    Height: 1080


Tło Browser Source jest przezroczyste.


Dlatego nie powinno zasłaniać rozgrywki ani kamery.


======================================================================
32. POZYCJA BROWSER SOURCE
======================================================================

Browser Source powinien być zazwyczaj umieszczony w:

    X: 0
    Y: 0


i powinien wypełniać całe płótno (canvas) OBS.


Jeśli Twoje płótno OBS ma:

    1920 x 1080


Browser Source również powinien mieć:

    1920 x 1080


Nie zmieniaj rozmiaru Browser Source do rozmiaru okna rozgrywki.


Współrzędne wskaźnika opierają się na całym płótnie OBS.


======================================================================
33. WAŻNE: DODAJ WSKAŹNIK TYLKO DO ODPOWIEDNICH SCEN
======================================================================

Browser Source OBS CURSOR OVERLAY jest nakładką (overlay).


Jeśli Browser Source zostanie dodany do sceny pokazującej pulpit
komputera, normalny kursor myszy systemu operacyjnego może
również być widoczny.


Może to skutkować jednoczesnym pojawieniem się:

    normalnego kursora systemu operacyjnego
           +
    kursora OBS CURSOR OVERLAY


w tym samym czasie.


Jest to zjawisko oczekiwane.


Na przykład, jeśli OBS jest używany do streamowania rozgrywki z
PlayStation 5, sama konsola PS5 nie posiada kursora myszy
komputera.


Nakładka OBS CURSOR OVERLAY zapewnia więc przydatny niestandardowy
kursor wewnątrz sceny z rozgrywką.


Jednak jeśli osobna scena pokazuje pulpit Windows/macOS/Linux,
normalny kursor systemu operacyjnego może również być widoczny.


Proste rozwiązanie to:

    Nie dodawaj Browser Source OBS CURSOR OVERLAY do scen, w których
    chcesz pokazywać normalny kursor pulpitu komputera.


Na przykład:


    Scena - PS5 Gameplay
        |
        +-- Gameplay
        +-- Camera
        +-- OBS CURSOR OVERLAY


    Scena - Desktop
        |
        +-- Desktop Capture
        +-- Camera
        |
        +-- BRAK OBS CURSOR OVERLAY


Pozwala to używać niestandardowego wskaźnika tylko tam, gdzie
jest to przydatne.


======================================================================
34. TESTOWANIE KURSORA
======================================================================

Poruszaj myszą komputera.


Niestandardowy kursor powinien pojawić się w OBS.


Gdy mysz przestanie się poruszać przez około:

    5 sekund


niestandardowy kursor znika.


Gdy mysz znów się porusza, kursor ponownie się pojawia.


Dokładne opóźnienie jest kontrolowane przez:

    pointer_config.json


za pomocą:

    "hide_delay"


Kursor powinien być w stanie dotrzeć do:

    lewego górnego rogu
    prawego górnego rogu
    lewego dolnego rogu
    prawego dolnego rogu


płótna OBS.


======================================================================
35. ZMIANA KURSORA BEZ RESTARTOWANIA OBS
======================================================================

Możesz zmienić aktywny kursor podczas działania OBS.


Kroki:


    1. Otwórz cursor_config.json.


    2. Zmień:

           "active_cursor"


    3. Zapisz plik.


    4. Wróć do OBS.


    5. Kliknij prawym przyciskiem myszy na Browser Source OBS
       Pointer.


    6. Wybierz:

           Refresh


Kursor powinien zmienić się natychmiast.


NIE musisz:

    - restartować OBS
    - restartować pointer.py
    - ponownie ładować start_pointer.py


======================================================================
36. ZMIANA KONFIGURACJI WSKAŹNIKA
======================================================================

pointer_config.json jest również odczytywany, gdy Browser Source
się łączy.


Jeśli zmienisz:

    pointer_width
    pointer_height
    fade_duration
    hide_delay
    output_width
    output_height
    tip_x
    tip_y


zapisz plik i odśwież Browser Source.


Serwer myszy w Pythonie zwykle nie musi być restartowany, aby te
zmiany zostały wysłane do świeżo odświeżonego Browser Source.


UWAGA:

Ponieważ output_width oraz output_height są używane przez
pointer.py do konwersji współrzędnych, zmiana ich podczas gdy
pointer.py już działa może wymagać restartu pointer.py, aby
serwer Python zaczął używać nowych wartości.


Dlatego po zmianie:

    output_width

lub:

    output_height


zrestartuj pointer.py, jeśli to konieczne.


Dla zwykłych zmian wizualnych, takich jak:

    pointer_width
    pointer_height
    fade_duration
    hide_delay
    tip_x
    tip_y


odświeżenie Browser Source jest wystarczające.


======================================================================
37. ROZWIĄZYWANIE PROBLEMÓW
======================================================================


----------------------------------------------------------------------
37.1 KURSOR SIĘ NIE POJAWIA
----------------------------------------------------------------------

Sprawdź:


    1. Czy pointer.py jest uruchomiony?


    2. Czy start_pointer.py jest załadowany w:

           Tools -> Scripts


    3. Czy log skryptu OBS mówi:

           pointer.py started


    4. Czy Browser Source jest obecny?


    5. Czy Browser Source ma ustawione te same wymiary co
       pointer_config.json?


    6. Czy Browser Source wskazuje na:

           pointer.html


    7. Czy Browser Source jest widoczny w bieżącej scenie?


    8. Spróbuj:

           Kliknij prawym przyciskiem na Browser Source -> Refresh



----------------------------------------------------------------------
37.2 KURSOR SIĘ POJAWIA, ALE SIĘ NIE PORUSZA
----------------------------------------------------------------------

Sprawdź, czy pointer.py jest uruchomiony.


Możesz przetestować to ręcznie.


Windows:

    cd C:\Your\Path\OBS-Cursor-Overlay

    python pointer.py


macOS/Linux:

    cd /Your/Path/OBS-Cursor-Overlay

    python3 pointer.py


Powinieneś zobaczyć:

    Listening ONLY on: 127.0.0.1:8765


Jeśli pointer.py jest uruchomiony, a Browser Source nadal się nie
porusza, odśwież Browser Source.


----------------------------------------------------------------------
37.3 KURSOR JEST PRZESUNIĘTY WZGLĘDEM MYSZY
----------------------------------------------------------------------

Upewnij się, że:


    Szerokość Browser Source
        =
    output_width w pointer_config.json


oraz:


    Wysokość Browser Source
        =
    output_height w pointer_config.json


Upewnij się także, że:


    Pozycja X Browser Source = 0

    Pozycja Y Browser Source = 0


Płótno OBS powinno używać tych samych wymiarów wyjściowych, które
zostały skonfigurowane w pointer_config.json.


Sprawdź również:

    tip_x
    tip_y


Te wartości kontrolują, gdzie w grafice SVG znajduje się
rzeczywisty czubek kursora.


----------------------------------------------------------------------
37.4 KURSOR NIE DOCIERA DO KRAWĘDZI
----------------------------------------------------------------------

Sprawdź, czy pointer.py używa aktualnego, wieloplatformowego kodu
skalowania współrzędnych.


Obecna wersja automatycznie wykrywa wymiary ekranu i konwertuje je
na skonfigurowaną rozdzielczość wyjściową OBS.


Nie dodawaj ręcznie przesunięć (offsetów), chyba że celowo
zmieniłeś architekturę.


Jeśli problem występuje wyłącznie na konkretnej konfiguracji
Retina w macOS, system współrzędnych wyświetlacza może wymagać
dostosowania specyficznego dla platformy.


----------------------------------------------------------------------
37.5 ZMIANA KURSORA SIĘ NIE POJAWIA
----------------------------------------------------------------------

Po zmianie cursor_config.json:


    Kliknij prawym przyciskiem na Browser Source
        ->
    Refresh


NIE musisz restartować OBS.


Browser Source celowo ładuje aktualną konfigurację, zamiast
polegać na wcześniej zapisanej w pamięci podręcznej kopii.


----------------------------------------------------------------------
37.6 BŁĄD JSON
----------------------------------------------------------------------

Jeśli plik JSON zawiera nieprawidłowy JSON, wczytanie konfiguracji
może się nie powieść.


Częste błędy:


Brakujący przecinek:

    "speed": "2.6s"
    "other": "value"


Poprawnie:

    "speed": "2.6s",
    "other": "value"


Użycie pojedynczych cudzysłowów:

    'active_cursor': 'pointers/arrow.svg'


JSON wymaga podwójnych cudzysłowów:

    "active_cursor": "pointers/arrow.svg"


Jeśli konfiguracja nie może zostać wczytana, pointer.py zgłasza
błąd konfiguracji w terminalu.


Błędy konfiguracji Browser Source są również zgłaszane w konsoli
Browser Source.


----------------------------------------------------------------------
37.7 BŁĄD TABULACJI/WCIĘĆ W PYTHONIE
----------------------------------------------------------------------

Python wymaga spójnych wcięć.


Nie mieszaj tabulatorów ze spacjami.


Jeśli zobaczysz:


    TabError: inconsistent use of tabs and spaces in indentation


zastąp dany plik oficjalną wersją projektu, zamiast ręcznie
zmieniać przypadkowe wcięcia.


----------------------------------------------------------------------
37.8 BŁĄD PAKIETU PYTHON
----------------------------------------------------------------------

Jeśli zobaczysz:


    ModuleNotFoundError: No module named 'websockets'


zainstaluj:

    python -m pip install websockets


lub na macOS/Linux:

    python3 -m pip install websockets


Jeśli zobaczysz:


    ModuleNotFoundError: No module named 'pynput'


zainstaluj:

    python -m pip install pynput


lub:

    python3 -m pip install pynput


----------------------------------------------------------------------
37.9 PORT 8765 JEST JUŻ ZAJĘTY
----------------------------------------------------------------------

Jeśli pointer.py zgłasza, że port 8765 nie może zostać otwarty,
inna aplikacja może już go używać.


Zwykle oznacza to, że inna kopia pointer.py już działa.


Sprawdź, czy nie:

    - uruchomiłeś ręcznie pointer.py
    - podczas gdy OBS już uruchomił swoją automatyczną kopię


Zatrzymaj dodatkową kopię.


Normalnie powinien działać jednocześnie tylko jeden serwer
pointer.py.


----------------------------------------------------------------------
37.10 POINTER.PY URUCHAMIA SIĘ, A NASTĘPNIE NATYCHMIAST SIĘ
ZATRZYMUJE
----------------------------------------------------------------------

Sprawdź terminal lub log skryptu OBS pod kątem błędu.


Częste przyczyny to:


    - brakujący pakiet Python
    - nieprawidłowy JSON
    - brakujący plik konfiguracyjny
    - niedostępne informacje o ekranie
    - port 8765 już używany
    - nieprawidłowa instalacja Pythona


Uruchom pointer.py ręcznie, aby zobaczyć pełny komunikat błędu.


======================================================================
38. TESTOWANIE BEZ OBS
======================================================================

Możesz przetestować serwer Python niezależnie.


Windows:

    cd C:\Folder\OBS-Cursor-Overlay

    python pointer.py


macOS/Linux:

    cd /Folder/OBS-Cursor-Overlay

    python3 pointer.py


Jeśli serwer uruchomi się pomyślnie, Python, wymagane pakiety,
pliki konfiguracyjne oraz wykrywanie ekranu/myszy działają
poprawnie.


Serwer będzie działał do momentu:

    Ctrl+C


======================================================================
39. ZWYKŁY CODZIENNY PRZEBIEG PRACY
======================================================================

Po skonfigurowaniu wszystkiego, normalne użytkowanie jest proste.


    1. Uruchom OBS.


    2. OBS automatycznie uruchamia pointer.py poprzez
       start_pointer.py.


    3. Wybierz scenę zawierającą Browser Source OBS CURSOR OVERLAY.


    4. Poruszaj myszą.


    5. Niestandardowy kursor się pojawia.


    6. Przestań poruszać myszą.


    7. Kursor znika po skonfigurowanym opóźnieniu.


Wiersz polecenia ani Terminal zazwyczaj nie są wymagane.


======================================================================
40. ZMIANA KURSORÓW PODCZAS STREAMU / NAGRYWANIA
======================================================================

Możesz zmienić kursor podczas działania OBS.


Kroki:


    1. Otwórz cursor_config.json.


    2. Zmień:

           "active_cursor"


    3. Zapisz plik.


    4. Wróć do OBS.


    5. Kliknij prawym przyciskiem myszy na Browser Source.


    6. Wybierz Refresh.


Kursor powinien zmienić się natychmiast.


Serwer myszy w Pythonie nie musi być restartowany.


======================================================================
41. PRZENOSZENIE PROJEKTU NA INNY KOMPUTER
======================================================================

Projekt został zaprojektowany, aby był przenośny.


Skopiuj cały folder:

    OBS-Cursor-Overlay/


na inny komputer.


Zainstaluj:

    Python 3.10+


oraz:

    pynput
    websockets


Następnie skonfiguruj skryptowanie Python w OBS, aby korzystać z
instalacji Pythona na tym komputerze.


Dodaj:

    start_pointer.py


do OBS.


Na koniec dodaj:

    pointer.html


jako Browser Source.


Aplikacja Python nie zawiera na stałe zapisanej ścieżki projektu.


Aplikacja automatycznie wykrywa system operacyjny.


======================================================================
42. CO NORMALNIE POWINIENEŚ EDYTOWAĆ
======================================================================

Do codziennego użytku:


    EDYTUJ:

        cursor_config.json


    EWENTUALNIE EDYTUJ:

        pointer_config.json


    EWENTUALNIE EDYTUJ:

        pointers/*.svg


    NORMALNIE NIE EDYTUJ:

        pointer.py
        pointer.html
        start_pointer.py


Projekt celowo oddziela konfigurację użytkownika od kodu
programu.


======================================================================
43. SZYBKI PRZEWODNIK (QUICK REFERENCE)
======================================================================

URUCHOM OBS:

    OBS automatycznie uruchamia pointer.py.


ZMIEŃ KURSOR:

    Edytuj:

        cursor_config.json


    Zmień:

        "active_cursor"


ZASTOSUJ ZMIANĘ KURSORA:

    OBS:

        Kliknij prawym przyciskiem na Browser Source
            ->
        Refresh


ZMIEŃ POŚWIATĘ:

    Edytuj dla danego kursora:

        color
        min
        max
        speed


ZMIEŃ ROZMIAR KURSORA:

    Edytuj:

        pointer_config.json


    Zmień:

        pointer_width
        pointer_height


ZMIEŃ OPÓŹNIENIE UKRYCIA:

    Edytuj:

        hide_delay


ZMIEŃ ZANIKANIE:

    Edytuj:

        fade_duration


ZMIEŃ CZUBEK KURSORA:

    Edytuj:

        tip_x
        tip_y


DODAJ KURSOR:

    Umieść SVG w:

        pointers/


    Dodaj jego konfigurację do:

        cursor_config.json


PRZETESTUJ PYTHONA:

    Windows:

        python pointer.py


    macOS/Linux:

        python3 pointer.py


ZAINSTALUJ PAKIETY:

    Windows:

        python -m pip install pynput websockets


    macOS/Linux:

        python3 -m pip install pynput websockets


ZATRZYMAJ SERWER RĘCZNIE:

    Ctrl+C


WEBSOCKET:

    ws://127.0.0.1:8765


DOMYŚLNY BROWSER SOURCE W OBS:

    Width: 1920
    Height: 1080


DOMYŚLNY WSKAŹNIK:

    Width: 90
    Height: 90


DOMYŚLNE OPÓŹNIENIE UKRYCIA:

    5 sekund


DOMYŚLNE SVG:

    viewBox:

        0 0 90 90


DOMYŚLNY CZUBEK MYSZY W SVG:

    (8,8)


======================================================================
44. AKTUALNA ARCHITEKTURA PROJEKTU
======================================================================

Ostateczny system jest celowo podzielony na niezależne warstwy:


                         SYSTEM OPERACYJNY
                       /        |        \
                      /         |         \
                 Windows      macOS      Linux
                      \         |         /
                       \        |        /
                        +-------+-------+
                                |
                                v
                         mysz z pynput
                                |
                                v
                           pointer.py
                                |
                                |
                                | WebSocket
                                | 127.0.0.1:8765
                                |
                                v
                           pointer.html
                                |
                  +-------------+-------------+
                  |                           |
                  v                           v
          cursor_config.json         pointer_config.json
                  |                           |
                  |                           |
                  +-------------+-------------+
                                |
                                v
                       grafika kursora SVG
                                |
                                v
                       Browser Source w OBS
                                |
                                v
                       STREAM / NAGRANIE


Ten podział jest celowy.


System operacyjny dostarcza informacje o myszy i pulpicie.


pynput zapewnia wieloplatformowy dostęp do myszy.


pointer.py:

    - wykrywa system operacyjny
    - wykrywa wymiary ekranu
    - odczytuje pozycję myszy
    - konwertuje współrzędne
    - udostępnia serwer WebSocket
    - wysyła konfigurację


pointer.html:

    - odbiera konfigurację
    - odbiera współrzędne
    - pozycjonuje kursor
    - stosuje efekty wizualne
    - obsługuje automatyczne ukrywanie


cursor_config.json:

    - kontroluje, który kursor jest wyświetlany
    - kontroluje poświatę kursora


pointer_config.json:

    - kontroluje wymiary wskaźnika
    - kontroluje zachowanie animacji
    - kontroluje opóźnienie ukrycia
    - kontroluje rozdzielczość wyjściową
    - kontroluje pozycję czubka kursora


Pliki SVG:

    - zawierają rzeczywistą grafikę kursora


OBS:

    - wyświetla Browser Source
    - łączy go z rozgrywką, kamerą i innymi źródłami
    - wysyła wynikową scenę do streamu lub nagrania


======================================================================
45. WAŻNE ZASADY PROJEKTOWE
======================================================================

Rozszerzając projekt, staraj się zachować poniższe zasady:


    1. Utrzymuj pointer.py skupiony na śledzeniu myszy,
       konwersji współrzędnych oraz lokalnym serwerze WebSocket.


    2. Utrzymuj pointer.html skupiony na wyświetlaniu kursora.


    3. Trzymaj wybór kursora i ustawienia poświaty w plikach
       JSON.


    4. Trzymaj ogólne zachowanie wskaźnika w
       pointer_config.json.


    5. Trzymaj grafikę SVG wewnątrz folderu pointers/.


    6. Utrzymuj przenośność projektu.


    7. Unikaj ścieżek zapisanych na stałe (hard-coded) dla
       konkretnego komputera.


    8. Utrzymuj WebSocket ograniczony do localhost.


    9. Utrzymuj wszystkie kursory SVG zgodne ze wspólną
       konwencją czubka.


    10. Utrzymuj przetwarzanie specyficzne dla systemu
        operacyjnego odizolowane wewnątrz pointer.py, zamiast
        tworzyć osobne wersje aplikacji dla każdego systemu
        operacyjnego.


    11. Unikaj dodawania niepotrzebnych zależności specyficznych
        dla platformy, gdy istniejąca wieloplatformowa
        biblioteka Python może wykonać wymagane zadanie.


    12. Trzymaj ustawienia edytowalne przez użytkownika poza
        głównym kodem programu.


======================================================================
46. PODSUMOWANIE ODPOWIEDZIALNOŚCI PLIKÓW
======================================================================

    pointer.py
        Wieloplatformowe śledzenie myszy i serwer WebSocket.

        Normalnie:
            NIE EDYTUJ.


    pointer.html
        Wizualizacja Browser Source.

        Normalnie:
            NIE EDYTUJ.


    cursor_config.json
        Wybór kursora i konfiguracja poświaty.

        Normalnie:
            EDYTUJ TO.


    pointer_config.json
        Ogólne zachowanie i wymiary wskaźnika.

        Okazjonalnie:
            EDYTUJ TO.


    start_pointer.py
        Skrypt pomocniczy automatycznego uruchamiania OBS.

        Normalnie:
            NIE EDYTUJ.


    pointers/*.svg
        Grafika kursorów.

        Edytuj lub dodawaj je podczas tworzenia nowych projektów
        kursorów.


    README.txt
        Dokumentacja.


======================================================================
47. OGRANICZENIA / OCZEKIWANIA
======================================================================

OBS CURSOR OVERLAY został zaprojektowany przede wszystkim dla
standardowego przepływu pracy OBS, w którym Browser Source oraz
płótno OBS używają tej samej skonfigurowanej rozdzielczości
wyjściowej.


Domyślna konfiguracja zakłada:

    1920 x 1080


Inne rozdzielczości wyjściowe można skonfigurować poprzez:

    pointer_config.json


Fizyczny wyświetlacz komputera może mieć inną rozdzielczość.


Na przykład:

    Komputer:
        2560 x 1440

    OBS:
        1920 x 1080


Aplikacja automatycznie skaluje współrzędne.


Normalny kursor myszy systemu operacyjnego NIE jest ukrywany.


OBS CURSOR OVERLAY jest dodatkowym wizualnym kursorem renderowanym przez
OBS.


Dlatego jeśli leżący u podstaw pulpit jest widoczny w streamie,
zarówno normalny kursor systemu operacyjnego, jak i OBS CURSOR OVERLAY
mogą być potencjalnie widoczne jednocześnie.


Dla scen, w których jest to niepożądane, po prostu nie dodawaj do
tej sceny Browser Source OBS CURSOR OVERLAY.


======================================================================
48. PRZYKŁADOWA KONFIGURACJA STREAMU Z PLAYSTATION 5
======================================================================

Typowa konfiguracja streamu z PlayStation 5 może wyglądać
następująco:


    PS5
      |
      v
    Urządzenie do przechwytywania HDMI (HDMI Capture Device)
      |
      v
    OBS
      |
      +---- Rozgrywka (Gameplay)
      |
      +---- Kamera
      |
      +---- Audio
      |
      +---- OBS CURSOR OVERLAY
      |
      v
    YouTube / Twitch / Nagranie


Mysz komputera jest podłączona do komputera, na którym działa
OBS.


Sama konsola PS5 nie dostarcza kursora myszy komputera.


OBS CURSOR OVERLAY odczytuje pozycję myszy komputera i tworzy wizualny
kursor wewnątrz sceny OBS.


Pozwala to streamerowi używać myszy jako wizualnego narzędzia
wskazującego, podczas gdy widz widzi niestandardowy kursor.


======================================================================
49. PRZYKŁADOWA ORGANIZACJA SCEN
======================================================================

Przydatna konfiguracja OBS może wyglądać tak:


    Scena - PS5 Gameplay

        Gameplay
        Camera
        Game Audio
        Microphone
        OBS CURSOR OVERLAY


    Scena - Camera

        Camera
        Microphone


    Scena - Desktop

        Display Capture
        Camera
        Microphone


OBS CURSOR OVERLAY nie musi być dołączony do każdej sceny.


Jest to szczególnie ważne w przypadku scen z pulpitem, ponieważ
normalny kursor systemu operacyjnego może być tam już widoczny.


======================================================================
50. FILOZOFIA PROJEKTU
======================================================================

OBS CURSOR OVERLAY został celowo zaprojektowany tak, aby pozostać mały i
prosty.


Nie wymaga:

    - zewnętrznego serwera
    - usługi w chmurze
    - bazy danych
    - konta online
    - systemu uwierzytelniania
    - rozszerzenia przeglądarki
    - dedykowanej wtyczki OBS


Komunikacja odbywa się lokalnie:


    pointer.py
         |
         | lokalny WebSocket
         v
    pointer.html


Projekt jest zatem lekki i przenośny.


Wygląd wizualny jest oddzielony od logiki śledzenia myszy.


Umożliwia to tworzenie nowych projektów kursorów bez konieczności
przepisywania aplikacji Python.


======================================================================
                       KONIEC README
======================================================================
