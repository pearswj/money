import cherrypy
import db
#import Cheetah

class HelloWorld(object):
    def index(self):
        return "Hello World!"
        
    index.exposed = True
    
    def transactions(self):
        return db.get_json()
        
    transactions.exposed = True

def start():
    cherrypy.quickstart(HelloWorld())