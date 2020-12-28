Title: Eksperyment - Powolne zlewanie nalewek
Date: 2020-12-16 23:00:00
Category: nalewki
Tags: nalewki, eksperymenty
Summary: zlewanie śliwkówki • zlewanie brzoskwiniówki • tabelka • wykresy • całki • czy warto czekać?
PreviewImage: sliwkowka_dm_nalew_by_dt.png

[W poprzednim wpisie]({filename}/4-zlewanie-brzoskwiniowki/zlewanie-brzoskwiniowki.md) opisywałem zlewanie nalewki brzoskwiniowej i dosypywanie do niej
cukru. Po dokonaniu prostych obliczeń czułem spory niedosyt, bo tak naprawdę nie wyjaśniło się, ile dodatkowego nalewu
pozwala uzyskać dodanie cukru.

Niestety napisanie tego posta zajęło mi znacznie więcej czasu niż chciałem, bo zbieranie danych zakończyłem już 27 listopada. Ale lepiej późno niż wcale.

## Spis treści

1. [Przebieg eksperymentu - śliwkówka](#przebieg-eksperymentu-sliwkowka)
    1. [Zlewanie nalewu z owoców](#zlewanie-nalewu-z-owocow)
    2. [Funkcja aproksymująca przyrost nalewu](#funkcja-aproksymujaca-przyrost-nalewu)
    3. [Uzyskanie i zlewanie syropu](#uzyskanie-i-zlewanie-syropu)
2. [Przebieg eksperymentu - Brzoskwiniówka](#przebieg-eksperymentu-brzoskwiniowka)
    1. [Funkcja aproksymująca przyrost nalewu](#funkcja-aproksymujaca-przyrost-nalewu_1)
    2. [Zlewanie syropu](#zlewanie-syropu)
    3. [Zalanie i zlewanie wody](#zalanie-i-zlewanie-wody)
    2. [Filtracja](#filtracja)
3. [Wnioski](#wnioski)
4. [Kod generujący wykresy](#kod-generujacy-wykresy)


## Obiekty badań - śliwka i brzoskwinia

Na szczęście, gdy przyszła mi chęć na poważniejsze zgłębienie tematu, cały czas w zanadrzu miałem ostatni słój
brzoskwiniówki, z którego wyniki mam szansę porównać z tymi wcześniejszymi. Do tego nadszedł czas, by zlać również śliwki -
owoce bardziej zwarte i wytwarzające znacznie mniej osadu. Uzyskanie szczegółowych informacji dotyczących przebiegu
zlewania nalewu i syropu cukrowego dałoby wgląd w ogólny przebieg tego procesu i wyciągnięcie wniosków, które być może
dałoby się rozszerzyć na wszystkie owoce.

# Przygotowanie do eksperymentu

Zacząłem od zważenia pustych słoików, a następnie zaplanowałem jakie parametry chcę śledzić. Najbardziej interesujące
moim zdaniem jest określenie zależności ilości wypływającego nalewu z owoców od czasu, a następnie ilości uzyskiwanego
syropu cukrowego od czasu. Pozwoli to stwierdzić, na ile cukier „wyciąga” dodatkowe soki. Warto będzie połączyć to z
badaniem czy uzyskiwany płyn składa się w większej części ze spirytusu czy cukru.

# Przebieg eksperymentu - Śliwkówka

Postanowiłem najpierw zlewać nalew ze słoja w takiej ilości, jaka sama wypłynie z owoców. Zlany przez sitko nalew trafi do drugiego, pustego słoja. Następnie zasypię owoce cukrem i w analogiczny sposób określę ilość uzyskanego syropu. Ocenię także ilość osadu odrzuconą w procesie filtrowania.

## Zlewanie nalewu z owoców

W chwili $t_0$ zlałem do drugiego słoja cały nalew, jaki wytworzył się z roztworu spirytusu i soków pochodzących z wnętrza przeciętych
śliwek. Było tego 2165 gramów, co oznacza, że już w tym momencie przekroczona została masa dwóch litrów spirytusu 70%
$m_\text{s70}$ ($\rho_\text{s70} = 0,88 \frac{\text{g}}{\text{cm^3}}$) = 1760 g i śliwki oddały z siebie o 405 gramów więcej niż wchłonęły. Nie mogę z całą pewnością stwierdzić, że oznacza to dokładnie 405 gramów soku w roztworze, bo równie dobrze może być go więcej, ale za cenę wniknięcia części spirytusu do owoców. Jestem niestety bardzo słabym chemikiem, ale sugestia, że stężenie spirytusu na zewnątrz i wewnątrz owoców będzie dążyło do równowagi, brzmi prawdopodobnie.

W tym momencie, po zlaniu nalewu nieznajdującego się w owocach, rozpoczęła się główna część eksperymentu: nalew powoli
wypływał z owoców i spływał na dno słoja, a ja w kilkugodzinnych odstępach przelewałem go przez sitko do oddzielnego słoja,
mierząc jednocześnie przyrost jego masy od ostatniego pomiaru. Pozwala to wyznaczyć przepływ ($S_\text{nalew}$), czyli przyrost masy nalewu od czasu.

$$S_\text{nalew} = \frac{\Delta m_\text{nalew}}{\Delta t}$$ 

<p class="text-center">Wzór 1. Przepływ nalewki</p>

Zgodnie z oczekiwaniami przyrost, na początku największy, po kilku godzinach zmniejszył się i dość stabilnie malał, co przedstawia poniższa tabela.

<table class="table table-striped table-bordered text-right">
<thead class="thead-light">
   <tr>
    <th>$$t [\text{h}]$$</th>
    <th>$$m_\text{nalew} [\text{g}]$$</th>
    <th>$$\Delta m_\text{nalew} [\text{g}]$$</th>
    <th>$$S_\text{nalew} [\frac{\text{g}}{\text{h}}]$$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0,0</td>
    <td>2165</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3,3</td>
    <td>2317</td>
    <td>152</td>
    <td>45,60</td>
  </tr>
  <tr>
    <td>15,3</td>
    <td>2460</td>
    <td>143</td>
    <td>11,92</td>
  </tr>
  <tr>
    <td>21,7</td>
    <td>2527</td>
    <td>67</td>
    <td>10,58</td>
  </tr>
  <tr>
    <td>27,5</td>
    <td>2581</td>
    <td>54</td>
    <td>9,26</td>
  </tr>
  <tr>
    <td>37,7</td>
    <td>2639</td>
    <td>58</td>
    <td>5,70</td>
  </tr>
  <tr>
    <td>43,2</td>
    <td>2668</td>
    <td>29</td>
    <td>5,27</td>
  </tr>
  <tr>
    <td>48,0</td>
    <td>2700</td>
    <td>32</td>
    <td>6,62</td>
  </tr>
  <tr>
    <td>52,3</td>
    <td>2721</td>
    <td>21</td>
    <td>4,85</td>
  </tr>
  <tr>
    <td>61,5</td>
    <td>2754</td>
    <td>33</td>
    <td>3,60</td>
  </tr>
  <tr>
    <td>71,5</td>
    <td>2782</td>
    <td>28</td>
    <td>2,80</td>
  </tr>
  <tr>
    <td>75,8</td>
    <td>2807</td>
    <td>25</td>
    <td>5,77</td>
  </tr>
  <tr>
    <td>85,7</td>
    <td>2838</td>
    <td>31</td>
    <td>3,15</td>
  </tr>
  <tr>
    <td>90,7</td>
    <td>2850</td>
    <td>12</td>
    <td>2,40</td>
  </tr>
</tbody>
</table>

<p class="text-center">Tabela 1. Ilość i przepływ nalewu wypływającego z owoców od czasu</p>

Po niespełna 4 dobach od rozpoczęcia eksperymentu przyrosty stały się na tyle małe, że uznałem kontynuację eksperymentu za bezcelową.

Wykres 1 przedstawia zmianę ilości nalewu od czasu, a wykres 2. stopniowy spadek przepływu wraz z upływem czasu. Chciałbym nazwać go pochodną masy nalewki po czasie, ale nie brzmiałoby to poważnie przy tak rzadkim próbkowaniu. Trzeba zaznaczyć tutaj, że zdecydowanie nie jest to funkcja monotoniczna, na co prawdopodobnie wpłynęły niedokładności pomiarowe. Przy okazji wykonywania obliczeń zbadałem także hipotezę, że położenie słoika na boku (tak, aby nalew miał mniej do przepłynięcia przed opuszczeniem słoja) pozwoli uzyskać większą ilość w jednostce czasu. Okazało się jednak, że różnica jest niezauważalna. Na wykresie 2. funkcja aproksymująca wyliczana jest z pominięciem pierwszego pomiaru, ponieważ już na pierwszy rzut oka dynamika wylewania się nalewu była wtedy zupełnie inna.

![Wykres 1. Masa zlanego nalewu od czasu]({attach}sliwkowka_m_nalew_by_t.png)

![Wykres 2. Zmiana przepływu nalewu od czasu]({attach}sliwkowka_dm_nalew_by_dt.png)

## Funkcja aproksymująca przyrost nalewu

Wzór funkcji aproksymującej (pomarańczowa krzywa na wykresie 2.), której współczynniki wyznaczone zostały przez bibliotekę Pandas, to:

$$
f(x) = e^{ax + b}, a = -0.0188, b = 2.6573
$$

<p class="text-center">Wzór 2. Funkcja aproksymująca przepływ nalewu śliwkowego</p>

Oczywiście, z chwilą wyznaczenia funkcji aproksymującej narzuca się wręcz pytanie: ile maksymalnie nalewu mógłbym uzyskać, gdybym postanowił poczekać nieskończenie wiele czasu, aż przeleje się wszystko (i zakładając, że wszelkie straty są zaniedbywalne)?

W tym celu konieczne jest wyliczenie całki powyższej funkcji. Nie jest to zadanie skomplikowane, ale jako że ze studiów pamiętam tylko jedną całkę: tę z $e^x$, to postaram się zrobić to tak, aby ta wiedza była wystarczająca. Zastosuję w tym celu metodę podstawiania:

$$
\int f(x) dx = \int e^{ax + b} dx = \left|\begin{array}{cl} v = ax + b \\ dv = adx \\ dx = \frac{dv}{a}\end{array}\right| = \int e^v \frac{dv}{a} = \frac{e^v}{a} + C = \frac{1}{a} e^{ax + b} + C
$$

<p class="text-center">Wzór 3. Funkcja aproksymująca ilość nalewu od czasu</p>

Mając wyznaczoną całkę nieoznaczoną, wyznaczenie wartości całki oznaczonej od chwili $t_1 = 3,3 [\text{h}]$ do nieskończoności jest zadaniem dość prostym. Jedyną trudnością jest fakt, że to całka niewłaściwa. Jak się to liczyło...? $ax + b$, jako że $a < 0$, dąży do $-\infty$, a $e$ z wykładnikiem dążacym do $-\infty$, więc cała granica dąży do zera.

$$
\int_{t_1}^{+\infty} f(x) dx = \lim_{x\to +\infty} \frac{1}{a} e^{ax+b} - \frac{1}{a} e^{a \cdot 3,3 + b} = 0 - \frac{1}{-0.0188} e^{2.59526} = - (-712.77) \approx 713
$$

<p class="text-center">Wzór 4. Wyznaczenie potencjalnego maksimum ilości nalewu</p>

To naturalnie przedział dla $t \in [3,3; +\infty]$, dlatego też trzeba dodać ilość zmierzoną eksperymentalnie dla przedziału $t \in [0; 3,3]$. Po zsumowaniu, ostateczny wynik to: $713 + 152 = 865$ gramów. W ciągu czterech dni udało mi się zebrać 685 gramów, czyli, wedle tych obliczeń, 80% możliwej ilości. Przez pozostałą wieczność mógłbym zebrać dodatkowo 180 gramów. Każdy musi zdecydować samodzielnie czy warto.

## Uzyskanie i zlewanie syropu

Do, wyglądających na suche, owoców (utraciły $\frac{1}{3}$ masy) wsypałem cukier, aby ten, wykorzystując swoje higroskopijne właściwości, wyciągnął z owoców resztę nalewu i zmienił się w syrop, który będzie mógł zostać połączony z nalewem.

Niektórzy owoce zalewają syropem - wodnym roztworem cukru - jednak nie widzę zalet takiego podejścia. Moim zdaniem im mniej doda się wody (najlepiej wcale), tym więcej będzie w stanie wyciągnąć z owoców cukier.

Aby obserwować prędkość uzyskiwania syropu, postanowiłem podzielić 1200 gramów cukru na trzy części: 600, 300 i 300 gramów, z których każdą rozpuszczałem oddzielnie. Kolejną partię dodawałem dopiero gdy zlałem do oddzielnego słoja cały syrop cukrowy z fazy poprzedniej. Ponieważ zlewanie nierozpuszczonego cukru mijało się moim zdaniem z celem, po wsypaniu cukru czekałem aż całkowicie się rozpuści. Stąd wzięły się bardzo długie przerwy między odczytami. Czas zlania po raz pierwszy syropu ze słoja oznaczyłem jako $t_0$. Następnie, podobnie jak w przypadku nalewu, zlewałem to, co w międzyczasie wypływało z owoców. Gdy przepływ $S_\text{syrop}$ zbliżył się do zera, wsypałem kolejną partię cukru i czekałem na jego całkowite rozpuszczenie. Wyniki tych działań przedstawia tabela 2.

<table class="table table-striped table-bordered text-right">
<thead class="thead-light">
  <tr>
    <th>$$t [\text{h}]$$</th>
    <th>$$m_\text{syrop} [\text{g}]$$</th>
    <th>$$\Delta m_\text{syrop} [\text{g}]$$</th>
    <th>$$S_\text{syrop} [\frac{\text{g}}{\text{h}}]$$</th>
    <th class="text-right">Uwagi</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0,0</td>
    <td></td>
    <td></td>
    <td></td>
    <td>dodanie 600 gramów cukru</td>
  </tr>
  <tr>
    <td>46,0</td>
    <td>1061</td>
    <td></td>
    <td>23,07</td>
    <td></td>
  </tr>
  <tr>
    <td>50,0</td>
    <td>1103</td>
    <td>42</td>
    <td>10,50</td>
    <td></td>
  </tr>
  <tr>
    <td>52,1</td>
    <td>1122</td>
    <td>19</td>
    <td>8,77</td>
    <td></td>
  </tr>
  <tr>
    <td>62,0</td>
    <td>1137</td>
    <td>15</td>
    <td>1,53</td>
    <td></td>
  </tr>
  <tr>
    <td>72,0</td>
    <td>1144</td>
    <td>7</td>
    <td>0,70</td>
    <td></td>
  </tr>
  <tr>
    <td>72,0</td>
    <td>1144</td>
    <td></td>
    <td></td>
    <td>Dodanie 300 gramów cukru</td>
  </tr>
  <tr>
    <td>119,0</td>
    <td>1590</td>
    <td>446</td>
    <td>9,49</td>
    <td></td>
  </tr>
  <tr>
    <td>119,0</td>
    <td>1590</td>
    <td></td>
    <td></td>
    <td>Dodanie 300 gramów cukru</td>
  </tr>
  <tr>
    <td>210,0</td>
    <td>1974</td>
    <td>384</td>
    <td>4,22</td>
    <td></td>
  </tr>
  <tr>
    <td>211,5</td>
    <td>2020</td>
    <td>46</td>
    <td>30,67</td>
    <td></td>
  </tr>
  <tr>
    <td>216,0</td>
    <td>2027</td>
    <td>7</td>
    <td>1,56</td>
    <td></td>
  </tr>
</tbody>
</table>

<p class="text-center">Tabela 2. Ilość i przyrost ilości syropu wypływającego z owoców od czasu</p>

Cukier dodawany był w czasach $t_0 = 0$, $t_1 = 72 [\text{h}]$, $t_2 = 119 [\text{h}]$. Okazało się, że przepływ syropu malał bardzo szybko po jego pierwszym zlaniu. Nie byłem tym bardzo zaskoczony, bo cukier prawdopodobnie nie wnika w owoce, a jedynie wyciąga z nich wodę (i inne smakowitości) samemu pozostając na zewnątrz, dzięki czemu łatwo jest przelać całość do drugiego słoja. Warto zwrócić uwagę na ilość syropu uzyskaną z kolejnych partii cukru.

<table class="table table-striped table-bordered text-right">
<thead class="thead-light">
  <tr>
    <th class="text-right">L.p.</th>
    <th>$$m_\text{cukier} [\text{g}]$$</th>
    <th>$$m_\text{syrop} [\text{g}]$$</th>
    <th>$$\frac{m_\text{syrop}}{m_\text{cukier}}$$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>600</td>
    <td>1144</td>
    <td>1,91</td>
  </tr>
  <tr>
    <td>2</td>
    <td>300</td>
    <td>446</td>
    <td>1,49</td>
  </tr>
  <tr>
    <td>3</td>
    <td>300</td>
    <td>436</td>
    <td>1,45</td>
  </tr>
</tbody>
</table>

<p class="text-center">Tabela 3. Ilość syropu uzyskana z kolejnych partii cukru</p>

![Wykres 3. Poglądowa ilość syropu od czasu (oś X nie zachowuje skali)]({attach}sliwkowka_m_syrop_by_t.png)

Wyniki są dość zaskakujące. Okazuje się, że ostatnia partia cukru pozwoliła uzyskać (proporcjonalnie) niewiele mniej syropu niż poprzednia. Masa końcowa samych śliwek wyniosła $m_\text{śliwki} = 1016 [\text{g}]$, co sprawia, że straciły niemal $\frac{2}{3}$ z początkowej masy 3000 gramów. Z całkowicie pewnego źródła informacji, jakim jest Internet, dowiedziałem się, że świeże śliwki mają 87% wody, a suszone 24%. Ubytek masy sugeruje, że pozbyłem się podobnej ilości wody co w procesie suszenia. Ich wygląd także przywodził na myśl wersję suszoną/wędzoną. Dla porównania, obok umieszam zdjęcie śliwek, które odłożyłem jako rzekomo „suche” podczas przygotowywania śliwkówki rok wcześniej. Różnica jest uderzająca.

![Śliwki. Na lewo: mocno wysuszone tegoroczne, na prawo: zeszłoroczne]({attach}suche_sliwki.png)

Jeśli chodzi o smak śliwek, to pozostały w zasadzie same skórki i smakowały mniej więcej jak żelki, choć były niemal całkowicie wyprane ze smaku. To doskonała wiadomość, bo oznacza, że smak w całości trafił do butelek.

# Przebieg eksperymentu - Brzoskwiniówka

Zacząłem analogicznie: od zlewania nalewu do drugiego słoja.

<table class="table table-striped table-bordered text-right">
<thead class="thead-light">
  <tr>
   <tr>
    <th>$$t [\text{h}]$$</th>
    <th>$$m_\text{nalew} [\text{g}]$$</th>
    <th>$$\Delta m_\text{nalew} [\text{g}]$$</th>
    <th>$$S_\text{nalew} [\frac{\text{g}}{\text{h}}]$$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0,0</td>
    <td>1714</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3,0</td>
    <td>1918</td>
    <td>204</td>
    <td>68,00</td>
  </tr>
  <tr>
    <td>5,4</td>
    <td>2026</td>
    <td>108</td>
    <td>44,69</td>
  </tr>
  <tr>
    <td>15,5</td>
    <td>2169</td>
    <td>143</td>
    <td>14,18</td>
  </tr>
  <tr>
    <td>21,0</td>
    <td>2245</td>
    <td>76</td>
    <td>13,82</td>
  </tr>
  <tr>
    <td>25,8</td>
    <td>2299</td>
    <td>54</td>
    <td>11,17</td>
  </tr>
  <tr>
    <td>30,2</td>
    <td>2351</td>
    <td>52</td>
    <td>12,00</td>
  </tr>
  <tr>
    <td>39,3</td>
    <td>2397</td>
    <td>46</td>
    <td>5,02</td>
  </tr>
  <tr>
    <td>49,3</td>
    <td>2442</td>
    <td>45</td>
    <td>4,50</td>
  </tr>
  <tr>
    <td>53,7</td>
    <td>2475</td>
    <td>33</td>
    <td>7,62</td>
  </tr>
  <tr>
    <td>63,5</td>
    <td>2510</td>
    <td>35</td>
    <td>3,56</td>
  </tr>
  <tr>
    <td>68,5</td>
    <td>2532</td>
    <td>22</td>
    <td>4,40</td>
  </tr>
  <tr>
    <td>73,5</td>
    <td>2554</td>
    <td>22</td>
    <td>4,40</td>
  </tr>
</tbody>
</table>

<p class="text-center">Tabela 4. Ilość nalewu uzyskana z brzoskwiń</p>

Wykresy 4 i 5 prezentują ilość nalewu i zmianę przepływu nalewu od czasu. Na wykresie 5. funkcja aproksymująca ignoruje pierwsze dwa wyniki, ponieważ różnią się znacznie od pozostałych. 

![Wykres 4. Ilość nalewu od czasu]({attach}brzoskwiniowka_m_nalew_by_t.png)

![Wykres 5. Zmiana przepływu nalewu od czasu]({attach}brzoskwiniowka_dm_nalew_by_dt.png)

## Funkcja aproksymująca przyrost nalewu

Tutaj nie będę się rozwodził i rozpisywał obliczeń. Jedyna różnica względem formuły dla śliwkówki jest odrzucenie dwóch, a nie jednego punktu. Funkcja aproksymująca przepływ (pomarańczowa krzywa na wykresie 5.) to:

$$
f(x) = e^{ax + b}, a = -0.0233, b = 2.9804
$$

<p class="text-center">Wzór 5. Funkcja aproksymująca przepływ nalewu brzoskwiniowego</p>

Potencjalne maksimum uzyskanego nalewu dla przedziału $t \in [5,4; +\infty]$ to:

$$
\int_{t_2}^{+\infty} f(x) dx = 0 - \frac{1}{-0.0233} e^{-0.0233 \cdot 5.4 + 2.9804} = 0 - (-745,37) \approx 745 
$$

<p class="text-center">Wzór 6. Możliwa do uzyskania ilość nalewu brzoskwiniowego</p>

Po doliczeniu 312 gramów z przedziału $t \in [0; 5,4]$ daje to 1057 gramów nalewu, czyli potencjalnie można by uzyskać o 217 gramów więcej.

## Zlewanie syropu

Drugi etap ponownie polegał na wsypaniu cukru, tym razem całych przewidzianych 400 gramów za jednym razem w chwili $t_0 = 0$.

<table class="table table-striped table-bordered text-right">
<thead class="thead-light">
  <tr>
    <th>$$t [\text{h}]$$</th>
    <th>$$m_\text{syrop} [\text{g}]$$</th>
    <th>$$\Delta m_\text{syrop} [\text{g}]$$</th>
    <th>$$S_\text{syrop} [\frac{\text{g}}{\text{h}}]$$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>46,0</td>
    <td>450</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>50,0</td>
    <td>519</td>
    <td>69</td>
    <td>17,25</td>
  </tr>
  <tr>
    <td>52,2</td>
    <td>552</td>
    <td>33</td>
    <td>15,23</td>
  </tr>
  <tr>
    <td>62,0</td>
    <td>593</td>
    <td>41</td>
    <td>4,17</td>
  </tr>
  <tr>
    <td>72,0</td>
    <td>614</td>
    <td>21</td>
    <td>2,10</td>
  </tr>
</tbody>
</table>

<p class="text-center">Tabela 5. Ilość syropu uzyskana z 400 gramów cukru</p>

Po niespełna dwóch dobach cukier rozpuścił się, dając syrop o nieznacznie większej masie. Widać tu inne zachowanie brzoskwiń w porównaniu ze śliwkami. Nie cały syrop uzyskałem za jednym razem, a kolejne godziny sprawiły, że wypłynęło go zauważalnie (o $\frac{1}{3}) więcej.

## Zalanie i zlewanie wody

Tutaj doszło do kolejnej zmiany. Zamiast w tym momencie zakończyć i wlać przewidziane przez przepis 600 mililitrów wody do słoja z syropem, postanowiłem wlać ją do do słoja z owocami, aby zobaczyć, czy uda się wyciągnąć w ten sposób choć trochę smaku lub ewentualne resztki nierozpuszczonego cukru.

<table class="table table-striped table-bordered text-right">
<thead class="thead-light">
  <tr>
    <th>$$t [\text{h}]$$</th>
    <th>$$m_\text{syrop+woda} [\text{g}]$$</th>
    <th>$$\Delta m_\text{syrop+woda} [\text{g}]$$</th>
    <th>$$S_\text{syrop+woda} [\frac{\text{g}}{\text{h}}]$$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0,0</td>
    <td>819</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>1,0</td>
    <td>881</td>
    <td>62</td>
    <td>62,00</td>
  </tr>
  <tr>
    <td>4,0</td>
    <td>971</td>
    <td>90</td>
    <td>30,00</td>
  </tr>
  <tr>
    <td>14,0</td>
    <td>1015</td>
    <td>44</td>
    <td>4,40</td>
  </tr>
  <tr>
    <td>19,0</td>
    <td>1044</td>
    <td>29</td>
    <td>5,80</td>
  </tr>
  <tr>
    <td>43,0</td>
    <td>1095</td>
    <td>51</td>
    <td>2,13</td>
  </tr>
  <tr>
    <td>48,0</td>
    <td>1121</td>
    <td>26</td>
    <td>5,20</td>
  </tr>
</tbody>
</table>

<p class="text-center">Tabela 6. Ilość syropu uzyskana z resztki cukru zmieszanej z 600 gramami wody</p>

Efekt widoczny jest w tabeli 6. i, choć nietypowy, to nie jest zaskakujący. 600 mililitrów wody zostało wchłonięte przez owoce i na początku tylko około $\frac{1}{3}$ wody mogła zostać odzyskana. W ciągu kolejnych kilkudziesięciu godzin udało się odzyskać w sumie 507 gramów płynu. Jednak najbardziej interesująca jest informacja: czy ma to jakikolwiek sens? Innymi słowy: czy pozwala uzyskać z owoców coś więcej? Niestety z braku odpowiedniej aparatury nie umiem udzielić obiektywnej odpowiedzi na to pytanie. Jedyną obserwacja, jaką mogłem dokonać, to ocena wyglądu i smaku. Płyn ma lekko brzoskwiniowy odcień. Nie da się wyczuć w nim ani cienia słodyczy, jednakże dość wyczuwalny jest alkohol. Oznacza to, że coś w tej wodzie jest, ale trudno stwierdzić, czy jest to ilość mająca jakiekolwiek znaczenie. W przyszłości prawdopodobnie odpuszczę sobie zalewanie wodą suchych owoców.

![Płyn uzyskany na koniec zlewania wody z owoców]({attach}ostatnia-krztyna-brzoskwiniowki.png)

## Filtracja

Ostatnim etapem przed butelkowaniem jest filtrowanie nalewki. Brzoskwinie zawierają ogromną ilość zanieczyszczeń, które pojawiają się zarówno w toku maceracji, jak i rozpuszczania cukru na syrop.

Proces filtrowania był następujący: nalew zlałem wężykiem znad osadu, a resztę przefiltrowałem za pomocą worka filtracyjnego. Następnie zmieszałem go z syropem. Miało to na celu zmniejszenie stężenia cukru, aby nie zaklejał on worka filtracyjnego, ale sprawiło to jednocześnie, że nie mogę stwierdzić ile zanieczyszczeń było w samym syropie, a ile dostało się z części nalewu zlanej znad osadu. Po odczekaniu na opadnięcie zanieczyszczeń na dno, ponownie zlałem całość znad osadu i przefiltrowałem pozostałość z dna.

W tym przypadku okazało się, że w 3536 gramach nieprzefiltrowanej nalewki znajduje się 405 gramów fusów, w tym z nalewu usunięte zostało ich 124 gramy. Efekt końcowy to 3131 gramów gotowej nalewki.

![Po lewej: osad, po prawej: przefiltrowana nalewka]({attach}nalewka_i_osad.png)

# Wnioski

Niestety, jak na tak długie obliczenia, wniosków nie mam wiele. Po pierwsze warto poczekać i co najmniej przez kilka godzin zlewać nalew z owoców przed dodaniem cukru. W zależności od pokładów cierpliwości, można wyciągnąć z owoców bardzo dużo. Do tego potwierdziłem doświadczalnie, że cukier ma zdolności higroskopijne. Ciekawie byłoby, gdyby eksperyment wykazał coś zupełnie przeciwnego. Brak grupy kontrolnej nie pozwala mi wygłaszać jednoznacznego werdyktu, ale myślę, że teza, iż lepiej zacząć od zalewania owoców spirytusem, a później zasypywać cukrem, jest znacznie bardziej prawdopodobna niż warianty alternatywne.

# Kod generujący wykresy

Kod generujący wykresy, wraz z instrukcją ich uruchomienia, znajduje się w [repozytorium bloga na GitHubie](https://github.com/alchrabas/blog-alkowadomowa/tree/master/content/5-eksperyment-zlewanie-nalewki/scripts).

Dziękuję bratu za ogólną pomoc i wyznaczenie parametrów funkcji aproksymujących oraz narysowanie wykresów.
