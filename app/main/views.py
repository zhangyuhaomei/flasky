# -*- coding:utf-8 -*-
from flask import redirect, render_template,session,url_for
from datetime import datetime

from . import main 
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(u)
			session['known'] = False
			if app.config['FLASKY_ADMIN']:
				send_email(app.config['FLASKY_ADMIN'], 'New User',
					'mail/new_user', user=user)
		else:
			session['known'] = True 
		session['name'] = form.name.data 
		return redirect(url_for('.index'))
	return render_template('index.html',
		form=form, name=session.get('name'),
		known=session.get('known', False),
		current_time=datetime.utcnow())
		