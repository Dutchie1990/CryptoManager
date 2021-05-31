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
- [Further Manual Testing](#Further-Manual-Testing)

# Epic Testing

## Homescreen

#### User stories

- As a new visitor I want to be able to navigate to the register page, so I can make a profile - <strong>Passed</strong>
- As a returning visitor I want to be able to navigate to the login page, so I can access my profile - <strong>Passed</strong>

<img src="cryptomanager\app\static\img\testing\homescreen.png">

#### Found issues

1. BUG1: If a user is logged in, he is not directed to the assets page if he directly try to open the homescreen

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

1. BUG2: If the user is registered, he is redirected to the homescreen instead of assets screen
2. BUG3: Emailfield in register and in login is case sensitive
3. BUG4: Frontend validation of firstname field is not the same as backend validation of the firstname field

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

1. BUG5: Current value field is not updated when making deposit or withdrawal

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

1. BUG6: When the user adjust the price and the VS currency is USD, the submit button won't be updated to available
2. BUG7: The transaction time should be trimmed to yyyy/mm/dd hr:min format
3. BUG8: The transaction time is not current server time

## Leaderboard

#### User stories

- As a user, I want to be able to see the best portfolio's based on profit and loss, in order to make investment decisions
- As a logged in user, I want to be able to see my own performance in order to compare my portfolio with the best performing portfolio's

## Error page
# Validators
# Further Manual Testing
