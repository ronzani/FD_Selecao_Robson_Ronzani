from sqlalchemy import text
from db_config import engine
from fastapi import APIRouter, HTTPException
import pandas as pd

router = APIRouter()

# Endpoint GET para retornar todos os produtos
@router.get("/produtos")
def get_produtos():
    try:
        # Consultar a tabela tb_produto
        query = text("SELECT * FROM tb_produto;")

        with engine.connect() as connection:
            result = connection.execute(query)
            produtos = result.mappings().all()

        if not produtos:
            raise HTTPException(status_code=404)

        return produtos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))