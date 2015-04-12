defaults = {
	"connect":"qemu:///system",
	#"virt-type":"kvm",
	"ram":"500",
	"disk":"path=<[args]>,size=10",
	"network":"network=default",
	"graphics":"vnc",
	#"os-variant":"generic",
	"wait":"0",
}
import os
def provider(body,hash,args,verbose,image,settings):
	for line in body.split('\n'):
		if '=' in line:
			left = line.split('=')[0]
			right = '='.join(line.split('=')[1:])
			defaults[left] = right
	cmdargs = ' '
	for i in defaults:
		cmdargs += ' --%s %s'%(i,defaults[i])
	
	if not os.path.isfile(args):
		storefile = '%s/%s'%(settings['imgcache'],args)
		storefile = storefile.replace('//','/')
		if os.path.isfile(storefile):
			args = storefile
		else:
			return('No image file found.')
	imgfile = os.path.abspath(args)
	cmdargs = cmdargs.replace('<[args]>',imgfile)
	if verbose:
		cmd = 'virt-install --autostart %s --import --force'%(cmdargs)
		print cmd
	else:
		cmd = 'virt-install --autostart -q %s --import --force >/dev/null 2>&1'%(cmdargs)
	return(os.system(cmd))

