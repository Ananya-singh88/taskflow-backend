from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('taskflow.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/analytics/tasks-summary', methods=['GET'])
def task_summary():
    conn = get_db_connection()
    
    total = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    completed = conn.execute("SELECT COUNT(*) FROM tasks WHERE completed=1").fetchone()[0]

    conn.close()

    return jsonify({
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": total - completed
    })

if __name__ == "__main__":
    app.run(port=5001, debug=True)