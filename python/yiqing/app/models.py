from app import db


class traditionalOffice(db.Model):
    __tablename__ = 'traditional_office'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    city = db.Column(db.String(255))
    area = db.Column(db.String(255))
    address = db.Column(db.String(255))
    completion_time = db.Column(db.String(255))
    floor_number = db.Column(db.Integer())
    floor_height = db.Column(db.Float())
    office_owner = db.Column(db.String(255))
    property_company = db.Column(db.String(255))
    peoelv_number = db.Column(db.Integer())
    freelv_number = db.Column(db.Integer())

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

