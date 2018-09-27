import os
print('The current working directory is ',os.getcwd())
os.system('mkdir today')
print("\n".join(dir(os)))

import sys
err = sys.stderr
err.write('hello world')