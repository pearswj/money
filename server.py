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
        #query = "SELECT * FROM transactions \
        #         WHERE description LIKE '%LUL%' \ 
        #         ORDER BY date"
        query = "SELECT * FROM transactions ORDER BY date"
        return db.get_json(query)
        
    transactions.exposed = True

def start():
    cherrypy.quickstart(HelloWorld())