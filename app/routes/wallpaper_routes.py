from flask import Blueprint, request, jsonify
from app.services.cloudinary_service import (
  get_images_by_tag,
  get_all_images,
  get_image_metadata,
  add_image_tag
)
from app.utils.tag_utils import normalize_tag

bp = Blueprint("wallpaper", __name__)

@bp.route('/wallpapers', methods=['GET'])
def get_wallpapers():
  tag = request.args.get("tag")
  try:
    result = get_images_by_tag(tag) if tag else get_all_images()
    images = []

    for img in result["resources"]:
      metadata = get_image_metadata(img["public_id"])
      images.append({
        "url": metadata["secure_url"],
        "public_id": metadata["public_id"],
        "tags": metadata.get("tags", [])
      })
    return jsonify({"wallpapers": images})
  
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@bp.route('/add-tag', methods=['POST'])
def add_tag_route():
  data = request.json
  public_id = data.get('public_id')
  tag = data.get('tag')

  if not public_id or not tag:
    return jsonify({"error": "Missing public_id or tag"}), 400

  try:
    result = add_image_tag(tag, public_id)
    return jsonify({"message": f"Tag '{tag}' added.", "result": result})
  except Exception as e:
    return jsonify({"error": str(e)}), 500
  
@bp.route('/<tag>', methods=['GET'])
def wallpapers_by_tag(tag):
  try: 
    normalized_tag = normalize_tag(tag)
    result = get_images_by_tag(normalized_tag)

    images = []

    for img in result["resources"]:
      metadata = get_image_metadata(img["public_id"])
      images.append({
        "url": metadata["secure_url"],
        "tags": metadata.get("tags", [])
      })
    return jsonify({"wallpapers": images})

  except Exception as e:
    return jsonify({"error": str(e)}), 500
  
@bp.route('/w/<path:public_id>', methods=['GET'])
def get_wallpaper_by_id(public_id):
    try:
        result = get_image_metadata(public_id)
        print(result)
        return jsonify({
            "url": result["secure_url"],
            "tags": result.get("tags", []),
            "format": result.get("format"),
            "width": result.get("width"),
            "height": result.get("height"),
            "created_at": result.get("created_at")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 404
