#!/usr/bin/env python3

from utils.all import *
from math import inf as INFINITY

advent.setup(2021, 23)
fin = advent.get_input()

def can_go_to_room(a, roomno, rooms):
	if a != roomno_to_a[roomno]:
		return False

	room = rooms[roomno]
	return room == a * len(room)

def move_to_room_cost(a, hi, roomno, n_in_room):
	n = abs(hi - ((roomno + 1) * 2))
	n += (max_in_room - n_in_room)
	n *= a_to_cost[a]
	return n

def move_to_room(a, hi, roomno, rooms, hallw):
	n_in_room = len(rooms[roomno])
	assert n_in_room < max_in_room
	assert a_to_roomno[a] == roomno
	assert hallw[hi] == a

	cost = move_to_room_cost(a, hi, roomno, n_in_room)

	newhallw = hallw[:hi] + '.' + hallw[hi + 1:]
	newrooms = deepcopy(rooms)
	oldroom = rooms[roomno]
	newrooms = newrooms[:roomno] + (a + oldroom[:],) + newrooms[roomno+1:]

	return cost, newhallw, newrooms

def move_to_hallw_cost(a, hi, roomno, n_in_room):
	n = abs(hi - ((roomno + 1) * 2))
	n += (max_in_room - n_in_room + 1)
	return a_to_cost[a] * n

def move_to_hallw(a, hi, roomno, rooms, hallw):
	n_in_room = len(rooms[roomno])
	assert 1 <= n_in_room <= max_in_room

	cost = move_to_hallw_cost(a, hi, roomno, n_in_room)

	newhallw = hallw[:hi] + a + hallw[hi + 1:]
	newrooms = deepcopy(rooms)
	oldroom = rooms[roomno]
	newrooms = newrooms[:roomno] + (oldroom[1:],) + newrooms[roomno+1:]

	return cost, newhallw, newrooms

def free_path(hi, roomno, hallw, log):
	hir = (roomno + 1) * 2

	if hi < hir:
		seg = hallw[hi + 1:hir + 1]
	elif hi == hir:
		seg = ''
	else:
		seg = hallw[hir:hi]

	ok = seg == '.' * len(seg)

	...#log('path "{}" {}\n', seg, 'free' if ok else 'NOT free')

	return ok

@selective_cache('hallw', 'rooms')
def solve(hallw, rooms, depth, path):
	log = rlog(depth)
	...#log('hallw: {} rooms: {}\n', hallw, rooms)

	if rooms == final:
		return 0, path

	best = INFINITY
	bestpath = None
	entered = False

	# move an amp from room to hallw
	for roomno, room in enumerate(rooms):
		if not room:
			continue

		target_a = roomno_to_a[roomno]
		if room == target_a * len(room):
			continue

		a = room[0]

		for hi in hallw_spots:
			...#log('spot {} {}\n', hi, hallw[hi])
			if hallw[hi] == '.':
				if free_path(hi, roomno, hallw, log):
					entered = True


					movecost, newhallw, newrooms = move_to_hallw(a, hi, roomno, rooms, hallw)
					...#log('{} to move {} to hallw {} from room {} --> {} {}\n', movecost, a, hi, roomno, newhallw, newrooms)

					newpath = path + (f'{a} r{roomno} --{movecost}-> h{hi}',)
					subcost, subpath = solve(newhallw, newrooms, depth + 1, newpath)
					tot = movecost + subcost

					if tot < best:
						best = tot
						bestpath = subpath

	if not entered:
		...#log('no move from room to hallw\n')

	entered = False

	# move an amp from hallw to a room
	for hi in hallw_spots:
		a = hallw[hi]
		if a == '.':
			continue

		roomno = a_to_roomno[a]

		if not can_go_to_room(a, roomno, rooms):
			continue

		if free_path(hi, roomno, hallw, log):
			entered = True
			movecost, newhallw, newrooms = move_to_room(a, hi, roomno, rooms, hallw)
			...#log('{} to move {} to room {} from hallw {} --> {} {}\n', movecost, a, roomno, hi, newhallw, newrooms)

			newpath = path + (f'{a} h{hi} --{movecost}-> r{roomno}',)
			subcost, subpath = solve(newhallw, newrooms, depth + 1, newpath)
			tot = movecost + subcost

			if tot < best:
				best = tot
				bestpath = subpath

	if not entered:
		...#log('no move from hallw to room\n')

	...#log('--> {}\n', best)
	return best, bestpath

# input:
#############
#...........#
###B#B#D#A###
  #D#C#A#C#
  #########

hallw = '...........'
rooms = ('BD', 'BC', 'DA', 'AC')
final = ('AA', 'BB', 'CC', 'DD')
chars = 'ABCD'
a_to_roomno = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
roomno_to_a = {v: k for k, v in a_to_roomno.items()}
a_to_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
hallw_spots = (0, 1, 3, 5, 7, 9, 10)
max_in_room = 2

ans, path = solve(hallw, rooms, 0, ())
advent.submit_answer(1, ans)


# input:
#############
#...........#
###B#B#D#A###
  #D#C#B#A#
  #D#B#A#C#
  #D#C#A#C#
  #########

hallw = '...........'
rooms = ('BDDD', 'BCBC', 'DBAA', 'AACC')
final = ('AAAA', 'BBBB', 'CCCC', 'DDDD')
chars = 'ABCD'
a_to_roomno = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
roomno_to_a = {v: k for k, v in a_to_roomno.items()}
a_to_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
hallw_spots = (0, 1, 3, 5, 7, 9, 10)
max_in_room = 4

ans, path = solve(hallw, rooms, 0, ())
advent.submit_answer(2, ans)