from flask import Flask, render_template
from flask_graphql import GraphQLView

app = Flask(__name__)
app.debug = True


app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view('graphql', graphiql=True))


@app.route('/')
def index():
    return "Go to /graphql"


if __name__ == "__main__":
    app.run()
