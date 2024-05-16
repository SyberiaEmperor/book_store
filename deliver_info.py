
from datetime import datetime

from enum import Enum

class Pay(Enum):
    UPON_RECEIPT = 1
    UPON_ORDER = 2

class DeliverInfo:

    def __init__(self, addr, date_time, pay_way):
        if date_time < datetime.now():
            raise InvalidDateTime
        self.addr = addr
        self.date = date_time
        self.pay = pay_way

class InvalidDateTime(Exception):
    pass
