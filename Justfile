@_:
    just --list --unsorted

[group("lifecycle")]
clean:
    rm -rf \
        .DS_Store \
        .ruff_cache \
        .venv
    find . -type d -name "__pycache__" -exec rm -r {} +

[group("lifecycle")]
install:
    uv venv --python 3.12 .venv
    uv pip install --requirements requirements.txt

[group("lifecycle")]
fresh: clean install

[group("qa")]
lint:
    uv run ruff check
    uv run ruff format --diff

[group("build")]
build-notebook notebook:
    uv run marimo export html-wasm \
        {{notebook}}/{{notebook}}.py \
        --output docs/{{notebook}} \
        --mode edit --show-code --force

[group("build")]
build-notebooks:
    just build-notebook 00_Bevezetes_es_kurzusinformaciok
    just build-notebook 01_A_Python_programozasi_nyelvrol
