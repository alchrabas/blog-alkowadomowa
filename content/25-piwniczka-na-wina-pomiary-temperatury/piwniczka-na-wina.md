Title: Piwniczka na wina — pomiary temperatury
Date: 2024-01-11 01:00:00
Category: działka
Tags: eksperymenty, działka
Summary: budowa piwniczki • temperatury • wnioski
PreviewImage: wykres-averaged.png

Rok 2022 (i 2023) naznaczony był pracą na mojej działce. Dwoma istotnymi elementami tego przedsięwzięcia były drzewka owocowe oraz piwniczka. Jej budowa, rozpoczęta tuż przed końcem 2021 roku, ciągnęła się dość długo, bo miałem bardzo konkretną wizję, której nie chciałem naginać do rzeczywistych możliwości.

![Zdjęcie poglądowe. U mnie wyglądało to podobnie]({attach}przyklad-montazu-piwniczki.png)

Piwniczka zbudowana była z gotowego betonowego zbiornika z dziurą na drzwi, a wejście do środka wprowadzało w klimat pustego szamba. Do tego potężna wichura zerwała w styczniu plandekę chroniącą wnętrze przed wpływaniem wody deszczowej, przez co pierwszym wyzwaniem na wiosnę 2022 było wypompowanie kilku tysięcy litrów wody z powstałego w ten sposób krytego basenu. Po przeprowadzeniu tej operacji konieczne było wstawienie drzwi, przekopanie odpływu wody, wyłożenie całości płytkami ceglanymi i urządzenie wnętrza w celu ułatwienia przechowywania napojów alkoholowych przy jednoczesnym utrudnieniu dostępu do nich osobom niepowołanym. W ten sposób uzyskałem dokładnie to, czego oczekiwałem.

<iframe width="800" height="450" src="https://www.youtube-nocookie.com/embed/UmjbNaWU0b8?si=jDPvRAnYky5Grdoq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

> „Napiłbym się dobrej żytniej. Takiej chłodnej, wiesz, prosto z piwniczki”  
> &ensp;&ensp;&ensp;&ensp;_Vesemir, Wiedźmin 3_

Drugim elementem całego przedsięwzięcia, nie mniej ważnym niż wygląd, było uzyskanie w środku odpowiedniej temperatury, tak aby Papa Vesemir był zadowolony. Na tym właśnie zamierzam skupić się w tym wpisie.

Jako osoba ceniąca naukowe podejście do wszelkich zagadnień związanych z alkoholem, na jesień 2022 (gdy piwniczka była mniej więcej szczelna, Stan Surowy Zamknięty) postanowiłem umieścić w niej termometr zbierający historię odczytów. Dane pobierane były co godzinę. Aby znać kontekst, drugi taki sam termometr umieściłem na zewnątrz tuż obok piwniczki, a że kupiłem też trzeci, to umieściłem go w sąsiednim (nieocieplonym) budynku drewnianym. W ciągu prawie 15 miesięcy zebrały w sumie ponad 31 tysięcy pomiarów, co pozwoliło na stworzenie dokładnych wykresów zmiany temperatur. O tym za chwilę, ale zacznę od przedstawienia miejsca pomiarów.

# Opis budowy ziemianki

Ziemianka składa się z betonowego prefabrykatu o wymiarach mniej więcej 2x3 metry, którego ściany mają 10 cm grubości. Sufit (półokrągły) i górna część ścian zabezpieczona jest od zewnątrz styrodurem (8 cm) oraz folią kubełkową, która przysypana jest w najcieńszym miejscu półmetrową warstwą ziemi.

Ściana frontowa zaizolowana jest sowitą, dwudziestocentymetrową warstwą styroduru oraz dodatkowo obłożona płytkami ceglanymi, co sprawiło, że jest to najbardziej ciepłoodporna część struktury. Do tego drzwi z Castoramy o współczynniku przenikania $U = 1,5\frac{m²K}{W}$ (opór cieplny wylicza się ze wzoru $R = \frac{1}{U}$ a ze współczynnika izolacyjności cieplnej $\lambda$ jest to $R = \frac{grubość}{\lambda}$) zostały dodatkowo zaizolowane pięciocentymetrową warstwą styroduru XPS i dekoracyjną warstwą desek sosnowych. Wiedząc też, że opory cieplne się sumują i znając wartości $\lambda$ z tablic, pozwala mi to wyliczyć wypadkowe $R_\text{wejścia}$ w następujący sposób:

$$
\lambda_{XPS} = 0,03 \frac{W}{mK} \\
\lambda_{\text{sosna w poprzek włókien}} = 0,16 \frac{W}{mK} \\
grubość_{\text{sosna}} = 0,03 m \\
grubość_{\text{XPS}} = 0,05 m \\
R_\text{drzwi} = \frac{1}{1,5} = 0,67\frac{m²K}{W} \\
R_\text{wejścia} = R_\text{sosna} + R_\text{XPS} + R_\text{drzwi} \\
R_\text{wejścia} = \frac{0,03}{0,16} + \frac{0,05}{0,03} + 0,67 = 0,1875 + 1,67 + 0,67 = 2,52 \frac{m²K}{W}
$$

