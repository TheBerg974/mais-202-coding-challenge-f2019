class Home_Ownership:
  # class home ownership with 3 data fields
  # id; the member id
  # loan_amount; how much money did the memner loan
  # type; the type of home ownership
  def __init__(self, id, loan_amount, type):
    self.id = id;
    self.loanAmmount = loan_amount;
    self.type = type;

  # getters
  def get_id(self):
    return self.id;

  def get_loan_amount(self):
    return self.loanAmmount;

  def get_type(self):
    return self.type;

   # setters
  def set_id(self, x):
    self.id = x;

  def set_loan_amount(self, x):
    self.loanAmmount = x;

  def set_loanType(self, x):
    self.type = x;