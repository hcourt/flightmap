#!/usr/bin/python

import sys, getopt
from graph import *
from lightest_path import *
from at_distance import *
from heaviest_round_trip import *

def build_map (input):
	print 'Building map...'

	map = Graph()

	for line in input.readlines():

		args = line.rstrip().split(',', 2)
		if args[2].isdigit():
			map.add_node(args[0])
			map.add_node(args[1])
			map.add_edge(args[0], args[1], int(args[2]))
		else:
			print 'Error: received improper map input.\n'
			sys.exit(1)

	print 'Build successful.\n'
	return map
	
def do_tasks (input, output, map):
	print 'Executing tasks...'

	if map is None:
		print 'Error: map was misread or empty.\n'
		sys.exit(1)

	for line in input.readlines():

		args = line.rstrip().split(',', 1)
		ret = ''

		#will perform lightest_path
		if (len(args) == 2 and args[0] in map.nodes and args[1] in map.nodes):
			print '\t-finding quickest flight path...'
			ret = lightest_path(args[0], args[1], map)

		#will perform at_distance
		elif (len(args) == 2 and args[0] in map.nodes and args[1].isdigit()):
			print '\t-finding all airports at given distance...'
			ret = at_distance(args[0], int(args[1]), map)

		#will perform heaviest_round_trip
		elif (len(args) == 1 and args[0] in map.nodes):
			print '\t-finding the longest-duration round-trip flight path...'
			ret = heaviest_round_trip(args[0], map)
		else:
			print 'Error: unknown task format: "' + line +'"\n'
			sys.exit(1)

		output.write(','.join(ret))
		output.write('\n')

	print 'Execution successful.\n'

def main (argc, argv):
	flightfile = ''
	taskfile = ''
   	outputfile = ''
   	try:
		opts, args = getopt.getopt(argv,'hf:t:o:',['flights=','tasks=', 'out='])
	except getopt.GetoptError:
		print 'usage: ./main.py -f <flightfile> -t <taskfile> -o <outputfile>'
  	else:
  		if opts != []:
			for opt, arg in opts:
				if opt == '-h':
					print './main.py -f <flightfile> -t <taskfile> -o <outputfile>'
					sys.exit()
				elif opt in ('-f', '--flights'):
					flightfile = arg
				elif opt in ('-t', '--tasks'):
					taskfile = arg
				elif opt in ('-o', '--out'):
					outputfile = arg
			print ''
			print 'Flight file is: ' + flightfile
			print 'Task file is: ' + taskfile
			print 'Output file is: ' + outputfile
			print ''

			output = open(outputfile, 'w')
			flights = open(flightfile, 'r')
			tasks = open(taskfile, 'r')

			map = build_map(flights)
			do_tasks(tasks, output, map)

			output.close()
			flights.close()
			tasks.close()


if __name__ == '__main__':
	main(len(sys.argv[1:]), sys.argv[1:])
