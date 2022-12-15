from flask import Flask, request, jsonify, render_template
import os, requests, json, datetime

app = Flask(__name__)

date = datetime.datetime.now().strftime('%d-%b-%Y')

@app.route('/')
def index():
  return 'Hello from Flask!'

@app.route('/today')
def today():
  if os.path.isfile("./Warehouse/{date}.txt".format(date=date)) == True:
    TodayLog = open("./Warehouse/{date}.txt".format(date=date), "r")
    return "<pre>" + TodayLog.read() + "<pre/>"
  else:
    return "<pre>" + "File Does Not Exists" + "<pre/>"

@app.route('/requests')
def requestslog():
  if os.path.isfile("./RequestsLog.txt") == True:
    RequestsLog = open("./RequestsLog.txt", "r")
    return "<pre>" + RequestsLog.read() + "<pre/>"
  else:
    return "<pre>" + "File Does Not Exists" + "<pre/>"

@app.route('/check', methods=['POST'])
def parse_request():
  data = request.get_json(force=True)
  
  RequestsLog = open("./RequestsLog.txt", "a")
  RequestsLog.write(str(json.dumps(data)) + "\n")
  
  if os.path.isfile("./Warehouse/{date}.txt".format(date=date)) == False:
    open("./Warehouse/{date}.txt".format(date=date), "w").write(date + "\n\n")
  
  with open("./Warehouse/{date}.txt".format(date=date), 'r') as file:
    # file.write(date + "\n\n")
    Warehouse = open("./Warehouse/{date}.txt".format(date=date), "a")
    content = file.read()
    if str(json.dumps(data)) in str(content):
      print(str(json.dumps(data)) + ' - Denied')
      return jsonify('{"allowed": "false"}')
    else:
      Warehouse.write(json.dumps(data) + "\n")
      print(str(json.dumps(data)) + ' - Approved')
      return jsonify('{"allowed": "true"}')
  
  # return jsonify(data)

app.run(host='0.0.0.0', port=81)