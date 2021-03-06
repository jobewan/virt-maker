import os
def info():
  print('')
def pre(marshal):
  command = 'qemu-img'
  from distutils.spawn import find_executable
  if not find_executable(command):
    print("Cannot find file '%s'"%(command))
    marshal['status'] = False
  return(marshal)
def build(marshal):
  args = marshal['link']['argument']
  body = marshal['link']['body']
  hash = marshal['link']['last']
  verbose = marshal['settings']['verbose']
  settings = marshal['settings']
  retval = False
  if args == "": args = False
  if args and not args == 'export':
    if verbose:
      cmd = 'qemu-img convert -f qcow2 -O qcow2 %s "%s"'%(hash,args)
      print(cmd)
    else:
      cmd = 'qemu-img convert -p -f qcow2 -O qcow2 %s "%s" >/dev/null 2>&1'%(hash,args)
  if os.system(cmd) == 0:
    marshal['status'] = True
  else:
    marshal['status'] = False
  return(marshal)