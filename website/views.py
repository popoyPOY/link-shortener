from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
from .models import URL
from . import db, random_str

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')

        match = re.match("^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$", link)
        if match:
            new_url = URL(url=link, shorten_url=random_str())
            db.session.add(new_url)
            db.session.commit()

            query = URL.query.filter_by(url=link).first()
            if query:
               flash(request.host_url + "short/"  + query.shorten_url, category="success")
        else:
            flash("Not a valid URL", category="error")

    return render_template("home.html")


@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")


@views.route('/short/<short_url>')
def short(short_url):
    query = URL.query.filter_by(shorten_url=short_url).first()
    
    if query:
        return redirect(query.url)