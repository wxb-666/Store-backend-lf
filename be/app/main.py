from fastapi import FastAPI, HTTPException
from app.database.connection import get_db_connection

app = FastAPI()


@app.get("/api/db-test")
def test_database():
    connection = None

    try:
        # 获取数据库连接
        connection = get_db_connection()

        # 创建游标
        with connection.cursor() as cursor:

            # 执行 SQL 查询
            cursor.execute("""
                SELECT
                    VERSION() AS mysql_version,
                    DATABASE() AS database_name,
                    CURRENT_USER() AS mysql_user
            """)

            # 获取查询结果
            result = cursor.fetchone()

        return {
            "success": True,
            "message": "MySQL connection successful!!!",
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )

    finally:
        # 关闭数据库连接
        if connection:
            connection.close()