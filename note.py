import subprocess
print '\n write:'
process = subprocess.Popen(['cat','-'], stdin=subprocess.PIPE)
# note that command `cat -` just echo what typed in after that
process.communicate('\tstdin: to stdin\n') # interact with process
