Quarto Multinode (Pre-phase)
The following instructions help you set up your environment for the project.

We highly and strongly recommend that you do it  the virtual environment way. it has two or three steps more but the knowledge about virtual environments are necessary for your future path in python programming.

 

Windows (the virtual environment way)
Open cmdor powershell in the folder which server.py and client.pyare in:

open the directory and hold SHIFT button and  Right-Click . then you must see the option Open command window here or Open PowerShell here.
In Windows 11 hold SHIFT button and press RightClick. While holding SHIFT click on Show more options. then you must see the option Open command window here or Open PowerShell here.
Install virtualenv package using pip:

pip3 install virtualenv
Create a virtual environment named quarto_venv:

virtualenv quarto_venv
activate your newly created virtualenvironment:

.\quarto_venv\Scripts\activate
note: If you're using powershell and got an error about PSSecurityException  execute the following command and execute the above command again.

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
 

now execute following command:

pip install python-socketio gevent requests websocket-client
the above command installs some python packages we need for this project.

then run server.py:

python server.py
on a separate command line run client.py:

python client.py
after running client.py , you should see some logs like following on server.py execution:

127.0.0.1 - - [2021-12-13 00:19:45] "GET /socket.io/?transport=polling&EIO=4&t=1639342185.6107757 HTTP/1.1" 200 243 0.000432
itgWKqS9A51uiinoAAAB connected!
127.0.0.1 - - [2021-12-13 00:19:45] "POST /socket.io/?transport=polling&EIO=4&sid=UEZimvolDphNpVJeAAAA HTTP/1.1" 200 143 0.001755
127.0.0.1 - - [2021-12-13 00:19:45] "GET /socket.io/?transport=polling&EIO=4&sid=UEZimvolDphNpVJeAAAA&t=1639342185.6165655 HTTP/1.1" 200 189 0.000128
note: The most important piece of log is itgWKqS9A51uiinoAAAB connected! which itgWKqS9A51uiinoAAAB is the socket id that defers time to time.

You're good to go.

 

Windows (not recommended)
Open cmdor powershell in the folder which server.py and client.pyare in:

open the directory and hold SHIFT button and  Right-Click . then you must see the option Open command window here or Open PowerShell here.
In Windows 11 hold SHIFT button and press RightClick. While holding SHIFT click on Show more options. then you must see the option Open command window here or Open PowerShell here.
execute following command:

pip3 install python-socketio gevent requests websocket-client
the above command installs some python packages we need for this project.

then run server.py:

python server.py
on a separate terminal run client.py:

python client.py
after running client.py , you should see some logs like following on server.py execution:

127.0.0.1 - - [2021-12-13 00:19:45] "GET /socket.io/?transport=polling&EIO=4&t=1639342185.6107757 HTTP/1.1" 200 243 0.000432
itgWKqS9A51uiinoAAAB connected!
127.0.0.1 - - [2021-12-13 00:19:45] "POST /socket.io/?transport=polling&EIO=4&sid=UEZimvolDphNpVJeAAAA HTTP/1.1" 200 143 0.001755
127.0.0.1 - - [2021-12-13 00:19:45] "GET /socket.io/?transport=polling&EIO=4&sid=UEZimvolDphNpVJeAAAA&t=1639342185.6165655 HTTP/1.1" 200 189 0.000128
note: The most important piece of log is itgWKqS9A51uiinoAAAB connected! which itgWKqS9A51uiinoAAAB is the socket id that defers time to time.

You're good to go.

 

 

Linux (the virtual environment way)
Open a terminal in the directory which server.py and client.pyare in and install virtualenv package using pip:

sudo pip3 install virtualenv
Create a virtual environment named quarto_venv:

virtualenv quarto_venv
activate your newly created virtualenvironment:

source quarto_venv/bin/activate
now execute following command:

pip install python-socketio gevent requests websocket-client
the above command installs some python packages we need for this project.

then run server.py:

python3 server.py
on a separate terminal run client.py:

python3 client.py
after running client.py , you should see some logs like following on server.py execution:

127.0.0.1 - - [2021-12-13 00:19:45] "GET /socket.io/?transport=polling&EIO=4&t=1639342185.6107757 HTTP/1.1" 200 243 0.000432
itgWKqS9A51uiinoAAAB connected!
127.0.0.1 - - [2021-12-13 00:19:45] "POST /socket.io/?transport=polling&EIO=4&sid=UEZimvolDphNpVJeAAAA HTTP/1.1" 200 143 0.001755
127.0.0.1 - - [2021-12-13 00:19:45] "GET /socket.io/?transport=polling&EIO=4&sid=UEZimvolDphNpVJeAAAA&t=1639342185.6165655 HTTP/1.1" 200 189 0.000128
note: The most important piece of log is itgWKqS9A51uiinoAAAB connected! which itgWKqS9A51uiinoAAAB is the socket id that defers time to time.

You're good to go.

 

Linux (not recommended)
Open a terminal which server.py and client.pyare in and execute following command:

sudo pip3 install python-socketio gevent requests websocket-client
the above command installs some python packages we need for this project.

then run server.py:

python3 server.py
on a separate terminal run client.py:

python3 client.py
after running client.py , you should see some logs like following on server.py execution:

127.0.0.1 - - [2021-12-13 00:19:45] "GET /socket.io/?transport=polling&EIO=4&t=1639342185.6107757 HTTP/1.1" 200 243 0.000432
itgWKqS9A51uiinoAAAB connected!
127.0.0.1 - - [2021-12-13 00:19:45] "POST /socket.io/?transport=polling&EIO=4&sid=UEZimvolDphNpVJeAAAA HTTP/1.1" 200 143 0.001755
127.0.0.1 - - [2021-12-13 00:19:45] "GET /socket.io/?transport=polling&EIO=4&sid=UEZimvolDphNpVJeAAAA&t=1639342185.6165655 HTTP/1.1" 200 189 0.000128
note: The most important piece of log is itgWKqS9A51uiinoAAAB connected! which itgWKqS9A51uiinoAAAB is the socket id that defers time to time.

You're good to go.

 
