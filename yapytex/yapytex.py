from yapytex.dictutils import DictWrapper
from yapytex.config import settings as conf
import yapytex.latex_directives as xdir
from yapytex import styles
from yapytex import languages
from yapytex.pieces import \
  YaPyTexPiece,\
  YaPyTexLipsum,\
  YaPyTexChapter,\
  YaPyTexParagraph,\
  YaPyTexPreface,\
  YaPyTexSection,\
  YaPyTexAppendix
from yapytex.document import Document

if conf.debug:
  conf.print_settings()

def quote(string,quote='\''):
  return quote+string+quote

class YaPyTexLibrary(object):
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
  
  _doc = Document()

  @property
  def cmd(self):
    return xdir
  
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

  def add_chapter(self,title):
    self._doc._type = 'book'
    piece = YaPyTexChapter(title)
    self._doc.add(piece)
    return piece

  def add_preface(self,children):
    piece = YaPyTexPreface(children)
    self._doc.add(piece)
    return piece

  def add_paragraph(self,par_text='',size=styles.font_sizes.normal,label='',doc_append=True,lipsum=0):
    children = []
    if lipsum:
      children = [YaPyTexLipsum(lipsum)]
    piece = YaPyTexParagraph(par_text,size,label,children=children)

    if doc_append:
      self._doc.add(piece)
    return piece

  def add_section(self,title,text='',doc_append=True,unnumbered=False,children=[]):
    piece = YaPyTexSection(title,text,unnumbered)
    piece.add_children(children)
    if doc_append:
      self._doc.add(piece)
    return piece

  def add_subsection(self,title,text=''):
    self._doc.add(YaPyTexPiece('\\subsection{{{0}}}{1}\n'.format(title,text)))

  def add_appendix(self,title,label,text,doc_append=True,children=[]):
    piece = YaPyTexAppendix(title,text,label,children)
    if doc_append:
      self._doc.add_appendix(piece)
    return piece


  def add_enumeration(self,items,ccontinue=False,close=True):
    if len(items) > 0:
      begin_token = xdir.enum_item
      end_token = ''
      if not ccontinue:
        begin_token = xdir.enum_begin
      if close:
        end_token= xdir.enum_end
      phrase = begin_token+'\n\\item '.join(items)+end_token
      #print(phrase)
      #wait = input('--parada -o- tecnica--')
      self._doc.add(YaPyTexPiece(phrase))

  def add_acronym_entry(self,entry,text=''):
    if not xdir.useglossaries in self._doc._pre:
      self._doc._pre.append(xdir.useglossaries)
    pattern = xdir.partial_acronym.format(entry,entry)
    if not any(pattern in s for s in self._doc._acronym):
      self._doc._acronym.append(xdir.acronym_new.format(entry,entry,text))
    return xdir.gls_item.format(entry)

  def add_glossary_entry(self,entry,label,text=''):
    if not xdir.useglossaries in self._doc._pre:
      self._doc._pre.append(xdir.useglossaries)
    pattern = 'name={0}'.format(entry)
    if not any(pattern in s for s in self._doc._glossary):
      self._doc._glossary.append(xdir.glossary_new.format(entry,label,text))
    return xdir.gls_item.format(entry)

  def close_enumeration(self):
    self._doc.add(YaPyTexPiece('\\end{enumerate}'))

  def add_list_item(self,items):
    if len(items) > 0:
      self._doc.add(YaPyTexPiece('\\begin{itemize}\n\\item '+'\n\\item '.join(items)+'\\end{itemize}'))

  def document(self,ttype):
    #doc.add(doc_content)
    return self._doc.build(self._doc._type)

  def add_lipsum(self,number_of_paragraphs=1,doc_append=True):
    piece = YaPyTexLipsum(number_of_paragraphs)
    if doc_append:
      self._doc.add(piece)
    return piece