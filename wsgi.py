from app import app
application = app # our hosting requires application in passenger_wsgi

if __name__ == "__main__":
    app.run()
