import random
import sys

def read_input(prompt: str, is_int: bool = False) -> str:
  """入力した後、それをstdinから読む関数"""
  sys.stdout.buffer.write(prompt.encode())
  sys.stdout.flush()
  user_input  = sys.stdin.buffer.readline().decode()
  #入力がint型の数でない場合エラーを返すようにする
  if is_int:
    try:
      return int(user_input)
    except ValueError:
      sys.stdout.buffer.write(b"Invalid input. Please enter an integer.\n")
      return read_input(prompt, is_int=True)


while True:
  min_number = read_input("Please input minimum number.\n", is_int=True)

  max_number = read_input("Please input maximum number.\n", is_int=True)

  if (max_number < min_number):
    sys.stdout.buffer.write(b'Your input is invalid.\n')
  else:
    break


rand_number = random.randint(min_number, max_number)

limit = 3 #制限回数

for _ in range(limit):
  sys.stdout.buffer.write(b"Please input your guess.\n")
  sys.stdout.flush()
  guessed_num = int((sys.stdin.buffer.readline()).decode())

  if rand_number == guessed_num:
    sys.stdout.buffer.write(b"Your guess is right.\n")
    break
  else:
    if _ == limit - 1:
      sys.stdout.buffer.write(b"Time is out!\n")
      sys.stdout.buffer.write(f"The right answer is {rand_number}\n".encode())
    else:
      sys.stdout.buffer.write(b"Wrong guess. Try again.\n")
