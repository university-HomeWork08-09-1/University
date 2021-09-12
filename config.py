from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd917274a73d200ab842c70309624f5ba'
app.config['TEMPLATES_AUTO_RELOAD'] = True