@_:
    just --list --unsorted

[group("lifecycle")]
clean:
    rm -rf \
        .ruff_cache \
        megalinter-reports \
        .venv
    find . -type f -name ".DS_Store" -delete
    find . -type d -name "__pycache__" -exec rm -r {} +
    find . -type d -name "__marimo__" -exec rm -r {} +
    find docs -mindepth 1 -maxdepth 1 ! -name "index.html" -exec rm -r {} +

[group("lifecycle")]
install *args:
    uv sync --all-groups {{ args }}

[group("lifecycle")]
upgrade:
    just install --upgrade

[group("lifecycle")]
fresh: clean install

[group("qa")]
lint:
    uv run ruff check
    uv run ruff format --diff

[group("qa")]
type:
    uv run ty check

[group("qa")]
check-all: lint type

[group("qa-extra")]
megalinter:
    npx mega-linter-runner --flavor cupcake --env "MEGALINTER_CONFIG=.github/linters/.megalinter.yml"

[group("qa-extra")]
prek:
    uv run prek run --all-files

[group("build")]
build-notebook lecke notebook mode="edit":
    uv run marimo export html-wasm \
        {{ lecke }}/{{ notebook }}.py \
        --output docs/{{ notebook }} \
        --mode {{ mode }} --show-code --force

[group("build")]
build-notebooks:
    just build-notebook 00_Bevezetes_es_kurzusinformaciok 00_Bevezetes_es_kurzusinformaciok
    just build-notebook 00_Bevezetes_es_kurzusinformaciok 00_Bevezetes_es_kurzusinformaciok_kviz run
    just build-notebook 01_A_Python_programozasi_nyelvrol 01_A_Python_programozasi_nyelvrol
    just build-notebook 01_A_Python_programozasi_nyelvrol 01_A_Python_programozasi_nyelvrol_kviz run
