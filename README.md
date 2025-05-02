# Analyzing Twitter Discourse and Public Sentiment after the May 2021 Coup d’État in Mali

This repository contains the LaTeX source for our conference paper analyzing French-language Twitter data around Mali’s May 2021 coup. We combine sentiment analysis, topic modeling, stance classification, and network clustering to understand how online discourse evolved in response to key political events.

---

## Repository Structure

- `main.tex`  
  The master LaTeX file that assembles all sections (Introduction, Timeline, Prior Work, Methodology, Results, Discussion & Future Work, Conclusion & Implications).

- `sections/`  
  Individual section files (e.g. `introduction.tex`, `methodology.tex`, `results.tex`, etc.) for modular editing.

- `figures/`  
  All figures referenced in the paper (PNG/SVG/PDF).

- `bibliography.bib`  
  BibTeX database of all citations used.

- `IEEEtran.cls` (and related style files)  
  IEEE conference template files.

---

## Prerequisites

- A TeX distribution (e.g. TeX Live, MikTeX) with the following packages:
  - `IEEEtran`
  - `cite`
  - `amsmath`, `amssymb`, `amsfonts`
  - `graphicx`
  - `hyperref`
  - `algorithmic`
  - `url`
  - `xcolor`

- `latexmk` (recommended) or a PDF-laTeX toolchain.

---

## Building the PDF

From the root directory, run:

```bash
latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" main.tex
