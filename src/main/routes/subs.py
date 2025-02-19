from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.model.repositories.subscribers_repository import SubscribersRepository
from src.controllers.subcribers.subscribers_creator import SubscribersCreator
from src.controllers.subcribers.subscribers_manager import SubscribersManager

subs_route_bp = Blueprint("subs_route", __name__)


@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_sub():
    subscribers_creator_validator(request)
    http_request = HttpRequest(request.json)

    subs_repo = SubscribersRepository()
    subs_creator = SubscribersCreator(subs_repo)

    http_response = subs_creator.create(http_request)
    return jsonify(http_response.body), http_response.status_code


@subs_route_bp.route("/subscriber/link/<link>/event/<event_id>")
def subscribers_by_link(link, event_id):
    http_request = HttpRequest(params={"link": link, "event_id": event_id})

    subs_repo = SubscribersRepository()
    subs_manager = SubscribersManager(subs_repo)

    http_response = subs_manager.get_subscribers_by_link(http_request)
    return jsonify(http_response.body), http_response.status_code


@subs_route_bp.route("/subscriber/ranking/event/<event_id>")
def link_ranking(event_id):
    http_request = HttpRequest(params={"event_id": event_id})

    subs_repo = SubscribersRepository()
    subs_manager = SubscribersManager(subs_repo)

    http_response = subs_manager.get_event_ranking(http_request)
    return jsonify(http_response.body), http_response.status_code
