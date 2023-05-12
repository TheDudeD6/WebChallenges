from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

flag = "INSERT FLAG"
app.config['SECRET_KEY'] = flag

@app.route("/")
def index():

    template = """
    <html>
        <head>
            <style>
                label[for="content"] {
                    display: block;
                    text-align: center;
                    font-size: 1.5rem;
                    color: limegreen;
                }
                #content {
                    display: block;
                    margin: 0 auto;
                    text-align: center;
                    font-size: 1.5rem;
                }
                input[type="submit"] {
                    display: block;
                    margin: 0 auto;
                    font-size: 1.5rem;
                }
            </style>
        </head>
        <body style="background-image: url('INSERT IMAGE URL');">
            <form method="GET">
                <label for="content">Enter content:</label>
                <input type="text" name="content" id="content">
                <input type="submit" value="Render">
            </form>
            <hr>
            <div>Rendered content:</div>
            <pre>{{ rendered_content }}</pre>
        </body>
    </html>
    """

    content = request.args.get('content', '')
    rendered_content = render_template_string(content)

    # Check if {{config}} is in rendered_content
    if '{{config}}' in rendered_content:
        # Replace {{config}} with the actual config dictionary
        rendered_content = rendered_content.replace('{{config}}', str(app.config))

    return render_template_string(template, rendered_content=rendered_content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=False)
