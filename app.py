from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/module1')
def module1():
    return render_template('module1.html')

@app.route('/module2')
def module2():
    return render_template('module2.html')

@app.route('/module3')
def module3():
    return render_template('module3.html')

@app.route('/trombinoscope')
def trombinoscope():
    return render_template('trombinoscope.html', persons=persons)

@app.route('/ressource')
def ressource():
    return render_template('ressource.html', persons=persons)

persons = [
    {"first_name": "Romain", "last_name": "GROTTO", "image": "Romain_GROTTO.jpg"},
    {"first_name": "Justine", "last_name": "SYLLA", "image": "Justine_SYLLA.jpg"},
    {"first_name": "Marina", "last_name": "FABRE", "image": "Marina_FABRE.jpg"},
    {"first_name": "Anaïs", "last_name": "MOREIRA", "image": "Anaïs_MOREIRA.jpg"},
    {"first_name": "Axel", "last_name": "JUAN", "image": "Axel_JUAN.jpg"},
    {"first_name": "Marie Nathalie", "last_name": "NERI", "image": "MarieNathalie_NERI.jpg"},
    {"first_name": "Sara", "last_name": "DUVAL", "image": "Sara_DUVAL.jpg"},
    {"first_name": "Mathilde", "last_name": "Schneider", "image": "Mathilde_Schneider.jpg"},
    {"first_name": "Manon", "last_name": "DELBOULBES", "image": "Manon_DELBOULBES.jpg"},
    {"first_name": "Stephanie", "last_name": "BELLAHCENE", "image": "Stephanie_BELLAHCENE.jpg"},
    {"first_name": "Aurélie", "last_name": "CANDELON", "image": "Aurelie_CANDELON.jpg"},
    {"first_name": "Beverly", "last_name": "BOUDINAR", "image": "Beverly_BOUDINAR.jpg"},
    {"first_name": "Ouarda", "last_name": "ZATOUT", "image": "Ouarda_ZATOUT.jpg"},
    {"first_name": "Solene", "last_name": "ROUSSELLE", "image": "Solene_ROUSSELLE.jpg"},
    {"first_name": "Emma", "last_name": "CASTELLA", "image": "Emma_CASTELLA.jpg"},
    {"first_name": "Lilian", "last_name": "MENA MENA", "image": "Lilian_MENAMENA.jpg"},
    {"first_name": "Clara", "last_name": "BREST", "image": "Clara_BREST.jpg"},
    {"first_name": "Alice", "last_name": "MARAL", "image": "Alice_MARAL.jpg"},
    {"first_name": "Lou", "last_name": "CATHALA", "image": "Lou_CATHALA.jpg"},
    {"first_name": "Thomas", "last_name": "CHMIELINSKI", "image": "Thomas_CHMIELINSKI.jpg"},



]


if __name__ == '__main__':
    app.run(debug=True)
