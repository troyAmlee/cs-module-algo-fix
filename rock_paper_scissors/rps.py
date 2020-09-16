#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  permutations = 3**n
  
  counterperm = 1

  counterpermutation = 3**counterperm

  arr = []

  count = 0
  
  if(n == 0):
    return arr

  def getarray(perm):
    r = ["rock"]
    p = ["paper"]
    s = ["scissors"]
    rps = [r, p, s]
    indexone = 0
    indextwo = 0
    permutations = 3**perm
    count = 0

    arr = []
    if(n == 0):
      return arr

    for i in range(len(rps)):
      
      
      for j in range(permutations//3):
        arr.append(rps[indexone])
      indexone += 1

    return arr

  print(getarray(n))

  rock_paper_scissors(n - 1)

    
    


  







      


    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')