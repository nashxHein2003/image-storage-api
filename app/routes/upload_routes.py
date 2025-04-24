from flask import Blueprint, request, jsonify
from app.services.cloudinary_service import upload_image

bp = Blueprint("upload", __name__)

@bp.route('/upload', methods=['POST'])
def upload_file():
  if 'file' not in request.files:
    return jsonify({"error": "No File Part."}), 400
  
  file = request.files['file']
  tags = request.form.get('tags', '')

  if file.filename == '':
        return jsonify({"error": "No selected file."}), 400

  try:
      result = upload_image(file, tags)
      return jsonify({
          "url": result['secure_url'],
          "tags": result.get('tags', []),
          "public_id": result['public_id']
      })
  except Exception as e:
      return jsonify({"error": str(e)}), 500