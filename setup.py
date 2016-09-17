from pip.req import parse_requirements
from distutils.core import setup

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

print(reqs)

setup(
  name='yapytex',
  version='1.0',
  description='Yet Another PYthon laTEX package',
  author='Juan A. Aguilar',
  author_email='juanantonioaguilar@gmail.com',
  url='https://github.com/jasset75/yapytex',
  packages=['yapytex'],
  install_requires=reqs,
)