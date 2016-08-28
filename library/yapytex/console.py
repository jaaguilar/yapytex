import sys
from colorama import init, Fore, Back, Style
from library.yapytex import colors

init()
#_Token = r'\033[{0}m'
ConsInfo=Fore.CYAN #_Token.format(colors.Cyan)
ConsWarning=Fore.YELLOW#_Token.format(colors.Yellow)
ConsError=Fore.RED#_Token.format(colors.LightRed)
Native=Fore.RESET#_Token.format('')

def _write(decorator,*args):
  if decorator in [Native,ConsInfo]:
    stream = sys.stdout
  elif decorator in [ConsError,ConsWarning]:
    stream = sys.stderr
  stream.write(decorator)
  print(*args,end='',file=stream)
  #stream.write(Native)

def _writeln(decorator,*args):
  nargs= args + (Native,'\n',)
  _write(decorator,*nargs)
def writeln(*args):
  _writeln(Native,*args)
def writeln_warning(*args):
  _writeln(ConsWarning,*args)
def writeln_error(*args):
  _writeln(ConsError,*args)
def writeln_info(*args):
  _writeln(ConsInfo,*args)
#abreviados
def warning(*args):
  writeln_warning(*args)
def werror(*args):
  writeln_error(*args)
def winfo(*args):
  writeln_info(*args)


