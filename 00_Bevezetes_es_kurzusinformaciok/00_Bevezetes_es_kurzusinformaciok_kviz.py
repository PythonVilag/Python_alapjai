import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Bevezetés és kurzusinformációk kvíz")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Bevezetés és kurzusinformációk — Kvíz

    Az alábbi kérdésekkel azonnal kiértékelheted, hogy mennyit tanultál ebből a leckéből. Kattints egy válaszra és a visszajelzés azonnal megjelenik.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    q1_kerdes = mo.md(r"""
    **1. Az alábbi módszerek közül, melyik NEM futtatja le a kód típusú cellát Google Colab-ban?**
    """)

    def q1_visszajelzes(valasz):
        if valasz == "Enter megnyomása":
            return mo.callout(
                mo.md(
                    "✅ **Helyes!** Az `Enter` megnyomása csak új sort kezd a cellában. A kód lefuttatásához a `Shift` és `Enter` billentyűk együttes lenyomása vagy a cella melletti lejátszás gomb szükséges."
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
            "Lejátszás gomb a cella mellett",
            "Enter megnyomása",
            "Shift és Enter megnyomása",
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
    **2. Kód cellában, milyen karakter segítségével futtathatunk Linux parancsokat?**
    """)

    def q2_visszajelzes(valasz):
        if valasz == "!":
            return mo.callout(
                mo.md(
                    "✅ **Helyes!** A felkiáltójel (`!`) után írt parancsok Linux parancsként futnak le, például: `!pip install <csomag neve>`."
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
        options=["!", "?", "#", "/"],
        inline=True,
        label="Válassz egy választ!",
        on_change=q2_frissites,
    )
    mo.vstack([q2_kerdes, q2_valaszto])
    return


@app.cell(hide_code=True)
def _(mo):
    q3_kerdes = mo.md(r"""
    **3. Összesen hány leckéből áll a kurzus?**
    """)

    def q3_visszajelzes(valasz):
        if valasz == "14":
            return mo.callout(
                mo.md(
                    "✅ **Helyes!** A kurzus a `0`-s számozású bevezető leckével kezdődik, és a `13`-as számozású leckéig tart, ezáltal összesen 14 leckéből áll."
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
        options=["-1", "11", "13", "14"],
        inline=True,
        label="Válassz egy választ!",
        on_change=q3_frissites,
    )
    mo.vstack([q3_kerdes, q3_valaszto])
    return


@app.cell(hide_code=True)
def _(mo):
    q4_kerdes = mo.md(r"""
    **4. Milyen karakterek közé vannak téve az általunk megadandó értékek a struktúrák jelölése során?**
    """)

    def q4_visszajelzes(valasz):
        if valasz == "Kacsacsőr <>":
            return mo.callout(
                mo.md(
                    "✅ **Helyes!** Az általunk megadandó értékek helyét kacsacsőrök (`<>`) jelölik, például: `<változó neve> = <változó értéke>`."
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
            "Zárójel ()",
            "Szögletes zárójel []",
            "Kapcsos zárójel {}",
            "Kacsacsőr <>",
        ],
        inline=True,
        label="Válassz egy választ!",
        on_change=q4_frissites,
    )
    mo.vstack([q4_kerdes, q4_valaszto])
    return


if __name__ == "__main__":
    app.run()
