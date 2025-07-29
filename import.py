import pandas as pd
from sqlalchemy import create_engine,text

# Thông tin kết nối MySQL
host = "localhost"
port = 3306
database = "law_db"
username = "root"
password = "08042004"

# Tạo engine kết nối đến MySQL
engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4"
)

# Đọc file CSV
df = pd.read_csv("E:\\thucTapTruong\\import\\all_import1.csv", encoding="utf-8", dtype={
    'case_id': int,
    'point': str,
    'clause': str,
    'article': str,
    'type': str,
    'Note': str
})

# Bổ sung cột thiếu vì k có trong csv
df["law_id"] = None

# Xóa dữ liệu cũ trong bảng case_law
with engine.begin() as conn:
    conn.execute(text("DELETE FROM case_law"))
    conn.execute(text("ALTER TABLE case_law AUTO_INCREMENT = 1"))

# Import vào bảng case_law
df.to_sql("case_law", con=engine, if_exists="append", index=False)
