from flask import Flask, render_template, url_for
from survey import survey
import socket

from list_questions import list_questions
from question_view import question_view
from edit import edit

app = Flask(__name__)
app.secret_key = 'alumniOverflow'
app.url_map.strict_slashes = False

app.register_blueprint(survey)
app.register_blueprint(list_questions)
app.register_blueprint(question_view)
app.register_blueprint(edit)

my_ip=([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]) #Get an IP that others can connect to.

@app.route('/')
def home():
    survey_link = url_for('survey.survey_q0')
    list_questions = url_for('list_questions.display')
    return render_template("home.html", survey_link=survey_link, list_questions=list_questions)
    
    
    #"<a href=" + url_for('survey.survey_q0') + ">Link to survey</a><br><a href="+ url_for('list_questions.display')  + ">Link to view questions</a>"

if __name__ == '__main__':
    app.run(host=my_ip, port=3134)
