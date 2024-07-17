class Employee:
  def __init__(self, id, name,isActive, dateOfJoining):
    self.id = id
    self.name = name
    self.isActive = isActive
    self.dateOfJoining = dateOfJoining

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'isActive': self.isActive,
      'dateOfJoining':self.dateOfJoining
    }