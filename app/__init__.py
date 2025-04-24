from flask import Flask
from .routes import upload_routes, wallpaper_routes
from app.config import Config

def create_app():
  app = Flask(__name__)
  app.config.from_object("app.config.Config")

  Config.init_cloudinary() 

  app.register_blueprint(upload_routes.bp)
  app.register_blueprint(wallpaper_routes.bp)

  return app
