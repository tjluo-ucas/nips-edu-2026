"""Characterize the starter's missing revocation rule without inventing policy."""

from src.access_policy import AccessContext, can_view_document


def test_starter_ignores_revocation_when_membership_is_also_active():
    context = AccessContext(
        active_project_ids=frozenset({"project-alpha"}),
        revoked_project_ids=frozenset({"project-alpha"}),
    )

    # This observation is an oracle gap, not yet a defect: an accountable owner
    # must validate whether revocation takes precedence before a repair is made.
    assert can_view_document("project-alpha", context) is True
