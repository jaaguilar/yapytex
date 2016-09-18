import unittest
import yapytex.latex_directives as xdir
from yapytex.pieces import YaPyTexPiece

class TestPieces(unittest.TestCase):
  def test_doc_begin(self):
    piece = YaPyTexPiece(xdir.doc_begin)
    self.assertEqual(str(piece),xdir.doc_begin)
  def test_chapter(self):
    piece = YaPyTexPiece(xdir.chapter.format('test'))
    self.assertEqual(str(piece),r'\chapter{test}')



if __name__ == '__main__':
  test = unittest.main()
  print('requete',test)