class Employee:
  def __init__(self, id, emp_id,name,isActive,dateOfJoining,email):
        self.id = id
        self.emp_id = emp_id  # Consider if emp_id should be unique and how it aligns with SQLite primary key
        self.name = name
        self.isActive = isActive
        self.dateOfJoining = dateOfJoining
        self.email = email

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'emp_id':self.emp_id,
      'name': self.name,
      'isActive': self.isActive,
      'dateOfJoining':self.dateOfJoining,
      "email": self.email
    }