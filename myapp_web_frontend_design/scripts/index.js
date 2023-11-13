document.getElementById("myBtn1").addEventListener("click", makes);
        
function makes() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://wwww.codershub/makes</span><br>
<br>This returns a json object for the car makes available.

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/makes/</span>

<br><br>Sample output below: 
<img src="images/makes.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}


document.getElementById("myBtn2").addEventListener("click", makesById);
        
function makesById() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://www.codershub/makes/make_id</span><br>
<br>This returns a json object for the car makes by make id.

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/makes/make_id</span>

<br><br>Sample output below: 
<img src="images/makes_by_id.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}


document.getElementById("myBtn3").addEventListener("click", makeModels);
        
function makeModels() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://www.codershub/make_models</span><br>
<br>This returns a json object for the car models (make_models).

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/make_models</span>

<br><br>Sample output below: 
<img src="images/make_model.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}


document.getElementById("myBtn4").addEventListener("click", makeModelsById);
        
function makeModelsById() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://www.codershub/make_models/make_id</span><br>
<br>This returns a json object for the car models (make_models) by model id.

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/make_models/make_id</span>

<br><br>Sample output below: 
<img src="images/make_models_by_id.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}


document.getElementById("myBtn5").addEventListener("click", trim);
        
function trim() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://www.codershub/make_model_trim</span><br>
<br>This returns a json object for the car Trims (make_model_trims).

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/make_model_trims</span>

<br><br>Sample output below: 
<img src="images/trims.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}



document.getElementById("myBtn6").addEventListener("click", trimByModelId);
        
function trimByModelId() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://www.codershub/make_model_trim/make_model_id</span><br>
<br>This returns a json object for the Trims of a particular model (make_model_trims) by model id.

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/make_model_trim/make_model_id</span>

<br><br>Sample output below: 
<img src="images/trim_by_id.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}


document.getElementById("myBtn7").addEventListener("click", users);
        
function users() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://www.codershub/users</span><br>
<br>This returns a json object for users of all makes.

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/users</span>

<br><br>Sample output below: 
<img src="images/users.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}



document.getElementById("myBtn8").addEventListener("click", usersByTrimId);
        
function usersByTrimId() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://www.codershub/users/trim_id</span><br>
<br>This returns a json object for users of a particular trim by Trim id.

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/users/trim_id</span>

<br><br>Sample output below: 
<img src="images/users_by_trim_id.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}



document.getElementById("myBtn9").addEventListener("click", userReviews);
        
function userReviews() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://www.codershub.tech/users_reviews</span><br>
<br>This returns a json object for user reviews of all makes.

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/users_reviews</span>

<br><br>Sample output below: 
<img src="images/user_reviews.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}



document.getElementById("myBtn10").addEventListener("click", userReviewsByTrim);
        
function userReviewsByTrim() {
document.getElementById("documentations").innerHTML = 
`<p>The CodersHub RESTFul API implements the four major HTTP methods:<br><br>
POST<br>
PUT</br>
GET</br>
DELETE</br>
</p>
<p>
Users or clients of our API are only allowed to use the GET method to fetch resources
from different endpoints.
<br>
Here is the makes endpoint: <br><span style="color: blue; font-weight: bold;
text-decoration: underline;">https://www.codershub.tech/users_reviews/trim_id</span><br>
<br>This returns a json object for user reviews for a particular trim by Trim id.

<br><br>Sample command:<br>
<span style="color: blue; font-weight: bold; text-decoration: underline;">curl -X GET https://www.codershub.tech/users_reviews/trim_id</span>

<br><br>Sample output below: 
<img src="images/usersReviews_by_trim_id.png" width="100%" height="400px" alt="">
</p>
<p>Your result response may be quite different from our post due to regular data update.
`
}