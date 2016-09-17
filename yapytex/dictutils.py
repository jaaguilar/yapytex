"""
Load dict to access as property style. Instead of:

  get <dict>['<key>'] -> <value> or set <dict>['<key>'] = <value>

use more pythonic way:

  get <dict>.<key> -> <value> or set <dict>.<key> = <value>
"""
class DictWrapper(object):
  def __init__(self, d, lowercase=False, uppercase=False):
    for a, b in d.items():
      if lowercase:
        a = str(a).lower()
      elif uppercase:
        a = str(a).upper()
      if isinstance(b, (list, tuple)):
        setattr(self, a, [__class__(x) \
          if isinstance(x, dict) \
          else x for x in b ])
      else:
        setattr(self, a, __class__(b) if isinstance(b, dict) else b)
  def __iter__(self):
    return self
  def __str__(self):
    list_attr = []
    for attr, value in self.__dict__.items():
      list_attr.append('{0}: {1}'.format(attr,value.__str__()))
    return '{{{0}}}'.format(', '.join(list_attr))