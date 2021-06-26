from flask import Flask
from flask import request, Response
import sys

#Added imports for prometheus metrics

from prometheus_flask_exporter import PrometheusMetrics

from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics


app = Flask(__name__)
port = sys.argv[1];
metrics = PrometheusMetrics(app=None, path='/metrics')


@app.route("/")
def home():
    msg = request.args.get('msg')
    return Response(msg, 200)

@app.route('/healthz')
def healthz():
    return "Health Check OK\n"


# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.1.0", app_config="Flaskee")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

run_simple(hostname="0.0.0.0", port=int(port), application=dispatcher)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
