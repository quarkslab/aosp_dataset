"""AOSP CVEs

Helper functions for AOSP CVEs project
"""

__version__ = "0.1.0"

from aosp_dataset.aospcve import AospCve
from aosp_dataset.compiled import PrecompiledDataset


def generate_schema():
    """Generate the JSON schema using pydantic"""
    
    with open("schemas/AospCve.schema.json", "w") as file:
        file.write(AospCve.schema_json(indent=2))

    with open("schemas/precompiled.schema.json", "w") as file:
            file.write(PrecompiledDataset.schema_json(indent=2))


__all__ = [
    __version__,
    # From aospcve.py
    AospCve,
    # From compiled.py
    PrecompiledDataset,
]
