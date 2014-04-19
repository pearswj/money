import cherrypy
import db
#import Cheetah

class HelloWorld(object):
    def index(self):
        f = open('index.html', 'r')
        d = f.read()
        f.close()
        return d
        
    index.exposed = True
    
    def transactions(self):
        return db.get_json()
        
    transactions.exposed = True

def start():
    cherrypy.quickstart(HelloWorld())