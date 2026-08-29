import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Bevezetés és kurzusinformációk kvíz")


@app.cell
def _():
    import random

    import marimo as mo

    return mo, random


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Bevezetés és kurzusinformációk — Kvíz

    Az alábbi kérdésekkel azonnal kiértékelheted, hogy mennyit tanultál ebből a leckéből. Kattints egy válaszra és a visszajelzés azonnal megjelenik.
    """)
    return


@app.cell(hide_code=True)
def _(mo, random):
    kerdesek = [
        {
            "kerdes": "**1. Az alábbi módszerek közül, melyik NEM futtatja le a kód típusú cellát Google Colab-ban?**",
            "lehetosegek": [
                "Lejátszás gomb a cella mellett",
                "Enter megnyomása",
                "Shift és Enter megnyomása",
            ],
            "helyes": "Enter megnyomása",
            "magyarazat": "✅ **Helyes!** Az `Enter` megnyomása csak új sort kezd a cellában. A kód lefuttatásához a `Shift` és `Enter` billentyűk együttes lenyomása vagy a cella melletti lejátszás gomb szükséges.",
        },
        {
            "kerdes": "**2. Kód cellában, milyen karakter segítségével futtathatunk Linux parancsokat?**",
            "lehetosegek": ["!", "?", "#", "/"],
            "helyes": "!",
            "magyarazat": "✅ **Helyes!** A felkiáltójel (`!`) után írt parancsok Linux parancsként futnak le, például: `!pip install <csomag neve>`.",
        },
        {
            "kerdes": "**3. Összesen hány leckéből áll a kurzus?**",
            "lehetosegek": ["-1", "11", "13", "14"],
            "helyes": "14",
            "magyarazat": "✅ **Helyes!** A kurzus a `0`-s számozású bevezető leckével kezdődik, és a `13`-as számozású leckéig tart, ezáltal összesen 14 leckéből áll.",
        },
        {
            "kerdes": "**4. Milyen karakterek közé vannak téve az általunk megadandó értékek a struktúrák jelölése során?**",
            "lehetosegek": [
                "Zárójel ()",
                "Szögletes zárójel []",
                "Kapcsos zárójel {}",
                "Kacsacsőr <>",
            ],
            "helyes": "Kacsacsőr <>",
            "magyarazat": "✅ **Helyes!** Az általunk megadandó értékek helyét kacsacsőrök (`<>`) jelölik, például: `<változó neve> = <változó értéke>`.",
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
