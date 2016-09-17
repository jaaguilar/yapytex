class YaPyTextPiece(object):
  _prefix = ''
  _sufix = ''
  _piece = ''
  _label = ''
  _childs = []

  @property
  def label(self):
    return self._label
  @property
  def childs(self):
    return self._childs
  def add_child(self,piece,label=''):
    self._childs.append(YaPyTextPiece(piece,label))
  def add_piece(self,piece):
    if not isinstance(piece,YaPyTextPiece):
      raise Exception('Piece argument must be YaPyTextPiece instance.')
    self._childs.append(piece)
  def __init__(self,piece,label='',prefix='',sufix=''):
    self._piece = piece
    self._label = label
  def __str__(self):
    parts = []
    if self._prefix:
      parts.append(self._prefix)
    if self._piece:
      parts.append(self._piece)
    if self.childs:
      parts.extend(map(str,self._childs))
    if self._sufix:
      parts.append(self._sufix)
    return '\n'.join(parts)