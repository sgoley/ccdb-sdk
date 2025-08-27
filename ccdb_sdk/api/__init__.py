# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from openapi_client.api.complaints_api import ComplaintsApi
    from openapi_client.api.trends_api import TrendsApi
    from openapi_client.api.typeahead_api import TypeaheadApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from openapi_client.api.complaints_api import ComplaintsApi
from openapi_client.api.trends_api import TrendsApi
from openapi_client.api.typeahead_api import TypeaheadApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