Widać więc, że ta pięciocentymetrowa warstwa styroduru daje całkiem dużo. Z ciekawości, wyliczyłem też orientacyjny opór cieplny stropu, który składa się w przybliżeniu z 10 cm żelbetu, 8 cm styroduru i co najmniej pół metra gliniastej ziemi. Można wyliczyć z tego samego wzoru:

$$
\lambda_\text{żelbetu} = 1,7 \frac{W}{mK} \\
\lambda_\text{XPS} = 0,03 \frac{W}{mK} \\
\lambda_\text{ziemi} = 0,85 \frac{W}{mK} \\
R_\text{stropu} = R_\text{żelbetu} + R_\text{XPS} + R_\text{ziemi} \\
R_\text{stropu} = \frac{0,1}{1,6} + \frac{0,08}{0,03} + \frac{0,5}{0,85} = 0,0625 + 2,67 + 0,59 = 3,32 \frac{m²K}{W}
$$

Ponownie okazuje się, że największy wpływ na izolację termiczną ma materiał izolacyjny. Niby oczywiste, ale i tak trzeba ich sprawdzać.

Warto wspomnieć, że w przypadku liczenia całkowitego oporu cieplnego np. dla ścian domu, np. żeby wiedzieć czy spełnia normy, trzeba jeszcze dodać opory cieplne na powierzchni zewnętrznej ($R_{se}$) i wewnętrznej ($R_{si}$). Ja tego nie robię, bo do niczego tych wyników nie potrzebuję.

Co wynika z tego, że opór cieplny wejścia stanowi $2,52 \frac{m²K}{W}$, a stropu (i pewnie też ścian) $3,32 \frac{m²K}{W}$? Nie znaczy to, że więcej ciepła (lub zimna) wchodzi przez drzwi niż przez wszystkie ściany, bo ich powierzchnia jest znacznie większa. Ale drzwi stanowią mostek termiczny, który przepuszcza przez siebie stosunkowo więcej ciepła na metr kwadratowy.

Oczywiście wszystkie te obliczenia dają jedynie wartości orientacyjne, które co najwyżej pozwalają myśleć o proporcjach w skuteczności izolacji różnych elementów.

Za inny słaby punkt konstrukcji można uznać część ściany pod progiem drzwi — jako że cała betonowa konstrukcja stoi na warstwie piasku, zaizolowane jest jedynie kilka centymetrów pod progiem. Nie powinno mieć to jednak zbyt dużego wpływu latem, bo i tak jest tam chłodniej niż na otwartej przestrzeni. A zimna się nie boję, bo wiem, że poniżej zera nie zejdzie.

# Wilgotność

Długi czas walczyłem w piwniczce z wilgocią, spowodowaną zapewne po części niewystarczającą wentylacją. Nie zdecydowałem się na instalację wentylacji mechanicznej, a grawitacyjna (w postaci kilkunastometrowej podziemnej rury nawiewowej i pionowego komina wylotowego — prawie jak **Gruntowy Wymiennik Ciepła**) zdaje się nie pracować zbyt wydajnie. Przez większość lata wilgotność względna była na poziomie 80-85%, dlatego też postanowiłem użyć pochłaniacza wilgoci. Zacząłem od wariantu pasywnego na bazie soli, który coś tam zebrał, ale nie na tyle, by obniżyć wilgotność względną. Po tym zdecydowałem się kupić i uruchomić mały osuszacz elektryczny.

Wielkie było moje zdziwienie, gdy wszedłem do piwnicy z nowo kupionym osuszaczem i spojrzałem na higrometr. Przez dwa tygodnie od poprzednich odwiedzin wilgotność na nim spadła sama z siebie z 80 do 70%. Najwyraźniej się przestraszyła. No ale i tak odpaliłem osuszacz na kilka tygodni, żeby wartość spadła do długoterminowo bezpiecznego poziomu. Po kolejnym miesiącu efekt jest taki, że w środku utrzymuje się wilgotność 45%. Oznacza to, że wkrótce, gdy zdecyduję się wstawić tam zakupione niedawno drewniane beczki, to będę martwił się jak tę wilgotność podwyższyć.

# Pomiary i wnioski

Po ukończeniu całego cyklu rocznego (od października 2022 do stycznia 2024) możliwe jest wygenerowanie wykresów i, po kilku prostych przekształceniach, przeprowadzenie analizy uzyskanych wyników.

![Wykresy z danych zbieranych co godzinę. Z powodu dużych zmian między dniem i nocą jest całkowicie nieczytelny]({attach}wykres-oryginalny.png)

