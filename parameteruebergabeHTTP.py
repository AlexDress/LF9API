from flask import Flask, request, jsonify
from markupsafe import escape
# initialisiere Flask-Server
app = Flask(__name__)
# definiere Route für Hauptseite
@app.route('/')
def index():
  # gebe Antwort an aufrufenden Client zurück
  return render_template('Index.html')

@app.route('/get', methods = ['GET'])
def get_json():
  Parameter = request.args.to_dict()
  return jsonify(Parameter)

@app.route('/post', methods = ['POST'])
def post_json():
  #if request.is_json:
  #  Parameter = request.json
  #else:
  #  Parameter = request.form
  return jsonify(request.form)

if __name__ == '__main__':
 # starte Flask-Server
 app.run(host='0.0.0.0', port=5000)