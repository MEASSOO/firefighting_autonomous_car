from flask import Flask, render_template_string, send_from_directory, send_file
import os
ServerApp = Flask(__name__)

ServerApp.config['UPLOAD_FOLDER'] ="./files"

print(ServerApp.config['UPLOAD_FOLDER'])

@ServerApp.route("/")
def Home():
    
    return render_template_string("<p>Hello World!</p>")

@ServerApp.route("/api/<filename>")
def getFile(filename):

    return send_from_directory(ServerApp.config['UPLOAD_FOLDER'], f"{filename}")

if __name__ == "__main__":
    
    ServerApp.run(debug=True, host="0.0.0.0")
    
    
