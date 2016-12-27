from data_africa.database import db
from data_africa.core.models import BaseModel
from data_africa.attrs.consts import ALL
from data_africa.attrs.models import Geo, PovertyGeo

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class BaseSpatial(db.Model, BaseModel):
    __abstract__ = True
    __table_args__ = {"schema": "spatial", "extend_existing": True}
    source_title = 'Spatial Data'
    source_link = ''
    source_org = 'IFPRI'

class PovertyXWalk(BaseSpatial):
    __tablename__ = "pov_geo_crosswalk"
    median_moe = 0

    poverty_geo = db.Column(db.String, db.ForeignKey(PovertyGeo.id), primary_key=True)
    geo = db.Column(db.String, db.ForeignKey(Geo.id), primary_key=True)
    st_area = db.Column(db.Float())
    pct_overlap = db.Column(db.Float())
