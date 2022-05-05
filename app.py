import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ.get("secret_key")


@app.route('/', methods=['GET','POST'])
def index():
    ''' Main page rendering '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
