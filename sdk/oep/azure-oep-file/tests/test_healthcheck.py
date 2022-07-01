import functools
import pytest

from devtools_testutils import AzureTestCase, PowerShellPreparer
import sys
import os
from azure.identity import DefaultAzureCredential
sys.path.append(os.path.abspath('../azure'))
from azure.oep.file._oep_file_client import OepFileClient

OepFilePreparer = functools.partial(
    PowerShellPreparer, 'azure'
)

class TestHealthCheckOperaion(AzureTestCase):

    # Start with any helper functions you might need, for example a client creation method:
    def create_oep_client(self, base_url):
        credential = self.get_credential(OepFileClient, is_async=False)
        client = self.create_client_from_credential(OepFileClient, credential=credential, base_url=base_url)
        return client

    def get_health_response(self, client, data_partition_id):
        return client.health.get_liveness_check(data_partition_id=data_partition_id,frame_of_reference='afabh')

    # Write your tests
    @OepFilePreparer()
    def test_health_get(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        client = self.create_oep_client(base_url=base_url)
        response = self.get_health_response(client=client, data_partition_id=data_partition_id)
        assert response == "File service is alive"
