from flask import Flask, request, jsonify, render_template_string
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = tf.keras.models.load_model("model.keras")

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Digit Classifier</title>
</head>
<body style="font-family:sans-serif;text-align:center;">
    <h1>Upload a 28x28 Digit Image</h1>
    <form action="/" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept=".png" required><br><br>
        <input type="submit" value="Predict">
    </form>
    {% if prediction is not none %}
        <h2>Prediction: {{ prediction }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        file = request.files["file"]
        if not file:
            return render_template_string(HTML_FORM, prediction="No file uploaded")

        image = Image.open(file).convert("L")   # grayscale
        image = image.resize((28, 28))
        img_array = np.array(image) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        result = model.predict(img_array)
        prediction = int(np.argmax(result))

    return render_template_string(HTML_FORM, prediction=prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
