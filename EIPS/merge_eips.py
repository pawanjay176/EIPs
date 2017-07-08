""" @author: Pawan Dhananjay """

import os

cwd = os.getcwd()
all_eips = [filename for filename in os.listdir(cwd) if filename.endswith('.md')]
all_eips.sort()
master_eip = open('master_eips.md','w')

for eip in all_eips:
	
	current_file = open(os.path.join(cwd,eip),'r')
	
	master_eip.write('#'+eip+'\n')
	master_eip.write(current_file.read())
	master_eip.write('\n\n')
	current_file.close()

master_eip.close()
