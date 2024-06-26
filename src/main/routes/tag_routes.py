from flask import Blueprint, request, jsonify
from src.validators.tag_creator_validator import tag_creator_validator
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreaterView

from src.errors.error_handler import handle_errors

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def creat_tag():
    response = None
    try:
        tag_creator_validator(request)
        tag_create_view = TagCreaterView()

        http_request = HttpRequest(body=request.json)
        response = tag_create_view.validate_and_create(http_request)
    except Exception as exception:
        response = handle_errors(exception)

    return jsonify(response.body),response.status_code
