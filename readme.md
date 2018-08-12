-------------
Steps to Run
-------------
pip install -r pip-freeze-list (ensuring all packages are installed including flask, redis etc.)
On terminal start redis using this command: redis-server
In another terminal tab start flask API server with this command: python AmazonAPIServer.py
In another terminal tab run Scheduler script with this command: python Scheduler.py

Output should be visible on terminal, which may be redirected to a file of choice using something like:
python Scheduler.py > /tmp/output.txt
