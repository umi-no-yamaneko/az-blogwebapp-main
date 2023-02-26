from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
app = Flask(__name__)

from datetime import datetime

security_headers = {
    'Strict-Transport-Security':
    'max-age=63072000; includeSubDomains; preload',
    'Content-Security-Policy':"default-src 'self'",
    'X-Content-Type-Options':'nosniff',
    'X-Frame-Options':'SAMEORIGIN',
    'X-XSS-Protection':'1; mode=block'
}

site_title = 'Test Blog'
date = datetime.now()

@app.route('/')
def index():
    return render_template('index.html',site_title = site_title, year = date.year)

@app.route('/work/page1/')
def work_c1():
    return render_template('page',page_title = 'page1',site_title = site_title, year = date.year)

@app.route('/work/page2/')
def work_c2():
    return render_template('page',page_title = 'page2',site_title = site_title, year = date.year)

@app.route('/work/page3/')
def work_c3():
    return render_template('hogehoge', page_title = 'page3',site_title = site_title, year = date.year)

@app.errorhandler(404) # 404エラーが発生した場合の処理
def error_404(error):
    return render_template('error/error.html', error_code = '404', site_title = site_title, year = date.year), 404

@app.errorhandler(500) # 500エラーが発生した場合の処理
def error_500(error):
    return render_template('error/error.html', error_code = '500', site_title = site_title, year = date.year), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)