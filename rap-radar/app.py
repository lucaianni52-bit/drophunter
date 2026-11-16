from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Sezione 1: Monitor Rapper (Tutti i nomi più ascoltati della scena rap/trap)
CONCERTI_DATABASE = [
    {
        "id": 1,
        "artista": "Kid Yugi",
        "tour": "I Nomi del Diavolo Tour",
        "citta": "Milano",
        "locale": "Unipol Forum",
        "data": "2026-12-12",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Parterre in Piedi", "prezzo": 46.00, "url": "https://www.ticketone.it"},
            {"piattaforma": "Ticketmaster", "settore": "Anello B Numerato", "prezzo": 52.50, "url": "https://www.ticketmaster.it"}
        ]
    },
    {
        "id": 2,
        "artista": "Artie 5ive",
        "tour": "Aspettando La Bella Vita",
        "citta": "Roma",
        "locale": "Atlantico Live",
        "data": "2026-12-18",
        "stato": "Pochi Biglietti",
        "biglietti": [
            {"piattaforma": "Dice", "settore": "Posto Unico", "prezzo": 34.50, "url": "https://dice.fm"}
        ]
    },
    {
        "id": 3,
        "artista": "Tony Boy",
        "tour": "Nostalgia Tour",
        "citta": "Padova",
        "locale": "Gran Teatro Geox",
        "data": "2027-01-15",
        "stato": "Sold Out (Monitoraggio Attivo)",
        "biglietti": []
    },
    {
        "id": 4,
        "artista": "Simba La Rue",
        "tour": "Tunnel Live",
        "citta": "Bologna",
        "locale": "Estragon",
        "data": "2027-01-22",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "Vivaticket", "settore": "Ingresso Standard", "prezzo": 32.00, "url": "https://www.vivaticket.com"},
            {"piattaforma": "TicketOne", "settore": "Ingresso Standard", "prezzo": 32.00, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 5,
        "artista": "Baby Gang",
        "tour": "L'Angelo del Male Tour",
        "citta": "Milano",
        "locale": "Fabrique",
        "data": "2027-01-29",
        "stato": "Pochi Biglietti",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Posto Unico", "prezzo": 36.80, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 6,
        "artista": "Shiva",
        "tour": "Milano Angels Live",
        "citta": "Milano",
        "locale": "Unipol Forum",
        "data": "2027-02-05",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Parterre in Piedi", "prezzo": 49.00, "url": "https://www.ticketone.it"},
            {"piattaforma": "Ticketmaster", "settore": "Tribuna Numerata", "prezzo": 58.00, "url": "https://www.ticketmaster.it"}
        ]
    },
    {
        "id": 7,
        "artista": "Capo Plaza",
        "tour": "Ferite Tour",
        "citta": "Napoli",
        "locale": "Casa della Musica",
        "data": "2027-02-11",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Posto Unico", "prezzo": 39.00, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 8,
        "artista": "Paky",
        "tour": "Salvatore Live",
        "citta": "Torino",
        "locale": "Teatro Concordia",
        "data": "2027-02-19",
        "stato": "Sold Out (Monitoraggio Attivo)",
        "biglietti": []
    },
    {
        "id": 9,
        "artista": "Niky Savage",
        "tour": "Rapper Tour",
        "citta": "Firenze",
        "locale": "Viper Theatre",
        "data": "2027-02-26",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "Dice", "settore": "Ingresso Standard", "prezzo": 28.00, "url": "https://dice.fm"},
            {"piattaforma": "TicketOne", "settore": "Ingresso Standard", "prezzo": 29.50, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 10,
        "artista": "Nerissima Serpe & Papa V",
        "tour": "Mafia Slime Live",
        "citta": "Milano",
        "locale": "Alcatraz",
        "data": "2027-03-04",
        "stato": "Pochi Biglietti",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Posto Unico", "prezzo": 31.00, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 11,
        "artista": "Rondodasosa",
        "tour": "Trenches Baby Tour",
        "citta": "Bologna",
        "locale": "Link",
        "data": "2027-03-12",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "Vivaticket", "settore": "Ingresso Standard", "prezzo": 30.00, "url": "https://www.vivaticket.com"}
        ]
    },
    {
        "id": 12,
        "artista": "Rhove",
        "tour": "Popolari Live",
        "citta": "Padova",
        "locale": "Hall",
        "data": "2027-03-19",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Posto Unico", "prezzo": 33.00, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 13,
        "artista": "Nayt",
        "tour": "Habitat Tour",
        "citta": "Roma",
        "locale": "Orion",
        "data": "2027-03-27",
        "stato": "Sold Out (Monitoraggio Attivo)",
        "biglietti": []
    },
    {
        "id": 14,
        "artista": "Guè",
        "tour": "La G la U la E Live",
        "citta": "Milano",
        "locale": "Fabrique",
        "data": "2027-04-02",
        "stato": "Pochi Biglietti",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Posto Unico", "prezzo": 42.00, "url": "https://www.ticketone.it"}
        ]
    }
]

