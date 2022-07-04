# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional, Union

import msrest.serialization


class AddMemberRequest(msrest.serialization.Model):
    """AddMemberRequest.

    :ivar email:
    :vartype email: str
    :ivar role: role. Known values are: "MEMBER", "OWNER".
    :vartype role: str or ~azure.oep.entitlement.models.Role
    """

    _attribute_map = {
        'email': {'key': 'email', 'type': 'str'},
        'role': {'key': 'role', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        email: Optional[str] = None,
        role: Optional[Union[str, "_models.Role"]] = None,
        **kwargs
    ):
        """
        :keyword email:
        :paramtype email: str
        :keyword role: role. Known values are: "MEMBER", "OWNER".
        :paramtype role: str or ~azure.oep.entitlement.models.Role
        """
        super(AddMemberRequest, self).__init__(**kwargs)
        self.email = email
        self.role = role


class AddMemberResponse(msrest.serialization.Model):
    """AddMemberResponse.

    :ivar email:
    :vartype email: str
    :ivar role:
    :vartype role: str
    """

    _attribute_map = {
        'email': {'key': 'email', 'type': 'str'},
        'role': {'key': 'role', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        email: Optional[str] = None,
        role: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword email:
        :paramtype email: str
        :keyword role:
        :paramtype role: str
        """
        super(AddMemberResponse, self).__init__(**kwargs)
        self.email = email
        self.role = role
