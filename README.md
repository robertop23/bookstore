## **Install docker**:
  OSX: https://hub.docker.com/editions/community/docker-ce-desktop-mac

**Users**:
  **Django Admin**:
    Username: admin
    Pass: 1212pass
  **Frontend**:
    Username: userconsumer
    Pass: 1212pass
    Username: userauthor
    Pass: 1212pass
    Username: userpublisher
    Pass: 1212pass


## **Architecture**:
  3 Docker servers:
    Server: Django with Django Rest Framework and Djoser
    Frontend: Nuxt.js with Vuetify
    DB: Postgres

## **What is working**:
  List books by store
  Show store book details
  Authentication
  Purchase/Rent Book (no cart/payment processing, just clicking on buttons)
  Increase on 0,05 the author earnings (for testing purposes, the starting views
  of author/publisher content is set to 5, so is trivial change this value to 1.000.000)

## **What is Missing**:
  Cart/Payment processing
  My books view
  Author views
  Publisher views
  Account views (to update password/email and others)
  Store Selector
  Admin views
  Analytics views
  Search engine
  Add permissions

## **Usage instructions**

1. Clone this repository
2. cd bookstore
3. Run Docker container:
     docker-compose up --build
4. Open frontend: http://127.0.0.1/ login as "userconsumer"
5. Rent or Purchase a book clicking on the corresponding book and button
6. Open http://127.0.0.1:8000/admin/ login as admin and check the earnings table
