from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # 渲染首页

@app.route('/about')
def about():
    return render_template('about.html')  # 渲染关于我们页面

@app.route('/services')
def services():
    return render_template('services.html')  # 渲染服务页面

if __name__ == '__main__':
    app.run(debug=True)  # 启动 Flask 应用
