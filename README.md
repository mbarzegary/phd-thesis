# My PhD Thesis

This repository contains all the LaTeX source files and the final PDF for my PhD thesis, as well as some accompanying files such as the scripts used for plotting the graphs.

## Thesis Information
* Title: Mathematical and computational modeling of metallic biomaterials biodegradation
* Author: Mojtaba Barzegari
* Institution: KU Leuven, Belgium
* Degree: PhD in Mechanical/Biomedical Engineering
* Date: 15 June 2023

## Final PDF

You can directly view the final PDF of the thesis [here](https://nbviewer.org/github/mbarzegary/phd-thesis/blob/451aafe85bad4afc6109516cc5c28d28f6c301fd/thesis.pdf).

## How to Compile

To compile the LaTeX files and generate the final PDF, follow these steps:

1. Make sure you have LaTeX installed on your system (e.g., `TeX Live`, `MiKTeX`, etc.).
1. Ensure all required LaTeX packages are installed.
1. Compile the thesis.tex file using a LaTeX editor (e.g., `Texmaker`, etc.) or from the command line:

```bash
xelatex thesis.tex
makeglossaries thesis
bibtex thesis
xelatex thesis.tex
xelatex thesis.tex
```

If you use a LaTeX editor, make sure to build the list of abbreviations by invoking `makeglossaries` or `makeindex` command during the compile process (like by putting `makeindex %.idx %.glo -t %.glg -s %.ist -o %.gls` as a User Command in `Texmaker`). Omit this step if you don't need the list of abbreviations with page numbers.
