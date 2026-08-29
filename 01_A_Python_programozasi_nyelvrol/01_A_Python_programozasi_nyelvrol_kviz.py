import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="A Python programozási nyelvről kvíz")


@app.cell
def _():
    import marimo as mo

    return (mo,)


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
def _(mo):
    q1_kerdes = mo.md(r"""
    **1. Mi történik, ha hivatkozni próbálunk egy értékre, melyet egy olyan cellában hoztunk létre, amit még nem futtattunk le?**
    """)

    def q1_visszajelzes(valasz):
        if valasz == "Hibát kapunk":
            return mo.callout(
                mo.md(
                    "✅ **Helyes!** Ha egy cellát még nem futtattunk le, az abban létrehozott érték még nem létezik, ezért a rá hivatkozás hibát eredményez."
                ),
                kind="success",
            )
        return mo.callout(
            mo.md(f"❌ A **{valasz}** válasz sajnos nem jó — próbáld újra!"),
            kind="danger",
        )

    def q1_frissites(valasz):
        mo.output.replace(mo.vstack([q1_kerdes, q1_valaszto, q1_visszajelzes(valasz)]))

    q1_valaszto = mo.ui.radio(
        options=[
            "A másik cella is automatikusan lefut, hogy ne kapjunk hibát",
            "Hibát kapunk",
        ],
        inline=True,
        label="Válassz egy választ!",
        on_change=q1_frissites,
    )
    mo.vstack([q1_kerdes, q1_valaszto])
    return


@app.cell(hide_code=True)
def _(mo):
    q2_kerdes = mo.md(r"""
    **2. A felsorolt tulajdonságok közül melyik NEM igaz a Python programozási nyelvre?**
    """)

    def q2_visszajelzes(valasz):
        if valasz == "Egyik leggyorsabb nyelv":
            return mo.callout(
                mo.md(
                    "✅ **Helyes!** A Python az egyik legolvasmányosabb és legsokoldalúbb programozási nyelv, azonban a futási sebesség nem az erőssége."
                ),
                kind="success",
            )
        return mo.callout(
            mo.md(f"❌ A **{valasz}** válasz sajnos nem jó — próbáld újra!"),
            kind="danger",
        )

    def q2_frissites(valasz):
        mo.output.replace(mo.vstack([q2_kerdes, q2_valaszto, q2_visszajelzes(valasz)]))

    q2_valaszto = mo.ui.radio(
        options=[
            "Logikus és átlátható formázás",
            "Rengeteg előre megírt kód",
            "Egyik leggyorsabb nyelv",
            "Platform független",
        ],
        inline=True,
        label="Válassz egy választ!",
        on_change=q2_frissites,
    )
    mo.vstack([q2_kerdes, q2_valaszto])
    return


@app.cell(hide_code=True)
def _(mo):
    q3_kerdes = mo.md(r"""
    **3. Az alábbiak közül melyik területen nem optimális a Python használata?**
    """)

    def q3_visszajelzes(valasz):
        if valasz == "Mobil alkalmazás írása":
            return mo.callout(
                mo.md(
                    "✅ **Helyes!** A Python kiváló választás általános problémamegoldáshoz, feladatok automatizálásához és gépi tanuláshoz, viszont mobil alkalmazások írására nem optimális."
                ),
                kind="success",
            )
        return mo.callout(
            mo.md(f"❌ A **{valasz}** válasz sajnos nem jó — próbáld újra!"),
            kind="danger",
        )

    def q3_frissites(valasz):
        mo.output.replace(mo.vstack([q3_kerdes, q3_valaszto, q3_visszajelzes(valasz)]))

    q3_valaszto = mo.ui.radio(
        options=[
            "Általános problémamegoldás",
            "Feladatok automatizálása",
            "Gép tanulás",
            "Mobil alkalmazás írása",
        ],
        inline=True,
        label="Válassz egy választ!",
        on_change=q3_frissites,
    )
    mo.vstack([q3_kerdes, q3_valaszto])
    return


@app.cell(hide_code=True)
def _(mo):
    q4_kerdes = mo.md(r"""
    **4. Hogyan tudunk a Python kódban leírást kapni parancsokról?**
    """)

    def q4_visszajelzes(valasz):
        if valasz == "help()":
            return mo.callout(
                mo.md(
                    "✅ **Helyes!** A beépített `help()` függvénnyel kaphatunk leírást a parancsokról, például: `help(print)`."
                ),
                kind="success",
            )
        return mo.callout(
            mo.md(f"❌ A **{valasz}** válasz sajnos nem jó — próbáld újra!"),
            kind="danger",
        )

    def q4_frissites(valasz):
        mo.output.replace(mo.vstack([q4_kerdes, q4_valaszto, q4_visszajelzes(valasz)]))

    q4_valaszto = mo.ui.radio(
        options=[
            "segitseg()",
            "help()",
            "help_me()",
            "Nem lehet leírást kapni a kódon belül",
        ],
        inline=True,
        label="Válassz egy választ!",
        on_change=q4_frissites,
    )
    mo.vstack([q4_kerdes, q4_valaszto])
    return


if __name__ == "__main__":
    app.run()
