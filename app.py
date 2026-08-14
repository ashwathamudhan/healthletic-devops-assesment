from flask import Flask, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

DATABASE = os.getenv("DATABASE_PATH", "healthletic.db")


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_db_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS health_check (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            checked_at TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return jsonify(
        {
            "application": "Healthletic Lifestyle Backend",
            "status": "running",
            "version": os.getenv("APP_VERSION", "v1.0.0"),
        }
    )


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy",
            "application": "healthletic-backend",
            "version": os.getenv("APP_VERSION", "v1.0.0"),
        }
    )


@app.route("/health/db")
def database_health():
    try:
        connection = get_db_connection()

        connection.execute("SELECT 1")

        connection.execute(
            "INSERT INTO health_check (checked_at) VALUES (?)",
            (datetime.utcnow().isoformat(),),
        )

        connection.commit()
        connection.close()

        return jsonify(
            {
                "status": "healthy",
                "database": "connected",
            }
        ), 200

    except Exception as error:
        return jsonify(
            {
                "status": "unhealthy",
                "database": "disconnected",
                "error": str(error),
            }
        ), 500


@app.route("/api/status")
def api_status():
    return jsonify(
        {
            "api": "online",
            "service": "backend",
            "message": "Healthletic API is working",
        }
    )


if __name__ == "__main__":
    initialize_database()

    port = int(os.getenv("PORT", "5000"))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
    )