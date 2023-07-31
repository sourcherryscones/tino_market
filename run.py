from app import app, create_app

if app is None:
    app = create_app()