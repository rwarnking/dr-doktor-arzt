from flask import Flask, render_template
from flask_static_digest import FlaskStaticDigest

flask_static_digest = FlaskStaticDigest()

app = Flask(__name__)

flask_static_digest.init_app(app)

@app.route('/')
#@app.route('/[a-z]{2}')
def startpage(name='René'):

    # Deutsch
    #json_obj = hallormeinjsonloader(path)

    #return render_template('mainpage.html', json_obj)
    return render_template('mainpage.html', name=name)

#@app.route('/gb')
#def hello(name='René'):

    # Englisch
    #json_obj = hallormeinjsonloader(path)

    #return render_template('mainpage.html', json_obj)
    #return render_template('mainpage.html', name=name)


@app.route('/diagnostic')
def diagnostic():
    return render_template('diagnostic.html')


@app.route('/team')
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

    return render_template('teampage.html', doctor_dict=doctor_dict, assistant_dict=assistant_dict)


@app.route('/location')
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

    return render_template('location.html', tour_list=tour_list)

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')
