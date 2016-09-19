from yapytex.dictutils import DictWrapper
from yapytex import latex_directives as xdir
from yapytex import styles
from yapytex import miscelanea as misc
from yapytex.pieces import YaPyTexPiece
from yapytex.abstract import YaPyTexBase

_d_misc_options = dict(
  numbered = r'numbered',
  pprint = r'print',
  index = r'index'
)

misc_options = DictWrapper(_d_misc_options)

_default_doc_options = [
  misc_options.numbered,
  styles.font_sizes.sz12pt,
  styles.font_families.times,
  misc_options.pprint,
  misc_options.index,
]

class Document(YaPyTexBase):
  _preface = []
  _pre = []
  _glossary = []
  _acronym = []
  _pieces = []
  _title = None
  _author = None
  _language = xdir.default_language
  _hook_load_packages = None
  _type = 'article'

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
    if not isinstance(piece,YaPyTexPiece):
      raise Exception('Piece argument must be YaPyTexPiece instance.')
    self._pieces.append(piece)

  def build(self,ttype):
    pre_header = [
      xdir.doc_class.format(','.join(_default_doc_options),ttype),
      xdir.useinputenc,
      xdir.usenumerate,
      xdir.usehyperref,
    ] + self._pre

    if self._hook_load_packages:
      self._hook_load_packages(pre_header)
    if self._language is 'es_ES':
      pre_header.append(xdir.es_ES)
    if self._title:
      pre_header.append(xdir.doc_title.format(self._title))
    if self._author:
      pre_header.append(xdir.doc_author.format(self._author))
    

    if xdir.useglossaries in pre_header and len(self._glossary) > 0:
    #  name_gloss_file = '_glossary'
    #  with open(name_gloss_file+'.tex', 'w') as file:
    #    file.write('\n'.join(self._glossary))
    #  pre_header.append(_load_glossary.format(name_gloss_file))  
      pre_header.append(xdir.make_glossaries)
      pre_header.append(xdir.gls_entry_italic)


    header = []
    #document's begin
    header.append(xdir.doc_begin)

    post_header = self._preface

    if self._title:
      post_header.append(xdir.maketitle)
      post_header.append(xdir.cleardoublepage)
    pieces = map(misc.format,self._pieces)
    footer = []
    if xdir.useglossaries in pre_header and len(self._glossary) > 0:
      footer.append(xdir.print_glossaries)
    if xdir.useglossaries in pre_header and len(self._acronym) > 0:
      footer.append(xdir.print_acronyms)
    #this line may be the last of footer
    footer.append(xdir.doc_end)
    pre_header.extend(self._glossary)
    pre_header.extend(self._acronym)
    return \
      '\n'.join(pre_header)+\
      '\n'.join(header)+\
      '\n'.join(post_header)+\
      '\n'.join(pieces)+'\n'+\
      '\n'.join(footer)
