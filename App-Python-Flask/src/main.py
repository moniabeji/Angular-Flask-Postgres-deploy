
from flask import Flask, jsonify, request

from flask_cors import CORS

from entities.entity import Session, engine, Base
from entities.exam import Exam, ExamSchema
# ... other import statements ...

# creating the Flask application
app = Flask(__name__)
CORS(app)
print(app)

# if needed, generate database schema
#Base.metadata.create_all(engine)
# check for existing data

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/exams')
def get_exams():
    # fetching from the database
    session = Session()
    exam_objects = session.query(Exam).all()

    # transforming into JSON-serializable objects
    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return jsonify(exams)
    


@app.route('/exams', methods=['POST'])
def add_exam():
    # mount exam object
    posted_exam = ExamSchema(only=('title', 'description'))\
        .load(request.get_json())
    print(posted_exam)
    exam = Exam(**posted_exam, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam)
    session.close()
    return jsonify(new_exam), 201

if __name__ == '__main__':
    app.run(port=8081)