from library.yapytex.dictutils import DictWrapper

_d_paper_type = dict(
  a4paper = r'a4paper'
)

_d_font_family = dict(
  times= r'times'
)

_d_font_sizes = dict(
  sz11pt = r'11pt',
  sz12pt = r'12pt',
  tiny = r'\tiny',
  script = r'\scriptsize',
  small = r'\small',
  normal = r'\normalsize',
  huge = r'\huge',
  footnote = r'\footnotesize',
  large = r'\large',
  Large = r'\Large',
  LARGE = r'\LARGE',
  Huge = r'\Huge'
)

font_families = DictWrapper(_d_font_family)
paper_type = DictWrapper(_d_paper_type)
font_sizes = DictWrapper(_d_font_sizes)
