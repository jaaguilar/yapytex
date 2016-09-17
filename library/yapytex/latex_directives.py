maketitle= r'\maketitle'
cleardoublepage= r'\cleardoublepage'
useinputenc =r'\usepackage[utf8]{inputenc}'
usenumerate =r'\usepackage{enumerate}'
usehyperref = r'\usepackage[colorlinks,hidelinks=true]{hyperref}'
useblindtext = r'\usepackage{blindtext}'
useglossaries = r'\usepackage[acronym]{glossaries}'
default_language = 'es_ES'
es_ES = r'\usepackage[spanish, es-tabla]{babel}'
frontmatter = r'\frontmatter'
doc_class = '\\documentclass[{0}]{{{1}}}'
doc_title = '\\title{{{0}}}'
doc_author = '\\author{{{0}}}'
doc_begin = r'\begin{document}'
doc_end = r'\end{document}'
load_glossary = '\\input{{{0}}}'
make_glossaries = r'\makeglossaries'
print_glossaries = '\\printglossary'
enum_item = r'\item '
enum_begin = '\\begin{enumerate}\n\\item '
enum_end = '\n\\end{enumerate}'
gls_item = '\\gls{{{0}}}'
acronym_new = '\\newacronym{{{0}}}{{{1}}}{{{2}}}'
glossary_new = '\\newglossaryentry{{{0}}}{{name={1},description={{{2}}}}}'
gls_entry_italic = r'\renewcommand{\glstextformat}[1]{\textit{#1}}'