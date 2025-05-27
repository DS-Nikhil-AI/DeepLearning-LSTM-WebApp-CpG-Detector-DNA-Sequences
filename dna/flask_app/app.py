from flask import Flask, render_template, request
from model_utils import load_model, predict

app = Flask(__name__)
model_fixed = load_model("flask_app/models/128dim_model.pkl")
model_padded = load_model("flask_app/models/128dim_padding_model.pkl")

@app.route('/', methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        sequence = request.form['sequence']
        model_type = request.form['model']
        if model_type == "fixed":
            output = predict(model_fixed, sequence, pad=False)
        else:
            output = predict(model_padded, sequence, pad=True, max_len=20)
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True, reload=True)
