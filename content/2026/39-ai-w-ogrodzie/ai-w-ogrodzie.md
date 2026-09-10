Title: AI w ogrodzie
Date: 2026-04-30 19:00:00
Category: inne
Tags: działka
Summary: AI wszędzie • NotebookLM • Claude
PreviewImage: notebook-thumbnail.png

Nie myślałem, że ten temat pojawi się akurat na tym blogu, bo unikam tu tematów związanych z pracą, ale wygląda, że inaczej się nie da. Zastanawiałem się jak wykorzystać sztuczną inteligencję w kontekście moich zainteresowań, skoro wszyscy korzystają z niej do wszystkiego, nawet jeśli w konkretnym zastosowaniu wydaje się nie mieć sensu. No i coś znalazłem.

Pierwsza myśl była taka, że skoro zdarza mi się, że pisanie jednego prostego artykułu potrafi zajmować ponad rok (bo zawsze jest coś lepszego do roboty), to może wrzucę szkielet wpisu oraz jakieś obrazki i niech AI wypluje treść. Po chwili zastanowienia stwierdziłem jednak, że sensem istnienia tego bloga jest pisanie tego, co chcę napisać, a nie _generowanie treści_. Nie zależy mi, żeby treści powstawały, bo i tak na nich nie zarabiam, ani żeby były wypuszczane szybko, bo wszystko mi jedno.

Ważne, żeby to, co piszę, było moimi słowami, bo robię to dla przyjemności.

I tak od lat używam AI-owych myślników, czyli dywizu — zamiast minusa -, bo tak podpowiada mi edytor PyCharm, więc nie będę próbował nikogo przekonać, że piszę to sam. Jeśli chcesz — mogę wygenerować tę odpowiedź w formacie pdf lub w formie infografiki. 💡

# NotebookLM

Jako że jestem żywym i leniwym człowiekiem, to zacząłem zastanawiać się w czym AI mogłoby mi realnie pomóc. Stwierdziłem, że tym tematem może być zarządzanie ogrodem. Przy okazji oceniłem, że w całości mnie w tym nie zastąpi, a jedynie usprawni pracę, czyli w sumie dla mnie dobrze.

Innymi słowy, używam narzędzi AI by pomógł mi w rzeczach, których bez niego bym nie zrobił, a przynajmniej często bym o nich zapominał.

![]({attach}notebook-thumbnail.png)

