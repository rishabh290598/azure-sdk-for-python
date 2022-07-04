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

class TestHealthCheckOperaion(AzureTestCase):

    # Start with any helper functions you might need, for example a client creation method:
    def create_oep_client(self, base_url):
        credential = self.get_credential(OepEntitlementClient, is_async=False)
        client = self.create_client_from_credential(OepEntitlementClient, credential=credential, base_url=base_url)
        return client

    def get_liveness_response(self, client, data_partition_id):
        return client.health.get_liveness_check(data_partition_id=data_partition_id)

    def get_readiness_response(self, client, data_partition_id):
        return client.health.get_readiness_check(data_partition_id=data_partition_id)

    # Write your tests
    @OepEntitlementPreparer()
    def test_health_get(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        client = self.create_oep_client(base_url=base_url)
        liveness_response = self.get_liveness_response(client=client, data_partition_id=data_partition_id)
        assert liveness_response is None
        readiness_response = self.get_readiness_response(client=client, data_partition_id=data_partition_id)
        assert  readiness_response is None
