import unittest
from yapytex import styles
import yapytex.latex_directives as xdir
from yapytex.yapytex import YaPyTexLibrary
from yapytex.pieces import YaPyTexPiece, YaPyTexChapter, YaPyTexParagraph, YaPyTexPreface,YaPyTexSection

def funcion(piece):
  return piece._piece


class TestPieces(unittest.TestCase):
  def test_doc_begin(self):
    piece = YaPyTexPiece(xdir.doc_begin)
    self.assertEqual(str(piece),xdir.doc_begin)
  def test_chapter(self):
    piece = YaPyTexChapter('test')
    self.assertEqual(str(piece),r'\chapter{test}')
  def test_paragraph(self):
    par = 'this is a paragraph'
    piece = YaPyTexParagraph(par,size=styles.font_sizes.normal)
    self.assertEqual(str(piece),'{{{0}\n{1}\n\\par}}'.format(styles.font_sizes.normal,par))
  def test_preface(self):
    lib = YaPyTexLibrary()
    paragraphs = []
    par_txt_1 = 'this is a paragraph'
    paragraphs.append(YaPyTexParagraph(par_txt_1,size=styles.font_sizes.normal))
    par_txt_2 = 'this is another paragraph'
    paragraphs.append(YaPyTexParagraph(par_txt_2,size=styles.font_sizes.normal))
    preface = YaPyTexPreface(paragraphs)
    preface_str = '\\frontmatter\n\\chapter{Prefacio}\n{\\normalsize\nthis is a paragraph\n\par}\n{\\normalsize\nthis is another paragraph\n\\par}\n\\mainmatter'
    self.assertEqual(str(preface),preface_str)
  def test_section(self):
    section_title = 'this is a section'
    section_txt = 'and this is the content of the section'
    piece = YaPyTexSection(section_title,section_txt,unnumbered=False)
    self.assertEqual(str(piece),xdir.section.format(section_title,section_txt,''))

if __name__ == '__main__':
  test = unittest.main()
  print('requete',test)