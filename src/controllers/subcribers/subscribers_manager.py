from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.subscribers_repository import (
    SubscribersRepositoryInterface,
)


class SubscribersManager:
    def __init__(self, subs_repo: SubscribersRepositoryInterface):
        self.__subs_repo = subs_repo

    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        link = http_request.params["link"]
        event_id = http_request.params["event_id"]

        subs = self.__subs_repo.select_subscribers_by_link(link, event_id)
        return self.__format_subs_by_link(subs)

    def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.params["event_id"]
        ranking = self.__subs_repo.get_ranking(event_id)
        return self.__format_event_ranking(ranking)

    def __format_subs_by_link(self, subs: dict) -> HttpResponse:
        formatted_subscribers = [{"nome": sub.nome, "email": sub.email} for sub in subs]

        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": len(formatted_subscribers),
                    "subscribers": formatted_subscribers,
                },
            },
            status_code=200,
        )

    def __format_event_ranking(self, ranking: list) -> HttpResponse:
        formatted_ranking = [
            {"link": position.link, "total_subscribers": position.total}
            for position in ranking
        ]

        return HttpResponse(
            body={
                "data": {
                    "Type": "Ranking",
                    "count": len(formatted_ranking),
                    "ranking": formatted_ranking,
                },
            },
            status_code=200,
        )
