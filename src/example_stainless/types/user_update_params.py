# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    id: int

    age: int

    email: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    full_name: Annotated[str, PropertyInfo(alias="fullName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    password: str

    phone: str

    username: str

    user_status: Annotated[int, PropertyInfo(alias="userStatus")]
    """User Status"""
