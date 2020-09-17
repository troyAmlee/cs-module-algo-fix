#!/usr/bin/python

import sys

def rock_paper_scissors(n):
	empty_list = [["rock"],["paper"],["scissors"]]
	rock = ["rock"]
	paper = ["paper"]
	scissors = ["scissors"]

	if n == 0:
		print("So we just gonna sit here?")
		return None

	if n == 1:
		print(empty_list)
		return empty_list
	else:

		def rps_rounds(n, rps_list):
			new_list = []
			
			if n == 1:
				print(rps_list)
				return rps_list
			else:
				for i in rps_list:
					new_list.append(i + rock)
					new_list.append(i + paper)
					new_list.append(i + scissors)

				rps_rounds(n-1, new_list)

			
		rps_rounds(n,empty_list)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    rock_paper_scissors(num_plays)
  else:
    print('Usage: rps.py [num_plays]')