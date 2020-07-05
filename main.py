# Flask
from flask import request, render_template

# Local
from bot.bot import make_tweet
from app import create_app
from task import publish

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        message = request.form['message']
        tags = request.form['tags']

        full_message = message + '\n' + tags

        publish.delay(full_message)
        

    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)

