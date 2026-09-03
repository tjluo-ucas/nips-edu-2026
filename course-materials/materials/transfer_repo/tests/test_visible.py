from src.access_policy import AccessContext, can_view_document


def test_active_project_member_can_view_document():
    context = AccessContext(
        active_project_ids=frozenset({"project-alpha"}),
        revoked_project_ids=frozenset(),
    )
    assert can_view_document("project-alpha", context) is True


def test_unrelated_user_cannot_view_document():
    context = AccessContext(
        active_project_ids=frozenset({"project-beta"}),
        revoked_project_ids=frozenset(),
    )
    assert can_view_document("project-alpha", context) is False


def test_matching_share_link_can_grant_access():
    context = AccessContext(
        active_project_ids=frozenset(),
        revoked_project_ids=frozenset(),
        share_link_project_id="project-alpha",
    )
    assert can_view_document("project-alpha", context) is True
