# run.py

from src.instance.config import config
from src.instance.flask_app import app
from src.misc.service_logger import serviceLogger as logger

if __name__ == '__main__':
    logger.info("service started at {}:{}".format(config['host_service']['host'],
                                                  config['host_service']['port']
                                                  ))

    app.run(host=config['host_service']['host'],
            port=int(config['host_service']['port']),
            threaded=True,
            debug=True
            )
