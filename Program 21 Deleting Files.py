# YOU CANNOT RESTORE FILES IF THEY ARE DELETED.

import os
if os.path.isfile('log_old.txt'):
    os.remove('log_old.txt')
    print("The log_old file has been eradicated.")
else:
    print("We couldn't find the log_old file.")
