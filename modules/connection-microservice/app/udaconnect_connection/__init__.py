def register_routes(api, app, root="api"):
    from app.udaconnect_connection.controllers import api as udaconnect_connection_api

    api.add_namespace(udaconnect_connection_api, path=f"/{root}")
