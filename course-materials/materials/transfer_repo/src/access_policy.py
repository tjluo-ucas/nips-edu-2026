from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AccessContext:
    active_project_ids: frozenset[str]
    revoked_project_ids: frozenset[str]
    share_link_project_id: Optional[str] = None


def can_view_document(document_project_id: str, context: AccessContext) -> bool:
    """Return whether the supplied access context permits document viewing."""
    if document_project_id in context.active_project_ids:
        return True
    return context.share_link_project_id == document_project_id
