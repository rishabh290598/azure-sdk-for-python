import functools
import pytest

from devtools_testutils import AzureTestCase, PowerShellPreparer
import sys
import os
from azure.identity import DefaultAzureCredential
sys.path.append(os.path.abspath('../azure'))
from azure.oep.entitlement._oep_entitlement_client import OepEntitlementClient

OepEntitlementPreparer = functools.partial(
    PowerShellPreparer, 'azure'
)

class TestMemberOperaion(AzureTestCase):

    # Start with any helper functions you might need, for example a client creation method:
    def create_oep_client(self, base_url):
        credential = self.get_credential(OepEntitlementClient, is_async=False)
        client = self.create_client_from_credential(OepEntitlementClient, credential=credential, base_url=base_url)
        return client

    def get_add_member_response(self, client, data_partition_id, email, role):
        group_email = "users@dpId.contoso.com"
        return client.member.post_add_member(data_partition_id=data_partition_id,group_email=group_email,body={
            "email": email,
            "role": role
        })

    # Write your tests
    @OepEntitlementPreparer()
    def test_member_post(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        email="abcd@domain.com"
        role="MEMBER"
        client = self.create_oep_client(base_url=base_url)
        add_member_response = self.get_add_member_response(client=client, data_partition_id=data_partition_id, email=email, role=role)
        assert add_member_response is not None
        assert  add_member_response.email == email
        assert add_member_response.role == role
