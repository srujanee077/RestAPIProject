import flask
from flask import request, jsonify, url_for,redirect

app = flask.Flask(__name__)
#app.config['JSON_SORT_KEYS'] = True
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 2,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 1,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'},

    {'id': 3,
     'title': 'Eragon',
     'author': 'J.K Rowling',
     'first_sentence': 'The Dragon.',
     'published': '2000'},

    {'id': 4,
     'title': 'Eragon',
     'author': 'J.K Rowling',
     'first_sentence': 'The Dragon.',
     'published': '2000'},

    {'id': 5,
     'title': 'Eragon',
     'author': 'J.K Rowling',
     'first_sentence': 'The Dragon.',
     'published': '2000'},

    {'id': 7,
     'title': 'Eragon',
     'author': 'J.K Rowling',
     'first_sentence': 'The Dragon.',
     'published': '2000'},

    {'id': 6,
     'title': 'Eragon',
     'author': 'J.K Rowling',
     'first_sentence': 'The Dragon.',
     'published': '2000'},

    {'id': 8,
     'title': 'Eragon',
     'author': 'J.K Rowling',
     'first_sentence': 'The Dragon.',
     'published': '2000'},

    {'id': 10,
     'title': 'Eragon',
     'author': 'J.K Rowling',
     'first_sentence': 'The Dragon.',
     'published': '2000'},

    {'id': 9,
     'title': 'Eragon',
     'author': 'J.K Rowling',
     'first_sentence': 'The Dragon.',
     'published': '2000'}


]
def get_books(pageNo, per_page):
    data=sorted(books, key=lambda i: (i['id'], i['title']))
    return data[(pageNo-1)*per_page: (pageNo * per_page)]

def get_filter(keyValList):
    #list(filter(lambda d: d['type'] in keyValList, books))
    matching_dict = list(filter(lambda x: x['id'] == keyValList, books))
    return matching_dict
    # if len(matching_dict) >= 1:
    #     print (matching_dict)
    #     return matching_dict
    # else:
    #     return "Found zero or more than one in Dictionary"
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route('/books/all',methods=['GET'])
def getallBooks():
    return jsonify(sorted(books, key = lambda i: (i['id'], i['title'])) )

@app.route('/books/all/',methods=['GET'])
def getPagiBooks():
    print (request.args['page'])
    page =int(request.args['page'])
    pageSize =int( request.args['pagesize'])
    print(request.args['pagesize'])
    return jsonify(get_books(page,pageSize))

# @app.route('/books/<keyValList>] ',methods=['GET'])
# def getFilterBooks(keyValList):
#     return jsonify(get_filter(keyValList))

@app.route('/books', methods=['POST'])
def add_book():
    book = request.get_json()
    books.append(book)
    return {'id': len(books)}, 200


@app.route('/books/<int:bookID>',methods=['GET'])
def getBook(bookID):
    bookByID = [ book for book in books if (book['id'] == bookID) ]
    return jsonify({'book':bookByID})

@app.route('/books/<int:bookID>',methods=['PUT'])
def updateBook(bookID):
    book = request.get_json()
    books[bookID] = book
    return jsonify(books[bookID]),200

@app.route('/books/<int:bookID>',methods=['DELETE'])
def deleteBook(bookID):
    books.pop(bookID)
    return 'None', 200

#run app
if __name__ == '__main__':
    app.run( debug = True)