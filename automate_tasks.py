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
#git add
print('git add...')
call(['git', 'add', '.'])
#git commit
print('git commit...')
message = input('git commit message (blank to cancel): ') or 'n'

if message != 'n':
  call(['git', 'commit', '-m', message])
else:
  print('git commit skipped.')  

#git push origin  
print('git push origin master...')
push_ok = input('do you want to push changes to remote? [y/N]: ') or 'n'
if push_ok != 'n':
  #call(['git', 'commit', '-m', message])
  print('OK')
else:
  print('git commit skipped.')  
