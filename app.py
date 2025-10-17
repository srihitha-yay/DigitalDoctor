from flask import Flask, Response

app = Flask(__name__)

# --- Home Page (serves the whole website) ---
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Digital Doctor</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
            }
            button {
                margin: 10px;
                padding: 10px 20px;
                font-size: 16px;
            }
            #chatbox {
                margin-top: 20px;
                border: 1px solid #ccc;
                height: 200px;
                width: 80%%;
                margin-left: auto;
                margin-right: auto;
                padding: 10px;
                overflow-y: scroll;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Digital Doctor</h1>
        <button id="student">Student</button>
        <button id="doctor">Doctor</button>
        <button id="patient">Patient</button>

        <div id="chatbox"></div>

        <script>
            document.getElementById("student").addEventListener("click", () => alert("Student mode selected"));
            document.getElementById("doctor").addEventListener("click", () => alert("Doctor mode selected"));
            document.getElementById("patient").addEventListener("click", () => alert("Patient mode selected"));
        </script>
    </body>
    </html>
    """
    return Response(html_content, mimetype="text/html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
