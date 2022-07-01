import functools
import pytest

from devtools_testutils import AzureTestCase, PowerShellPreparer
import sys
import os
from azure.identity import DefaultAzureCredential
sys.path.append(os.path.abspath('../azure'))
from azure.oep.file.aio._oep_file_client import OepFileClient

OepFilePreparer = functools.partial(
    PowerShellPreparer, 'azure'
)

class TestHealthCheckOperaionAsync(AzureTestCase):

    @OepFilePreparer()
    async def test_health_get(self):
        data_partition_id="dpID"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        credential = self.get_credential(OepFileClient, is_async=True)
        client = self.create_client_from_credential(OepFileClient, credential=credential, base_url=base_url)
        response = await client.health.get_liveness_check(data_partition_id=data_partition_id,frame_of_reference='fafa')
        assert response == 'File service is alive'
