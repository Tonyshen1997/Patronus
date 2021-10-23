
import os
from flask import Flask, request, jsonify


# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.


UPLOAD_FOLDER = '/Users/TonyS/Project/Patronus/Patronus/Server/Upload'
ALLOWED_EXTENSIONS = set('jpg')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET" ,"POST"])
def upload_image():
    if request.method == 'POST':
        image = request.files['image']

        image.save(os.path.join(app.config['UPLOAD_FOLDER'], '2.jpg'))

    return jsonify({'msg': 'success'})


if __name__ == "__main__":
    app.run(debug=True)
