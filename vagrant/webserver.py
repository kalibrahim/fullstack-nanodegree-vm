from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                output += "<a href = /restaurants/new>Make a New Restaurant Here</a>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "<br>"
                    output += "<a href = #>Edit</a>"
                    output += "<br>"
                    output += "<a href = #>Delete</a>"
                    output += "</br></br></br>"
                
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/restaurants/new"):
                restaurants = session.query(Restaurant).all()
                output = ""
                self.send_response(200)
                self.send_header("Content-type", 'text/html')
                self.end_headers()
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><input name='restaurant' placeholder='New Restaurant Name' type='text'> <input type='submit' value='Submit'></form>"
            
            output += "</body></html>"
            self.wfile.write(output)
            return
            
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        server = HTTPServer(('', 8080), webServerHandler)
        print 'Web server running...open localhost:8080/restaurants in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()
