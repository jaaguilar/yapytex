from library.yapytex.config import settings as conf

if conf.debug:
  conf.print_settings()

doc_class = r'\documentclass{article}'
doc_begin = r'\begin{document}'
#r"{\Large Hello, world!}"
doc_end = r'\end{document}'

class YaPyTexBase(object):
  def document(self,doc_content):
    return doc_class+doc_begin+doc_content+doc_end

tex = YaPyTexBase()