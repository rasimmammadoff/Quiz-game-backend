web: gunicorn main:app

web: gunicorn --worker-class socketio.sgunicorn.GeventSocketIOWorker --log-file=- main:app


