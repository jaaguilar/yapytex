import unittest
import yapytex.latex_directives as xdir
from yapytex.pieces import YaPyTexPiece

class TestPieces(unittest.TestCase):
  def test_doc_begin(self):
    piece = YaPyTexPiece(xdir.doc_begin)
    self.assertEqual(str(piece),xdir.doc_begin)

if __name__ == '__main__':
  unittest.main()