from dotenv import load_dotenv
import cloudinary
import os

load_dotenv()

class Config:
  @staticmethod

  def init_cloudinary():
    cloudinary.config(
      cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
      api_key=os.getenv("CLOUDINARY_API_KEY"),
      api_secret=os.getenv("CLOUDINARY_API_SECRET")
    )
Config.init_cloudinary()