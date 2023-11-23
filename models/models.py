from sqlalchemy import Integer, String, Date, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, relationship
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class PatientInformation(BaseModel, Base):
    __tablename__ = "patient_information"
    
    patient_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    last_name: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    middle_name: Mapped[Optional[str]] = mapped_column(String(100))
    date_of_birth: Mapped[Date] = mapped_column(Date)
    patient_diagnosis: Mapped[str] = mapped_column(String(100))
    estimated_delivery_date: Mapped[Date] = mapped_column(Date)
    hepb_status_awareness: Mapped[str] = mapped_column(String(10))
    address: Mapped[Optional[str]] = mapped_column(String(255))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    sexual_partners: Mapped[Optional[str]] = mapped_column(String(100))
    state: Mapped[Optional[str]] = mapped_column(String(100))
    zip: Mapped[Optional[str]] = mapped_column(String(20))
    phone_number: Mapped[Optional[str]] = mapped_column(String(30))
    insurance_type: Mapped[Optional[str]] = mapped_column(String(100))
    race: Mapped[Optional[str]] = mapped_column(String(50))
    hispanic: Mapped[Optional[bool]] = mapped_column(Boolean)
    country_of_birth: Mapped[Optional[str]] = mapped_column(String(150))
    primary_language: Mapped[Optional[str]] = mapped_column(String(100))
    interpreter_needed: Mapped[Optional[bool]] = mapped_column(Boolean)

    # Relationships
    reports = relationship("ReportInformation", back_populates="patient")
    maternal_info = relationship("MaternalInformation", back_populates="patient")
    syphilis_test_info = relationship("SyphilisTestInformation", back_populates="patient")
    treatment_info = relationship("TreatmentInformation", back_populates="patient")
    serologic_response = relationship("SerologicResponse", back_populates="patient")


class ReportInformation(BaseModel, Base):
    __tablename__ = "report_information"
    
    report_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    report_date: Mapped[Date] = mapped_column(Date)
    reporting_state_fips: Mapped[str] = mapped_column(String(10))
    reporting_state_name: Mapped[str] = mapped_column(String(100))
    reporting_county_fips: Mapped[str] = mapped_column(String(10))
    reporting_county_name: Mapped[str] = mapped_column(String(100))
    
    # Foreign Key
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey("patient_information.patient_id", onupdate="CASCADE", ondelete="CASCADE"))
    
    # Relationships
    patient = relationship("PatientInformation", back_populates="reports")



class MaternalInformation(BaseModel, Base):
    __tablename__ = "maternal_information"
    
    maternal_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mother_state_fips: Mapped[str] = mapped_column(String(10))
    mother_state_name: Mapped[str] = mapped_column(String(100))
    mother_country_residence: Mapped[Optional[str]] = mapped_column(String(150))
    mother_county_fips: Mapped[str] = mapped_column(String(10))
    mother_county_name: Mapped[str] = mapped_column(String(100))
    mother_zip_code: Mapped[Optional[str]] = mapped_column(String(20))
    mother_date_of_birth: Mapped[Date] = mapped_column(Date)
    gravida: Mapped[int] = mapped_column(Integer)
    para: Mapped[int] = mapped_column(Integer)
    lmp: Mapped[Date] = mapped_column(Date)
    first_prenatal_date: Mapped[Date] = mapped_column(Date)
    no_prenatal_care: Mapped[Optional[bool]] = mapped_column(Boolean)
    trimester_first_prenatal: Mapped[Optional[int]] = mapped_column(Integer)
    hispanic_latino: Mapped[Optional[bool]] = mapped_column(Boolean)
    non_hispanic_latino: Mapped[Optional[bool]] = mapped_column(Boolean)
    
    # Foreign Key
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey("patient_information.patient_id", onupdate="CASCADE", ondelete="CASCADE"))
    
    # Relationships
    patient = relationship("PatientInformation", back_populates="maternal_info")


class SyphilisTestInformation(BaseModel, Base):
    __tablename__ = "syphilis_test_information"
    
    syphilis_test_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_prenatal_test: Mapped[Optional[bool]] = mapped_column(Boolean)
    gestation_test: Mapped[Optional[bool]] = mapped_column(Boolean)
    delivery_test: Mapped[Optional[bool]] = mapped_column(Boolean)
    marital_status_single: Mapped[Optional[bool]] = mapped_column(Boolean)
    marital_status_married: Mapped[Optional[bool]] = mapped_column(Boolean)
    marital_status_separated_divorced: Mapped[Optional[bool]] = mapped_column(Boolean)
    marital_status_widow: Mapped[Optional[bool]] = mapped_column(Boolean)
    marital_status_other: Mapped[Optional[bool]] = mapped_column(Boolean)
    marital_status_unknown: Mapped[Optional[bool]] = mapped_column(Boolean)
    
    # Foreign Key
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey("patient_information.patient_id", onupdate="CASCADE", ondelete="CASCADE"))
    
    # Relationships
    patient = relationship("PatientInformation", back_populates="syphilis_test_info")



class TreatmentInformation(BaseModel, Base):
    __tablename__ = "treatment_information"
    
    treatment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_penicillin_dose_date: Mapped[Date] = mapped_column(Date)
    penicillin_dose_before_pregnancy: Mapped[Optional[bool]] = mapped_column(Boolean)
    penicillin_dose_1st_trimester: Mapped[Optional[bool]] = mapped_column(Boolean)
    penicillin_dose_2nd_trimester: Mapped[Optional[bool]] = mapped_column(Boolean)
    penicillin_dose_3rd_trimester: Mapped[Optional[bool]] = mapped_column(Boolean)
    penicillin_dose_no_treatment: Mapped[Optional[bool]] = mapped_column(Boolean)
    penicillin_dose_unknown: Mapped[Optional[bool]] = mapped_column(Boolean)
    treatment_2_4m_units: Mapped[Optional[bool]] = mapped_column(Boolean)
    treatment_4_8m_units: Mapped[Optional[bool]] = mapped_column(Boolean)
    treatment_7_2m_units: Mapped[Optional[bool]] = mapped_column(Boolean)
    treatment_other: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_unknown: Mapped[Optional[bool]] = mapped_column(Boolean)
    
    # Foreign Key
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey("patient_information.patient_id", onupdate="CASCADE", ondelete="CASCADE"))
    
    # Relationships
    patient = relationship("PatientInformation", back_populates="treatment_info")


class SerologicResponse(BaseModel, Base):
    __tablename__ = "serologic_response"
    
    serologic_response_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    serologic_response_yes: Mapped[Optional[bool]] = mapped_column(Boolean)
    serologic_response_no: Mapped[Optional[bool]] = mapped_column(Boolean)
    serologic_response_unknown: Mapped[Optional[bool]] = mapped_column(Boolean)
    serologic_response_not_enough_time: Mapped[Optional[bool]] = mapped_column(Boolean)
    
    # Foreign Key
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey("patient_information.patient_id", onupdate="CASCADE", ondelete="CASCADE"))
    
    # Relationships
    patient = relationship("PatientInformation", back_populates="serologic_response")
        
        
        



        
        


