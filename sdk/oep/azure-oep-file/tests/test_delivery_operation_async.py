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

class TestDeliveryOperaionAsync(AzureTestCase):

    @OepFilePreparer()
    async def test_download_get(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        id = 'dpId:dataset--File.Generic:d9641337-e279-4c59-a894-152f211ea233'
        credential = self.get_credential(OepFileClient, is_async=True)
        client = self.create_client_from_credential(OepFileClient, credential=credential, base_url=base_url)
        dowloandURLResponse = await  client.delivery.get_download_url(data_partition_id=data_partition_id,frame_of_reference='afabh',id=id)
        assert dowloandURLResponse is not None
        assert dowloandURLResponse.signed_url is not None
