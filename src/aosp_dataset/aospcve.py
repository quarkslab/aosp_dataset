from pydantic import BaseModel, Field
from datetime import date

from typing import List


class CommitInformation(BaseModel):
    """Description of a commit"""

    commitId: str = Field(..., title="Commit ID", description="Hash of the commit")

    patchUrl: str = Field(
        ..., title="Patch URL", description="Direct link to the patch"
    )


class AospCve(BaseModel):
    """Description of a CVE"""

    cveId: str = Field(..., title="CVE ID", description="CVE Identifier")

    dateReported: date = Field(
        None, title="Reported date", description="CVE reported date"
    )

    vulnerabilityType: str = Field(
        None, title="Type", description="Class of vulnerability"
    )

    language: str = Field(
        None,
        title="Language",
        description="Language of source files affected by the CVE",
    )

    fixes: List[CommitInformation] = Field(
        ..., title="Fixes informations", description="Fixing commits", min_items=1
    )

    severity: str = Field(None, title="Severity", description="CVE Impact")

    component: str = Field(
        ..., title="Component", description="Affected component in AOSP"
    )
