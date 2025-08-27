# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from ccdb_sdk.api.complaints_api import ComplaintsApi
    from ccdb_sdk.api.trends_api import TrendsApi
    from ccdb_sdk.api.typeahead_api import TypeaheadApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from ccdb_sdk.api.complaints_api import ComplaintsApi
from ccdb_sdk.api.trends_api import TrendsApi
from ccdb_sdk.api.typeahead_api import TypeaheadApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
