"""Core client provides access to all the API endpoints."""

from theoneapi_sdk.request_handler import RequestHandler
from theoneapi_sdk.book.book import Book


_DEFUALT_URL: str = "https://the-one-api.dev/v2/"


class Client:
    """Provides access to all of "TheOne" API endpoints."""

    def __init__(self, token: str = None, api_url: str=_DEFUALT_URL):
        """Initialize the client."""

        if not token:
            raise ValueError("Token is required.")

        self.token = token
        self.api_url = api_url
        request_handler = RequestHandler(self.api_url, self.token)
        self._books_api = Book(request_handler)

    @property
    def book(self) -> "Book":
        """Provides access to the Books API."""
        return self._books_api
