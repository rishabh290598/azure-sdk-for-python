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

class TestMetadataOperaion(AzureTestCase):

    # Start with any helper functions you might need, for example a client creation method:
    def create_oep_client(self, base_url):
        credential = self.get_credential(OepFileClient, is_async=False)
        client = self.create_client_from_credential(OepFileClient, credential=credential, base_url=base_url)
        return client

    def get_file_metadata_by_id(self, client, data_partition_id,id):
        return client.metadata.get_file_metadata_by_id(data_partition_id=data_partition_id,frame_of_reference='afabh',id=id)

    def post_files_metadata(self, client, data_partition_id):
        return client.metadata.post_files_metadata(data_partition_id=data_partition_id,frame_of_reference='afabh',body={
            "kind": "osdu:wks:dataset--File.Generic:1.0.0",
            "acl": {
                "viewers": [
                    "data.default.viewers@dpId.contoso.com"
                ],
                "owners": [
                    "data.default.viewers@dpId.contoso.com"
                ]
            },
            "legal": {
                "legaltags": [
                    "dpId-R3FullManifest-Legal-Tag-Test8646767"
                ],
                "otherRelevantDataCountries": [
                    "US"
                ],
                "status": "compliant"
            },
            "data": {
                "Endian": "BIG",
                "DatasetProperties": {
                    "FileSourceInfo": {
                        "FileSource": "/osdu-user/1656677845295-2022-07-01-12-17-25-295/dd37956a22544814822bb375a7e8c3d7"
                    }
                }
            }
        })

    # Write your tests
    @OepFilePreparer()
    def test_metadata(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        client = self.create_oep_client(base_url=base_url)
        postMetadataResponse = self.post_files_metadata(client=client, data_partition_id=data_partition_id)
        assert postMetadataResponse is not None
        id = postMetadataResponse.id
        assert id is not None
        getMetaDataResponse = self.get_file_metadata_by_id(client=client, data_partition_id=data_partition_id,id=id)
        assert getMetaDataResponse.id == id

