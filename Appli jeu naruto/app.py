from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionnaire avec des noms et leurs statistiques
classement = {
    'Alice': {'score': 85, 'temps': 30, 'erreurs': 2},
    'Bob': {'score': 92, 'temps': 25, 'erreurs': 1},
    'Charlie': {'score': 78, 'temps': 35, 'erreurs': 3},
    'David': {'score': 95, 'temps': 28, 'erreurs': 0},
    'Eva': {'score': 88, 'temps': 32, 'erreurs': 1}
}

@app.route('/')
def index():
    return render_template('index.html', classement=classement)

@app.route('/classement', methods=['POST'])
def classement():
    statistique_classement = request.form['statistique']
    classement_trié = sorted(classement.items(), key=lambda x: x[1][statistique_classement], reverse=True)
    return render_template('classement.html', classement_trié=classement_trié, statistique_classement=statistique_classement)

if __name__ == '__main__':
    app.run(debug=True)
