"""Handles all the books related requests."""

from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from theoneapi_sdk.request_handler import RequestHandler

class Book:
    """Handles all the books related requests."""

    def __init__(self, api: 'RequestHandler'):
        """Initializes the Books class."""
        self._api = api

    def list(self, **kwargs) -> Dict[str, str]:
        """Gets a list of books."""
        return self._api._get('/book', **kwargs)

    def book(self, book_id: str, **kwargs) -> Dict[str, str]:
        """Gets a book by its ID."""
        return self._api._get('/book/{}'.format(book_id), **kwargs)

    def book_chapters(self, book_id: str, **kwargs) -> Dict[str, str]:
        """Gets a list of chapters for a book."""
        return self._api._get('/book/{}/chapter'.format(book_id), **kwargs)
