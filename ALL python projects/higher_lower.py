import random
data = [
    {"name": "Cristiano Ronaldo", "followers": 640, "description": "footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "followers": 505, "description": "footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 425, "description": "singer", "country": "United States"},
    {"name": "Dwayne Johnson", "followers": 396, "description": "actor", "country": "United States"},
    {"name": "Ariana Grande", "followers": 380, "description": "singer", "country": "United States"},
    {"name": "Kylie Jenner", "followers": 400, "description": "media personality", "country": "United States"},
    {"name": "Kim Kardashian", "followers": 360, "description": "media personality", "country": "United States"},
    {"name": "Beyoncé", "followers": 320, "description": "singer", "country": "United States"},
    {"name": "Khloé Kardashian", "followers": 310, "description": "media personality", "country": "United States"},
    {"name": "Justin Bieber", "followers": 295, "description": "singer", "country": "Canada"},
    {"name": "Kendall Jenner", "followers": 290, "description": "model", "country": "United States"},
    {"name": "Taylor Swift", "followers": 280, "description": "singer", "country": "United States"},
    {"name": "Jennifer Lopez", "followers": 250, "description": "singer", "country": "United States"},
    {"name": "Nicki Minaj", "followers": 230, "description": "rapper", "country": "Trinidad and Tobago"},
    {"name": "Miley Cyrus", "followers": 220, "description": "singer", "country": "United States"},
    {"name": "Katy Perry", "followers": 210, "description": "singer", "country": "United States"},
    {"name": "Drake", "followers": 145, "description": "rapper", "country": "Canada"},
    {"name": "Neymar Jr", "followers": 220, "description": "footballer", "country": "Brazil"},
    {"name": "LeBron James", "followers": 155, "description": "basketball player", "country": "United States"},
    {"name": "Virat Kohli", "followers": 270, "description": "cricketer", "country": "India"},
    {"name": "Rihanna", "followers": 150, "description": "singer", "country": "Barbados"},
    {"name": "Zendaya", "followers": 185, "description": "actress", "country": "United States"},
    {"name": "Shakira", "followers": 90, "description": "singer", "country": "Colombia"},
    {"name": "Cardi B", "followers": 165, "description": "rapper", "country": "United States"},
    {"name": "Billie Eilish", "followers": 120, "description": "singer", "country": "United States"},
    {"name": "Lewis Hamilton", "followers": 45, "description": "Formula 1 driver", "country": "United Kingdom"},
    {"name": "Stephen Curry", "followers": 55, "description": "basketball player", "country": "United States"},
    {"name": "Kevin Hart", "followers": 180, "description": "comedian", "country": "United States"},
    {"name": "Priyanka Chopra", "followers": 95, "description": "actress", "country": "India"},
    {"name": "Karim Benzema", "followers": 70, "description": "footballer", "country": "France"},
    {"name": "Emma Watson", "followers": 70, "description": "actress", "country": "United Kingdom"},
    {"name": "Dua Lipa", "followers": 90, "description": "singer", "country": "United Kingdom"},
    {"name": "Chris Brown", "followers": 145, "description": "singer", "country": "United States"},
    {"name": "Kylian Mbappé", "followers": 130, "description": "footballer", "country": "France"},
    {"name": "Bad Bunny", "followers": 45, "description": "singer", "country": "Puerto Rico"},
    {"name": "Anitta", "followers": 65, "description": "singer", "country": "Brazil"},
    {"name": "Angelina Jolie", "followers": 20, "description": "actress", "country": "United States"},
    {"name": "Tom Cruise", "followers": 10, "description": "actor", "country": "United States"},
    {"name": "Robert Downey Jr", "followers": 100, "description": "actor", "country": "United States"},
    {"name": "Scarlett Johansson", "followers": 9, "description": "actress", "country": "United States"},
    {"name": "Gal Gadot", "followers": 110, "description": "actress", "country": "Israel"},
    {"name": "Zac Efron", "followers": 50, "description": "actor", "country": "United States"},
    {"name": "Bruno Mars", "followers": 25, "description": "singer", "country": "United States"},
    {"name": "The Weeknd", "followers": 60, "description": "singer", "country": "Canada"},
    {"name": "Charlie Puth", "followers": 20, "description": "singer", "country": "United States"},
    {"name": "Camila Cabello", "followers": 65, "description": "singer", "country": "Cuba"},
    {"name": "Shawn Mendes", "followers": 70, "description": "singer", "country": "Canada"},
    {"name": "Novak Djokovic", "followers": 15, "description": "tennis player", "country": "Serbia"},
    {"name": "Roger Federer", "followers": 12, "description": "tennis player", "country": "Switzerland"},
    {"name": "Conor McGregor", "followers": 50, "description": "MMA fighter", "country": "Ireland"},
    {"name": "Anne Hathaway", "followers": 30, "description": "actress", "country": "United States"},
]
print("welcome to my higher or lower game!")
score = 0
endgame = True
while endgame:
    
    
    first_person = random.choice(data)
    print("compare A:",first_person["name"], ",",first_person["description"], "from", first_person["country"])
    
    print("""
    db    db .d8888.
    88    88 88'  YP
    Y8    8P `8bo.  
    `8b  d8'   `Y8b.
    `8bd8'  db   8D
      YP    `8888Y'
    """)

    second_person = random.choice(data)
    print("Against B:",second_person["name"], ",",second_person["description"], "from", second_person["country"])
    choice =input("who do you think has more followers on instagram? option A or B\n").lower()
    if choice not in ("a", "b"):
        print("invalid choice please choose between 'a' and 'b'")
        continue

    if first_person["followers"] == second_person["followers"]:
        print("it's a tie! moving to the next round.")
        continue

    a_is_higher = first_person["followers"] > second_person["followers"]
    correct = (choice == "a" and a_is_higher) or (choice == "b" and not a_is_higher)

    if correct:
        score += 1
        print(f"correct! your current score: {score}")
    else:
        print(f"sorry that is wrong, your final score: {score}")
        endgame = False


