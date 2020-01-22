import requests
import json
import pandas as pd
from http.server import BaseHTTPRequestHandler,HTTPServer

def getWorkers():
    db = pd.read_csv('Workers.csv')
    workersGroup = list()
    for workerFieldIndex in range(len(db)):
        worker ={'id' : int(db.iloc[workerFieldIndex]['index']),
                        'name': db.iloc[workerFieldIndex]['name'],
                        'struct': db.iloc[workerFieldIndex]['struct']}
        workersGroup.append(worker)
    return workersGroup

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(json.dumps(getWorkers()).encode('utf-8'))
serv = HTTPServer(("localhost",8000),HttpProcessor)
serv.serve_forever()