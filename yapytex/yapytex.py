from yapytex.dictutils import DictWrapper
from yapytex.config import settings as conf
import yapytex.latex_directives as xdir
from yapytex import styles
from yapytex import languages
from yapytex.pieces import YaPyTexPiece, YaPyTexChapter, YaPyTexParagraph, YaPyTexPreface
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

  def url(self,url,text='',brackets=True):
    if not text:
      text = url
    if brackets:
      return ' \\hyperref[{0}]{{{1} [\\ref*{{{0}}}] }}'.format(url,text)
    else:
      return ' \\hyperref[{0}]{{{1} \\ref*{{{0}}} }}'.format(url,text)

  def add_chapter(self,title):
    self._doc._type = 'book'
    piece = YaPyTexChapter(title)
    self._doc.add(piece)
    return piece

  def add_preface(self,children):
    YaPyTexPreface(children)

  def add_paragraph(self,par_text,size=styles.font_sizes.normal,label=''):
    piece = YaPyTexParagraph(par_text,size,label)
    self._doc.add(piece)
    return piece

  def add_section(self,title,text=''):
    self._doc.add(YaPyTexPiece('\\section{{{0}}}{1}\n'.format(title,text)))

  def add_subsection(self,title,text=''):
    self._doc.add(YaPyTexPiece('\\subsection{{{0}}}{1}\n'.format(title,text)))

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

  def add_acronym_entry(self,entry,text):
    if not xdir.useglossaries in self._doc._pre:
      self._doc._pre.append(xdir.useglossaries)
    self._doc._glossary.append(xdir.acronym_new.format(entry,entry,text))
    return xdir.gls_item.format(entry)

  def add_glossary_entry(self,entry,label,text):
    if not xdir.useglossaries in self._doc._pre:
      self._doc._pre.append(xdir.useglossaries)
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