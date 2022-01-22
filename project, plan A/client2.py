from socketio import *

client = Client()
client.connect("http://127.0.0.1:5000")


username = input('Enter your name : ') 
def user_mes(user_mes):
    print(user_mes)
client.emit('add user', data = username )#, callback = user_mes)

@client.on('player added')
def player_added(data) :
    print(data)
@client.event
def connect():
    print ("I'm connected!")

@client.event
def disconnect() :
    print ('im disconnected')

@client.on('game start')
def start (data) :
    print(data)
