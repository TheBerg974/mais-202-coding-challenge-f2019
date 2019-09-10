import pandas
import matplotlib.pyplot as plt
from Home_Ownership import Home_Ownership

userArray = [];
loan_data_dictionary = {};

# parsing through both csv files
home_ownership_data = pandas.read_csv('home_ownership_data.csv');
loan_data = pandas.read_csv('loan_data.csv');

# for loop to get ids and types
for x in range(home_ownership_data.__len__()):
    userArray.append(Home_Ownership(home_ownership_data['member_id'][x], 0, home_ownership_data['home_ownership'][x]));

# making the dictionary for the loan data
for x in range(loan_data.__len__()):
    loan_data_dictionary[loan_data['member_id'][x]] = loan_data['loan_amnt'][x];

# associating loan amount with the right user
for x in range(userArray.__len__()):
    userArray[x].set_loan_amount(loan_data_dictionary[userArray[x].get_id()]);

total_loan_ammount_rent = 0;
total_loan_ammount_mortgage = 0;
total_loan_ammount_own = 0;

total_rent = 0;
total_mortgage = 0;
total_own = 0;

# calculating sum and number of home ownership in order to calculate the average
for x in range(userArray.__len__()):
    if userArray[x].get_type() == 'RENT':
        total_loan_ammount_rent += userArray[x].get_loan_amount();
        total_rent += 1;
    elif userArray[x].get_type() == 'MORTGAGE':
        total_loan_ammount_mortgage += userArray[x].get_loan_amount();
        total_mortgage += 1;
    else:
        total_loan_ammount_own += userArray[x].get_loan_amount();
        total_own += 1;

# calculating the averages
rent_average = total_loan_ammount_rent / total_rent;
mortgage_average = total_loan_ammount_mortgage / total_mortgage;
own_average = total_loan_ammount_own / total_own;

labels = ['MORTGAGE', 'OWN', 'RENT'];
data = [mortgage_average, own_average, rent_average];


# plotting the graph
def plot_bar_x():
    plt.bar(labels, data);
    plt.xlabel('Home ownership', fontsize=10);
    plt.ylabel('Average loan amount ($)', fontsize=10);
    plt.title('Average loan amount per home ownership');
    plt.show();


plot_bar_x();
