from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

# 引入数据库连接引擎
from app.database.connection import engine

app = FastAPI()


@app.get("/api/db-test")
def test_database():

    try:
        # 获取数据库连接
        with engine.connect() as connection:

            # 执行sql查询
            result = connection.execute(
                text(
                    """
                    select
                        VERSION() as db_version,
                        DATABASE() as db_name,
                        CURRENT_USER() as db_user
                    """
                )
            )

            # 获取查询结果，返回的是一个行对象，也就是row，是用mappings()方法将其转换为字典形式
            data = result.mappings().fetchone()
        
        # 返回查询结果
        return {
            "success": True,
            "message": "Database connection successful!!!",
            "data": dict(data) if data else None
        }

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )