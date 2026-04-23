Title: AI w ogrodzie
Date: 2026-06-10 01:00:00
Category: inne
Tags: działka
Status: draft
Summary: AI wszędzie • zastosowania u mnie • rozwój

Nie myślałem, że ten temat pojawi się akurat na tym blogu, bo unikam tu tematów związanych z moją pracą, ale wygląda, że inaczej się nie da. Zastanawiałem się jak wykorzystać AI w kontekście moich zainteresowań, skoro wszyscy korzystają z niego do wszystkiego, nawet jeśli w konkretnym zastosowaniu wydaje się nie mieć sensu, no i coś znalazłem.

Pierwsza myśl była taka, że skoro zdarza mi się, że pisanie jednego prostego artykułu potrafi zajmować mi ponad rok (bo zawsze jest co innego do roboty), to może wrzucę szkielet wpisu oraz jakieś obrazki i niech AI wypluje treść. Po chwili zastanowienia stwierdziłem jednak, że sensem istnienia tego bloga jest pisanie tego, co chcę napisać, a nie _generowanie treści_. Nie zależy mi, żeby treści powstawały, bo i tak na nich nie zarabiam, ani żeby były wypuszczane szybko, bo wszystko mi jedno.

Ważne, żeby to, co piszę, było moimi słowami, bo robię to dla przyjemności.

I tak od lat używam AI-owych myślników, czyli dywizu — zamiast minusa -, bo tak podpowiada mi edytor PyCharm, więc nie będę próbował nikogo przekonać, że piszę to sam. Czy zamiast tego chcesz wygenerować tę odpowiedź w formacie pdf lub w formie infografiki?

# NotebookLM

Jako że jestem żywym i leniwym człowiekiem, to zacząłem zastanawiać się w czym AI mogłoby mi realnie pomóc. Stwierdziłem, że tematem może być zarządzanie ogrodem. Przy okazji oceniłem, że w całości mnie w tym nie zastąpi, a jedynie usprawni pracę, czyli w sumie dobrze.

Innymi słowy, używam narzędzi AI do rzeczy, których bez tego nie zrobiłbym wcale, a przynajmniej często bym o nich zapominał.

Zacząłem bawić się tym narzędziem dopiero niedawno i nie jestem pewien czy jest to idealne rozwiązanie do moich zastosowań, ale jak na razie sprawdził się najlepiej do trwałego przechowywania wiedzy.

Do mojego notatnika dodałem dwa źródła w formie dokumentu Google. Pierwszy to instrukcja:

> ## Instrukcje
> Nie jestem profesjonalistą, więc informacje dotyczące moich działań w źródłach nie powinny być wyznacznikiem właściwego zachowania względem roślin. Odpowiadaj mi z perspektywy doświadczonego ogrodnika/sadownika/winogrodnika i wykorzystuj wiedzę ekspercką by doradzać w kwestii nawożenia, oprysków i innych czynności ogrodniczych. Proponuj zarówno oczywiste i obowiązkowe działania, jak i opcjonalne rzeczy, żeby dana uprawa miała się jeszcze trochę lepiej.

Drugi to arkusz kalkulacyjny zawierający w sobie następujące arkusze:

 - Rośliny - informacje o posiadanych przeze mnie roślinach, w tym: gatunek i odmiana, liczba, nasłonecznienie, wiek, jakość i ilość owoców, data posadzenia, data usunięcia
 - Obserwacje - opisuje pojedynczą obserwację rośliny danego dnia. Pozwala notatnikowi określić bieżący stan ogrodu i sugerować działania do podjęcia
 - Czynności - historia wszystkich działań dokonywanych w ogrodzie np. oprysk, nawożenie, przesadzanie
 - Dostępne opryski - lista posiadanych przeze mnie oprysków, nawozów itp. żeby notatnik sugerował mi w pierwszej kolejności użycie tego, co już mam

Teraz, wybierając się na roboty do ogrodu, mogę pytać notatnik jakie czynności powinienem wykonywać. Częste zapisywanie obserwacji dotyczących rośliny sprawia, że sugestie dotyczące optymalnego terminu oprysku są dużo lepiej dostosowane do mojego przypadku. Jest to znacznie lepsze niż szukanie tego rodzaju informacji w internecie.  Mam nadzieję, że po kilku latach takiego notowania będę w stanie uzyskać informacje w rodzaju "w tym roku wegetacja rozpoczęła się tydzień wcześniej niż zwykle, więc optymalnie będzie zrobić X za kilka dni". 

Czy rozwiązuje to wszystkie problemy i sprawia, że nie muszę myśleć? Nie do końca. Stosuję to raczej jako przypominajkę dla rzeczy, które mógłbym przegapić, albo pomocnicze źródło danych. Mimo wszystko muszę umieć zweryfikować czy porada jest sensowna albo np. dawka nawozu się zgadza. Trzeba pamiętać, że AI, przynajmniej obecnie, ma z jednej strony tendencję do ulegania sugestii pytającego, a z drugiej zachęca czasem do podejmowania nadmiarowych działań. Przykładowo, na podstawie zdjęcia z pleśnią na ziemi przy rozsadzie pomidorów, ChatGPT zareagował na zasadzie: "Szybko, wymiana ziemi, płukanie wodą utlenioną, ostatnia szansa, bo pomidory zginą!!!!111", a inne źródła i moje doświadczenia sugerują, że jeśli po przesadzaniu będę bardziej ostrożny z podlewaniem, to zwykle to wystarczy.

# Claude

Widzę, że ostatnio Claude jest bardziej na topie niż ChatGPT, więc postanowiłem wykorzystać go jako uzupełnienie działania NotebookLM. Stworzyłem do niego skill, czyli powtarzalne zadanie, w którym nakazuję mu dokonać oceny stanu rośliny na podstawie zdjęcia. Wynik w formie krótkiej notatki weryfikuję, po czym przeklejam do arkusza ogrodowego.