from os import name
from flask import Flask

run=Flask(__name__)

@run.route('/')
def index():
    return 'This is first Html'
if __name__=='__main__':
    run.run(debug=True)