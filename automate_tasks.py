import os
from subprocess import call

print(os.environ['GITHUB_USER'])
print(os.environ['GITHUB_PASSWORD'])

print('git add...')
call(['git', 'add', '.'])
print('git commit...')
message = input('git commit message:')

if message != 'false':
  call(['git', 'commit', '-m', message])
else:
  print('git commit skipped.')  