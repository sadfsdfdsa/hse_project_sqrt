from flask import Flask, jsonify, render_template, request

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='static')

errors = []


# frontend index page
@app.route('/')
def index():
    return render_template('index.html')


# all to vue router
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')


# API
@app.route('/api/v1/error', methods=['POST'])
def frontend_post_errors():
    errors.append(request.json)
    return jsonify(result='success')


@app.route('/api/v1/error', methods=['GET'])
def frontend_get_errors():
    return jsonify(errors=errors)


if __name__ == '__main__':
    app.run()
