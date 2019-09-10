import pandas
from Loaner import Loaner

userArray = [];
loan_data_dictionary = {};

home_ownership_data = pandas.read_csv('home_ownership_data.csv');
loan_data = pandas.read_csv('loan_data.csv');

# for loop to get ids and types
for x in range(home_ownership_data.__len__()):
    userArray.append(Loaner(home_ownership_data['member_id'][x], 0,home_ownership_data['home_ownership'][x]));

# making the dictionary for the loan data
for x in range(loan_data.__len__()):
    loan_data_dictionary[loan_data['member_id'][x]] = loan_data['loan_amnt'][x];

# associating loan amount with the right user
for x in range(userArray.__len__()):
    userArray[x].set_loanAmmount(loan_data_dictionary[userArray[x].get_id()]);

print(userArray[0].get_id());
print(userArray[0].get_loanAmmount());
print(userArray[0].get_type());



