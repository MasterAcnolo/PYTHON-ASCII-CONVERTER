from flask import Flask, render_template, request, send_file
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ASCII_SETS = {
    "classic": "@%#*+=-:. ",
    "pixel": "█▓▒░ ",
    "detailed": "$@B%8&WM#oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,^'. "
}

def image_to_ascii(image_path, new_width=100, charset="classic", color=False):
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    image = image.resize((new_width, new_height)).convert("RGB")

    ascii_chars = ASCII_SETS.get(charset, ASCII_SETS["classic"])
    pixels = list(image.getdata())

    ascii_str = ""
    for i in range(0, len(pixels), new_width):
        line = ""
        for j in range(new_width):
            if i + j < len(pixels):
                gray = sum(pixels[i + j]) // 3
                char = ascii_chars[gray // (255 // (len(ascii_chars) - 1))]
                if color:
                    r, g, b = pixels[i + j]
                    char = f'<span style="color: rgb({r},{g},{b})">{char}</span>'
                line += char
        ascii_str += line + "\n"
    return ascii_str

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "Aucun fichier envoyé", 400
        
        file = request.files["file"]
        if file.filename == "":
            return "Aucun fichier sélectionné", 400

        width = int(request.form.get("width", 100))
        charset = request.form.get("charset", "classic")
        color = "color" in request.form
        
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        ascii_art = image_to_ascii(file_path, width, charset, color)
        return render_template("index.html", ascii_art=ascii_art, width=width, charset=charset, color=color)

    return render_template("index.html", ascii_art=None)

@app.route("/download")
def download():
    ascii_art = request.args.get("ascii_art", "")
    with open("ascii_output.txt", "w", encoding="utf-8") as f:
        f.write(ascii_art)
    return send_file("ascii_output.txt", as_attachment=True)

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
