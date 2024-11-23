import random
import sys

while True:
  sys.stdout.buffer.write(b'Please input minimum number.\n')
  sys.stdout.flush()

  n = sys.stdin.buffer.readline()
  print('You input ' + n.decode())

  sys.stdout.buffer.write(b'Please input maximum number.\n')
  sys.stdout.flush()

  m = sys.stdin.buffer.readline()
  if (int(m.decode()) < int(n.decode())):
    print('Your input is invalid\n')
  else:
    break

min_number = int(n.decode())
max_number = int(m.decode())

rand_number = random.randint(min_number, max_number)

limit = 3

for _ in range(limit):
  sys.stdout.buffer.write(b"Please input your guess.\n")
  sys.stdout.flush()
  guessed_num = int((sys.stdin.buffer.readline()).decode())

  if rand_number == guessed_num:
    print("Your guess is right.\n")
    break
  else:
    if _ == limit-1:
      print("Time is out!/n")
      print(f"Right answer is {rand_number}")
