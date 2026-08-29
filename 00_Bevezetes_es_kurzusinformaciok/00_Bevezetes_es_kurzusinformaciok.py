import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    [⚡ A kód futtatható verziójának a megnyitása ⚡](https://python-alapjai.pythonvilag.hu/00_Bevezetes_es_kurzusinformaciok/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Bevezetés
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Kezdjük az alapoktól! A *Python alapjai* sorozat elkezdéséhez semmi előismeretre nincsen szükséged. Közösen kezdjük el használni a Pythont és ismerkedünk meg a programozás alapvető építőelemeivel. Később ezeket kombináljuk és elmélyítjük tudásunk azáltal, hogy együtt oldunk meg feladatokat.

    Vágjunk is bele, a lejátszási listát az alábbi linken találod: [Python alapjai](https://www.youtube.com/playlist?list=PLQlAYHQ-8OLW9pllYvte10mZbjmNnZIjX)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Python környezet kialakítása
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A kód írásához és futtatásához a Notebook (jegyzetfüzet) formátumot fogjuk használni.

    Ez lehetővé teszi, hogy komolyabb előismeretek nélkül, a böngészőből tudjunk dolgozni, és ezáltal a lehető legegyszerűbben vághass bele a tanulásba és az alapok teljes megértésére tudj fókuszálni.

    A jegyzetfüzet legfontosabb tulajdonságai:
    - A jegyetfüzet cellákból áll.
    - 2 fő típusú cella létezik, a szöveg (markdown) és a kód (python).
    - A szöveget [markdown](https://www.markdownguide.org/cheat-sheet/) kóddal tudjuk formázni. Ha duplán rákattintunk egy szöveg cellára láthatóvá válik a kimenetet generáló kód.
    - Kód esetén egyszerűen belekattintunk a kódba és már szerkeszthetjük is.
    - Mindkét esetben a Shift + Enter billentyűk lenyomásával tudjuk menteni a változtatásokat.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Egyszerű példa Python kódra
    """)
    return


@app.cell
def _():
    print("Helló, világ!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Tananyag szerkezeti felépítése
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sokszor segít, ha már az elején látjuk, hogy pontosan miket is fogunk megtanulni. Lehet, hogy az itt felsorolt fogalmak közül sokat még nem ismersz, de ez nem probléma. Azért vagy itt (nagyon helyesen), hogy ezekkel megismerkedj.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    0. [Bevezetés és kurzusinformációk](https://python-alapjai.pythonvilag.hu/00_Bevezetes_es_kurzusinformaciok/)

    Itt vagy jelenleg. Ebben a leckében ismerjük meg a programozó környezetet, a tananyag felépítését, illetve a leckék során használt jelölésrendszert. <br> <br>

    1. [A Python programozási nyelvről](https://python-alapjai.pythonvilag.hu/01_A_Python_programozasi_nyelvrol/)

    Itt lesz szó arról, hogy miért olyan szuper a Python programozási nyelv, de a hiányosságokról is fogunk beszélni. Megértjük hogyan működik a futtatási folyamat nagy vonalakban, és hogy hol érdemes segítséget kérni ha elakadtál. <br> <br>

    2. [Változók, típusok és műveleteik](https://python-alapjai.pythonvilag.hu/02_Valtozok_tipusok_es_muveleteik_elmelet/)

    Bemutatásra kerülnek a változók, melyek az alapját képzik bármely programozásos feladatnak. Megtanulunk számokat/szöveget elmenteni a memóriába és különböző műveleteket végrehajtani rajtuk. <br> <br>

    3. [Komment, kiírás, bekérés](https://python-alapjai.pythonvilag.hu/03_Komment_kiiras_bekeres_elmelet/)

    Kiegészítjük a kódunkat megértést segítő megjegyzésekkel és megtanulunk kommunikálni a külvilággal adatok bekérésén és eredmények kiírásán keresztül. <br> <br>

    4. [Lista és dictionary](https://python-alapjai.pythonvilag.hu/04_Lista_es_dictionary_elmelet/)

    A következő lépés, hogy megtanuljuk milyen formában tudunk több összetartozó adatot együtt tárolni. Megismerjük ezek között a fontos különbségeket, és hogy melyiket milyen körülmények között érdemes használni. <br> <br>

    5. [Elágazások és igazságvizsgálat](https://python-alapjai.pythonvilag.hu/05_Elagazasok_es_igazsagvizsgalat_elmelet/)

    Létrehozunk olyan kódot, ami képes feltételekről eldönteni, hogy igazak-e, és ez alapján különbözőképpen viselkedik. <br> <br>

    6. [Ciklusok és iteráció](https://python-alapjai.pythonvilag.hu//06_Ciklusok_es_iteracio_elmelet/)

    Megtanuljuk, hogyan tudunk elemenként végigmenni összetartozó adatokon ciklusok segítségével. Majd összehasonlítjuk és elemezzük a ciklusok fajtáit.<br> <br>

    7. [Függvények létrehozása és meghívása](https://python-alapjai.pythonvilag.hu/07_Fuggvenyek_letrehozasa_es_meghivasa_elmelet/)

    Amikor egy algoritmust sokszor akarunk elvégezni, lehetőségünk van egyszer leprogramozni és a későbbiekben ugyanazt a kódrészletet meghívni. Ebben segítenek nekünk a függvények. <br> <br>

    8. [Szöveges fájlok olvasása és írása](https://python-alapjai.pythonvilag.hu/08_Szoveges_fajlok_olvasasa_es_irasa_elmelet/)

    Megtanuljuk a számítógépen található szöveges állományokat beolvasni, módosításokat végrehajtani rajtuk, majd kiírni őket egy új fájlba. <br> <br>

    9. [Hibakezelés és hibatípusok](https://python-alapjai.pythonvilag.hu/09_Hibakezeles_es_hibatipusok_elmelet/)

    Sokszor a program futása közben olyan nem várt esemény léphet fel amire nem tudtunk teljesen felkészülni. Ilyen esetekben meg lehet adni a programnak, hogy hol számítson hibákra és hogyan reagáljon rájuk. <br> <br>

    10. [Osztályok és példányaik](https://python-alapjai.pythonvilag.hu/10_Osztalyok_es_peldanyaik_elmelet/)

    Az osztályok (class) ismerete egy új utat nyit a programozás világában. Megtanuljuk hogyan tudunk összekapcsolni különböző paramétereket és függvényeket, hogy ezek segítségével új adattípusokat hozzunk létre. <br> <br>

    11. [Külső forrású kódok használata](https://python-alapjai.pythonvilag.hu/11_Kulso_forrasu_kodok_hasznalata_elmelet/)

    Itt fogjuk megtanulni, hogy hogyan tudunk mások által megírt kódot letölteni, meghívni a kódunkba és lefuttatni azt. <br> <br>

    12. [Virtuális környezet alkalmazása](https://python-alapjai.pythonvilag.hu/12_Virtualis_kornyezet_alkalmazasa/)

    Megnézzük milyen esetekben és hogyan érdemes a projektjeinknek külön környezetet létrehozni, ahol minden adott a futtatásukhoz. <br> <br>

    13. [Python fejlesztési környezetek](https://python-alapjai.pythonvilag.hu/13_Python_fejlesztesi_kornyezetek/)

    A kurzus által bemutatott böngészőben történtő programozás mellett számos egyéb módon lehet Python kódot írni. Ezeket mutatom be, hogy ki tudd választani a hosszútávon neked legjobban tetsző módszert.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Puska
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A leckék anyagát tömören összefoglaló puska (cheat sheet) az alábbi linken érhető el: [Python alapjai puska](https://github.com/PythonVilag/Python_alapjai)

    Érdemes lehet kinyomtatni, mert kezdetben nagyban meg tudja gyorsítani a programozást.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Jelölések
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Szövegbe integrált kódrészlet
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ezt a sort követi a kód, amit nem tudunk lefuttatni, mivel szöveg típusú cellába van integrálva.
    ```python
    print('Helló, világ!')
    ```
    Ez a sor már a kód után jön.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Általunk megadandó értékek
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Amikor a kódban a kötelező kulcsszavak mellett olyan helykitöltőt használok aminek a nevét nekünk kell majd megadni azt kacsacsőrök (`<>`) közé teszem és az elnevezésével utalok arra, hogy milyen jellegű értéket kell a helyére írni.

    ```python
    <változó neve> = <változó értéke>
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Kód futásának szemléltetése
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Valahányszor új, kicsit bonyolultabb koncepciókat tanulunk, lehetőség van a [https://pythontutor.com/](https://pythontutor.com/) által biztosított, beágyazott modul segítségével a kódot soronként lefuttatni, hogy pontosan lássuk, hogy hogyan és milyen sorrendben értékelődnek ki a parancsok.

    Azt ehhez tartozó kódrészlet a `Show code` gomb megnyomása után válik futtathatóvá, a lentebb látható módon.
    """)
    return


@app.cell
def _():
    print("Nincs itt semmi látnivaló!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Haladó tananyag (🐟)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Néhány helyen az alap tananyagot kiegészítem kicsit bonyolultabb gondolatokkal, melyket zárójelbe tett  hal emoji-val (🐟) jelölök.

    Ezek azt a célt szolgálják, hogy megmutassanak egy másik, sokszor "pythonosabb" megoldást egy adott problémára, vagy hogy betekintést adjanak, hogy az adott témában mire érdemes még rákeresni és alaposabban utánanézni a későbbiekben.

    Ezt azt is jelenti, hogy az adott anyagrész nem szükségszerű az alapok megértéséhez, de elég gyakori ahhoz, hogy találkozzunk vele a "nagyvilágban".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Vicces kép vagy videó (😊)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hogy a tananyag ~~kevésbé unalmas~~  könnyebben megjegyezhető legyen, megpróbáltam néhány helyen meme-ekkel kiegészíteni, melyeket a [https://www.reddit.com/r/ProgrammerHumor/](https://www.reddit.com/r/ProgrammerHumor/)-ról szereztem be.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Hibák keresése programozás során (😊)</summary>
    <img src="https://github.com/PythonVilag/Python_alapjai/blob/main/00_Bevezetes_es_kurzusinformaciok/data/debugging.gif?raw=true" alt="drawing" width="500"/>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Kiegészítő gondolatok
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A kiegészítő, csatolt gondolatokat a kiegészítendő cella alatt kisebb betűkkel jelölöm.
    ```python
    uj_valtozo = valtozo + 1
    ```

    <sup>Az előző érték megnőtt 1-el.</sup>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Feladatok
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Az első két bevezető órához nem tartozik még gyakorlat, de ha át szeretnéd ismételni az itt tanultakat, akkor a weboldalamon minden leckéhez tartoznak feleletválasztós kérdések: <br>
    [Bevezetés és kurzus információk](https://pythonvilag.hu/pv/python/python_alapjai/00_Bevezetes_es_kurzusinformaciok/)<br> <br>

    Ezen kívül extra feladat, hogy írd le, miért szeretnél megtanulni programozni. Ezt tedd ki magad elé az asztalra, hogy amikor nehezebb témákba vágjuk a fejszénket, akkor is legyen motivációd folytatni és végül befejezni a kurzust. <br> <br>

    Találkozunk a következő leckében!
    """)
    return


if __name__ == "__main__":
    app.run()
