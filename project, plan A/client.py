from socketio import *
from print_module import *

client = Client()

client.connect("http://127.0.0.1:5000")

@client.on('start alaki')
def start_alaki () :
    client.emit('alaki')

@client.on('printer')
def printer (data) :
    print(data)

@client.on('printer2')
def printer2 (data) :
    print(data, end = ' ')

@client.on('table')
def table(data) :
    print('im table')
    table_printer(data)

@client.on('pieces')
def pieces (data) :
    print('im piece')
    pieces_printer(data)

@client.on('get_input')
def input_geter (data):
    inp = input(data)
    if 'Row' in data :
        client.emit('Row getter', data = inp)
    elif 'Column' in data :
        client.emit('Column getter', data = inp)
    elif 'piece' in data :
        client.emit('piece getter', data = inp)
    pass


@client.on('player added')
def player_added(data) :
    print(data)

@client.event
def connect():
    print ("I'm connected!")

@client.event
def disconnect() :
    print ('I\'m disconnected')

@client.on('game start')
def start (data) :
    print(data)


username = input('Enter your name : ') 
def user_mes(user_mes):
    print(user_mes)
client.emit('add user', data = username )#, callback = user_mes)




