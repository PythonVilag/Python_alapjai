import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="A Python programozási nyelvről")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    [⚡ A kód futtatható verziójának a megnyitása ⚡](https://python-alapjai.pythonvilag.hu/01_A_Python_programozasi_nyelvrol/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Általános információk
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Futtatás
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - A program futásának sorrendjét a cellák futtatási sorrendje határozza meg.

    - Egy cellán belül a Python kód fentről lefelé, soronként értékelődik ki.

    - A kód futtatásához kattintsunk a cellába és nyomjuk meg a Shift + Enter billentyű kombinációt.

    - Egy cellát többször is lefuttathatunk.

    - Ha a cellának van kimenete az a cella alatt jelenik meg.

    - Ha hamarabb hivatkozunk egy elemre, minthogy létrehozzuk azt, hibát kapunk.

    - Az elmentett változók törölhetők a futtatókörnyezet újraindításával: "Futtatókörnyezet → Futtatókörnyezet újraindítása".
    """)
    return


@app.cell
def _():
    print("Az elsőtől mindenkinek úúú de klassz a kedve.")
    print("A második a rossz dolgokat varázsolja szebbre.")
    return


@app.cell
def _():
    print("A második a rossz dolgokat varázsolja szebbre.")
    print("Az elsőtől mindenkinek úúú de klassz a kedve.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A Python bemutatása
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A Python bemutatást tartalmazó prezentáció: [link](https://github.com/PythonVilag/Python_alapjai/blob/main/01_A_Python_programozasi_nyelvrol/data/Python_bemutatasa/Python_bemutatasa.pdf)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Pszeudokód átalakítása Python kóddá (😊)</summary>
    <img src="https://github.com/PythonVilag/Python_alapjai/blob/main/01_A_Python_programozasi_nyelvrol/data/pseudo.jpg?raw=true" alt="drawing" width="500"/>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A Python működése (🐟)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A Python működését ismertető prezentáció: [link](https://github.com/PythonVilag/Python_alapjai/blob/main/01_A_Python_programozasi_nyelvrol/data/Python_mukodese/Python_mukodese.pdf)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Segítségkérés
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Mivel a tananyag nem tud az elérhető parancsok minden apró részletére kitérni, így fontos, hogy mi magunk is meg tudjuk keresni bizonyos problémákra a választ.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Internetes
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Google kereséssel
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Google-be írjuk be a problémát angolul kompakt módon kulcsszavak használatával.

    Az alábbi weboldalakon lehet a legnagyobb esélyünk megtalálni amit keresünk:
    - [https://docs.python.org/](https://docs.python.org/)

    - [https://stackoverflow.com/](https://stackoverflow.com/)

    - [https://www.w3schools.com/](https://www.w3schools.com/)

    - [https://realpython.com/](https://realpython.com/)

    - [https://www.geeksforgeeks.org/](https://www.geeksforgeeks.org/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Kommentben
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ha valamivel elakadnál vagy egy része a tananyagnak nem lenne tiszta, akkor írd meg kommentben a videó alatt. Megpróbálok én is segíteni, vagy mások is segíthetnek akik már utánajártak a dolognak.

    Ehhez hasonlóan nézz rá te is a kommentekre és segíts másoknak, ha meg van hozzá a tudásod és az időd! :)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Internetes fórumokon
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ha a korábbiak közül egyik sem vált be, akkor még megérhet egy próbát [Reddit](https://www.reddit.com/)-en segítséget kérni.

    Itt található a csatorna dedikált közössége [r/PythonVilag](https://www.reddit.com/r/PythonVilag/) néven.

    Ezen kívül, ha magyarul kérdeznél, akkor az [r/programmingHungary](https://www.reddit.com/r/programmingHungary/) oldalt érdemes megpróbálni, ha viszont angolul is meg tudod fogalmazni a kérdést, akkor az [r/learnpython](https://www.reddit.com/r/learnpython/) oldalon még több felhasználó tud segíteni.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Programkódos
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A `help` parancsot meghívva betekintést kapunk a hivatalos dokumentációba.
    """)
    return


@app.cell
def _():
    help
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Segítségkérés Pythonban (😊)</summary>
    <img src="https://github.com/PythonVilag/Python_alapjai/blob/main/01_A_Python_programozasi_nyelvrol/data/help.jpg?raw=true" alt="drawing" width="500"/>
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Vagy még specifikusabb adatra meghívva a `help()`-et további információkhoz tudunk jutni
    """)
    return


@app.cell
def _():
    help()
    return


@app.cell
def _():
    help(str)
    return


@app.cell
def _():
    help(str.startswith)
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
    Ahogy az előző órán már szó volt róla ehhez az anyaghoz sem tartozik még gyakorlat, de ha át szeretnéd ismételni az itt tanultakat, akkor a weboldalamon minden leckéhez tartoznak feleletválasztós kérdések: <br>
    [A Python programozási nyelvről](https://pythonvilag.hu/pv/python/python_alapjai/01_A_Python_programozasi_nyelvrol/)<br> <br>

    Találkozunk a következő leckében!
    """)
    return


if __name__ == "__main__":
    app.run()
