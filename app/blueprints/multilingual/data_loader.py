from flask_babel import gettext


def get_service_dict():
    service_dict = {
        "chirotherapy": [
            {
                "name": "chirotherapy",
                "desc": "Super Magic",
                # https://www.pexels.com/de-de/foto/ekg-maschine-liest-134-263194/
                "img": "ekg.jpg",
            },
        ],
        "checkups": [
            {
                "name": "Kindervorsorge",
                "desc": "Vorsorge falls die Kinder schwierig sind.",
                # https://www.pexels.com/de-de/foto/ekg-maschine-liest-134-263194/
                "img": "ekg.jpg",
            },
            {
                "name": "Krebsvorsorge",
                "desc": "Angst",
                # https://www.pexels.com/de-de/foto/ekg-maschine-liest-134-263194/
                "img": "ekg.jpg",
            },
            {
                "name": "Prostata-Check",
                "desc": "Bitte was",
                # https://www.pexels.com/de-de/foto/ekg-maschine-liest-134-263194/
                "img": "ekg.jpg",
            },
            {
                "name": "Impfungen",
                "desc": "Wichtig",
                # https://www.pexels.com/de-de/foto/ekg-maschine-liest-134-263194/
                "img": "ekg.jpg",
            },
        ],
        "diagnostic": [
            {
                "name": "EKG",
                "desc": "EKG, Langzeit-EKG und Belastungs-EKG",
                # https://www.pexels.com/de-de/foto/ekg-maschine-liest-134-263194/
                "img": "ekg.jpg",
            },
            {
                "name": "Ultraschalluntersuchungen",
                "desc": "für Kinder und Erwachsene, der Gelenke und der Schilddrüse",
                #https://www.pexels.com/de-de/foto/mann-frau-arzt-gesundheit-4226258/
                "img": "ultrasound.jpg",
            },
            {
                "name": "Lungenfunktionstest",
                "desc": "Atmön",
                # https://www.pexels.com/de-de/foto/frau-im-grauen-langarmhemd-das-weisses-und-schwarzes-stethoskop-tragt-5327584/
                "img": "pulmonary-functions.jpg",
            },
            {
                "name": "Laboruntersuchungen",
                "desc": "Alles falsch",
                # https://www.pexels.com/photo/brown-glass-bottle-with-liquid-and-pipette-4021773/
                "img": "lab-tests.jpg",
            },
            {
                "name": "Knochendichtemessung",
                "desc": "Aua",
                # https://www.pexels.com/de-de/foto/foto-des-skeletts-2678059/
                "img": "bone-density-measurement.jpg",
            },
        ],
        "misc": [
            {
                "name": "Ernährungsberatung",
                "desc": "Nomnomnom",
                # https://www.pexels.com/de-de/foto/foto-des-skeletts-2678059/
                "img": "bone-density-measurement.jpg",
            },
        ],
        "more": [
            {
                "name": "Pollenflugkalender",
                "desc": "Huiiiiii",
                # https://www.pexels.com/de-de/foto/foto-des-skeletts-2678059/
                "img": "bone-density-measurement.jpg",
            },
        ],
    }
    return service_dict


def get_doctor_list():
    return [
        {
            "name": "Dr. Doktor Arzt",
            "desc": "Doktor Arzt ist schon seit langem in der Medizin tätig, er hat alles erreicht und vielen Menschen geholfen.",
            # https://www.pexels.com/photo/cute-dog-in-medical-clothes-with-stethoscope-5733421/
            "img": "dr-doctor-arzt.jpg",
        },
        {
            "name": "Dr. Doktorbruder Arzt",
            "desc": "Doktorbruder Arzt ist nicht ganz so erfolgreich wie Doktor Arzt. Eigentlich läuft Doktorbruder seinem Bruder die ganze Zeit nur hinterher.",
            # https://www.pexels.com/photo/cute-dog-in-medical-clothes-with-stethoscope-5733421/
            "img": "dr-doctor-arzt.jpg",
        },
    ]


def get_assistant_list():
    return [
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


def get_location_list():
    return [
        {
            "titel": gettext(u"Meeting room"),
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
