from collections import OrderedDict
import src.misc.constants as cn
from src.misc.response_generator import response_generator
from src.instance.flask_app import db
from flask_api import status
import datetime
from src.misc.service_logger import serviceLogger as logger

# db add, commit, flush and refresh
def db_save(obj):
    db.session.add(obj)
    db.session.commit()
    db.session.flush()
    db.session.refresh(obj)

def db_hard_delete(obj):
    db.session.commit()
    db.session.flush()

# DictSerializable
class DictSerializable(object):
    def getasdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result

# some datatime conversion functions, being commonly used
def datetime_format(obj,format):
    if format == '%Y-%m-%d %H:%M:%S':
        datetime_output=datetime.datetime.fromtimestamp(obj).strftime('%Y-%m-%d %H:%M:%S')
    elif format == '%Y-%m-%dt%H-%M-%S':
        datetime_output=datetime.datetime.fromtimestamp(obj).strftime('%Y-%m-%dt%H-%M-%S')
    elif format == '%Y-%m':
        datetime_output=datetime.datetime.fromtimestamp(obj).strftime('%Y-%m')
    else:
        logger.error(cn.MSG_UNSUPPORTED_DATE_FORMAT, exc_info=True)
        return response_generator(cn.MSG_UNSUPPORTED_DATE_FORMAT, status.HTTP_400_BAD_REQUEST)

    return datetime_output

def datetime_now_in_epoch():
    return datetime.datetime.now().strftime('%s')
