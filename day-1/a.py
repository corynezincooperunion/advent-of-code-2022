import pprint
import heapq

with open("day1.txt") as f:
  lines = list(f)
  lines = [l.strip() for l in lines]

  big_list = []
  small_list = []
  for line in lines:
    if line == '':
      big_list.append(small_list)
      small_list = []
    else:
      small_list.append(int(line))

  big_list.append(small_list)
  
  big_list = [sum(x) for x in big_list]

  result = heapq.nlargest(3, big_list)

print(sum(result))
