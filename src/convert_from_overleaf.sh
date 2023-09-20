#!/bin/bash

# Convert from zip file from overleaf to Rmd source files

# Unzip
yes | unzip "$1"



for file in *_*.tex; do
    fname=`basename ${file} .tex`;

    # Convert llista-exercicis
    sed -i 's/\\begin{llista-exercicis}/\\subsection*{Exercicis recomanats}\nEls exercicis que segueixen són útils per practicar el material presentat. La numeració és la de \\cite{Bret}.\n\\begin{description}/g;s/\\end{llista-exercicis}/\\end{description}/g' ${fname}.tex
    # Convert using Pandoc
    pandoc --shift-heading-level-by=1 -p -f latex -t markdown+autolink_bare_uris+tex_math_single_backslash ${fname}.tex -o ${fname}.Rmd ;
    #  --shift-heading-level-by=1
    # Do extra substitutions
    ./convert.py ${fname}.Rmd | sponge ${fname}.Rmd;
done;

rm 99_Apendix.Rmd 0_Intro.Rmd espais_abstractes.Rmd

echo "# Matrius i equacions lineals" | cat - 1_*.Rmd | sponge 1_*.Rmd
echo "# Espais vectorials i aplicacions lineals" | cat - 2_*.Rmd | sponge 2_*.Rmd
echo "# Diagonalització" | cat - 3_*.Rmd | sponge 3_*.Rmd
echo "# Ortogonalitat" | cat - 4_*.Rmd | sponge 4_*.Rmd
