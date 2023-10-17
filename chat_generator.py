import random
from datetime import datetime, timedelta

names = [
    "Ahmed",
    "Fatima",
    "Youssef",
    "Layla",
    "Omar",
    "Amina",
    "Khaled",
    "Sara",
    "Mohammed",
    "Nour",
    "Ali",
    "Aisha",
    "Hassan",
    "Leila",
    "Mustafa",
    "Rana",
    "Abdullah",
    "Zahra",
    "Sami",
    "Nadia"
]

verbs = [
    "Talked",
    "Ate",
    "Wrote",
    "Slept",
    "Drove",
    "Walked",
    "Read",
    "Built",
    "Played",
    "Danced",
    "Sang",
    "Saw",
    "Bought",
    "Flew",
    "Cut",
    "Fell",
    "Gave",
    "Took",
    "Made",
    "Said"
]

nouns = [
    "Table",
    "Chair",
    "Computer",
    "Book",
    "Car",
    "Phone",
    "Television",
    "House",
    "Bicycle",
    "Window",
    "Shoes",
    "Painting",
    "Refrigerator",
    "Desk",
    "Guitar",
    "Camera",
    "Clock",
    "Plant",
    "Cup",
    "Lamp"
]

last_names = [
    "Johnson",
    "Williams",
    "Smith",
    "Brown",
    "Jones",
    "Davis",
    "Harris",
    "Jackson",
    "Taylor",
    "Wilson",
    "Moore",
    "Robinson",
    "Clark",
    "Hall",
    "Thompson",
    "Turner",
    "Thomas",
    "Wright",
    "Walker",
    "Young"
]

chats = [
    "AlphaStrike",
    "TangoForce",
    "BravoSquad",
    "EchoRangers",
    "DeltaOps",
    "FoxtrotElite",
    "G.I.Jokers",
    "NavySeals",
    "RapidRecon",
    "S.W.A.T.Unit"
]

def generate_sentence():
    name = random.choice(names)
    verb = random.choice(verbs)
    noun = random.choice(nouns)
    sentence = " ".join( [name, verb, "the", noun] ) + "."
    return sentence

def generate_username():
    first_initial = random.choice(names)[0]
    last_name = random.choice(last_names)
    username = first_initial + "." + last_name
    return username

def generate_chatname():
    chat = random.choice(chats)
    return chat

def generate_chatnames(number):
    chatnames = {}
    for i in range(1, number+1):
        chatname = generate_chatname()
        chatnames[chatname] = i
        print(f'INSERT INTO "chat" (chat_name) VALUES (\'{chatname}\');')
    return chatnames

def generate_usernames(number):
    usernames = {}
    for i in range(1, number+1):
        username = generate_username()
        usernames[username] = i
        print(f'INSERT INTO "user" (username) VALUES (\'{username}\');')
    return usernames

def generate_chats(number):
    timestamp = datetime.now()

    chatnames = generate_chatnames(5)
    usernames = generate_usernames(10)
  
    for i in range(number):
        chat = random.choice( list(chatnames.values()) )
        user = random.choice( list(usernames.values()) )
        content = generate_sentence()
        print(f"INSERT INTO \"message\" (chat_id, user_id, timestamp, content) VALUES ( {chat} , {user} , '{timestamp}' , '{content}' );")

        timestamp += timedelta(seconds = random.randint(1,30))

print(generate_chats(5))