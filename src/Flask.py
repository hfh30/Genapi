from flask import Flask, request, render_template_string
from urllib.parse import urlparse, urlunparse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    url = 'https://www.training.cam.ac.uk/api/v1/event/path'
    if request.method == 'POST':
        new_path = request.form.get('text')     
        components = urlparse(url)
        new_components = components._replace(path=new_path)
        url = urlunparse(new_components)
    
    return render_template_string('''
        <form method="POST">
            <input name="text" type="text" placeholder="Enter new path">
            <input type="submit">
        </form>
        <p>URL: {{ url }}</p>
    ''', url=url)

if __name__ == '__main__':
    app.run(debug=True)
