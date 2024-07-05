import importlib
import pkgutil
import types
from typing import Text
from typing import Union

import structlog

structlogger = structlog.get_logger()

def register_package(package: Union[Text, types.ModuleType]) -> None:
    """
    Dynamically loads embeddings as plugins
    :param directory:
    :return:
    """
    _import_submodules(package)

def _import_submodules(
        package: Union[Text, types.ModuleType], recursive: bool = True
) -> None:
    """Import a module, or a package and its submodules recursively.

    Args:
        package: Package or module name, or an already loaded Python module.
        recursive: If `True`, and `package` is a package, import all of its
            sub-packages as well.
    """
    if isinstance(package, str):
        package = _import_module(package)

    if not getattr(package, "__path__", None):
        return

    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + "." + name
        _import_module(full_name)

        if recursive and is_pkg:
            _import_submodules(full_name)

def _import_module(name: Text) -> types.ModuleType:
    """Import a Python module. If possible, register the file where it came from.

    Args:
        name: The module's name using Python's module path syntax.

    Returns:
        The loaded module.
    """
    module = importlib.import_module(name)
    structlogger.debug(f"import {name}")
    return module