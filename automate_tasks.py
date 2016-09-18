import os
from subprocess import run
#setting up environment
command = ['bash','-c','source ./environment.sh']
res = run(command)
if res.returncode:
  raise Exception('set up environment failed!')
github_user = os.environ['GITHUB_USER']
github_passwd = os.environ['GITHUB_PASSWORD']
project_name = os.environ['PROJECT_NAME']
#project name
print('project name ',project_name)
#force install package
print('installing package...')
res = run(['pip','install','--upgrade','--force-reinstall','--no-deps','.'])
if res.returncode:
  raise Exception('pip failed!')
#run tests
print('running tests...')
res = run(['python', './tests/test_pieces.py'])
if res.returncode:
  raise Exception('test not passed!')
#git add
print('git add...')
run(['git', 'add', '.'])
#git commit
print('git commit...')
message = input('git commit message (blank to cancel): ') or 'n'
if message != 'n':
  res = run(['git', 'commit', '-m', message])
  if res.returncode:
    raise Exception('git commit failed!')
else:
  print('git commit skipped.')  
#git push origin  
push_ok = input('Do you want to push changes to remote? [y/N]: ') or 'n'
print('git push origin master...')
if push_ok != 'n':
  run(['git','push','https://{0}:{1}@github.com/{0}/{2}'.format(github_user,github_passwd,project_name),'master'])
else:
  print('git push skipped.')  
