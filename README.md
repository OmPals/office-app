# summergeeks11111100100 | SDE-Intern Assignment | office-app
##### [problem statement](https://summergeeks.in/static/assignments/summergeeks%202020%20-%20SDE%20Assignment.pdf?utm_campaign=SummerGeeks%202020&utm_source=hs_email&utm_medium=email&utm_content=79542605&_hsenc=p2ANqtz--viFrAMzY7DASDAZIKHA56SZgxYXWPDZp5IGeBI6r7kbP5hEI6zDuCxUo3yxMoXKDQAFRE13zqkiWTN5sUFXdBFAGHXQ&_hsmi=79542605 "problem statement")

### Approach:
1. Entity Relationship diagram:- 
[![ER diagram](https://github.com/OmPals/office-app/blob/master/images/er.png "ER diagram")](https://github.com/OmPals/office-app/blob/master/images/er.png "ER diagram")
2. Database: Relational schema:-
[![Relational schema](https://github.com/OmPals/office-app/blob/master/images/rel.png "Relational schema")](https://github.com/OmPals/office-app/blob/master/images/rel.png "Relational schema")

##### Check out[ models.py ](https://github.com/OmPals/office-app/blob/master/office/models.py " models.py ")in office folder for database definition from [Django ORM](https://tutorial.djangogirls.org/en/django_orm/ "Django ORM"). on Postgres server.
#### Mysite is a django project. Office is an django app.

#### A visit can be created on localhost http://127.0.0.1:8000/admin/office/ after running `python3 manage.py runserver` from terminal.

### What has been done till now:-
1. I added an extra attribute 'send_mail_opt' to the visit table for whether the mail has been sent or not.  Default value is set to 'not_sent' => while meeting is going on.
2. When meeting is over,   'send_mail_opt' takes value 'send now!!'
3. then in Postgres backend, a query is executed for the visits which has 'send_mail_opt' = 'send now!!' 
4. Fetching those email addresses, send_mail function is called.
5. Example email is:- 
[![mail_arrived](https://github.com/OmPals/office-app/blob/master/images/mail-arrived.png "mail_arrived")](https://github.com/OmPals/office-app/blob/master/images/mail-arrived.png "mail_arrived")

6. At the end, the value for 'send_mail_opt' is changed to 'already_sent'.

##### Screenshots for [admin-site](https://github.com/OmPals/office-app/tree/master/images "admin-site")

### Thank you
