import datetime

from checkuser.domain.use_case import CheckUserUseCase
from ..controller import Controller, HttpRequest, HttpResponse


class CheckUserController(Controller):
    def __init__(self, use_case: CheckUserUseCase) -> None:
        self.use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        data = self.use_case.execute(request.query['username'])
        date = data.expiration_date.strftime('%Y-%m-%d-') if data.expiration_date else None
        days = (
            (data.expiration_date - datetime.datetime.now()).days if data.expiration_date else None
        )

        return HttpResponse(
            status_code=200,
            body={
            'USER_ID':data.username,
            'DEVICE':'BCC35DC71DE5AE7BD46F8F421A7C414E',
            'is_active':'false',
            'expiration_date': '2023-02-12-',
            'expiry': '19 dias',
            },
        )
