"""Smoke test for ISO compliance gate."""
import importlib


def test_package_importable():
    module = importlib.import_module("filedgr_lib_ipfs")
    assert module is not None


def test_package_has_dunder_path():
    module = importlib.import_module("filedgr_lib_ipfs")
    assert hasattr(module, "__path__"), "filedgr_lib_ipfs is not a package"
