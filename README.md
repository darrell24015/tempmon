# tempmon

Python program to monitor CPU temperature on a Raspberry Pi and push data to [AdafruitIO](https://io.adafruit.com/).

There are free and paid plans for AdafruitIO. Once you have an account, create a new feed.
A dashboard can be configured to display the data from the feed in different formats.
Complete documentation is [available on readthedocs.io](https://adafruit-io-python-client.readthedocs.io/en/latest/index.html).

On the Raspberry Pi, install the AdafruitIO library (pip3 is the Python package manager):

```python
 pip3 install adafruit-io
 ```
 If uploading your code to a public repository such as Github, do not expose your AdafruitIO credentials.
 Instead, put the username and API key in a separate file such as creds.py and then include the file name
 in the .gitignore file.
 
 **creds.py**
 ```python
 # Credentials for your AdafruitIO account
username = "Your_UserName"
key = "Your_API_key"
```

**.gitignore**
```python
# Hide credentials file
creds.py
```

In the main program, import the library and credentials then create an instance of the REST client
```python
import creds
from Adafruit_IO import Client

# Setup connection to AdafruitIO REST client
adafruit_io_username = creds.username
adafruit_io_key = creds.key
aio = Client(adafruit_io_username, adafruit_io_key)
```

Take a look at the code in cpu_tempmon.py for further comments.

Have fun!
 
 
 


