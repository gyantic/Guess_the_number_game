import random
import sys


while True:
  sys.stdout.buffer.write(b'Please input minimum number.\n')
  sys.stdout.flush()

  n = sys.stdin.buffer.readline()
  print('You input' + n.decode())

  sys.stdout.buffer.write(b'Please input maximum number.\n')
  sys.stdout.flush()

  m = sys.stdin.buffer.readline()
  if (m.decode() < n.decode()):
    print('Your input is invalid\n')
  else:
    break

rand_number = random.randint(n.decode(),m.decode())

limit = 3

#for _ in range(limit):
