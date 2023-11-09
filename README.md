# This is a project (RESTFUL API) done as a portfolio project for the end of the foundations course at ALX Africa.


## Anyone can clone the repo and create a mysql database called api_db to begin running the application locally.


### This section describes the Routes and sample POST data implementing the four major HTTP methods (GET, POST, PUT and DELETE).


GET all makes:
--------------
curl -X GET http://10.247.161.4:5000/makes


GET make by id:
---------------
curl -X GET http://10.247.161.4:5000/makes/make_id_here


POST Add make to db:
--------------------
curl -X POST -H "Content-Type: application/json" -d '{
  "make": "Toyota",
  "origin": "Japan"
}' http://10.247.161.4:5000/makes


DELETE make by id:
------------------
curl -X DELETE http://10.247.161.4:5000/makes/<int:make_id>


PUT UPDATE make by id:
----------------------
curl -X PUT http://10.247.161.4:5000/makes/<int:make_id>


GET all models (make_models):
-----------------------------
curl -X GET http://10.247.161.4:5000/make_models


GET models (make_model) of a particular make by make id:
--------------------------------------------------------
curl -X GET http://10.247.161.4:5000/make_models/make_id_here


POST Add make_model to db:
--------------------------
curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Toyota Avensis",
  "year": 2023,
  "description": "Simple"
}' http://10.247.161.4:5000/make_models/make_id_here


DELETE model by model id:
-------------------------
curl -X DELETE http://10.247.161.4:5000/make_models/<int:model_id>


PUT update model by model id:
-----------------------------
curl -X PUT http://10.247.161.4:5000/make_models/<int:model_id>


GET all trims:
--------------
curl -X GET http://10.247.161.4:5000/make_model_trim


GET all trims of a make by make id:
-----------------------------------
curl -X GET http://10.247.161.4:5000/make_model_trim/make_model_id_here


POST Add trim to db:
--------------------
curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "XLE",
  "engine_type": "2GR",
  "horse_power": 320,
  "price": 35000,
  "fuel_type": "Gasoline",
  "transmission": 5,
  "features": "Leather seat, Cruise control, AC"
}' http://10.247.161.4:5000/make_model_trim/make_model_id_here


DELETE a trim by trim id:
-------------------------
curl -X DELETE http://10.247.161.4:5000/make_model_trim/<int:trim_id>


PUT update a trim by trim id:
-----------------------------
curl -X PUT http://10.247.161.4:5000/make_model_trim/<int:trim_id>


GET all users:
--------------
curl -X GET http://10.247.161.4:5000/users


GET users of a particular trim by trim_id:
------------------------------------------
curl -X GET http://10.247.161.4:5000/users/trim_id_here


POST Add users of a Trim to db:
-------------------------------
curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Navi212",
  "email": "navi@vavi.com",
  "country": "USA",
  "state": "Ohio",
  "zip_code": "100221",
  "age": 95,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/trim_id_here


DELETE a user by user id:
-------------------------
curl -X DELETE http://10.247.161.4:5000/users_trim/<int:user_id>


PUT update a user by user id:
-----------------------------
curl -X PUT http://10.247.161.4:5000/users_trim/<int:user_id>


GET all user reviews for all trims:
-----------------------------------
curl -X GET http://10.247.161.4:5000/users_reviews


GET user reviews for a particular trim by trim id:
--------------------------------------------------
curl -X GET http://10.247.161.4:5000/users_reviews/trim_id_here


Add user reviews for a Trim to db:
-----------------------------------
Sample:
-------
curl -X POST -H "Content-Type: application/json" -d '{
  "rating": 4.5,
  "review": "Comfortable and good for tropical roads",
}' http://10.247.161.4:5000/users_reviews/<int:user_id>/<int:trim_id>


DELETE a review by review id:
-----------------------------
curl -X DELETE http://10.247.161.4:5000/users_trim/<int:review_id>


PUT update a review by review id:
---------------------------------
curl -X PUT http://10.247.161.4:5000/users_trim/<int:user_id>/<int:review_id>


Authors:
-------
+ Joseph Nweke         -(https://github.com/Navi212)
+ Stanhope Chukwunonso -(https://github.com/stanarthur)
+ Ike Dimkpa	     -(https://github.com/ikdimkpa)
