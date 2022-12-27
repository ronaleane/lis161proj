from flask import Flask, render_template
from data import menu 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu/<option_type>')
def animal(option_type):
    item = menu[option_type] 
    return render_template('option_type.html', option_type_template = option_type, item_template=item) 

@app.route('/menu/<option_type>/<int:option_id>')
def specific_option(option_type, option_id):
    specific_item = menu[option_type][option_id]
    return render_template('specific_item.html', specific_item=specific_item)  

if __name__ == '__main__':
    app.run()
