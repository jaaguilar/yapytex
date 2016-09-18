import os
from subprocess import call

github_user = os.environ['GITHUB_USER']
github_passwd = os.environ['GITHUB_PASSWORD']
project_name = os.environ['PROJECT_NAME']

#project name
print('project name ',project_name)
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
push_ok = input('Do you want to push changes to remote? [y/N]: ') or 'n'
if push_ok != 'n':
  call(['git','push','https://{0}:{1}@github.com/{0}/{2}'.format(github_user,github_passwd,project_name),'master'])
else:
  print('git push skipped.')  
