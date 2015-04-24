import multiprocessing

bind = "127.0.0.1:8081"
pidfile = "/var/log/gunicorn/lin.pid"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "/var/log/gunicorn/lin_access.log"
errorlog = "/var/log/gunicorn/lin_error.log"
loglevel = "debug"
