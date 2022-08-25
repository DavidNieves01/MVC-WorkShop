from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from model import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = Person.get_all()


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')

@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    person_found = Person.find_person(id_person)
    if(person_found):
        return render_template('person_repeat.html')
    Person.save_person(p)
    return render_template('person_detail.html', value=p)

@app.route('/update/<id>',methods=['GET'])
def update(id):
    person_found = Person.find_person(id)
    return render_template('person_update.html',value=person_found)

@app.route('/person_update/<id>',methods=['POST'])
def person_update(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    Person.edit_person(id,first_name,last_name)
    person_found = Person.find_person(id)
    return render_template('person_detail.html', value=person_found)

@app.route('/person_delete/<id>',methods=['GET'])
def person_delete(id):
    Person.delete_person(id)   
    return render_template('person_delete.html')

@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in Person.get_all()]
    return render_template('people.html', value=data)

if __name__ == '__main__':
    app.run()