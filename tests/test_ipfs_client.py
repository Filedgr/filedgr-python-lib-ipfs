import pytest

# Skipped at module level: these are integration tests that require a local
# IPFS daemon at 127.0.0.1:5001 and reference absolute paths from a former
# author's workstation. They need rewriting against a containerized IPFS
# fixture before they can run in CI.
pytest.skip(
    "stale: integration tests require local IPFS daemon",
    allow_module_level=True,
)

from unittest import IsolatedAsyncioTestCase

from filedgr_lib_ipfs.ipfs_client import IpfsClient


class TestIpfsClient(IsolatedAsyncioTestCase):

    def setUp(self):
        self.client = IpfsClient(host="127.0.0.1", port=5001)

    async def test_add_file(self):
        res = await self.client.add_file("testfile.txt")
        print(f"The result of the add file call: {res}")
        self.assertIn('Hash', res)
        self.assertIn('Name', res)
        self.assertIn('Size', res)

    async def test_add_directory(self):
        res = await self.client.add_directory(path="/Users/ericfalk/ws_filedgr/filedgr-python-lib-ipfs/tests/testdir",
                                              remove_prefix="/Users/ericfalk/ws_filedgr/filedgr-python-lib-ipfs/tests/")
        result = [entry for entry in res if entry["Name"] == "testdir/testdircontent.txt"]
        print(f"The result of the add file call: {res}")
        self.assertIn('Hash', res)
        self.assertIn('Name', res)
        self.assertIn('Size', res)

    async def test_ls_directory(self):
        res = await self.client.ls()
        print(f"The result of the add file call: {res}")
        # self.assertIn('Hash', res)
        # self.assertIn('Name', res)
        # self.assertIn('Size', res)
