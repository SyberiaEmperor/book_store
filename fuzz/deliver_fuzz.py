# pylint: skip-file

from pythonfuzz.main import PythonFuzz
from datetime import *

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from deliver_info import *

@PythonFuzz
def deliver_info_fuzzing(buf):
    try:
        string = buf.decode("ascii")
        date_time = datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')
        di = DeliverInfo(string, date_time, Pay.UPON_RECEIPT)
    except ValueError:
        pass
    except InvalidDateTime:
        pass 
    
if __name__ == '__main__':
    deliver_info_fuzzing()
