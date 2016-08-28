import sys
import yaml
from library.yapytex import console as cons
from library.yapytex.fs_utils import error_if_not_file_exists
from library.yapytex.dictutils import DictWrapper

class Settings(DictWrapper):
  _settings = None

  def __init__(self, filename='yapytex-config.yaml', lowercase=False, uppercase=False):
    _filename = filename
    error_if_not_file_exists(_filename)
    with open(_filename, 'r') as ymlfile:
      settings = super(self.__class__,self).__init__(yaml.load(ymlfile), lowercase, uppercase)

  def __str__(self):
    return str(self)

  def print_settings(self):
    cons.winfo('-- configuration ----')
    cons.winfo(yaml.dump(self, default_flow_style=False))
    cons.winfo('-------------------')  

settings = Settings()
