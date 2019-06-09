from database.base import db_session
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.debug = True


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    db_session.close_all()


@app.route('/')
def index():
    return "Апи тут: /graphql"


if __name__ == '__main__':
    app.run()
