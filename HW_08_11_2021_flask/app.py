from dotenv import load_dotenv

from flask import Flask
from flask import request

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/<string:name>', methods=['GET', 'POST'])
def index(name='WORLD'):
    print('ARGS', request.args)
    print('JSON', request.json)
    start_word = request.args.get('start_word', 'HELLO')
    finish_word = request.json.get('finish_word', '!')

    return f'<h1>{start_word.upper()} {name.upper()} {finish_word.upper()}</h1>'


@app.route('/pupils', methods=['GET', 'POST'])
def pupils():
    from db import Pupil, session
    if request.method == 'GET':
        first_name=request.args.get('first_name')
        objects = session.query(Pupil). \
                    filter(Pupil.first_name.like(f'%{first_name}%')).all()
        html_string = ''
        print(objects)
        for obj in objects:
            print(obj)
            html_string += f'<h1>{str(obj)}</h1>'
        print(html_string)
        return html_string
    if request.method == 'POST':
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        group_id = request.json.get('group_id')

        p = Pupil(first_name=first_name, last_name=last_name, group_id=group_id)
        session.add(p)
        session.commit()

        return str(p)

if __name__ == '__main__':
    app.run(reload=True)