Pierwszym i najbardziej oczywistym wykresem jest porównanie chwilowych temperatur. Jako że różnice temperatur na zewnątrz pomiędzy porami dnia są bardzo duże i obniżają czytelność wykresu, to przekształciłem te pomiary do formy [średniej ruchomej](https://pl.wikipedia.org/wiki/%C5%9Arednia_ruchoma), gdzie temperatura w punkcie stanowi średnią z 24 godzin - 12 przed i 11 po. Taki wynik stanowi w przybliżeniu średnią dzienną, likwidując zwłaszcza jednorazowe wyskoki z powodu nietypowych zjawisk pogodowych. Warto zauważyć, że rozwiązanie takie wygładza wykres, ale nie powoduje utraty danych go tworzących — na przykład, zamiast trwającego godzinę skoku o 24 stopnie, na wykresie widoczny jest skok o 1 stopień przez 24 godziny.

![Wykres temperatury na zewnątrz i w piwniczce uśredniony średnią ruchomą]({attach}wykres-averaged.png)

Skupię się jednak na piwniczce. Zmiany temperatury tamże były bardzo niewielkie, poza wyjątkowymi sytuacjami, na przykład gdy drzwi musiały być otwarte z powodu prowadzonych prac. Udało mi się jednak wygładzić wykres w celu usunięcia artefaktów i widać jak wolno następują tam zmiany w warunkach normalnych. Po przejściu całego cyklu rocznego widać już, że dobrze zaizolowana piwniczka utrzymuje z lata kilka stopni więcej niż było rok temu. Oznacza to, że będę musiał dodatkowo wychłodzić ją przed wiosną.

![Widać wpływ temperatury na zewnątrz na piwniczkę, ale jest bardzo powolny]({attach}wykres-piwniczka.png)

Co jeszcze udało mi się zauważyć? Wykonałem jeszcze jedno przekształcenie, wyliczając wartość zwaną roboczo **współczynnikiem ciepła**. Jest to proporcja zmiany temperatur w środku do różnicy temperatur między wnętrzem a zewnętrzem.

$$
w = \frac{T'_\text{piwniczka}}{T_\text{piwniczka} - T_\text{zewnątrz}}, \text{dla temperatur w danej chwili}
$$

Innymi słowy, mówi jak bardzo temperatura zewnętrzna wpływa na temperaturę w środku. Wynik jest dość zaskakujący, bo okazuje się, ze większość kamieni milowych w procesie izolowania piwniczki nie miała przesadnie dużego wpływu na tę wartość. Dwoma kluczowymi datami są początek maja 2023 - koniec wykonywania izolacji ściany frontowej, a także początek lipca 2023 - wykonanie izolacji drzwi.

![]({attach}wykres-wspolczynnik-ciepla.png)

Dlaczego fioletowy **współczynnik ciepła** (prawie) zawsze jest dodatni? Bo prawie zawsze zmiana temperatury w piwniczce idzie w tym samym kierunku, co różnica między światem zewnętrznym a piwniczką. Obie wartości są dodatnie albo obie ujemne. Interesującą obserwacją dotyczącą wykresu jest to, że wpływ różnicy temperatur na temperaturę w piwniczce jest największy w sezonach przejściowych, a najmniejszy, gdy piwniczka osiąga swoje roczne ekstrema temperaturowe.

Możliwe, że dzieje się tak, ponieważ istnieje dodatkowe źródło zmian temperatury, którego nie biorę pod uwagę w obliczeniach. Temperatura ziemi na około dwóch metrach głębokości powinna, według mądrych wykresów w internecie, zmieniać się pomiędzy 3 a 13 stopni, co, zwłaszcza od strony niezaizolowanej, może mieć duży wpływ na zmiany temperatury w środku.

![Wykorzystanie informacji z tego wykresu pozwala mi, niczym Anteuszowi, czerpać energię z ziemi]({attach}temperatury-na-glebokosciach.jpg)

Nie jestem w stanie zweryfikować konkretnych wartości, ale ogólna zasada powinna się zgadzać. Ciężko mi wyobrazić sobie wciągnięcie tego parametru do moich, mocno przybliżonych, obliczeń, ale może będę w stanie oszacować to po kolejnym sezonie.

W ostatnim okresie **współczynnik ciepła** spada do bardzo niskich poziomów. MMoże to być powiązane z brakiem mojego łażenia wte i wewte, bo niemal wcale nie przebywam na działce, a każde otwarcie drzwi ma znaczenie.

# Wnioski

Wódeczka będzie chłodna.

Piwniczka nie działa tak doskonale, jak na to liczyłem, ale jest nieźle, zwłaszcza że izolacja była w stu procentach gotowa dopiero na początku lipca, gdy w środku było już ponad 14 stopni. Sprawia to, że w przyszłym sezonie musi być jeszcze lepiej. Mam podstawy, by być dobrej myśli i zawieźć do niej odpowiednią ilość alkoholu.
