import os
def provider(body,hash,args,verbose,image):
	cmd = 'virt-builder'
	if verbose:
		cmd = '%s %s'%(cmd,args)
	else:
		cmd = '%s --quite %s'%(cmd,args)
	return(os.system(cmd))