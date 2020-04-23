import sys
import os
import io
import re
from datetime import datetime,timedelta

def shift(path,offset):
    with io.open('synced.srt','wt',encoding='utf8') as synced:
        with io.open(path,'r',encoding='utf8') as file:
            for line in file:
                line=replace(line,offset)
                synced.write(line)
            

def replace(line,offset):
    match=re.search("^(\d+:\d+:\d+,\d+)\s--\>\s(\d+:\d+:\d+,\d+)",line)
    if match:
        return add_offset(match.group(1),offset)+" --> "+add_offset(match.group(2),offset)+"\n"
    else:
        return line
        
def add_offset(time,offset):
    time=datetime.strptime(time,'%H:%M:%S,%f')
    return (time+timedelta(seconds=offset)).strftime("%H:%M:%S,%f")[:-3]

if __name__=="__main__":
	if len(sys.argv) < 3 :
    		print("error")
    		sys.exit("usage: python sub-sync.py srt_file offset")

	if os.path.isfile(sys.argv[1])==False :
    		sys.exit("Error: invalid file path")

	offset=int(sys.argv[2])
	path=sys.argv[1]

    if offset==0:
		sys.exit("already shifted :)")
        
	shift(path,offset)