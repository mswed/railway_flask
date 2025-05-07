from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def hello():
    logger.info('Root route accessed!')
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
