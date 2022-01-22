from socketio import *
from checking import *

server = Server(async_mode='gevent')

# varible assignment start
players = {}
flag = False
#flag_start = False
m = ''

game_table = [['empt', 'empt', 'empt', 'empt'],
              ['empt', 'empt', 'empt', 'empt'],
              ['empt', 'empt', 'empt', 'empt'],
              ['empt', 'empt', 'empt', 'empt']
              ]

pieces = ['WTCE', 'WTCF', 'WTSE', 'WTSF',
          'WSCE', 'WSCF', 'WSSE', 'WSSF',
          'BTCE', 'BTCF', 'BTSE', 'BTSF',
          'BSCE', 'BSCF', 'BSSE', 'BSSF'
          ]

# varible assignment end

# function definition start

def put_piece(m) :
    ''' 
    it accepts the name of piece as input and place it 
    '''
    global game_table
    server.emit('printer', data = '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
    server.emit('printer', data = '▓▓▓▓▓▓▓C1▓▓▓▓▓▓C2▓▓▓▓▓▓C3▓▓▓▓▓▓C4▓▓▓▓▓▓')
    for i in range(len(game_table)) :
        server.emit('printer', data = '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        server.emit('printer', data = '▓R' + str(i+1) + '▓▓ ' + ' ║║ '.join(game_table[i]) + ' ▓▓▓▓')
        server.emit('printer', data = '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
    
    while True :
        server.emit('printer', data = 'Choose an empty place to put piece there')
        server.emit('get_input', data = 'Row : ')
        server.emit('get_input', data = 'Column : ')
        if -1 < row < 4 and -1 < column < 4 and game_table[row][column] == 'empt' :
            game_table[row][column] = m
            break
        else :
            server.emit('printer', data = 'Nonempty place or invalid input, try again..')
    
    server.emit('table', data = game_table)

    server.emit('printer', data = '\n\n')
    return None

def choose_piece () :
    global pieces, game_table
    server.emit('table', data = game_table)
    server.emit('pieces', data = pieces)
    server.emit('printer', data = '')
    while True :
        server.emit('get_input', data = 'Enter the piece name which you want to choose :')
        if m in pieces :
            pieces.remove(m)
            return m
        else :
            server.emit('printer' , data = 'Such a piece doesn\'t exist, Try again')


def check_player_num(dict) :
    if len(players.keys()) == 2 :
        for i in dict.keys() :
            server.emit('game start', data = 'The game is started \n let\'s goooo :)', room = dict[i][0])


# function definition end

#events

@server.event
def connect(sid, environ, auth):
    print(sid, "connected!")

@server.on('add user')
def add (sid, inp) :
    global players, flag_start
    if inp not in players.keys():
        players[inp] = [sid, 0]
        server.emit('player added', data = f'Welcome to the game {inp}, You are added succesfully \n Wait to start', room = players[inp][0])
        #flag_start = True
    else :
        return 'player name exist, failed to add player!'
    server.emit('start alaki')
    check_player_num(players)

@server.on('Row getter')
def Row_getter (sid, data) :
    global row 
    row = int(data) - 1

@server.on('Column getter')
def Column_getter (sid, data) :
    global column 
    column = int(data) - 1

@server.on('piece getter')
def piece_getter(sid, data) :
    global m
    m = data    
#starts ...
@server.on('alaki')
def alaki (sid):
    print('ooopppssss')
    p = choose_piece()
    print('ooopppssss', p)
    put_piece(p)





















app = WSGIApp(server)
from gevent import pywsgi

pywsgi.WSGIServer(("127.0.0.1", 5000), app).serve_forever()
