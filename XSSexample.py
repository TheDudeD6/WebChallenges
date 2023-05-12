from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>XSS Vulnerable Page - Results</title>
            </head>
            <body>
                <h1>Your input:</h1>
                {input_text}
            </body>
            </html>
            '''
    else:
        return '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>XSS Vulnerable Page</title>
            </head>
            <body>
                <form method="post">
                    <label for="input_text">Enter your input:</label><br>
                    <input type="text" id="input_text" name="input_text"><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>
            '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=False)
