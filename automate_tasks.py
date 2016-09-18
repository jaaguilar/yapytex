import os
from subprocess import call

print(os.environ['GITHUB_USER'])
print(os.environ['GITHUB_PASSWORD'])

#force install package
print('installing package...')
res = call(['pip','install','--upgrade','--force-reinstall','--no-deps','.'])
if res:
  raise Exception('pip failed!')

#run test
print('running tests...')
res = call(['python', './tests/test_pieces.py'])
if res:
  raise Exception('test not found!')
print('git add...')
call(['git', 'add', '.'])

print('git commit...')
message = input('git commit message: ')

if message != 'false':
  call(['git', 'commit', '-m', message])
else:
  print('git commit skipped.')  
