def format(piece):
  if piece.label:
    txt_piece = '{0}\n\\label{{{1}}}'.format(str(piece),piece.label)
    return txt_piece
  else:
    return str(piece)
