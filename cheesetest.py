from flask import Flask, request, render_template

app = Flask(__name__)

## Basic App
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

## Routing
# @app.route('/profile/<username>') # plain string
# def profile(username):
#     return '<h3>hey there %s</h3>' % username

@app.route('/post/<int:post_id>') # spacific type
def show_post(post_id):
    return '<h3>Post ID is %s</h3>' % post_id

## HTTP method : import request
@app.route('/method')
def method():
    return 'Method used : %s' % request.method

@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == "POST":
        return 'You are using POST'
    else:
        return 'You are probably using GET'

## HTML Templates
# need packages : templates , static
@app.route('/profile/<name>')
def profileWithTemplate(name):
    return render_template('profile.html', name=name)

## Mapping Multiple URLs
@app.route('/multi')
@app.route('/multi/<user>')
def multi(user=None): ## None by default
    return render_template('user.html', user=user)


## Passing Objects into Templates
@app.route('/shopping')
def shopping():
    food = ["Cheese", "Tuna", "Beef"]
    return render_template('shopping.html', food=food)


if __name__ == '__main__':
    app.run(debug=True) # Debugger is active!

