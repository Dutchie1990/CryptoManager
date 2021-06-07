# Testing

[return to README.md](https://github.com/Dutchie1990/CryptoManager)

# Table of Content 
- [Epic Testing](#Epic-Testing)
    - [Login/Register](#Login/Register)
    - [Assets](#Assets)
    - [Transactions](#Transactions)
    - [Leaderboard](#Leaderboard)
    - [Error page](#Errorpage)
- [Validators](#Validators)

# Epic Testing

## Homescreen

#### User stories

- As a new visitor I want to be able to navigate to the register page, so I can make a profile - <strong>Passed</strong>
- As a returning visitor I want to be able to navigate to the login page, so I can access my profile - <strong>Passed</strong>

<img src="cryptomanager\app\static\img\testing\homescreen.png">

#### Found issues

1. BUG1: If a user is logged in, he is not directed to the assets page if he directly try to open the homescreen - <strong>Fixed</strong>

## Login/Register

#### User stories

- As a new visitor, I want to be able to register in order to make an own profile - <strong>Passed</strong>

<img src="cryptomanager\app\static\img\testing\register.gif">

- As a returning visitor, I want to be able to log in order to access my profile - <strong>Passed</strong>

<img src="cryptomanager\app\static\img\testing\login.gif">

- As a logged in user, I want to be able to log out in order to exit my profile - <strong>Passed</strong>

<img src="cryptomanager\app\static\img\testing\logout.gif">

#### Further testing
 - Frontend field validations - <strong>Passed</strong>
 - Backend field validations - <strong>Passed</strong>

#### Found issues

1. BUG2: If the user is registered, he is redirected to the homescreen instead of assets screen - <strong>Fixed</strong>
2. BUG3: Emailfield in register and in login is case sensitive - <strong>Fixed</strong>
3. BUG4: Frontend validation of firstname field is not the same as backend validation of the firstname field - <strong>Fixed</strong>

## Assets

#### User stories

- As a logged in user, I want to be able to make a deposit in order to imitate my real investments - <strong>Passed</strong>

<img src="cryptomanager\app\static\img\testing\deposit.gif">

- As a logged in user, I want to be able to make a withdrawal in order to imitate my real investments - <strong>Passed</strong>

<img src="cryptomanager\app\static\img\testing\withdrawal.gif">

- As a logged in user, I want to be able to see how my assets perform to make real-time investments decisions - <strong>Passed</strong>

<img src="cryptomanager\app\static\img\testing\asset-screen.png">

#### Further testing
- Database transactions - <strong>Passed</strong>
- Frontend field validations - <strong>Passed</strong>
- Backend field validations - <strong>Passed</strong>

#### Found issues

1. BUG5: Current value field is not updated when making deposit or withdrawal - <strong>Fixed</strong>

## Transactions

#### User stories

- As a logged in user, I want to be able to register my transaction to register my investments activities

<img src="cryptomanager\app\static\img\testing\add-transaction.gif">

- As a logged in user, I want to be able to adjust the prices of my transactions in case I want to register an old transactions to get a real overview of my investment activities

<img src="cryptomanager\app\static\img\testing\adjust-transaction-prize.gif">

- As a logged in user, I want to be able to make sell and buy transaction against different crypto's or USD in order to register my investment activities

<img src="cryptomanager\app\static\img\testing\transaction-screen.png">

#### Further testing
- Database transactions - <strong>Passed</strong>
- Frontend field validations - <strong>Passed</strong>
- Backend field validations - <strong>Passed</strong>

#### Found issues

1. BUG6: When the user adjust the price and the VS currency is USD, the submit button won't be updated to available - <strong>Fixed</strong>
2. BUG7: The transaction time should be trimmed to yyyy/mm/dd hr:min format - <strong>Fixed</strong>
3. BUG8: The transaction time is not current server time - <strong>Fixed</strong>

## Leaderboard

#### User stories

- As a user, I want to be able to see the best portfolio's based on profit and loss, in order to make investment decisions - <strong>Passed</strong>
- As a logged in user, I want to be able to see my own performance in order to compare my portfolio with the best performing portfolio's - <strong>Passed</strong>

<img src="cryptomanager\app\static\img\testing\leaderboard-screen.png">

#### Found issues

1. BUG9: When a user doesn't have any USD asset a exception is thrown - <strong>Fixed</strong>
2. BUG10: The leaderboard is not limited to the best 10 portfolio's - <strong>Fixed</strong>

## Error page

- The error page consist with a standard text. The user is able to navigate from the page with the navigation bar.

<img src="cryptomanager\app\static\img\testing\error-screen.png">

# Validators

## JS validator
For the validation of my JavaScript code I used JSHint. All the JavaScript files are conform to existing standards

## Python PEP8
I have tried to be as much as PEP8 compliant as possible. The only issues are found in the main __init__.py file.
- missing whitespace around modulo operator pycodestyle(E402)
- module level import not at top of file pycodestyle(E228)

Trying to resolve these issues will lead to bugs such as circular imports and the formatting filter will break as well. Therefore I decided to ignore those 2 issues. 

