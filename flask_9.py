from flask import Flask, render_template

app = Flask(__name__) #make instance

def Articles():
    articles = [
        { 'id' : 1,
          'title' : 'Article One',
          'body' : 'Hello Dic',
          'author' : 'chu',
          'create_date' : '04-09-2017'},
        {'id': 2,
         'title': 'Article Two',
         'body': 'Hello Dic',
         'author': 'yeon',
         'create_date': '04-09-2017'},
        {'id': 3,
         'title': 'Article Three',
         'body': 'Hello Dic',
         'author': 'jin',
         'create_date': '04-09-2017'}
    ]
    return articles


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9209)