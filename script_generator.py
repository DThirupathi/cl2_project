from optparse import OptionParser
import math
parser = OptionParser()
#parser.add_option("--file",dest="folderpath",help="corpus folder path - where each document has a seperate file for it")
parser.add_option("--start",dest="start",type="int",help="start range of files")
parser.add_option("--end",dest="end",type="int",help="end range of files")
parser.add_option("--processors",dest="processors",type="int",help="range jump")
(options,args) = parser.parse_args()

s = options.start
e = options.end
j = int(math.ceil((options.end-options.start+1)/float(options.processors)))

outputfilename = 'runpar2.sh'
f = open(outputfilename,'wb')

for i in range(s,e+1):
	
	if (i-s)%j == 0:

		if i+j-1<=e:
			str1 = 'python preprocessing.py --folderpath newunlabeledstatusfiles/ --start ' + str(i) + ' --end ' + str(i+j-1) + ' --outputfolder processed_unlabeledstatusfiles/'
		else:
			str1 = 'python preprocessing.py --folderpath newunlabeledstatusfiles/ --start ' + str(i) + ' --end ' + str(e) + ' --outputfolder processed_unlabeledstatusfiles/'

		#print str1
		f.write("%s\n" % str1)

f.close()
