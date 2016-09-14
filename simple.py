import sys
from faker import Factory
from library.yapytex.base import tex, font_sizes, quote
from latex import build_pdf

tex.doc.title = 'Esta es una primera aproximación'
tex.doc.author = 'Juan Antonio Aguilar'

def my_hook_load_packages(pre):
  pre.append(tex.cmd.useblindtext)

tex.doc.hook_load_packages = my_hook_load_packages

fake = Factory.create('es_ES')

str_text = 'Hello World... to infinite and beyond!!!'

tex.add_paragraph(fake.text())
tex.add_paragraph(str_text,font_sizes.Huge)
tex.add_paragraph('<<Esto es una quote.>>',font_sizes.Huge)

tex.add_section(fake.name(),fake.text())
tex.add_paragraph(fake.text())

tex.add_paragraph("""
On the other hand, we denounce with righteous indignation
 and dislike men who are so beguiled and demoralized by the charms of
  pleasure of the moment, so blinded by desire, that they cannot foresee
   the pain and trouble that are bound to ensue; and equal blame belongs to 
   those who fail in their duty through weakness of will, which is the same
  as saying through shrinking from toil and pain. 
  These cases are perfectly simple and easy to distinguish. In a free hour, 
  when our power of choice is untrammelled and when nothing 
  prevents our being able to do what we like best, 
  every pleasure is to be welcomed and every pain avoided. 
  But in certain circumstances and owing to the claims of duty or 
  the obligations of business it will frequently occur that pleasures
   have to be repudiated and annoyances accepted. 
   The wise man therefore always holds in these matters 
   to this principle of selection: he rejects pleasures to 
   secure other greater pleasures, or else he endures pains to avoid worse pains.  
""",label='marca1')


tex.add_section(fake.name(),"""
But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born
 and I will give
  you a complete account of the system, and expound the actual
   teachings of the great explorer of the truth, 
   the master-builder of human happiness. No one rejects, dislikes, 
   or avoids pleasure itself, because it is pleasure, but because those who do not 
   know how to pursue pleasure rationally encounter consequences that are extremely painful. 
   Nor again is there anyone who loves or pursues or desires to obtain pain of itself, 
   because it is pain, but because occasionally circumstances occur in which toil and pain
    can procure him some great pleasure{0} {1} {2} {3}.  To take a trivial example, which of us ever 
    undertakes laborious physical exercise, except to obtain some advantage 
    from it? But who has any right to find fault with a man who chooses to enjoy a 
    pleasure that has no annoying consequences, or one who avoids a pain that 
    produces no resultant pleasure?
""".format(
  tex.ref('marca1'),
  tex.url('https://en.wikipedia.org/wiki/LaTeX','Esto es una URL'),
  tex.href('Una marca','https://en.wikipedia.org/wiki/LaTeX'),
  tex.href('Un fichero','run:./form_letter.pdf')))


tex.add_section(fake.name())
tex.add_paragraph("""
Este párrafo no es ni este mundo ni el otro...
""")



tex.add_subsection(fake.name(),fake.text())
items = [fake.name() for i in range(10)]
tex.add_enumeration(items)

tex.add_subsection(fake.name(),fake.text())
items = [fake.name() for i in range(55)]
tex.add_list_item(items)



tex.add_subsection('enumeración partida','primero 5 items, y luego otros 5... ¿cuantos items?')

items = [fake.name() for i in range(3)]
tex.add_enumeration(items,close=False)

tex.add_paragraph("""
Este es un ejemplo, claramente, de un párrafo cuyo cuerpo está dentro (inside) de un item (item)
dentro de una enumeración. Gracias por leer atentamente.
Aprovecho para poner un acrónimo {0}
""".format(tex.add_glos_entry('HTML','Hyper Text Markup Language')))

items = [fake.name() for i in range(2)]
tex.add_enumeration(items,ccontinue=True,close=False)


#enumeration inside enumeration
items = [fake.name() for i in range(10)]
tex.add_enumeration(items)


items = [fake.name() for i in range(5)]
tex.add_enumeration(items,ccontinue=True,close=True)




#tex.add_paragraph('\\item \\blindtext')

doc = tex.document()

# this builds a pdf-file inside a temporary directory
print(doc)

pdf = build_pdf(doc)

# look at the first few bytes of the header
pdf.save_to('ex1.pdf')
print('Finished!')