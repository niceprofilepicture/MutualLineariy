PYTHON ?= python3

.PHONY: all verify preview
all: main.pdf

main.pdf: main.tex references.bib
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
	cp build/main.pdf main.pdf

verify:
	$(PYTHON) verify_derivation.py

preview: main.pdf
	pdftoppm -r 125 -png main.pdf build/page
