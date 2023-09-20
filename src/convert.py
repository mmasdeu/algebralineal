#!/usr/bin/python
import re
import fileinput
import sys

translations = [\
                ('notacio', 'notation'),
                ('exemple', 'example'),
                ('proposicio', 'proposition'),
                ('teorema', 'theorem'),
                ('lema', 'lemma'),
                ('observacio', 'remark'),
                ('exercici', 'exercise'),
                ('definicio', 'definition'),
                ('corollari', 'corollary')]

substitutions = [\
                 (r'\\begin{pmatrix\*}\[r\]', r'\\begin{pmatrix}'),
                 (r'\\begin{pmatrix\*}\[l\]', r'\\begin{pmatrix}'),

                 (r'\\end{pmatrix\*}', r'\\end{pmatrix}'),
                 (r'\n\s+\\end\{aligned\}', r'\n\\end{aligned}'),\
                 # (r'\$\$', r'\n$$\n'),\
                 (r'(\n[#]* [^\n]*)\n\n\[\][^"]*"([^"]*)"}',r'\1 {#\2}\n'),\
                 (r'(?:^|\\G)\\t',''),\
                 (r'\n[ \t]+\n',r'\n'),\
                 (r' ',r''),\
                 (r'◻',r''),\
                 (r'\\label{(.+?)}',r'(\\#\1)'),\
                 (r'val_sing',r'valsing'),\
                 (r'\*Proof\.\* ',r''),\
                 # (r'^[^#]*',r''),\
                 (r' ',r''),\
                 (r'−',r'-'),\
                 (r'\[\\\[(.*)\\\]\].+?reference-type="ref"\s*reference=\".+?\"\}',r' \@ref(\1)'),\
                 (r'\[\\\[(.*)\\\]\].+?reference-type="eqref"\s*reference=\".+?\"\}',r' \@ref(\1)'),\
                 (r'\\@ref\(teo',r'\@ref(thm'),\
                 (r'\\@ref\(obs',r'\@ref(rmk'),\
                 (r'\\@ref\(lema',r'\@ref(lem'),\
                 (r'\\@ref\(prop',r'\@ref(prp'),\
                 (r'\\@ref\(exempl.?:',r'\@ref(exm:'),\
                 (r'\\@ref\(exem:',r'\@ref(exm:'),\
                 (r'',r''),\
                 (r'{#(.*) .unnumbered}',r''),\
                 (r'#  {#section .unnumbered}',r'# Introducció {-#Intro}')] + \
                 [(r'::: %s'%a, r':::{.%s}'%b) for a, b in translations] + [(r'::: \s*(.*)', r'::: {.\1}')] + \
                 [(r':::\{.(.*)\}\n\[\]\{.+?label=".+?:(.*)"\}',r'::: {.\1 #\2}\n')]

def substitute(fname=None):
    with open(fname, 'r') as ff:
        data = ff.read()
        for a, b in substitutions:
            data = re.sub(a, b, data)
        sys.stdout.write(data)

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        fname = args[0]
    else:
        fname = None
    substitute(fname)
