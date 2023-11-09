This describes the Routes and sample POST data implementing the
four major HTTP methods (GET, POST, PUT and DELETE).

==============================================================
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

curl -X POST -H "Content-Type: application/json" -d '{
  "make": "Lexus",
  "origin": "Japan"
}' http://10.247.161.4:5000/makes

curl -X POST -H "Content-Type: application/json" -d '{
  "make": "Mercedes",
  "origin": "Germany"
}' http://10.247.161.4:5000/makes

curl -X POST -H "Content-Type: application/json" -d '{
  "make": "Buggati",
  "origin": "Italy"
}' http://10.247.161.4:5000/makes

curl -X POST -H "Content-Type: application/json" -d '{
  "make": "Ferrari",
  "origin": "Italy"
}' http://10.247.161.4:5000/makes



DELETE make by id:
------------------
curl -X DELETE http://10.247.161.4:5000/makes/<int:make_id>


PUT UPDATE make by id:
----------------------
curl -X PUT http://10.247.161.4:5000/makes/<int:make_id>
==============================================================





==============================================================
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


curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Toyota Avensis",
  "year": 2023,
  "description": "Simple"
}' http://10.247.161.4:5000/make_models/1


curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Toyota Corolla",
  "year": 2020,
  "description": "Cute"
}' http://10.247.161.4:5000/make_models/1

curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Toyota Avalon",
  "year": 2022,
  "description": "Silent and Fast"
}' http://10.247.161.4:5000/make_models/1

curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Lexus RX",
  "year": 2023,
  "description": "Smart looking"
}' http://10.247.161.4:5000/make_models/2

curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Lexus GX",
  "year": 2023,
  "description": "Smart looking"
}' http://10.247.161.4:5000/make_models/2

curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Mercedes GLK",
  "year": 2013,
  "description": "Good looking"
}' http://10.247.161.4:5000/make_models/3

curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Mercedes GLA",
  "year": 2011,
  "description": "Portable"
}' http://10.247.161.4:5000/make_models/3

curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Mercedes GLE",
  "year": 2020,
  "description": "A beast"
}' http://10.247.161.4:5000/make_models/3

curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Bugatti Chiron",
  "year": 2010,
  "description": "Fantastic Beast"
}' http://10.247.161.4:5000/make_models/4

curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Bugatti Veron",
  "year": 2024,
  "description": "Awesome Beast"
}' http://10.247.161.4:5000/make_models/4

curl -X POST -H "Content-Type: application/json" -d '{
  "model": "Ferarri SRT",
  "year": 2013,
  "description": "Good looking"
}' http://10.247.161.4:5000/make_models/5

DELETE model by model id:
-------------------------
curl -X DELETE http://10.247.161.4:5000/make_models/<int:model_id>


PUT update model by model id:
-----------------------------
curl -X PUT http://10.247.161.4:5000/make_models/<int:model_id>

===================================================================






===================================================================
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


curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Toyota Avensis CX",
  "engine_type": "2GR",
  "horse_power": 320,
  "price": 35000,
  "fuel_type": "Gasoline",
  "transmission": 5,
  "features": "Leather seat, Cruise control, AC"
}' http://10.247.161.4:5000/make_model_trim/1


curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Toyota Corolla CE",
  "engine_type": "VVTI",
  "horse_power": 280,
  "price": 28000,
  "fuel_type": "Gasoline",
  "transmission": 4,
  "features": "Fabric seat, Cruise control, AC"
}' http://10.247.161.4:5000/make_model_trim/2

curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Toyota Corolla SE",
  "engine_type": "BE-1010",
  "horse_power": 320,
  "price": 30000,
  "fuel_type": "Gas",
  "transmission": 6,
  "features": "Leather, Cruise control, AC"
}' http://10.247.161.4:5000/make_model_trim/2


curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Toyota Corolla XCE",
  "engine_type": "4GR",
  "horse_power": 360,
  "price": 48000,
  "fuel_type": "Gas",
  "transmission": 6,
  "features": "Leather seat, Airbag, AC"
}' http://10.247.161.4:5000/make_model_trim/2

curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Lexus RX 350",
  "engine_type": "4GR",
  "horse_power": 360,
  "price": 48000,
  "fuel_type": "Gas",
  "transmission": 6,
  "features": "Leather seat, Airbag, AC"
}' http://10.247.161.4:5000/make_model_trim/4

curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Lexus RX 330",
  "engine_type": "4GR",
  "horse_power": 360,
  "price": 48000,
  "fuel_type": "Gas",
  "transmission": 6,
  "features": "Leather seat, Airbag, AC"
}' http://10.247.161.4:5000/make_model_trim/4

curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Lexus RX 300",
  "engine_type": "4GR",
  "horse_power": 360,
  "price": 48000,
  "fuel_type": "Gas",
  "transmission": 6,
  "features": "Leather seat, Airbag, AC"
}' http://10.247.161.4:5000/make_model_trim/4

curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Lexus GX 470",
  "engine_type": "4GR",
  "horse_power": 360,
  "price": 48000,
  "fuel_type": "Gas",
  "transmission": 6,
  "features": "Leather seat, Airbag, AC"
}' http://10.247.161.4:5000/make_model_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Mercedes GLK 350",
  "engine_type": "4GR",
  "horse_power": 360,
  "price": 48000,
  "fuel_type": "Gas",
  "transmission": 6,
  "features": "Leather seat, Airbag, AC"
}' http://10.247.161.4:5000/make_model_trim/6

curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Mercedes GLK 300",
  "engine_type": "4GR",
  "horse_power": 360,
  "price": 48000,
  "fuel_type": "Gas",
  "transmission": 6,
  "features": "Leather seat, Airbag, AC"
}' http://10.247.161.4:5000/make_model_trim/6

curl -X POST -H "Content-Type: application/json" -d '{
  "trim_name": "Mercedes GLK 400",
  "engine_type": "4GR",
  "horse_power": 360,
  "price": 48000,
  "fuel_type": "Gas",
  "transmission": 6,
  "features": "Leather seat, Airbag, AC"
}' http://10.247.161.4:5000/make_model_trim/6

DELETE a trim by trim id:
-------------------------
curl -X DELETE http://10.247.161.4:5000/make_model_trim/<int:trim_id>


PUT update a trim by trim id:
-----------------------------
curl -X PUT http://10.247.161.4:5000/make_model_trim/<int:trim_id>


======================================================================






======================================================================
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


curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Navi212",
  "email": "navi@vavi.com",
  "country": "USA",
  "state": "Ohio",
  "zip_code": "100221",
  "age": 95,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/1


curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Johnnycole",
  "email": "j@cole.com",
  "country": "USA",
  "state": "CA",
  "zip_code": "19991",
  "age": 95,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/2


curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Swastika",
  "email": "s@swa.com",
  "country": "Frace",
  "state": "Paris",
  "zip_code": "333",
  "age": 80,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/3


curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Stanley",
  "email": "stanhope@stan.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/4


curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Armani",
  "email": "joe@armani.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/4

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Ike",
  "email": "ike@ike.com",
  "country": "Hawaii",
  "state": "Honolulu",
  "zip_code": "1111",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/4

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Vandi",
  "email": "vandi@vandi.com",
  "country": "India",
  "state": "Diwali",
  "zip_code": "99921",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/4

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Rita",
  "email": "Rita@rita.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Thel",
  "email": "thel@thel.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Jay",
  "email": "jay@jay.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Joe",
  "email": "joe@joe.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Chris",
  "email": "chris@chris.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Queen",
  "email": "queen@queen.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Sophia",
  "email": "sophia@sophia.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "UK",
  "email": "uk@uk.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Bethel",
  "email": "bethel@bethel.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Lily",
  "email": "lily@lily.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Vic",
  "email": "vic@vic.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/5

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "Ratty",
  "email": "ratty@ratty.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/6

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "trump",
  "email": "trump@trump.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/6

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "william",
  "email": "willi@willi.com",
  "country": "CA",
  "state": "Ontario",
  "zip_code": "54421",
  "age": 50,
  "sex": "Male"
}' http://10.247.161.4:5000/users_trim/7

DELETE a user by user id:
-------------------------
curl -X DELETE http://10.247.161.4:5000/users_trim/<int:user_id>


PUT update a user by user id:
-----------------------------
curl -X PUT http://10.247.161.4:5000/users_trim/<int:user_id>

=========================================================================





=========================================================================
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



curl -X POST -H "Content-Type: application/json" -d '{
  "rating": 4.5,
  "review": "Comfortable and good for tropical roads"
}' http://10.247.161.4:5000/users_reviews/1/2


curl -X POST -H "Content-Type: application/json" -d '{
  "rating": 4.0,
  "review": "Economical and powerful"
}' http://10.247.161.4:5000/users_reviews/2/1

curl -X POST -H "Content-Type: application/json" -d '{
  "rating": 3.0,
  "review": "Good"
}' http://10.247.161.4:5000/users_reviews/1/2

curl -X POST -H "Content-Type: application/json" -d '{
  "rating": 3.1,
  "review": "Flashy"
}' http://10.247.161.4:5000/users_reviews/1/5


DELETE a review by review id:
-----------------------------
curl -X DELETE http://10.247.161.4:5000/users_trim/<int:review_id>


PUT update a review by review id:
---------------------------------
curl -X PUT http://10.247.161.4:5000/users_trim/<int:user_id>/<int:review_id>


========================================================================
