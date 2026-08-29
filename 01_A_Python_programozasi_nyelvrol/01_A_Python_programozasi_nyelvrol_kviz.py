import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="A Python programozási nyelvről kvíz")


@app.cell
def _():
    import random

    import marimo as mo

    return mo, random


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    [← Vissza az elmélethez](../01_A_Python_programozasi_nyelvrol/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A Python programozási nyelvről — Kvíz

    Az alábbi kérdésekkel azonnal kiértékelheted, hogy mennyit tanultál ebből a leckéből. Kattints egy válaszra és a visszajelzés azonnal megjelenik.
    """)
    return


@app.cell(hide_code=True)
def _(mo, random):
    kerdesek = [
        {
            "kerdes": "**1. Mi történik, ha hivatkozni próbálunk egy értékre, melyet egy olyan cellában hoztunk létre, amit még nem futtattunk le?**",
            "lehetosegek": [
                "A másik cella is automatikusan lefut, hogy ne kapjunk hibát",
                "Hibát kapunk",
            ],
            "helyes": "Hibát kapunk",
            "magyarazat": "✅ **Helyes!** Ha egy cellát még nem futtattunk le, az abban létrehozott érték még nem létezik, ezért a rá hivatkozás hibát eredményez.",
        },
        {
            "kerdes": "**2. A felsorolt tulajdonságok közül melyik NEM igaz a Python programozási nyelvre?**",
            "lehetosegek": [
                "Logikus és átlátható formázás",
                "Rengeteg előre megírt kód",
                "Egyik leggyorsabb nyelv",
                "Platform független",
            ],
            "helyes": "Egyik leggyorsabb nyelv",
            "magyarazat": "✅ **Helyes!** A Python az egyik legolvasmányosabb és legsokoldalúbb programozási nyelv, azonban a futási sebesség nem az erőssége.",
        },
        {
            "kerdes": "**3. Az alábbiak közül melyik területen nem optimális a Python használata?**",
            "lehetosegek": [
                "Általános problémamegoldás",
                "Feladatok automatizálása",
                "Gép tanulás",
                "Mobil alkalmazás írása",
            ],
            "helyes": "Mobil alkalmazás írása",
            "magyarazat": "✅ **Helyes!** A Python kiváló választás általános problémamegoldáshoz, feladatok automatizálásához és gépi tanuláshoz, viszont mobil alkalmazások írására nem optimális.",
        },
        {
            "kerdes": "**4. Hogyan tudunk a Python kódban leírást kapni parancsokról?**",
            "lehetosegek": [
                "segitseg()",
                "help()",
                "help_me()",
                "Nem lehet leírást kapni a kódon belül",
            ],
            "helyes": "help()",
            "magyarazat": "✅ **Helyes!** A beépített `help()` függvénnyel kaphatunk leírást a parancsokról, például: `help(print)`.",
        },
    ]

    valaszok = {}

    def valasz_blokk(sorszam, adat, valasz):
        if valasz == adat["helyes"]:
            return mo.callout(mo.md(adat["magyarazat"]), kind="success")
        return mo.callout(
            mo.md(f"❌ A **{valasz}** válasz sajnos nem jó — próbáld újra!"),
            kind="danger",
        )

    def kviz_frissites():
        blokkok = []
        for sorszam, (radio, adat) in enumerate(radiok, start=1):
            blokk = [mo.md(adat["kerdes"]), radio]
            if sorszam in valaszok:
                blokk.append(valasz_blokk(sorszam, adat, valaszok[sorszam]))
            blokkok.append(mo.vstack(blokk))
        mo.output.replace(mo.vstack(blokkok))

    radiok = []
    for sorszam, adat in enumerate(kerdesek, start=1):
        lehetosegek = random.sample(adat["lehetosegek"], k=len(adat["lehetosegek"]))

        def valtozott(uj_valasz, sorszam=sorszam):
            valaszok[sorszam] = uj_valasz
            kviz_frissites()

        radiok.append(
            (
                mo.ui.radio(
                    options=lehetosegek,
                    inline=True,
                    label="Válassz egy választ!",
                    on_change=valtozott,
                ),
                adat,
            )
        )

    kviz_frissites()
    return


if __name__ == "__main__":
    app.run()
