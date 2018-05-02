from src.misc.service_logger import serviceLogger as logger
from flask import Response, json
from datetime import datetime, date

def response_generator(payload, status):
    logger.info(payload)
    return Response(response=json.dumps({"payload": payload}), status=status, mimetype='application/json')

# json serializer
def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    return str(obj)