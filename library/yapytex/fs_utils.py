import os
from library.yapytex import console as cons

def file_exists(path):
  return os.path.isfile(path)


def error_if_not_file_exists(path,warning=False):
  message = 'File "{0}" not found or not accessible'.format(path)
  if not file_exists(path):
    if warning:
      cons.warning(message)
    else:
      raise Exception(message)
