from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from .models import Task, User
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return jsonify({"msg": "Task Manager API Running 🚀"})


# ✅ ADD TASK
@main.route('/add', methods=['POST'])
@jwt_required()
def add_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"msg": "Title is required"}), 400

    user_id = int(get_jwt_identity())

    task = Task(
        title=data['title'],
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"msg": "Task Added"}), 201


# ✅ ADD MULTIPLE TASKS
@main.route('/add-multiple', methods=['POST'])
@jwt_required()
def add_multiple_tasks():
    data = request.get_json()

    if not isinstance(data, list):
        return jsonify({"msg": "Send list of tasks"}), 400

    user_id = int(get_jwt_identity())

    for item in data:
        if "title" in item:
            task = Task(
                title=item['title'],
                user_id=user_id
            )
            db.session.add(task)

    db.session.commit()

    return jsonify({"msg": "Multiple tasks added"}), 201


# ✅ GET TASKS (ROLE + PAGINATION + FILTERING)
@main.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = int(get_jwt_identity())
    claims = get_jwt()
    role = claims.get("role", "user")  # 🔥 JWT से role लो

    # Query params
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 5, type=int)
    filter_user = request.args.get('user_id', type=int)

    query = Task.query

    # 🔐 Role-based access
    if role != "admin":
        query = query.filter_by(user_id=user_id)

    # 🔍 Filtering (admin ही दूसरे users filter कर सके)
    if filter_user:
        if role == "admin":
            query = query.filter_by(user_id=filter_user)
        else:
            return jsonify({"msg": "Only admin can filter by user_id"}), 403

    # 📄 Pagination
    tasks = query.paginate(page=page, per_page=limit, error_out=False)

    result = []
    for task in tasks.items:
        result.append({
            "id": task.id,
            "title": task.title,
            "user_id": task.user_id
        })

    return jsonify({
        "page": page,
        "total": tasks.total,
        "tasks": result
    })


# ✅ DELETE TASK
@main.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    user_id = int(get_jwt_identity())
    claims = get_jwt()
    role = claims.get("role", "user")

    task = Task.query.get(id)

    if not task:
        return jsonify({"msg": "Task not found"}), 404

    if role != "admin" and task.user_id != user_id:
        return jsonify({"msg": "Not authorized"}), 403

    db.session.delete(task)
    db.session.commit()

    return jsonify({"msg": "Task deleted"})


# ✅ UPDATE TASK
@main.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    user_id = int(get_jwt_identity())
    claims = get_jwt()
    role = claims.get("role", "user")

    task = Task.query.get(id)

    if not task:
        return jsonify({"msg": "Task not found"}), 404

    if role != "admin" and task.user_id != user_id:
        return jsonify({"msg": "Not authorized"}), 403

    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"msg": "Title is required"}), 400

    task.title = data['title']

    db.session.commit()

    return jsonify({"msg": "Task updated"})