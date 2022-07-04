import functools
import pytest

from devtools_testutils import AzureTestCase, PowerShellPreparer
import sys
import os
from azure.identity import DefaultAzureCredential
sys.path.append(os.path.abspath('../azure'))
from azure.oep.entitlement.aio._oep_entitlement_client import OepEntitlementClient

OepEntitlementPreparer = functools.partial(
    PowerShellPreparer, 'azure'
)

class TestMemberOperaionAsync(AzureTestCase):

    @OepEntitlementPreparer()
    async def test_member_post(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        email="abcde@domain.com"
        role="MEMBER"
        group_email = "users@dpId.contoso.com"
        credential = self.get_credential(OepEntitlementClient, is_async=True)
        client = self.create_client_from_credential(OepEntitlementClient, credential=credential, base_url=base_url)
        add_member_response = await client.member.post_add_member(data_partition_id=data_partition_id, group_email=group_email, body={
            "email": email,
            "role": role
        })
        assert  add_member_response is not None
        assert  add_member_response.email == email
        assert add_member_response.role == role
