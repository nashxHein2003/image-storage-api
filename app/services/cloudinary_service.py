from cloudinary.uploader import upload, add_tag
from cloudinary.api import resource, resources, resources_by_tag

def upload_image(file, tags):
  tag_list = tags if tags else []
  return upload(file, tags = tag_list, folder = "wallpapers")

def get_images_by_tag(tag):
  return resources_by_tag(tag, max_results=100)

def get_all_images():
  return resources(type="upload", prefix="wallpapers/", max_results=100)

def get_image_metadata(public_id):
  return resource(public_id)

def add_image_tag(tag, public_id):
  return add_tag(tag, public_id)