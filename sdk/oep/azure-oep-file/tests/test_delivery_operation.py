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

class TestDeliveryOperaion(AzureTestCase):

    # Start with any helper functions you might need, for example a client creation method:
    def create_oep_client(self, base_url):
        credential = self.get_credential(OepFileClient, is_async=False)
        client = self.create_client_from_credential(OepFileClient, credential=credential, base_url=base_url)
        return client


    # Write your tests
    @OepFilePreparer()
    def test_download_get(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        client = self.create_oep_client(base_url=base_url)
        id = 'dpId:dataset--File.Generic:d9641337-e279-4c59-a894-152f211ea233'
        dowloandURLResponse = client.delivery.get_download_url(data_partition_id=data_partition_id,frame_of_reference='afabh',id=id)
        assert dowloandURLResponse is not None
        assert dowloandURLResponse.signed_url is not None

