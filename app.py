from App import create_app
from Route.main_route import main

app = create_app()
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')