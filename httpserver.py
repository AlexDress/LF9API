from flask import Flask, render_template
from markupsafe import escape
# initialisiere Flask-Server
app = Flask(__name__)
# definiere Route für Hauptseite
@app.route('/')
def index():
 # gebe Antwort an aufrufenden Client zurück
 return render_template('Index.html')

@app.route('/eingaenge')
def eingaenge():
 # Antwort
    return render_template('eingaenge.html')

@app.route('/ausgaenge')
def ausgaenge():
 # Antwort
    return render_template('ausgaenge.html')

if __name__ == '__main__':
 # starte Flask-Server
 app.run(host='0.0.0.0', port=5000)

