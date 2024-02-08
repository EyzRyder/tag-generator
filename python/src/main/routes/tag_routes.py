import re
from flask import Blueprint, request, jsonify
from src.views.http_types import HttpRequest
from src.views.tag_creator_view import TagCreaterView

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def creat_tag():
    tag_create_view = TagCreaterView()

    http_request = HttpRequest(body=request.json)
    response = tag_create_view.validate_and_create(http_request)

    return jsonify(response.body),response.status_code
