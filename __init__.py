# Overlord library
from core.library.api import UniversalAPI


class _API(UniversalAPI):

  # API.NAME [ usually dictates the origin of endpoints ]
  NAME = "universal_api"

  # API.CLIENT_NAME [ dictates that this api belongs to a specific client ]
  CLIENT_NAME = "web_client"

  def __init__(self) -> None:
    super().__init__()


API = _API()
