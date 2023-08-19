from sanic.config import Config
from sanic.request import Request
from sanic.response import (
    empty as empty_response,
    HTTPResponse,
)


class AppRequest(Request):
    @property
    def user(self) -> any:
        return self.ctx.user

    @user.setter
    def user(self, value) -> None:
        self.ctx.user = value

    @property
    def user_token(self) -> any:
        return self.ctx.user_token

    @user_token.setter
    def user_token(self, value) -> None:
        self.ctx.user_token = value

    @property
    def config(self) -> Config:
        return self.app.config

    @classmethod
    def empty(cls) -> HTTPResponse:
        return empty_response()
