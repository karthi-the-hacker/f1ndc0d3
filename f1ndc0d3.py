import requests
import sys


yellow ='\033[33m'
cyan ='\033[36m'
pyr = '\033[35m'

def banner():
	print (pyr)
	print " .-----------------------------.           "
	print " |  Hi Hackers                 |           "
	print (" |  Tool   : "+ cyan + "f1nd0d3           "+pyr+   "|")
	print " |  Author : @karthi_the_hacker|           "
	print " |           Jai Hind          |           "
	print " '-----------------------------'           "
	print "                 ^      (\_/)    "
	print "                 '----- (O.o)    "
	print "                        (> <)    "
	print " "



def all():
	url = sys.argv[2]
	try:
		r = requests.get(url)
		code = r.status_code
		print(pyr + url +  cyan +"   <---- [ {} ]".format(r.status_code) )
		sys.exit()
	except:
		sys.exit()

def single():
	try:
		url = sys.argv[3]
		inl = sys.argv[2]
		r = requests.get(url)
		if ( int(r.status_code) == int(inl)):
			print(pyr + url +  cyan +"   <---- [ {} ]".format(r.status_code) )
			sys.exit()
	
	except:
		sys.exit()


def helpl():
	banner()
	print (cyan + "For single domain and all status code : " + yellow + "python f1nd0d3.py --all http://yourserver.com/ ")
	print (cyan + "For multiple domain and particular single status code : " + yellow + "cat live-domain.txt | xargs -n1 -p50 python c3cilia.py 301 http://yourserver.com/  " + yellow)
	


if (len(sys.argv)<=1):
	banner()
	print("You must provide a target. Use -h or --help for help.")
	print(" ")
	sys.exit()


if (str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help"):
	helpl()
	sys.exit()

if (str(sys.argv[1]) == "-a" or str(sys.argv[1]) == "--all"):
	all()


if (str(sys.argv[1]) == "-c" or str(sys.argv[1]) =="--code"):
	single()	


