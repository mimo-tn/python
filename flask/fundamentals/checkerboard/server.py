from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html",row = 4, col = 4, color_1 = "black", color_2 = "white")
@app.route('/<int:row>')
def index_row(row):
    half_row = int(row / 2)
    return render_template("index.html",row = half_row, col = 4, color_1 = "black", color_2 = "white")
@app.route('/<int:row>/<int:col>')
def index_row_col(row,col):
    half_row = int(row / 2)
    half_col = int(col / 2)
    return render_template("index.html",row = half_row, col = half_col, color_1 = "black", color_2 = "white")

@app.route('/<int:row>/<int:col>/<string:color_11>/<string:color_22>')
def index_row_col_color(row,col,color_11,color_22):
    half_row = int(row / 2)
    half_col = int(col / 2)
    return render_template("index.html",row = half_row, col = half_col, color_1 = color_11, color_2 = color_22)
if __name__ == "__main__":
    app.run(debug=True)