from typing import Any, Final, Optional
from .logger import Logger

class Music:
    CONVERTION_RATIO: Final[int] = ...
    def __init__(self, logger: Optional[Logger] = ...) -> None: ...
    def set_ratings_from_discogs(self, ratings: dict[str,Any], songs: bool = ..., override: bool = ...) -> None: ...
