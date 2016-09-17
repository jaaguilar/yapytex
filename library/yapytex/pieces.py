def _format(piece):
  if piece.label:
    txt_piece = '{0}\n\\label{{{1}}}'.format(str(piece),piece.label)
    return txt_piece
  else:
    return str(piece)


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
