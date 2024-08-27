from enum import Enum

from adh_sample_library_preview import AuthorizationTag

setup_authorization_tag = AuthorizationTag('setupAuthorizationTag')


class AuthorizationTagEnum(Enum):
    SetupAuthorizationTag = setup_authorization_tag
