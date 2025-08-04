from flask import Flask, render_template, send_from_directory

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk melayani aset statis (termasuk images dalam assets)
@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)