from library.yapytex.dictutils import DictWrapper
from library.yapytex.config import settings as conf

if conf.debug:
  conf.print_settings()

_doc_class = '\\documentclass[{0}]{{article}}'
_doc_title = '\\title{{{0}}}'
_doc_author = '\\author{{{0}}}'
_doc_begin = r'\begin{document}'
_doc_end = r'\end{document}'
_make_glossaries = r'\makeglossaries'
_print_glossaries = r'\printglossaries'
_enum_item = r'\item '
_enum_begin = '\\begin{enumerate}\n\\item '
_enum_end = '\n\\end{enumerate}'
_gls_item = '\\gls{{{0}}}'
_acronym_new = '\\newacronym{{{0}}}{{{1}}}{{{2}}}'

_d_languages = dict(
  es_ES = 'Spanish',
  en_EN = 'English'
)

_d_cmd = dict(
  maketitle= r'\maketitle',
  cleardoublepage= r'\cleardoublepage',
  useinputenc =r'\usepackage[utf8]{inputenc}',
  usenumerate =r'\usepackage{enumerate}',
  usehyperref = r'\usepackage[hidelinks=true]{hyperref}',
  useblindtext = r'\usepackage{blindtext}',
  useglossaries = r'\usepackage[acronym]{glossaries}'
)

_d_paper_type = dict(
  a4paper = r'a4paper'
)

_d_font_family = dict(
  times= r'times'
)

_d_misc_options = dict(
  numbered = r'numbered',
  pprint = r'print',
  index = r'index'
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

_cmd = DictWrapper(_d_cmd)
misc_options = DictWrapper(_d_misc_options)
font_families = DictWrapper(_d_font_family)
misc_options_dict = DictWrapper(_d_misc_options)
paper_type = DictWrapper(_d_paper_type)
font_sizes = DictWrapper(_d_font_sizes)
languages = DictWrapper(_d_languages)

_default_doc_options = [
  misc_options.numbered,
  font_sizes.sz12pt,
  font_families.times,
  misc_options.pprint,
  misc_options.index,
]

_default_language = 'es_ES'
_es_ES = r'\usepackage[spanish, es-tabla]{babel}'

def quote(string,quote='\''):
  return quote+string+quote

class YaPyTextBase(object):
  pass

class YaPyTextPiece(object):
  _piece = ''
  _label = ''

  @property
  def label(self):
    return self._label
  def __init__(self,piece,label=''):
    self._piece = piece
    self._label = label
  def __str__(self):
    return self._piece

def _format(piece):
  if piece.label:
    txt_piece = '{0}\n\\label{{{1}}}'.format(str(piece),piece.label)
    return txt_piece
  else:
    return str(piece)

class YaPyTexLibrary(object):
  @property
  def cmd(self):
    return _cmd
  
  class FontSize(object):
    sz11pt = r'11pt'
    sz12pt = r'12pt'
    tiny = r'\tiny'
    script = r'\scriptsize'
    small = r'\small'
    normal = r'\normalsize'
    huge = r'\huge'
    footnote = r'\footnotesize'
    large = r'\large'
    Large = r'\Large'
    LARGE = r'\LARGE'
    Huge = r'\Huge'
  
  class Document(YaPyTextBase):
    _pre = []
    _glossary = []
    _pieces = []
    _title = None
    _author = None
    _language = _default_language
    _hook_load_packages = None

    @property
    def language(self):
      return self._language
    @language.setter
    def language(self):
      return self._language

    @property
    def title(self):
      return self._title

    @title.setter
    def title(self,title):
      self._title = title

    @property
    def author(self):
      return self._author

    @property
    def hook_load_packages(self):
      return self._hook_load_packages
    
    @hook_load_packages.setter
    def hook_load_packages(self,hook):
      self._hook_load_packages = hook
     
    @author.setter
    def author(self,author):
      self._author = author

    def add(self, piece):
      self._pieces.append(piece)

    def build(self):
      pre_header = [
        _doc_class.format(','.join(_default_doc_options)),
        _cmd.useinputenc,
        _cmd.usenumerate,
        _cmd.usehyperref,
      ] + self._pre
      if self._hook_load_packages:
        self._hook_load_packages(pre_header)
      if self._language is 'es_ES':
        pre_header.append(_es_ES)
      if self._title:
        pre_header.append(_doc_title.format(self._title))
      if self._author:
        pre_header.append(_doc_author.format(self._author))
      
      if _cmd.useglossaries in pre_header and len(self._glossary) > 0:
        pre_header.append(_make_glossaries)

      header = []
      header.append(_doc_begin)
      post_header = []
      if self._title:
        post_header.append(_cmd.maketitle)
        post_header.append(_cmd.cleardoublepage)
      pieces = map(_format,self._pieces)
      footer = []
      if _cmd.useglossaries in pre_header and len(self._glossary) > 0:
        footer.append(_print_glossaries)
      #this line may be the last of footer
      footer.append(_doc_end)
      pre_header.extend(self._glossary)
      return \
        '\n'.join(pre_header)+\
        '\n'.join(header)+\
        '\n'.join(post_header)+\
        '\n'.join(pieces)+'\n'+\
        '\n'.join(footer)
  _doc = Document()

  @property
  def doc(self):
    return self._doc
  
  def href(self,label,href='',brackets=True):
    if brackets:
      return ' \\href{{{0}}}{{[{1}]}}'.format(href,label)
    else:
      return ' \\href{{{0}}}{{{1}}}'.format(href,label)

  def ref(self,label,brackets=True):
    if brackets:
      return '[\\ref{{{0}}}]'.format(label)
    else:
      return '\\ref{{{0}}}'.format(label)

  def url(self,url,text='',brackets=True):
    if not text:
      text = url
    if brackets:
      return ' \\hyperref[{0}]{{{1} [\\ref*{{{0}}}] }}'.format(url,text)
    else:
      return ' \\hyperref[{0}]{{{1} \\ref*{{{0}}} }}'.format(url,text)

  def add_paragraph(self,par_text,size=font_sizes.normal,label=''):
    self._doc.add(YaPyTextPiece('{{{0}\n{1}\\par}}'.format(size,par_text),label))

  def add_section(self,title,text=''):
    self._doc.add(YaPyTextPiece('\\section{{{0}}}{1}\n'.format(title,text)))

  def add_subsection(self,title,text=''):
    self._doc.add(YaPyTextPiece('\\subsection{{{0}}}{1}\n'.format(title,text)))

  def add_enumeration(self,items,ccontinue=False,close=True):
    if len(items) > 0:
      begin_token = _enum_item
      end_token = ''
      if not ccontinue:
        begin_token = _enum_begin
      if close:
        end_token= _enum_end
      phrase = begin_token+'\n\\item '.join(items)+end_token
      #print(phrase)
      #wait = input('--parada -o- tecnica--')
      self._doc.add(YaPyTextPiece(phrase))

  def add_glos_entry(self,entry,text):
    if not _cmd.useglossaries in self._doc._pre:
      self._doc._pre.append(_cmd.useglossaries)
    self._doc._glossary.append(_acronym_new.format(entry,entry,text))
    return _gls_item.format(entry)


  def close_enumeration(self):
    self._doc.add(YaPyTextPiece('\\end{enumerate}'))

  def add_list_item(self,items):
    if len(items) > 0:
      self._doc.add(YaPyTextPiece('\\begin{itemize}\n\\item '+'\n\\item '.join(items)+'\\end{itemize}'))

  def document(self):
    #doc.add(doc_content)
    return self._doc.build()

tex = YaPyTexLibrary()