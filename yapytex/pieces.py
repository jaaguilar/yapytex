from yapytex import styles
from yapytex import latex_directives as xdir

class YaPyTexPiece(object):
  _prefix = ''
  _sufix = ''
  _piece = ''
  _label = ''

  @property
  def label(self):
    return self._label
  @property
  def children(self):
    return self._children
  def add_child(self,piece,label=''):
    self._children.append(YaPyTexPiece(piece,label))
  def add_children(self,children):
    self._children.extend(children)
  def add_piece(self,piece):
    if not isinstance(piece,YaPyTexPiece):
      raise Exception('Piece argument must be YaPyTexPiece instance.')
    self._children.append(piece)
  def __init__(self,piece,label='',prefix='',sufix=''):
    self._children = []
    self._piece = piece
    self._label = label
    self._prefix = prefix
    self._sufix = sufix
  def __str__(self):
    parts = []
    if self._prefix:
      parts.append(self._prefix)
    if self._piece:
      parts.append(self._piece)
    parts.extend(map(str,self._children))
    if self._sufix:
      parts.append(self._sufix)
    return '\n'.join(parts)

class YaPyTexChapter(YaPyTexPiece):
  def __init__(self,title):
    super(self.__class__, self).__init__(xdir.chapter.format(title))    
    
class YaPyTexParagraph(YaPyTexPiece):
  def __init__(self,text,size=styles.font_sizes.normal,label='',children=[]):
    super(self.__class__, self).__init__(text,prefix=xdir.par_prefix.format(size),sufix=xdir.par_sufix,label=label)
    self.add_children(children)

class YaPyTexPreface(YaPyTexPiece):
  def __init__(self,children=[]):
    super(self.__class__, self).__init__(xdir.chapter.format('Prefacio'),prefix=xdir.frontmatter,sufix=xdir.mainmatter)
    self.add_children(children)

class YaPyTexLipsum(YaPyTexPiece):
  def __init__(self,number_of_paragraphs):
    if not (isinstance(number_of_paragraphs,int) and number_of_paragraphs > 0):
      raise('number_of_paragraphs must be a none zero positive integer.')
    super(self.__class__, self).__init__(xdir.lipsum.format(number_of_paragraphs))


class YaPyTexSection(YaPyTexPiece):
  def __init__(self,title,text,unnumbered,label=''):
    asterisk = '*'
    if not unnumbered:
      asterisk = ''
    if label:
      piece = xdir.labeled_section.format(title,text,asterisk,label)
    else:
      piece = xdir.section.format(title,text,asterisk)
    super(self.__class__,self).__init__(piece)

#class YaPyTexAppendix(YaPyTexSection):
class YaPyTexAppendix(YaPyTexPiece):
  def __init__(self,title,text,label,children=[]):
    if label:
      piece = xdir.labeled_section.format(title,text,'*',label)
    else:
      piece = xdir.section.format(title,text,'*')
    super(self.__class__,self).__init__(piece)
    self.add_children(children)

"""
  def __init__(self,title,text,unnumbered,label,children=[]):
    super(self.__class__,self).__init__(title,text,unnumbered,label=label)
    self.add_children(children)
"""    