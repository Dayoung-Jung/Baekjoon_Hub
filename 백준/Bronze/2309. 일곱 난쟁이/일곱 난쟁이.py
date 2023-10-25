import random

list_x = [int(input()) for _ in range(9)]

while True:
  list_sample = random.sample(list_x, 7)
  
  if sum(list_sample) == 100:
    list_sample.sort()
    break

print(*list_sample, sep='\n')