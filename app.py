from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    t = ''
    q = ''

    if request.method == 'POST':
        t = request.form.get('t', '').strip()
        if t:
            q = f'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={t}'

    return render_template('index.html', t=t, q=q)

if __name__ == '__main__':
    app.run(debug=True)
