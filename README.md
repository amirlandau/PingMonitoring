<h1>PingMonitoring</h1>
PingMonitoring is a Flask project that helps you to monitor the network availability of the servers in your data center using multi-threaded ping, with an option to connect remotely.

<h2>Demo</h2>
Video demo: https://vimeo.com/722235043.

<h2>Setup & Installtion</h2>

Move into the home directory:

```
$ cd ~/
```

First, you need to clone this repository:

```
$ git clone https://github.com/amirlandau/PingMonitoring.git
```

Move into the parent website directory:

```
$ cd PingMonitoring
$ cd website
```

Create a new virtual environment. We're going to call ours venv (You should too!):

```
$ python -m venv venv 
```

Activate it:

```
$ . venv/Scripts/activate  # on Windows, use "venv\Scripts\activate" instead
```

Upgrade pip:

```
$ pip install --upgrade pip  # on Windows, use "python -m pip install --upgrade pip"
```

Now go back one directory:

```
$ cd ..
```

Install the Python dependencies:

```
$ pip install -r requirements.txt
```

Running The App: 
```
$ python main.py
```

Viewing The App:
Go to `http://127.0.0.1:5000`
