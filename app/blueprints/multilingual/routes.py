from flask import render_template, Blueprint, g, redirect, request, current_app, abort, url_for
from flask_babel import gettext
from app import app

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
def startpage(name='René'):
    return render_template('multilingual/startpage.html', languages=current_app.config['LANGUAGE_DATA'])


@multilingual.route('/diagnostik', defaults={'lang_code': 'de'})
@multilingual.route('/diagnostic', defaults={'lang_code': 'en'})
@multilingual.route('/diagnostica', defaults={'lang_code': 'fr'})
def diagnostic():
    return render_template('multilingual/diagnostic.html', languages=current_app.config['LANGUAGE_DATA'])


@multilingual.route('/team')
def team():

    doctor_dict = {
        "doctor1": "Dr. Doktor Arzt",
        "doctor1desc": "Doktor Arzt ist schon seit langem in der Medizin tätig, er hat alles erreicht und vielen Menschen geholfen.",
        "doctor2": "Dr. Doktorbruder Arzt",
        "doctor2desc": "Doktorbruder Arzt ist nicht ganz so erfolgreich wie Doktor Arzt. Eigentlich läuft Doktorbruder seinem Bruder die ganze Zeit nur hinterher.",
    }

    # TODO make name list
    assistant_dict = [
        {
            "name": "Frau Arzt Helferin",
            "desc": "Doktor Arzt ist schon seit langem in der Medizin tätig, er hat alles erreicht und vielen Menschen geholfen.",
            # https://www.pexels.com/photo/crop-doctor-in-medical-uniform-with-stethoscope-standing-in-clinic-corridor-4173251/
            "img": "arzt-helferin.jpg",
        },
        {
            "name": "Herr Doktorhelfer Arzt",
            "desc": "Doktor Arzt ist schon seit langem in der Medizin tätig, er hat alles erreicht und vielen Menschen geholfen.",
            # https://www.pexels.com/de-de/foto/mann-menschen-buro-tablet-4989135/
            "img": "doktorhelfer-arzt.jpg",
        },
        {
            "name": "Frau Arzthelferin Doktor",
            "desc": "Doktor Arzt ist schon seit langem in der Medizin tätig, er hat alles erreicht und vielen Menschen geholfen.",
            # https://www.pexels.com/de-de/foto/frau-in-der-weissen-kochuniform-die-rotes-und-schwarzes-smartphone-halt-5327580/
            "img": "arzthelferin-doktor.jpg",
        },
        {
            "name": "Frau Helferinnen Helferin",
            "desc": "Doktor Arzt ist schon seit langem in der Medizin tätig, er hat alles erreicht und vielen Menschen geholfen.",
            # https://www.pexels.com/photo/woman-in-white-scrub-suit-wearing-black-framed-eyeglasses-5214964/
            "img": "helferinnen-helferin.jpg",
        },
    ]

    return render_template('multilingual/teampage.html', languages=current_app.config['LANGUAGE_DATA'], doctor_dict=doctor_dict, assistant_dict=assistant_dict)


@multilingual.route('/location')
def location():
    tour_list = [
        {
            "titel": "Besprechungszimmer",
            "text": "Im Besprechungszimmer kann Dr. Doktor Arzt Patienten behandeln, die keine direkten Körperlichen beschwerden haben. Das heißt hier können Gespräche über privates oder phsychische Probleme gehalten werden.",
            # https://www.pexels.com/photo/brown-wooden-desk-with-rolling-chair-and-shelves-near-window-667838/
            "img": "office-2.jpg",
        },
        {
            "titel": "Entspannungs Tische",
            "text": "Die Gestaltung der Büroräume wurde von Dr. Doktor Arzt höchstpersönlich übernommen. Dabei hat er besonders auf eine gemütliche Atmosphäre geachtet.",
            # https://www.pexels.com/de-de/foto/himalaya-salzlampe-in-der-nahe-von-laptop-auf-holztisch-3653849/
            "img": "office-1.jpg",
        },
        {
            "titel": "Unser Operationssaal",
            "text": "Dies ist einer der Räume wo unsere Operationen durchgeführt werden. Aber keine Sorge die meisten Probleme und Krankheiten kann Dr. Doktor Arzt durch handauflegen behandeln und heilen.",
            # https://www.pexels.com/photo/photo-of-healthcare-professional-inside-the-operating-room-4483323/
            "img": "operation-room.jpg",
        },
        {
            "titel": "Modernste Technik",
            "text": "Bei uns kommt nur die modernste Technik zum Einsatz um garantieren zu können, dass unsere Patienten die bestmögliche Behandlung erhalten. Dr. Doktor Arzt inspiziert die Geräte täglich und stellt sicher das alles nach seiner Schnauze läuft.",
            # https://www.pexels.com/de-de/foto/blick-auf-den-operationssaal-247786/
            "img": "operation-room-modern.jpg",
        },
        {
            "titel": "Unsere Zimmer",
            "text": "Unsere Betten sind unglaublich gemütlich und alle Patienten freuen sich über die Gesellschaft in den anliegenden Betten. Besonders wenn sie sich über die unglaublichen Geschichten austauschen können, die sie mit Dr. Doktor Arzt erleben.",
            # https://www.pexels.com/de-de/foto/weisse-krankenhausbetten-236380/
            "img": "hospital-bed.jpg",
        },
        {
            "titel": "Warten im Flur",
            "text": "Manchmal kann es sogar passieren, das sich ganze Gruppen von Menschen in unseren Fluren sammeln, nur um einmal einen Blick auf Dr. Doktor Arzt erhaschen zu können.",
            # https://www.pexels.com/de-de/foto/menschen-glas-fenster-klinik-127873/
            "img": "hallway.jpg",
        },
        {
            "titel": "Frau Helferinnen Helferin bei der Arbeit",
            "text": "Die Arbeit hier ist vielfältig und aufregend, besonder wenn Dr. Doktor Arzt mal wieder im Raum ist, dann kann kaum einer die Hände bei sich halten.",
            # https://www.pexels.com/photo/woman-in-white-dress-shirt-using-macbook-air-5214959/
            "img": "hard-at-work.jpg",
        },
    ]

    return render_template('multilingual/location.html', languages=current_app.config['LANGUAGE_DATA'], tour_list=tour_list)

@multilingual.route('/Stellenangebote', defaults={'lang_code': 'de'})
@multilingual.route('/Jobs', defaults={'lang_code': 'en'})
@multilingual.route('/Offres', defaults={'lang_code': 'fr'})
# @multilingual.route('/jobs')
def jobs():
    return render_template('multilingual/jobs.html', languages=current_app.config['LANGUAGE_DATA'])
