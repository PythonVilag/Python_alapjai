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
build-notebook notebook:
    uv run marimo export html-wasm \
        {{ notebook }}/{{ notebook }}.py \
        --output docs/{{ notebook }} \
        --mode edit --show-code --force

[group("build")]
build-notebooks:
    just build-notebook 00_Bevezetes_es_kurzusinformaciok
    just build-notebook 01_A_Python_programozasi_nyelvrol
