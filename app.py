from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 数据库模型
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)


# 路由定义
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # 在此处理表单数据，例如保存到数据库或发送邮件
        return f"感谢您的留言, {name}! 我们将尽快回复您。"
    return render_template("contact.html")


@app.route("/resources")
def resources():
    all_resources = Resource.query.all()
    return render_template("resources.html", resources=all_resources)


@app.route('/media')
@app.route('/news')
def media_or_news():
    return render_template('media_and_news.html')



# 启动应用
if __name__ == "__main__":
    # 确保数据库已创建
    with app.app_context():
        db.create_all()
    app.run(debug=True)


@app.route('/all-news')
def all_news():
    news_data = [
        {"title": "恒丰银行北京分行...", "date": "2024年11月21日", "link": "https://example.com/news1",
         "image_url": "static/images/news1.png"},
        {"title": "暖城有爱...", "date": "2024年11月15日", "link": "https://example.com/news2",
         "image_url": "static/images/news2.png"},
        {"title": "由打造‘光明影院’...", "date": "2024年11月17日", "link": "https://example.com/news3",
         "image_url": "static/images/news3.png"},
        # 添加更多新闻数据
    ]
    return render_template('all_news.html', all_news=news_data)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # 首页

@app.route('/media')
def media():
    return render_template('media.html')  # 媒体页面

@app.route('/news')
def news():
    return render_template('news.html')  # 新闻页面

@app.route('/videos')
def videos():
    return render_template('videos.html')  # 视频页面


@app.route('/resources')
def resources():
    return render_template('resources.html')  # 加载资源中心页面


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # 使用SQLite数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁用信号系统
db = SQLAlchemy(app)

# app/models.py
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.String(200), nullable=False)  # 摘要字段，不能为空
    content = db.Column(db.Text, nullable=False)
    published_on = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f"<News {self.title}>"
@app.before_request
def create_tables():
    db.create_all()  # 创建所有表


def models():
    return None
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blind-awareness')
def blind_awareness():
    return render_template('blind-awareness.html')

if __name__ == '__main__':
    app.run(debug=True)
