"""Views __init__ file."""
from learning_journal.views.default import(
    list_view,
    detail_view,
    create_view,
    update_view
)


def includeme(config):
    """List of views to include for configurator."""
    config.add_view(list_view, route_name='list')
    config.add_view(detail_view, route_name='detail')
    config.add_view(create_view, route_name='create')
    config.add_view(update_view, route_name='update')
