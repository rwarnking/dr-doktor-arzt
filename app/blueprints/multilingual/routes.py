from flask import render_template, Blueprint, g, redirect, request, current_app, abort, url_for, jsonify
from flask_babel import gettext

from datetime import datetime, date
from app import app

from .data_loader import get_assistant_list, get_doctor_list, get_frontpage_entry_list, get_job_list, get_location_list, get_service_dict
from .appointment import month_data, get_selected_date

multilingual = Blueprint('multilingual', __name__, template_folder='templates', url_prefix='/<lang_code>')


@multilingual.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)


@multilingual.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')


@multilingual.before_request
def before_request():
    if g.lang_code not in current_app.config['LANGUAGES']:
        adapter = app.url_map.bind('')
        try:
            endpoint, args = adapter.match('/de' + request.full_path.rstrip('/ ?'))
            return redirect(url_for(endpoint, **args), 301)
        except:
            abort(404)

    dfl = request.url_rule.defaults
    if 'lang_code' in dfl:
        if dfl['lang_code'] != request.full_path.split('/')[1]:
            abort(404)


@multilingual.route('/')
def startpage():
    frontpage_entry_list = get_frontpage_entry_list()
    return render_template('multilingual/startpage.html', languages=current_app.config['LANGUAGE_DATA'], frontpage_entry_list=frontpage_entry_list)


@multilingual.route('/leistungen', defaults={'lang_code': 'de'})
@multilingual.route('/services', defaults={'lang_code': 'en'})
@multilingual.route('/service', defaults={'lang_code': 'fr'})
def services():
    service_dict = get_service_dict()

    return render_template('multilingual/services.html', languages=current_app.config['LANGUAGE_DATA'], service_dict=service_dict)


@multilingual.route('/wir', defaults={'lang_code': 'de'})
@multilingual.route('/team', defaults={'lang_code': 'en'})
@multilingual.route('/équipe', defaults={'lang_code': 'fr'})
def team():
    doctor_list = get_doctor_list()
    assistant_list = get_assistant_list()

    return render_template('multilingual/teampage.html', languages=current_app.config['LANGUAGE_DATA'], doctor_list=doctor_list, assistant_list=assistant_list)


@multilingual.route('/räumlichkeiten', defaults={'lang_code': 'de'})
@multilingual.route('/location', defaults={'lang_code': 'en'})
@multilingual.route('/locaux', defaults={'lang_code': 'fr'})
def location():
    location_list = get_location_list()

    return render_template('multilingual/location.html', languages=current_app.config['LANGUAGE_DATA'], location_list=location_list)


@multilingual.route('/anfahrt', defaults={'lang_code': 'de'})
@multilingual.route('/arrival', defaults={'lang_code': 'en'})
@multilingual.route('/arrivée', defaults={'lang_code': 'fr'})
def arrival():
    position = [52.66796769973959, 7.937729225488056] # A random hospital (Quakenbrück Germany)
    layer = 18
    return render_template('multilingual/arrival.html', languages=current_app.config['LANGUAGE_DATA'], position=position, layer=layer)


@multilingual.route('/termine', defaults={'lang_code': 'de'})
@multilingual.route('/appointment', defaults={'lang_code': 'en'})
@multilingual.route('/rencontre', defaults={'lang_code': 'fr'})
def appointment():
    day_today = datetime.today()
    selected_date = get_selected_date(day_today)
    day_slots = month_data[selected_date["month_idx"]][selected_date["day_idx"] - 1];

    today = {
        "day_idx" : day_today.day,
        "month_idx" : day_today.month,
        "year" : day_today.year,
    }

    # app.logger.warning(day_today)

    return render_template('multilingual/appointment.html', languages=current_app.config['LANGUAGE_DATA'], day_slots=day_slots, s_date=selected_date, today=today)


@multilingual.route('/appointment/<int:year>/<int:month>/<int:day>/<int:slot>', methods=['POST'])
def make_appointment(year, month, day, slot):

    if month_data[month][day-1][slot][1] == "Free":
        month_data[month][day-1][slot][1] = "Taken"

    day_slots = month_data[month][day-1];

    selected_day = date(year, month, day)
    selected_date = get_selected_date(selected_day)

    return render_template('appointment-slots.html', languages=current_app.config['LANGUAGE_DATA'], day_slots=day_slots, s_date=selected_date)


@multilingual.route('/appointment/<int:year>/<int:month>/<int:day>')
def appointment_slots(year, month, day):

    day_slots = month_data[month][day-1]

    selected_day = date(year, month, day)
    selected_date = get_selected_date(selected_day)

    return render_template('appointment-slots.html', languages=current_app.config['LANGUAGE_DATA'], day_slots=day_slots, s_date=selected_date)


@multilingual.route('/appointment/<int:year>/<int:month>')
def appointment_days(year, month):

    selected_day = date(year, month, 1)
    selected_date = get_selected_date(selected_day)

    day_today = datetime.today()
    today = {
        "day_idx" : day_today.day,
        "month_idx" : day_today.month,
        "year" : day_today.year,
    }

    return render_template('appointment-days.html', languages=current_app.config['LANGUAGE_DATA'], s_date=selected_date, today=today)


@multilingual.route('/stellenangebote', defaults={'lang_code': 'de'})
@multilingual.route('/jobs', defaults={'lang_code': 'en'})
@multilingual.route('/offres', defaults={'lang_code': 'fr'})
def jobs():
    job_list = get_job_list()
    return render_template('multilingual/jobs.html', languages=current_app.config['LANGUAGE_DATA'], job_list=job_list)
