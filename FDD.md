FDD-Põhine Projektikava: TTHK Koduleht
1. Ülevaade (Overall Model)
Loome kaasaegse ja kasutajasõbraliku kodulehe Tallinna Tööstushariduskeskusele. Veebileht sisaldab kooli infot, erialade tutvustusi, kontaktandmeid ja uudiseid. Projekti eesmärk on pakkuda funktsionaalset ja informatiivset keskkonda õppuritele, õpetajatele ning huvilistele.

2. Funktsioonide loetelu (Feature List)
Funktsioonid on grupeeritud funktsionaalsetesse alajaotustesse:

Avaleht
F001: Kuvada kooli tervitustekst

F002: Kuvada sissejuhatus õppimisvõimalustest

F003: Lülituda keele vahel (ET/EN)

Erialad
F004: Kuvada erialade loetelu

F005: Kirjeldada iga eriala (nt IT, elektrik, kokk)

F006: Mitmekeelsus erialade sisus

Uudised
F007: Kuvada uudiste loend

F008: Lisada staatiline uudiste sisu

F009: Kuupäevade ja sündmuste korrektne vormistus

Kontakt
F010: Kuvada kooli kontaktandmed (telefon, e-post, aadress)

F011: Lisada asukoha kaart (Could have)

F012: Mitmekeelne kontaktileht

3. Planeerimine ja iteratsioonid (Feature Planning & Design by Feature)
Iteratsioon 1: Põhistruktuur ja navigeerimine
F001, F002, F004, F010

Disain ja ehitus: menüüriba, HTML-struktuur, CSS-stiilid

Iteratsioon 2: Mitmekeelsus ja infosektsioonid
F003, F005, F006, F012

Keelelülitus rakendatud URL-parameetriga

Dünaamiline sisusõltuvus keelevalikust

Iteratsioon 3: Uudised ja viimistlus
F007, F008, F009, F011 (osaliselt)

Kujunduse täiendamine, mobiilitugi

Stiilivastavus kooli visuaalile

4. Ehitamine funktsioonide kaupa (Build by Feature)
Iga funktsioon rakendatakse väikese iseseisva kooditükina (nt @app.route) ja testitakse koheselt. Arendusmeeskond (1 disainer, 2 arendajat, 1 tester) jagab funktsioonid vastavalt pädevustele.

5. Lõpptulemus ja esitlus
Valmis: kõik „Must have“ funktsioonid, suurem osa „Should have“

Koduleht toimib nii mobiilis kui arvutis

Sisu on selge ja keeleliselt vahetatav

Esitlus: demo toimivast lahendusest + väärtuste esiletoomine (nt ligipääsetavus, kasutusmugavus)

