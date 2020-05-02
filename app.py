from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/solreiki/solreiki/blog.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/engramarbollas/Projects/solreiki/blog.db'

db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/treatments', methods=['GET', 'POST'])
def treatments():
    return render_template('treatments.html')

@app.route('/practitioners', methods=['GET', 'POST'])
def practitioners():
    return render_template('practitioners.html')

@app.route('/testimonials', methods=['GET', 'POST'])
def testimonials():
    return render_template('testimonials.html')

@app.route('/events', methods=['GET', 'POST'])
def events():
    return render_template('events.html')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/blogeditable', methods=['GET', 'POST'])
def blogeditable():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('blogeditable.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']
    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('blogeditable'))

@app.route('/edit/<int:post_id>')
def edit(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    print('post-----------> ',post.content)
    return render_template('edit.html', post=post)

@app.route('/editpost', methods=['POST'])
def editpost():
    if request.form['btn_submit'] == 'update':
        post_id = request.form['id']
        blog = Blogpost.query.get(post_id)
        blog.title = request.form['title']
        blog.subtitle = request.form['subtitle']
        blog.author = request.form['author']
        blog.content = request.form['content']
        db.session.commit()
    if request.form['btn_submit'] == 'delete':
        post_id = request.form['id']
        Blogpost.query.filter_by(id=post_id).delete()
        db.session.commit()
    return redirect(url_for('blogeditable'))

@app.route('/faqs', methods=['GET', 'POST'])
def faqs():
    return render_template('faqs.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__': 
    app.run(debug=True) 