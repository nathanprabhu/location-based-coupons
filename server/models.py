from app import db

class Coupon(db.Model):
  __tablename__ = 'coupons'

  id = db.Column(db.SmallInteger, primary_key=True)
  store_name = db.Column(db.String())
  latitude = db.Column(db.Float())
  longitude = db.Column(db.Float())
  coupon_desc = db.Column(db.Text())

  def __init__(self, store_name, latitude, longitude, coupon_desc):
    self.store_name = store_name
    self.latitude = latitude
    self.longitude = longitude
    self.coupon_desc = coupon_desc

  def __repr__(self):
    return '<id {}>'.format(self.id)
  
  def serialize(self):
    return {
      'id': self.id,
      'store_name': self.store_name, 
      'latitude': self.latitude,
      'longitude': self.longitude,
      'coupon_desc':self.coupon_desc
    }