# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from petstore_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    FOO = "/foo"
    PET = "/pet"
    PET_PET_ID = "/pet/{petId}"
