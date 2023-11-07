from flask import Flask,send_file

app=Flask(__name__)

@app.route('/')
def index():
    return send_file("Invoice.pdf")

if __name__ == '__main__':
    app.run(port=5000)