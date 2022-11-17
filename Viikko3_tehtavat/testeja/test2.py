from flask import Flask

app = Flask(__name__)
@app.route('/kaiku/<teksti>')
def kaiku(teksti):
    vastaus = {
        "kaiku" : teksti + " " + teksti
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)