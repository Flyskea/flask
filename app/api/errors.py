from flask import render_template, request, jsonify
from ..main import main

@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'page not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404

def forbidden(message):
    response =  jsonify({'errors': 'forbidden', 'message': message})
    response.status_code = 403
    return response
    
def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response