Zacząłem bawić się notatnikiem [NotebookLM](https://notebooklm.google.com/) od Google dopiero niedawno i nie jestem pewien czy jest to idealne rozwiązanie do moich zastosowań, ale jak na razie do trwałego przechowywania wiedzy sprawdza mi się najlepiej. Głównym zastosowaniem okazało się przechowywanie historii rzeczy, które robię na działce, i przypominanie co jeszcze powinienem tam zrobić.

Do mojego notatnika dodałem dwa źródła w formie dokumentów Google. Pierwszy to instrukcja:

> ## Instrukcje
> Nie jestem profesjonalistą, więc informacje dotyczące moich działań w źródłach nie powinny być wyznacznikiem właściwego zachowania względem roślin. Odpowiadaj mi z perspektywy doświadczonego ogrodnika/sadownika/winogrodnika i wykorzystuj wiedzę ekspercką, by doradzać w kwestii nawożenia, oprysków i innych czynności ogrodniczych. Proponuj zarówno oczywiste i obowiązkowe działania, jak i opcjonalne rzeczy, żeby dana uprawa miała się jeszcze trochę lepiej.

Drugi to arkusz kalkulacyjny zawierający w sobie następujące arkusze:

 - Rośliny — informacje o posiadanych przeze mnie roślinach, w tym: gatunek i odmiana, liczba, nasłonecznienie, wiek, jakość i ilość owoców, data posadzenia, data usunięcia
 - Obserwacje — wiersz opisuje pojedynczą obserwację rośliny danego dnia. Pozwala notatnikowi określić bieżący stan ogrodu i sugerować działania do podjęcia
 - Czynności — historia wszystkich działań dokonywanych w ogrodzie np. oprysk, nawożenie, przesadzanie
 - Dostępne opryski — lista posiadanych przeze mnie oprysków, nawozów itp. żeby notatnik sugerował mi w pierwszej kolejności użycie tego, co już mam

![Mój arkusz kalkulacyjny z obserwacjami]({attach}dokument-ogrod.png)

Teraz, wybierając się na roboty do ogrodu, mogę zapytać notatnik jakie czynności powinienem wykonywać. Częste zapisywanie obserwacji dotyczących rośliny sprawia, że sugestie dotyczące optymalnego terminu oprysku są dużo lepiej dostosowane do mojego przypadku. Jest to znacznie lepsze niż szukanie tego rodzaju informacji w internecie.  Mam nadzieję, że po kilku latach notowania będę w stanie uzyskać informacje w rodzaju „w tym roku wegetacja rozpoczęła się tydzień wcześniej niż zwykle, więc optymalnie będzie planować zrobienie X za kilka dni”.

Czy rozwiązuje to wszystkie problemy i sprawia, że nie muszę myśleć?

Nie do końca.

Stosuję to raczej jako przypominajkę dla rzeczy, które mógłbym przegapić, albo pomocnicze źródło danych. Mimo wszystko muszę umieć zweryfikować czy porada jest sensowna np. czy dawka nawozu się zgadza. Trzeba pamiętać, że AI, przynajmniej obecnie, ma z jednej strony tendencję do ulegania sugestii pytającego, a z drugiej zachęca czasem do podejmowania nadmiarowych działań.

Przykładowo, na podstawie zdjęcia z pleśnią w ziemi przy rozsadzie pomidorów, ChatGPT zareagował na zasadzie: „Szybko, wymiana ziemi, płukanie wodą utlenioną, ostatnia szansa, bo pomidory zginą!!!!111”, a inne źródła i moje doświadczenia sugerują, że jeśli po przesadzeniu będę bardziej ostrożny z podlewaniem, to zwykle powinno to wystarczyć. Tak też było w tym roku.

Dlatego też każdą sugestię warto zweryfikować w wiarygodnych źródłach i zapisać co się ostatecznie zrobiło.

# Claude

Widzę, że ostatnio [Claude](https://claude.ai) jest bardziej na topie niż ChatGPT, więc to właśnie jego postanowiłem wykorzystać jako uzupełnienie działania NotebookLM. Stworzyłem do niego skill, czyli powtarzalne zadanie, w którym nakazuję mu dokonać oceny stanu rośliny na podstawie zdjęcia. Wywołuje się go poprzez wspomnienie nazwy skilla, a Claude ogarnia resztę. Wynik w formie krótkiej notatki weryfikuję, po czym przeklejam do arkusza ogrodowego.

Skrócona treść mojego skilla:

```
Skill: Ocena stanu rośliny

Wcielasz się w doświadczonego ogrodnika-praktyka z wieloletnią wiedzą fenologiczną i znajomością
skali BBCH. Patrzysz na serię zdjęć i opisujesz każde z nich krótką notatką.

Zasady ogólne

Gatunek: Jeśli użytkownik podał gatunek – przyjmij bez kwestionowania. Zgaduj tylko gdy
nie podano.
...

Struktura notatki
Zdjęcie N – [Nazwa polska] ([Nazwa łacińska])
[Faza BBCH XX–XX], [opis aktualnego stanu fenologicznego].
[Ewentualne obserwacje: kondycja, zagrożenia, gleba, ściółka, uszkodzenia – tylko jeśli widoczne i zmienne].
Faza BBCH – jak opisywać
Podawaj przedział BBCH odpowiadający temu, co widać na zdjęciu.
```

Cała treść skilla do przeczytania [tutaj]({attach}SKILL.html).

![Skill opisujący wiśnię]({attach}opis-wisni.png)

Ogólnie nie pisałem tego skilla samodzielnie, bo Claude posiada skilla „tworzenie skilli”, czyli można mu krótko opowiedzieć czego się oczekuje, a on go stworzy: wyskoczy przycisk „dodaj” i wszystko będzie działać. W moim przypadku wystarczyło jedno zdanie oczekiwanych efektów i kilka przykładowych notatek. To może być nieoczywiste, ale często jest tak, że najlepsze prompty (polecenia) dla AI tworzy samo AI.

Używając tych dwóch narzędzi jestem w stanie uzyskać całkiem dobre rezultaty. Po pierwsze bez zbędnego wysiłku prowadzę historię stanu ogrodu. Po drugie dostaję przypomnienia o rzeczach, które powinienem zrobić, a wciąż do mnie należy decyzja czy i jak zareagować. Większość zaleceń i tak ignoruję, bo nie są kluczowe, ale kilka razy mi pomogły.

![Konwersacja w NotebookLM. Miedzian na parcha to niezbyt skuteczny pomysł]({attach}notebook-lm.png)

# Co dalej?

Cały czas jestem początkujący w kwestii zastosowania AI, więc spodziewam się, że już niedługo uznam powyższe porady za niewystarczające, ale w tej formie pomagają mi zarządzać ogrodem, więc myślę, że warto. Zachęcam do eksperymentowania, przynajmniej tak długo, jak powyższe narzędzia pozostają darmowe.
