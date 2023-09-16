# ATM Simulator

The main functions of the ATM simulator may be summarized as follows:

Before performing any transaction, the user must enter his or her username and PIN (personal identification number) at an input screen/prompt (GUI or otherwise).
The system must validate the user information against the information that is pre-built into the system.
For the purposes of this project, the system will have the following three username: PIN pairings to start.

1. User1: 1234
2. User2: 2222
3. User3: 3333

These can be stored in volatile (temporary) storage or in a file or series of files depending on whether you opt for the Basic Functionality or the Extended Functionality.
The prompt for the user information should allow for three attempts. If the user does not enter a valid username: PIN combination, the system must display an appropriate error message after each attempt and re-prompt. After the third invalid attempt, the system simply ends the program

1. Use files to store Usernames and PINS
2. Must have an administrator login feature

The names and PINs of users must be validated using data contained in the appropriate lists or files using the following criteria:

1. Username (String)
2. PIN (String – 4 characters)

Once access has been authorized, the main transaction screen of the application should allow the user to carry out one of the following transactions:

1. Add new user
2. Delete user
3. Plot Account Balances
4. Exit

If the user is a regular user The Menu options are:

1. Account Balance
2. Withdraw
3. Deposit
4. Change PIN
5. Exit

For the purposes of this project, all transactions will be carried out on a single account per user. There is no distinction between a chequing and a savings account.
After each transaction, with the exception of Exit, the system must return to the menu display and prompt the user for another transaction choice. In the case of the Administrator, upon exiting, the system should prompt for a new user and PIN.

## About Deposit

The user must enter the amount to be deposited into his or her account. The amount of the deposit must be added to the current balance into the account. Appropriate confirmation messages must be provided indicating the amount of the deposit and the new current balance. Proper data input validation to ensure that numerical data is input must be used along with error handling.
Keep in mind that if you are working with the Basic Functionality model, the balances are stored  in the list, which will be lost once the program ends. If you use files to store the information, then the new balances should be saved and available when the program runs subsequent times.

## About withdrawal

The user must enter the amount to withdraw. Each withdrawal transaction is subject to a maximum of $1,000 per transaction. If the user enters an amount greater than $1000, the system must present a message indicating that $1000 is the maximum per withdrawal. The ATM accepts only transactions for which the amount entered is a multiple of $10. There is no daily maximum amount apart from the user’s account balance in which case the system must also inform the user if the account balance is less than the transaction amount.

## About Account balance

When the user selects this option, the system simply checks the data for that user and displays the current balance. Checking the account balance does not alter the balance itself.

## About Changing of PIN

Changing the PIN is available to all users. The difference in how this feature operates depends on how you set up the program. If you are using the Basic Functionality model, using lists to store user information, the change in PIN will only be effective during the current running of the program.
Once you quit the program and start it again all data values return to the original  values. However, if you are working with the Extended Functionality model and you are using files to store the information, the change in PIN will be committed to the file and be available for subsequent accesses using this new value.

The following functions concern the ATM's functioning with respect to the system administrator and the internal mechanisms of the ATM, not the user.

1. The system administrator, as any other user, must enter his or her name and PIN (personal identification number) on the same input screen. The system administrator may perform only system transactions (he or she has no personal account).
2. The System Administrator must login with the unique User Name of SysAdmin and the PIN 1357. When these credentials are entered, the system must automatically display only the Administrator screen with its options:

1. Add new user
2. Delete user
3. Exit

## About Adding a new user

The administrator is the only user wo can create new user accounts. When this option is selected, the system must create a file or files for the new user to store the user information and account transactions and balances. There are many ways that this can be setup. You can use a single file to store all usernames and PINS followed by individual files for each user’s account details (hint, name each user’s account file using the username as the file name). Alternatively, you can create a single file per user which stores the username, PIN and account balances. There is no right or wrong way, it is up to you to decide how you want to set it up.

Hint: This feature should be one of the first functions that you create so that you can then use it to create your user files with the three initial users indicated in the first section of the specifications. You have to determine how you will store the information ( Single file containing all users, and account information, single file for users and PINS with individual user account files, or a series of individual user files that house all user and account details for that user.)

## About user deletion

When the administrator selects this option, they should be able to simply prevent the user in question from logging in. This could be accomplished by deleting the file(s) associated with that user, or, by changing the PIN number for the user to a pre-determined value that would remain unknown to the user.

## About Plotting Account Balances

This feature of the Administrator menu is not something that is realistic, however it is used in this project for the sole purpose of having you implement the use of Python’s graph and plotting feature using matplotlib.
When the administrator selects this option, the program will work through the user accounts and plot the current account balances for each user (you can use the type of plot of your choice: pie, bar, etc.) Keep this to a maximum of 10 users. The plot should indicate the user and corresponding account balance.

## About Exit

When the administrator selects this option, the system should return to prompting for a new username and PIN.
