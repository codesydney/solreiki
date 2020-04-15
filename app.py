from flask import Flask, render_template, url_for

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
    return render_template('blog.html')

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