from sqlalchemy import Integer, String, ForeignKey, DataTime, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class BaseModel:
    @declared_attr
    def _tablename_(cls):
        return cls._name_.lower()
    
    class Base(DeclarativeBase)
        pass

    class ChlamydiaGonorrhea(Base, BaseModel):
        _tablename_ = 'chlamydia_gonorrhea'
        id:Mapped[int] = mapped_column(Integer, primary_key=True)
        created_at:Mapped[datetime] = mapped_column(DateTime,insert_default=func.now())
        updated_at:Mapped[datetime] = mapped_column(DateTime,insert_default=func.now())
        created_by:Mapped[str] = mapped_column(String(100), insert_default='system')
        updated_by:Mapped[str] = mapped_column(String(100), insert_default='system')
        unique_id:Mapped[str] = mapped_column(String(100), unique=True)
        Date:Mapped[datetime] = mapped_column(DateTime)
        personcompletingtheform:Mapped[str] = mapped_column(String(100))
        HealthProvider:Mapped[str] = mapped_column(String(100))
        Contactphonenumber:Mapped[str] = mapped_column(String(100))
        Name:Mapped[str] = mapped_column(String(100))
        Dateofbirth:Mapped[datetime] = mapped_column(DateTime)
        Gender:Mapped[str] = mapped_column(String(100))
        houseaddress:Mapped[optional[str]] = mapped_column(String(100))
        phonenumber:Mapped[optional[str]] = mapped_column(String(100))
        alternative:Mapped[str] = mapped_column(String(100))
        pregnanttestresult:Mapped[str] = mapped_column(String(100))
        ethnicity:Mapped[str] = mapped_column(String(100))
        race:Mapped[str] = mapped_column(String(100))
        genderofsexpartner:Mapped[str] = mapped_column(String(100))
        chlamydiapositiveresultdate:Mapped[datetime] = mapped_column(DateTime)
        gonorrheapositiveresultdate:Mapped[datetime] = mapped_column(DateTime)
        positivehivtesting:Mapped[datetime] = mapped_column(DateTime)
        gonorrheatreatmentplan:Mapped[str] = mapped_column(String(100))
        chlamydiatreatmentplan:Mapped[str] = mapped_column(String(100))
        partnermanagementplan:Mapped[str] = mapped_column(String(100))


        class CongenitalSyphilis (Base, BaseModel):
        _tablename_ = 'congenital_syphilis'
        id:Mapped[int] = mapped_column(Integer, primary_key=True)
        created_at:Mapped[datetime] = mapped_column(DateTime,insert_default=func.now())
        updated_at:Mapped[datetime] = mapped_column(DateTime,insert_default=func.now())
        created_by:Mapped[str] = mapped_column(String(64), insert_default='system')
        updated_by:Mapped[str] = mapped_column(String(64), insert_default='system')
        unique_id:Mapped[str] = mapped_column(String(64), ForeignKey("congenital_syphilis.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
        Reportdatetohealthdept:Mapped[datetime] = mapped_column(Datetime)
        ReportingstateFIPScode:Mapped[str] = mapped_column(String(64))
        ReportingcountyFIPScode:Mapped[str] = mapped_column(String(64))
        MothersstateFIPScode:Mapped[str] = mapped_column(String(64))
        MothersCountryofresidence:Mapped[str] = mapped_column(String(64))
        MotherssresidencecountyFIPScode:Mapped[str] = mapped_column(String(64))
        MothersresidenceZIPcode:Mapped[str] = mapped_column(String(64))


        class HepatitisBinfected (Base, BaseModel):
        __tablename__ = 'HepatitisB_infected'
        id:Mapped[int] = mapped_column(Integer, primary_key=True)
        created_at:Mapped[datetime] = mapped_column(DateTime,insert_default=func.now())
        updated_at:Mapped[datetime] = mapped_column(DateTime,insert_default=func.now())
        created_by:Mapped[str] = mapped_column(String(64), insert_default='system')
        updated_by:Mapped[str] = mapped_column(String(64), insert_default='system')
        unique_id:Mapped[str] = mapped_column(String(64), ForeignKey("HepatitisBinfected.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
        lastname:Mapped[optional[str]] = mapped_column(String(64))
        firstname:Mapped[str] = mapped_column(String(64))
        middlename:Mapped[optional[str]] = mapped_column(String(64))
        dateofbirth:Mapped[datetime] = mapped_column(Datetime)
        MothersCountryofresidence:Mapped[str] = mapped_column(String(64))
        estimateddateofdelivery:Mapped[datetime] = mapped_column(DateTime)
        PatientawareofHepb+status:Mapped[str] = mapped_column(String(64))
        
        


