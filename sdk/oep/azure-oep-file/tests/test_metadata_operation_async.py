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

class TestMetadataOperaionAsync(AzureTestCase):


    @OepFilePreparer()
    async def test_metadata(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        credential = self.get_credential(OepFileClient, is_async=True)
        client = self.create_client_from_credential(OepFileClient, credential=credential, base_url=base_url)
        postMetadataResponse = await client.metadata.post_files_metadata(data_partition_id=data_partition_id,frame_of_reference='afabh',body={
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
                        "FileSource": "/osdu-user/1656619195836-2022-06-30-19-59-55-836/9202cae7488f4d55b7c0a24a259d3096"
                    }
                }
            }
        })
        assert postMetadataResponse is not None
        id = postMetadataResponse.id
        assert id is not None
        getMetaDataResponse = await client.metadata.get_file_metadata_by_id(data_partition_id=data_partition_id,frame_of_reference='afabh',id=id)
        assert getMetaDataResponse.id == id
