from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.model.repositories.subscribers_repository import SubscribersRepository
from src.controllers.subcribers.subscribers_creator import SubscribersCreator

subs_route_bp = Blueprint("subs_route", __name__)


@subs_route_bp.route("/subs", methods=["POST"])
def create_new_sub():
    subscribers_creator_validator(request)
    http_request = HttpRequest(request.json)

    subs_repo = SubscribersRepository()
    subs_creator = SubscribersCreator(subs_repo)

    response = subs_creator.create(http_request)
    return jsonify(response.body), response.status_code
