from flask_babel import gettext


def get_service_dict():
    service_dict = {
        gettext(u"chirotherapy"): [
            {
                #"name": "Chirotherapie",
                #"desc": "Super Magic",
                "name": gettext(u"chirotherapy"),
                "desc": gettext(u"chirotherapy desc"),
                # https://www.pexels.com/photo/crop-anonymous-chiropractor-examining-spine-of-fit-lady-in-hospital-4506110/
                "img": "chirotherapy.jpg",
            },
        ],
        gettext(u"checkups"): [
            {
                #"name": "Kindervorsorge",
                #"desc": "Vorsorge falls die Kinder schwierig sind.",
                "name": gettext(u"child-screening"),
                "desc": gettext(u"child-screening desc"),
                # https://www.pexels.com/photo/person-coloring-art-with-crayons-159579/
                "img": "child-screening.jpg",
            },
            {
                #"name": "Krebsvorsorge",
                #"desc": "Angst",
                "name": gettext(u"cancer-screening"),
                "desc": gettext(u"cancer-screening desc"),
                # https://www.pexels.com/photo/handwritten-list-on-paper-5466204/
                "img": "cancer-screening.jpg",
            },
            {
                #"name": "Diabeteseinstellungen DMP",
                #"desc": "Zucker",
                "name": gettext(u"diabetes"),
                "desc": gettext(u"diabetes desc"),
                # https://www.pexels.com/photo/person-holding-black-tube-1001897/
                "img": "diabetes.jpg",
            },
            {
                #"name": "Impfungen",
                #"desc": "Wichtig",
                "name": gettext(u"vaccine"),
                "desc": gettext(u"vaccine desc"),
                # https://www.pexels.com/photo/a-vaccine-vial-on-white-background-5878482/
                "img": "vaccine.jpg",
            },
        ],
        gettext(u"diagnostic"): [
            {
                #"name": "EKG",
                #"desc": "EKG, Langzeit-EKG und Belastungs-EKG",
                "name": gettext(u"ekg"),
                "desc": gettext(u"ekg desc"),
                # https://www.pexels.com/de-de/foto/ekg-maschine-liest-134-263194/
                "img": "ekg.jpg",
            },
            {
                #"name": "Ultraschalluntersuchungen",
                #"desc": "für Kinder und Erwachsene, der Gelenke und der Schilddrüse",
                "name": gettext(u"ultrasound"),
                "desc": gettext(u"ultrasound desc"),
                #https://www.pexels.com/de-de/foto/mann-frau-arzt-gesundheit-4226258/
                "img": "ultrasound.jpg",
            },
            {
                #"name": "Lungenfunktionstest",
                #"desc": "Atmön",
                "name": gettext(u"pulmonary-functions"),
                "desc": gettext(u"pulmonary-functions desc"),
                # https://www.pexels.com/de-de/foto/frau-im-grauen-langarmhemd-das-weisses-und-schwarzes-stethoskop-tragt-5327584/
                "img": "pulmonary-functions.jpg",
            },
            {
                #"name": "Laboruntersuchungen",
                #"desc": "Alles falsch",
                "name": gettext(u"lab-tests"),
                "desc": gettext(u"lab-tests desc"),
                # https://www.pexels.com/photo/brown-glass-bottle-with-liquid-and-pipette-4021773/
                "img": "lab-tests.jpg",
            },
            {
                #"name": "Knochendichtemessung",
                #"desc": "Aua",
                "name": gettext(u"bone-density-measurement"),
                "desc": gettext(u"bone-density-measurement desc"),
                # https://www.pexels.com/de-de/foto/foto-des-skeletts-2678059/
                "img": "bone-density-measurement.jpg",
            },
        ],
        gettext(u"misc"): [
            {
                #"name": "Ernährungsberatung",
                #"desc": "Nomnomnom",
                "name": gettext(u"foodadvice"),
                "desc": gettext(u"foodadvice desc"),
                # https://www.pexels.com/photo/red-apple-fruit-on-surface-209449/
                "img": "foodadvice.jpg",
            },
        ],
        gettext(u"more"): [
            {
                #"name": "Pollenflugkalender",
                #"desc": "Huiiiiii",
                "name": gettext(u"pollen"),
                "desc": gettext(u"pollen desc"),
                # https://www.pexels.com/photo/white-dandelion-flower-shallow-focus-photography-54300/
                "img": "pollen.jpg",
            },
        ],
    }
    return service_dict


def get_doctor_list():
    return [
        {
            "name": gettext(u"Doktor Arzt M.D."),
            "desc": gettext(u"Doktor Arzt desc"),
            # https://www.pexels.com/photo/cute-dog-in-medical-clothes-with-stethoscope-5733421/
            "img": "dr-doctor-arzt.jpg",
        },
        {
            "name": gettext(u"Doktorbruder Arzt M.D."),
            "desc": gettext(u"Doktorbruder Arzt desc"),
            # https://www.pexels.com/photo/cute-dog-in-medical-clothes-with-stethoscope-5733421/
            "img": "dr-doctor-arzt.jpg",
        },
    ]


