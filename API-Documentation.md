# API Documentation

## Login API
### step 1: Open Postman
### step 2: Select Post method
### step 3: Enter Below URL in url box
http://127.0.0.1:5000/login

#### Note: Port number might be different according to configuration

### step 4: Select "body" option then select "raw" option and choose "Json" from dropdown
### step 5: Enter below json text in body textArea and click on "Send" button
{
    "username": "admin",
    "password": "PasswordBarrier"
}
![img_1.png](img_1.png)
### step 6: In response body you will get JWT token copy that token
![img_2.png](img_2.png)
### step 7: Select "Authorization", from type choose "Bearer Token" and paste token in token textBox
#### Note: After 1 hour token will expire follow same steps to regenerate new token
![img_3.png](img_3.png)

## Dataframes Join API

### step 1: Select Post Method
### step 2: Enter Below URL in url box
http://127.0.0.1:5000/joinDataframes
#### Note: Port number might be different according to configuration
### step 3: Make sure you are using correct JWT token
### step 4: Select "body" option then select "raw" option and choose "Json" from dropdown
![img_4.png](img_4.png)
### step 5: Open "body_example1.json" file from project directory and copy whole Sample json text
### step 6: Paste Json text in request body textArea
### step 7: make changes according to your data and need and click on send button
![img_5.png](img_5.png)
### step 8: In response body you will get joined dataframe according to your join type
![img_6.png](img_6.png)
