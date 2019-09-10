class Loaner:
  def __init__(self, id, loanAmmount, type):
    self.id = id;
    self.loanAmmount = loanAmmount;
    self.type = type;

  # getters
  def get_id(self):
    return self.id;

  def get_loanAmmount(self):
    return self.loanAmmount;

  def get_type(self):
    return self.type;

   # setters
  def set_id(self, x):
    self.id = x;

  def set_loanAmmount(self, x):
    self.loanAmmount = x;

  def set_loanType(self, x):
    self.type = x;