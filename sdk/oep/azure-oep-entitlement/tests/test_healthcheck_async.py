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

class TestHealthCheckOperaionAsync(AzureTestCase):

    @OepEntitlementPreparer()
    async def test_health_get(self):
        data_partition_id="dpId"
        base_url="https://fake-instance.oep.ppe.azure-int.net"
        credential = self.get_credential(OepEntitlementClient, is_async=True)
        client = self.create_client_from_credential(OepEntitlementClient, credential=credential, base_url=base_url)
        liveness_response = await  client.health.get_liveness_check(data_partition_id=data_partition_id)
        assert liveness_response is None
        readiness_response = await client.health.get_readiness_check(data_partition_id=data_partition_id)
        assert  readiness_response is None
