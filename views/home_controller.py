from flask import render_template
from config import app


class HomeController(object):

    @staticmethod
    @app.route('/')
    def index():
        return render_template('home/index.html')

    @staticmethod
    @app.route('/about')
    def about():
        return render_template('home/about.html')

    @staticmethod
    @app.route('/contact')
    def contact():
        return render_template('home/contact.html')

    @staticmethod
    @app.route('/unit')
    def unit():
        return render_template('home/unit.html')

    @staticmethod
    @app.route('/science')
    def science():
        return render_template('home/science.html')

    @staticmethod
    @app.route('/accreditation')
    def accreditation():
        return render_template('home/accreditation.html')

    @staticmethod
    @app.route('/entrants')
    def entrants():
        return render_template('home/entrants.html')

    @staticmethod
    @app.route('/students')
    def students():
        return render_template('home/students.html')