def get_assistant_list():
    return [
        {
            "name": gettext(u"Ms. Arzt Helferin"),
            "desc": gettext(u"Arzt Helferin desc"),
            # https://www.pexels.com/photo/crop-doctor-in-medical-uniform-with-stethoscope-standing-in-clinic-corridor-4173251/
            "img": "arzt-helferin.jpg",
        },
        {
            "name": gettext(u"Mr. Doktorhelfer Arzt"),
            "desc": gettext(u"Doktorhelfer Arzt desc"),
            # https://www.pexels.com/de-de/foto/mann-menschen-buro-tablet-4989135/
            "img": "doktorhelfer-arzt.jpg",
        },
        {
            "name": gettext(u"Ms. Arzthelferin Doktor"),
            "desc": gettext(u"Arzthelferin Doktor desc"),
            # https://www.pexels.com/de-de/foto/frau-in-der-weissen-kochuniform-die-rotes-und-schwarzes-smartphone-halt-5327580/
            "img": "arzthelferin-doktor.jpg",
        },
        {
            "name": gettext(u"Ms. Helferinnen Helferin"),
            "desc": gettext(u"Helferinnen Helferin desc"),
            # https://www.pexels.com/photo/woman-in-white-scrub-suit-wearing-black-framed-eyeglasses-5214964/
            "img": "helferinnen-helferin.jpg",
        },
    ]


def get_location_list():
    return [
        {
            "titel": gettext(u"Meeting room"),
            "text": gettext(u"Meeting room text"),
            # https://www.pexels.com/photo/brown-wooden-desk-with-rolling-chair-and-shelves-near-window-667838/
            "img": "office-2.jpg",
        },
        {
            "titel": gettext(u"Chill Table"),
            "text": gettext(u"Chill Table text"),
            # https://www.pexels.com/de-de/foto/himalaya-salzlampe-in-der-nahe-von-laptop-auf-holztisch-3653849/
            "img": "office-1.jpg",
        },
        {
            "titel": gettext(u"Operating room"),
            "text": gettext(u"Operating room text"),
            # https://www.pexels.com/photo/photo-of-healthcare-professional-inside-the-operating-room-4483323/
            "img": "operation-room.jpg",
        },
        {
            "titel": gettext(u"Modern Instruments"),
            "text": gettext(u"Modern Instruments text"),
            # https://www.pexels.com/de-de/foto/blick-auf-den-operationssaal-247786/
            "img": "operation-room-modern.jpg",
        },
        {
            "titel": gettext(u"Our Rooms"),
            "text": gettext(u"Our Rooms text"),
            # https://www.pexels.com/de-de/foto/weisse-krankenhausbetten-236380/
            "img": "hospital-bed.jpg",
        },
        {
            "titel": gettext(u"Waiting in the hallway"),
            "text": gettext(u"Waiting in the hallway text"),
            # https://www.pexels.com/de-de/foto/menschen-glas-fenster-klinik-127873/
            "img": "hallway.jpg",
        },
        {
            "titel": gettext(u"Ms. Helferinnen Helferin at work"),
            "text": gettext(u"Ms. Helferinnen Helferin at work text"),
            # https://www.pexels.com/photo/woman-in-white-dress-shirt-using-macbook-air-5214959/
            "img": "hard-at-work.jpg",
        },
    ]


def get_job_list():
    return [
        {
            "titel": gettext(u"a Dog person"),
            "offer": [
                gettext(u"good workclimate"),
                gettext(u"education"),
                gettext(u"space"),
                gettext(u"more money"),
            ],
            "profile" : [
                gettext(u"GCSE O-levels"),
                gettext(u"Workexperience"),
                gettext(u"written and spoken Animalknowledge"),
            ],
            # https://www.pexels.com/photo/brown-wooden-desk-with-rolling-chair-and-shelves-near-window-667838/
            "img": "office-2.jpg",
        },
        {
            "titel": gettext(u"a cardiologist"),
            "offer": [
                gettext(u"good workclimate"),
                gettext(u"education"),
                gettext(u"big hearts"),
                gettext(u"more money"),
            ],
            "profile" : [
                gettext(u"German doctorate"),
                gettext(u"Workexperience"),
                gettext(u"sciencific interest"),
                gettext(u"very German language"),
            ],
            # https://www.pexels.com/photo/brown-wooden-desk-with-rolling-chair-and-shelves-near-window-667838/
            "img": "office-2.jpg",
        },
        {
            "titel": gettext(u"a medical assistant"),
            "offer": [
                gettext(u"good workclimate"),
                gettext(u"education"),
                gettext(u"view onto the parkingspot"),
                gettext(u"less money"),
            ],
            "profile" : [
                gettext(u"finished school"),
                gettext(u"Time"),
                gettext(u"Russian language"),
            ],
            # https://www.pexels.com/photo/brown-wooden-desk-with-rolling-chair-and-shelves-near-window-667838/
            "img": "office-2.jpg",
        },
    ]
