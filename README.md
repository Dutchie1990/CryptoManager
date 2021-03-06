# The Crypto Investment Monitor

<img src="cryptomanager\app\static\img\testing\homepage-picture.png">

Access to the project: 

LIVE: Click [here](https://crypto-investment-monitor.herokuapp.com/) to access the live website. <br>
REPO: Click [here](https://github.com/Dutchie1990/CryptoManager) to access the Github repository.

# Table of Contents
- [Project Goal](#Project-goal)
- [The Five Planes of UX design](#The-Five-Planes-Of-UX-Design)
    - [Strategy](#Strategy)
    - [Scope](#Scope)
    - [Structure](#Structure)
    - [Skeleton](#Skeleton)
    - [Surface](#Surface)
- [Database design](#Database-design)
- [Features](#Features)
- [Technologies & Tools](#Technologies-&-Tools)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credits](#Credits)
    - [Content](#Content)
    - [Acknowledgments](#Acknowledgments)
    - [Used websites](#Used-websites)

# Project Goal
Monitoring your assets is always the best thing to do as a cryptocurrency investor. For this reason, this project aims to provide a comprehensive overview of the assets which the users' holds as well the transactions made by the user. Besides managing your own assets, it will also consist a leaderboard whereby you can see the other users' profits and lost as well the portfolio overview. You can learn how other investors spread their investments. 

# The Five Planes Of UX Design

## Strategy
The platform's concept is to provide a comprehensive overview of currently holding crypto assets. The user are able to set up a deposit and insert their transactions. The platform combines this to a overview, with current profit and loss calculated on real time prices. In the leaderboard section of the platform the top 10 users with most profits are listed. Other users can see the crypto's in which are investing and are able to learn from others based on the best performing portfolio's. 

## User stories

The platform is divided in several epics with their own features and user stories. The existing epics are:
### Homescreen

- As a new visitor I want to be able to navigate to the register page, so I can make a profile
- As a returning visitor I want to be able to navigate to the login page, so I can access my profile

### Login/Register

- As a new visitor, I want to be able to register in order to make an own profile
- As a returning visitor, I want to be able to log in order to access my profile
- As a logged in user, I want to be able to log out in order to exit my profile

### Assets

- As a logged in user, I want to be able to make a deposit in order to imitate my real investments 
- As a logged in user, I want to be able to make a withdrawal in order to imitate my real investments
- As a logged in user, I want to be able to see how my assets perform to make real-time investments decisions

### Transactions

- As a logged in user, I want to be able to register my transaction to register my investments activities
- As a logged in user, I want to be able to adjust the prices of my transactions in case I want to register an old transactions to get a real overview of my investment activities
- As a logged in user, I want to be able to make sell and buy transaction against different crypto's or USD in order to register my investment activities

### Leaderboard

- As a user, I want to be able to see the best portfolio's based on profit and loss, in order to make investment decisions
- As a logged in User, I want to be able to see my own performance in order to compare my portfolio with the best performing portfolio's

## Scope
The project itself is a crypto investment monitoring tool. The project consist out of different epics which work together as a whole. 

### Nice to have 
One downside of the platform is the manual input used from the user to register their assets and transactions. It would be ideal to wire up the trading platform with the monitoring platform to automatically import the trades and assets from the user's account. But this is not in the scope of this project. 

# Structure 

The website will contain different pages as well for logged in users and not logged in users. The following tree map structure will further outline the intented structure for the website. 

<img src="cryptomanager\app\static\img\tree-map.jpg">

Furthermore, the portfolio is be compatible with all kind of devices. Small design changes can be expected such as omitting some data at smaller devices screens. But the main functionalities should be easy to use and understand on all devices. 

# Skeleton

The webapp consist out of the following views: 
- Welcome view
- Login view
- Register view
- Leaderboard view (while logged in)
- Leaderboard view (not logged in)
- Assets view
- Deposit/Withdrawal view
- Transactions view
- Add transaction view 
- General error view

Click [here](https://github.com/Dutchie1990/CryptoManager/blob/Documentation-and-testing/cryptomanager/app/static/img/testing/wireframes.pdf) for the designs

# Surface

To optimize the user's experience of the site, it is design is very simple and basic. Relaxing colors are used with maximum contrast. The next colors are used in this project. 

<img src="cryptomanager\app\static\img\color-pallet.png">

The projects typography is standard to maximize the simplicity of the application. On bigger screens the headers are uppercase to emphasize headings information. 

# Database design

The database provider for the project is MongoDB. This is a non-relational database based on documents. The following database scheme is used for this project including 3 documents. 

<img src="cryptomanager\app\static\img\database-scheme.png">

# Epics & Features 
## <strong>Homescreen</strong>
This epic is the entry point of the website, from here the users can navigate to the login or register page as well to the leaderboard. 
#### Features 
- Presentation

The presentation of the homescreen is very basic. The background give some inside in how the app looks like. Furthermore, there are buttons, 'Register now!' and 'Login' which are call to action buttons. At last, there is also a possibility to access the leaderboard by the link on in the navigation bar.

- Button functionality

The button 'Register now!' must lead to the register page and the button 'Login' must lead to the login page.


## <strong>Login/Register</strong>
This epic enables users or potential users to make an account and login to the platform. The user will be connected to his own assets and transactions make the platform personalized for each user. Also, the options to register a deposit or a transaction can only be made when a user is logged on to his account. Lastly, a user must be able to delete his account with all underlying assets and transactions as well. 
#### Features 
- Presentation

The epic 'Login/Register' consist of 2 pages, the register page and the login page. As a user successfully makes a profile there must be success message as well as the login is successfull. The success messages must be in a green box and the error messages must be in a red box. 

- Login 

As a user already have profile the emailaddress and the password should be match with the data in the database. When there is a match the user profile is loaded. If there is no match the user will see an error message. Furthermore, there must be field validation like the password should be longer then 5 characters and the email field should include a '@' and should be longer then 5 characters. Those validations should be validated real-time. When all validations are met, the submit button should be available for the user. Lastly, when a user typed some input in the field the clear button should clear all input. 

- Logout

As a user is logged in the logout navigation link should be visible for the user. When the user click the logout button, the user will be logged out and redirected to the homepage. It is not possible for the user to access their profile again before log in again. 

- Register 

If a user decide to make profile, he should fill in the register form, where he should register his firstname, emailaddress and password. To extra check the password, the user should repeat his newly chosen password. There are several frontend field validation such as firstname should be longer then 3 characters, email should include '@' and should be longer then 5 characters, password field should be longer the 5 characters and the confirm password field should be the same as the password field. Those validations should be validated real-time. When all validations are met, the submit button should be available for the user. Lastly, when a user typed some input in the field the clear button should clear all input. In the backend there is also a validation if the emailaddress already exists, when the emailaddress is already in use the user is not able to make a new profile with the same emailaddress. When the user is succesfully registered, the user is automatically logged in and can work with his profile.

- Delete 

This feature is implemented because I wanted the user to make a full CRUD action from the frontend. When the user delete his account, all underlying assets and transactions are also deleted

- Adjust password

This feature is implemented because I wanted the user to make a full CRUD action from the frontend. When the user change his password, this password should be used to login again.

## <strong>Assets</strong> 
This epic consist out off different features which are connected to the assets management of the user. The user will be able to register their asset in USD. From their they can obtain other assets by doing transactions. Those assets will be visually presented by to the user as well the unrealized profits will be shown. Also a complete valuation will be shown to the user to make them able to monitor their assets closely with real-time information.  
#### Features 

- Presentation

At the asset page the user should get an overview of his current assets and he should have the possibility to make a deposit and/or withdrawal of fiat currency (USD). The assets are presented in a table where the user can find the asset name, the amount, the buying rate against usd, the total value and the profit or loss since the user bought the assets in percentage. 

- Deposit 

In the jumbtron there is a deposit button which opens up a modal to make a deposit. When an number is entered, the confirm button will be available to make the deposit. When the user enter a non number, there will be a validation error. Lastly, when a user enter some value in the input box the clear button will be available for clearing the values. If the user make a valid desposit the transanction will be saved in the transaction table as well the asset will be saved and added to the withdrawable balance and also can be used to make new transaction or withdraw again.

- Withdrawal

In the jumbtron there is a deposit button which opens up a modal to make a withdraw. When an number is entered, the confirm button will be available to make the withdraw. When the user enter a non number, there will be a validation error. Lastly, when a user enter some value in the input box the clear button will be available for clearing the values. When a user try to make a withdrawal, the value will be validated. If the user does not have enough withdrawable funds available there will be a validation error. In case the user have sufficient withdrawable currency availble, the withdraw value is substracted from the withdrawable balance. 

- Live valuation

The asset page has a live validation of the current assets. This value will be shown in the Value field of the table. The web api which is used to obtain the current value of the assets is coingecko. 

- Profit and Loss 

The profit and loss collumn will be a calculation of the appreciation of depreciation of the assets value since the moment the user obtain the asset. When the asset is percentage is positive it will be a green color and whenever the percentage is negative the color will be red. 

## <strong>Transactions</strong> 
The transactions are as well a backbone of the platform. As soon the users register their first asset in USD, they are able to register their transaction. Those transactions will be saved into the database and can be looked into. 
#### Features 
- Presentation

The transactions are presented in a table. The following values are presented to the users: the date of the transaction, the ordertype, the pair, the rate based on the pair traded, the volume of the transaction and the costs of the transaction. Furthermore, is there a button to add a transaction which opens a new page to add the transactions. 

- Add transaction

In the transactions screen the user can choose whether he want to sell or buy assets with a dropdown. When the user select his ordertype the user should choose which asset he will buy or sell. At last, the user must also enter the VS currency which is the currency against the trade will be done. When the user decided which coin he will buy or sell against which currency or coin, the user can input the volume. When the volume is entered the prize of the transaction is calculated live. Lastly, when a user also want to adjust the prize of the transaction, the user can manually adjust the prize's value. 

When the ordertype is 'BUY' the user will obtain the currency which is selected at the BUY/SELL dropdown and the user will pay with the coin or currency which is selected by the VS currency field

When the ordertype is 'SELL', the user will sell the currency which is selected at tthe BUY/SELL dropdown and the user will obtain the coin or currency which is selected by the VS currency field

- Transaction validation and calculation

In both cases, buy and sell orders, the amount of VS currency or the currency which the user want to sell is validated whether it is sufficient. When the user do not have sufficient funds, there will be an error message. 

For all the transactions the original price paid in USD is calculated and save in the asset table. If the asset already exists the avarage price for the asset will be calculated. Whenever a user manually adjust the price, then the new USD value is also calculated. The USD price is used in the asset page to calculate the profit and loss per asset. 

## <strong>Leaderboard</strong>
The leaderboard is a open for everyone part of the platform. The aim of this page is to inform people about the most succesfull portfolio's. The overview show the top 10 succesfull portfolio's and give an overview which assets are included in the portfolio. 
#### Features 
- Presentation

In the leaderboard a overview of the best 10 profiles are shown based on profits and losses. The username is shown along with the profits and a button to explore their profile. When the explore button is clicked the, an overview of the assets is given in percentages. Whenever a logged in user is in the list of the best profiles, the color of his line will be different from the others. 

## <strong>Error handling</strong>
The error handling is part of defensive programming. In order to prevent the application to digest malicious data, some error handling measures are in place. Firstly, the unauthorized error, page not found error and also an internal service error. Those errors will be catched and the user will be redirected to the error page.
#### Features 
- Presentation general

The error page consist with a standard text. The user is able to navigate from the page with the navigation bar.

# Technologies & Tools

### Languages

- HTML - used to setup the presentation of the flask application
- CSS - used to add custom styling to the flask application
- Python - used to setup the flask application as well communication with database and api
- JavaScript - used for different purposes as communication with the flask app and frontend validations

### Programs

- VS code - IDE used to build the project
- Balsamiq - Used to make mockups for the project
- Github - Used for source control and to make pull requests
- Git - Used to make branches for different assets and commits 
- Outklip - Used to make gif files to document testing
- Moon Modeler - Used to make the database design
- MongoDB Atlas - Used as database provider
- Heroku - Used for application deployement

### Most important dependencies 

- Jquerydatatables - Used to render the asset and transaction data in tables
- Flask - Used as microframework to make the application
- Flask-WTF - Used in order to easily validate and make forms
- Flask-Login - Used to manage user login functionality
- MongoDB - Used to communicate with the database
- Requests - Used to communicate with external API
- Axios - Used to communicate with external API from JavaScript
- Ninja2 - Used as template engine 
- Bootstrap - Used to style the website

# Testing

[visit TESTING.md](https://github.com/Dutchie1990/CryptoManager/blob/main/TESTING.md)

# Deployment

### Heroku

The project has been deployed and hosted on Heroku. To deploy the application, please follow the next steps: 

1. Create a Procfile with the following command ```echo web: python run.py > Procfile```. Please do not forget to delete the blank line at the bottom of the file. 
2. Create a requirement.txt with the following command ```pip freeze > requirements.txt```
3. Push both files to github by using git -A --> git commit -m "files for deployement" --> git push
4. Make your account at Heroku website and create a new app.
5. Within the app, navigate to the "Deploy" tab and, under "Deployment method" select github
6. Connect with the github repository by clicking "Connect"
7. Navigate to the "Settings" tab, and click "Reveal Config Vars". Enter the following values:
    - "IP": "0.0.0.0"
    - "PORT": "5050"
    - "MONGODB_URI": The database URI
    - "MONGO_DBNAME": The database name
    - "SECRET_KEY": Your FLASK secret key
8. Deploy the app in the "Deploy" tab under "Manual deploy", select the desired branch and click "Deploy Branch"
9. Another option is to configure automatic deployment from the main branch of github.
10. When deployement is finished successfully, a message will display "Your app was successfully deployed", then you can click View to launch it.

### Local 

For local running the application please follow the next steps:

1. Open your IDE and paste the following command ```gh repo clone Dutchie1990/CryptoManager```
2. Install the required modules with the following command ```pip install -r requirements.txt```
3. In MONGODB, create a new database "crypto_portfolio" and make the following collections "User", "Assets" and "Transactions"
4. Create a env.py file within the app folder and add the file to the .gitignore file
5. Configure your env.py file

```
import os

os.environ.setdefault("IP", [your value])
os.environ.setdefault("PORT", [your value])
os.environ.setdefault("MONGODB_URI", [your value])
os.environ.setdefault("MONGO_DBNAME", [your value])
os.environ.setdefault("SECRET_KEY", [your value])

```

6. You can run the app by typing ```python run.py```

# Credits

### Content
All the content is written by me. The background image comes from the following website: https://designmodo.com/free-crypto-icons/

### Acknowledgments
Thanks to my tutors and my mentor Spencer for valueable tips and tricks and helping me throughout the project. I would also like to thank the community on Slack and StackOverflow for valuble input regarding the project.

### Used Websites
- https://coolors.co/ 
- https://www.rgbtohex.net/hextorgb/
- https://docs.mongodb.com/guides/
- http://mongoengine.org/
- https://flask.palletsprojects.com/en/2.0.x/
- https://app.pluralsight.com/ (Structuring a Growing Flask Application)
- https://docs.python.org/3/library/index.html
- https://www.coingecko.com/en/api
- https://flask-wtf.readthedocs.io/en/0.15.x/
- https://getbootstrap.com/docs/4.3/getting-started/introduction/
- https://stackoverflow.com/

NOTE: 

Thanks for reading my ReadMe.md, I hope you will beat me in the leaderboard! 

<hr>
-- Succes with your investments. -- 




