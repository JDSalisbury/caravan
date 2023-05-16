import os


def when_ready(server):
    # Add the static file mapping here
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    server.cfg.set("static-map", "/static={}".format(static_path))


workers = 3  # Number of worker processes
bind = '127.0.0.1:8000'  # Address and port to bind the server
timeout = 120  # Time in seconds before a worker is killed and restarted
preload_app = True  # Load application code before the worker processes are forked

on_worker_init = when_ready
