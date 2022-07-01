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

class TestLocationOperaionAsync(AzureTestCase):

    @OepFilePreparer()
    async def test_location_get(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        credential = self.get_credential(OepFileClient, is_async=True)
        client = self.create_client_from_credential(OepFileClient, credential=credential, base_url=base_url)
        response = await client.location.get_location_file(data_partition_id=data_partition_id,frame_of_reference='fafa')
        assert response is not None
        assert response.location is not None
        # assert response.additional_properties['Location'] is not None
        assert response.location['SignedURL'] is not None
        assert response.location['FileSource'] is not None
        signedURL = response.location['SignedURL']
