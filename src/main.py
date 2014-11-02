#!/usr/bin/python

import sys, getopt

def main (argc, argv):
	flightfile = ''
   	outputfile = ''
   	try:
		opts, args = getopt.getopt(argv,'hf:t:o:',['flights=','tasks=', 'out='])
	except getopt.GetoptError:
		print 'usage: ./main.py -f <flightfile> -t <taskfile> -o <outputfile>'
      	#sys.exit(2)
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
			print 'Flight file is: ' + flightfile
			print 'Task file is: ' + taskfile
			print 'Output file is: ' + outputfile

			output = open(outputfile, 'w')
			output.write ('hello there\n')

if __name__ == '__main__':
	main(len(sys.argv[1:]), sys.argv[1:])
