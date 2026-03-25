bind = "0.0.0.0:8000"
workers = 2
threads = 2

daemon = False
pidfile = "gunicorn.pid"

errorlog = "gunicorn_error.log"
accesslog = "gunicorn_access.log"

max_requests = 3000
max_requests_jitter = 150