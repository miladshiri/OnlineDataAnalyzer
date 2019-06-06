# OnlineDataAnalyzer
###About the project

This is a web-based application that allows you to upload your data, define different machine learning methods, train them with the data and finally use
the trained model for predication tasks. 
The backend is written in Django 2.2, which utilizes high quality tools to store and analyze data. Various machine learning
 algorithms have been implemented to perform classification, clustering and dimension reduction tasks on the data using python packages
 like scikit-learn, pandas and numpy. For test purposes sqlite is used as the database but postgreSql is preferred for practical usage.


###Instructions

Before starting, you need to sign in to be able to use the application. So, in case you are not logged in, links are provided at the menu
 to sign up or log in.
 First, upload your data. Then you should configure a machine.
 It is really easy. Just go to Select & config method and select a method, followed by a page in which
 you can choose custom parameters for that specific method. Now, it is time to train the defined machine by the data you uploaded before. Click on
 Train the model and choose the data and machine. Finally, you can use the trained machine on a new data
 for prediction tasks.
