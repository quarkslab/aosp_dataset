from pydantic import BaseModel, Field, AnyHttpUrl

from typing import List


class CveLink(BaseModel):
    """A link towards a CVE"""

    cveId: str = Field(..., title="CVE ID", description="CVE Identifier")

    commitId: str = Field(..., title="Commit Id", description="Hash of the commit")

    link: AnyHttpUrl = Field(
        ..., title="Download link", description="Direct link to download the CVE"
    )


class PrecompiledDataset(BaseModel):
    """Precompiled dataset"""

    compiledCves: List[CveLink] = Field(
        ...,
        title="Compiled CVEs",
        description="List of precompiled CVEs links",
        min_items=1,
        unique_items=True,
    )