# Sezione 2: Eventi Principali / Big Names (Grandi numeri, Palazzetti e Stadi)
EVENTI_TOP = [
    {
        "id": 101,
        "artista": "ANNA (Anna Pepe)",
        "evento": "Vera Baddie Arena Tour",
        "citta": "Milano",
        "locale": "Unipol Forum",
        "data": "2026-12-05",
        "tag": "🔥 Altissima Richiesta",
        "stato": "Pochi Biglietti",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Parterre in Piedi", "prezzo": 49.00, "url": "https://www.ticketone.it"},
            {"piattaforma": "Ticketmaster", "settore": "Tribuna Gold", "prezzo": 69.00, "url": "https://www.ticketmaster.it"}
        ]
    },
    {
        "id": 102,
        "artista": "Sfera Ebbasta",
        "evento": "X2VR Live Tour",
        "citta": "Roma",
        "locale": "Palazzo dello Sport",
        "data": "2027-02-14",
        "tag": "⭐ Evento Top",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Parterre", "prezzo": 57.50, "url": "https://www.ticketone.it"},
            {"piattaforma": "Vivaticket", "settore": "Anello C Numerato", "prezzo": 46.00, "url": "https://www.vivaticket.com"}
        ]
    },
    {
        "id": 103,
        "artista": "Geolier",
        "evento": "Live Nei Palasport",
        "citta": "Napoli",
        "locale": "PalaPartenope",
        "data": "2027-03-10",
        "tag": "🚨 Quasi Sold Out",
        "stato": "Sold Out (Monitoraggio Attivo)",
        "biglietti": []
    },
    {
        "id": 104,
        "artista": "Lazza",
        "evento": "Locura Tour",
        "citta": "Torino",
        "locale": "Inalpi Arena",
        "data": "2027-03-22",
        "tag": "🔥 Altissima Richiesta",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "Ticketmaster", "settore": "Parterre in Piedi", "prezzo": 55.00, "url": "https://www.ticketmaster.it"},
            {"piattaforma": "TicketOne", "settore": "Secondo Anello", "prezzo": 44.00, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 105,
        "artista": "Tedua",
        "evento": "Il Paradiso Tour",
        "citta": "Firenze",
        "locale": "Nelson Mandela Forum",
        "data": "2027-04-04",
        "tag": "⭐ Evento Top",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Posto Unico Parterre", "prezzo": 51.75, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 106,
        "artista": "Tony Effe",
        "evento": "Icon Live Tour",
        "citta": "Roma",
        "locale": "Palazzo dello Sport",
        "data": "2027-04-12",
        "tag": "🔥 Altissima Richiesta",
        "stato": "Pochi Biglietti",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Parterre in Piedi", "prezzo": 48.00, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 107,
        "artista": "Rose Villain",
        "evento": "Radio Sakura Arena",
        "citta": "Milano",
        "locale": "Unipol Forum",
        "data": "2027-04-18",
        "tag": "⭐ Evento Top",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "Ticketmaster", "settore": "Parterre", "prezzo": 45.00, "url": "https://www.ticketmaster.it"},
            {"piattaforma": "TicketOne", "settore": "Anello B", "prezzo": 40.00, "url": "https://www.ticketone.it"}
        ]
    },
    {
        "id": 108,
        "artista": "Bresh",
        "evento": "Mediterraneo Live",
        "citta": "Genova",
        "locale": "Stadium Genova",
        "data": "2027-05-02",
        "tag": "🚨 Quasi Sold Out",
        "stato": "Sold Out (Monitoraggio Attivo)",
        "biglietti": []
    },
    {
        "id": 109,
        "artista": "Thasup",
        "evento": "c@ra++ere s?ec!@le Live",
        "citta": "Milano",
        "locale": "Ippodromo Snai",
        "data": "2027-06-15",
        "tag": "🔥 Evento Speciale",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Posto Unico", "prezzo": 52.00, "url": "https://www.ticketone.it"},
            {"piattaforma": "Ticketmaster", "settore": "PIT Gold", "prezzo": 74.00, "url": "https://www.ticketmaster.it"}
        ]
    },
    {
        "id": 110,
        "artista": "Ghali",
        "evento": "Casa Ghali Live",
        "citta": "Bologna",
        "locale": "Unipol Arena",
        "data": "2027-05-14",
        "tag": "⭐ Evento Top",
        "stato": "Disponibile",
        "biglietti": [
            {"piattaforma": "TicketOne", "settore": "Parterre", "prezzo": 49.50, "url": "https://www.ticketone.it"}
        ]
    }
]

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "").lower()
    solo_disponibili = request.args.get("disponibili") == "on"
    
    risultati = []
    for c in CONCERTI_DATABASE:
        match_nome = query in c["artista"].lower() or query in c["citta"].lower() or query in c["tour"].lower()
        match_disp = not solo_disponibili or len(c["biglietti"]) > 0
        if match_nome and match_disp:
            risultati.append(c)
            
    ultimo_controllo = datetime.now().strftime("%H:%M:%S")
    return render_template("index.html", concerti=risultati, query=query, solo_disponibili=solo_disponibili, ultimo_controllo=ultimo_controllo, pagina="home")

@app.route("/eventi", methods=["GET"])
def eventi():
    query = request.args.get("q", "").lower()
    solo_disponibili = request.args.get("disponibili") == "on"
    
    risultati = []
    for e in EVENTI_TOP:
        match_nome = query in e["artista"].lower() or query in e["citta"].lower() or query in e["evento"].lower()
        match_disp = not solo_disponibili or len(e["biglietti"]) > 0
        if match_nome and match_disp:
            risultati.append(e)
            
    ultimo_controllo = datetime.now().strftime("%H:%M:%S")
    return render_template("index.html", concerti=risultati, query=query, solo_disponibili=solo_disponibili, ultimo_controllo=ultimo_controllo, pagina="eventi")

if __name__ == "__main__":
    app.run(debug=True)
