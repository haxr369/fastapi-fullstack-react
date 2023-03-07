from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.plant import SimpleSpecies, DetailSpecies
from schemas.plant_sch import SimpleSpeciesSCHCreate, DetailSpeciesSCHCreate

#누가 넣었는지 알 필요가 있을까?...
class CRUDSimpleSpecies(CRUDBase[SimpleSpecies, SimpleSpeciesSCHCreate, SimpleSpeciesSCHCreate]):
    def create_with_species(
        self, db: Session, *, obj_in: SimpleSpeciesSCHCreate
    ) -> SimpleSpecies:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # 식물의 간단 정보 조회
    def get_by_Plant_id(
        self, db: Session,*, species : str
    ) -> SimpleSpecies:
        species = db.query(SimpleSpecies).filter(SimpleSpecies.species_name == species).first()
        return species

    # 쿼리로 식물 검색하는 함수 넣을 예정


crud_SimpleSpecies= CRUDSimpleSpecies(SimpleSpecies)

class CRUDDetailSpecies(CRUDBase[DetailSpecies, DetailSpeciesSCHCreate, DetailSpeciesSCHCreate]):
    def create(
        self, db: Session, *, obj_in: DetailSpeciesSCHCreate
    ) -> DetailSpecies:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

crud_DetailSpecies= CRUDDetailSpecies(DetailSpecies)