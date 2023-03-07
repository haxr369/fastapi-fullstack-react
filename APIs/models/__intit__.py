"""

Fast API가 사용할 데이터 모델 선언

테이블의 한 행에 포함되는 데이터 클래스를 정의

DB와 서버가 연결된것.
DB의 테이블 데이터를 이걸로 가져온다.
"""

from db.base_class import Base
from db.session import engine

Base.metadata.create_all(bind=engine)