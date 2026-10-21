import sqlite3
from pathlib import Path

from fastapi import FastAPI

app = FastAPI(title="FDE Lab")

DB_PATH = Path(__file__).resolve().parent / "lab.db"


def init_db() -> None:
    print(f"DB_PATH={DB_PATH}")
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                grade TEXT NOT NULL,
                height_cm REAL
            )
            """
        )
        count = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
        print(f"students count before init: {count}")

        if count == 0:
            conn.executemany(
                "INSERT INTO students (name, grade, height_cm) VALUES (?, ?, ?)",
                [
                    ("学生A", "初一1班", 162.5),
                    ("学生B", "初一2班", 158.0),
                    ("学生C", "初一1班", 170.2),
                ],
            )
            conn.commit()
            print("学生数据已插入")
        else:
            print("学生表中已有数据，无需插入")

        after_count = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
        print(f"students count after init: {after_count}")


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok","version": "1"}


@app.get("/students")
def list_students() -> list[dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, name, grade, height_cm FROM students ORDER BY id"
        ).fetchall()
    print(f"查询到 {len(rows)} 条学生记录")
    return [dict(row) for row in rows]