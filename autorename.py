import os
dir='.'
subdirs = [x[0] for x in os.walk(dir)]                                                                            
for subdir in subdirs:                                                                                            
	files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):
		i=0
		#print subdir
		if len(subdir)>3: 
			if not (subdir[2]=='.'):          
				print subdir[2:]                                                                                
				for file in files: 
					new_name=subdir[2:] + "-" + str(i)                                                                                       
					#print new_name        
					i=i+1
					cmd="mv \""+subdir+"/"+file+"\" \""+subdir+"/"+new_name+".jpg\""
					print cmd+"\n"
					os.system(cmd)
