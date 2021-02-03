# To run: 
Go to project directory
```terminal
python manage.py runserver
```

# To test:
Go to project directory
```terminal
python manage.py test
```
Only tested user creation

## Register:<br />
URL: http://127.0.0.1:8000/api_app/users/ (POST)  <br />
**POST Body**:  <br />
 {  <br />
        "email": "users@user.com",  <br />
        "username": "iamuser", <br />
         "password": "somepass" <br />
} <br />
(registers and creates token)

## Login:<br />
URL: http://127.0.0.1:8000/api_app/login/ (POST)  <br />
**POST Body**:  <br />
 {  <br />
        "email": "users@user.com", (optional) <br />
        "username": "iamuser", <br />
         "password": "somepass" <br />
} <br />
(This gives the token)

## Products:<br /> Only Admin

1. Categories View / Add: http://127.0.0.1:8000/api_app/products/categories/ (GET / POST)  <br />
**POST Body**:  <br />
 {  <br />
        "category_name": "Magical Accessories",  <br />
        "category_detail": "Diagon Alley"  <br />
} <br />
**Header**:<br /> 
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a”<br /> 

2. Brand View / Add: http://127.0.0.1:8000/api_app/products/brands/ (GET / POST)<br />  
**POST Body**:  <br />
 {  <br />
        "brand_name":"Wands",<br />
        "brand_detail":"Magical wands"<br />
}<br />
**Header**:<br /> 
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a”<br /> 

3. Products View / Add: http://127.0.0.1:8000/api_app/products/productsview/ (GET / POST)<br />
**POST Body**:<br />
{<br />
    "name":"Elder wand",<br />
    "description":"This is cool",<br />
    "category":"Magical Accessories",<br />
    "brand":"Wands"<br />
}<br />
**Header**:<br /> 
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a”<br /> 


4. Edit Products : http://127.0.0.1:8000/api_app/products/productsedit/(<)productid) (GET / PATCH / DELETE)<br />
**PATCH Body**:<br />
{<br />
    "name":"my product"  <br />
}<br />
**Header**:<br /> 
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a”<br /> 

6. Edit Category : http://127.0.0.1:8000/api_app/products/categoryedit/(categoryid) (GET / PATCH / DELETE)<br />
**PATCH Body**:<br />
{<br />
   "category_name": "my category"<br />  
}<br /> 
**Header**:<br /> 
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a”<br />   
   

## Cart:<br /> Any user (Customer)

7.	Customer Cart : http://127.0.0.1:8000/api_app/cart/mycart/ (GET / POST)<br /> 
**POST Body**: (creates a cart)<br />  
{}<br /> 
**POST / GET Header**:<br /> 
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a” (Customer token)<br /> 
  

8.	Products in Cart :  http://127.0.0.1:8000/api_app/cart/products-in-cart/ (GET / POST)<br /> 
**POST Body**:<br /> 
{<br /> 
"product":"1", (product id)<br /> 
"at_price":"800"<br /> 
}<br />

**POST/GET Header**:<br /> 
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a” <br />  

9. Update Products in Cart:  http://127.0.0.1:8000/api_app/cart/update-cart-product/(product_id) (PATCH / GET /  DELETE)<br /> 

**PATCH Body**:<br /> 
{<br /> 
    "quantity": 3<br /> 
}<br /> 
    
**PATCH / GET / DELETE Header**:<br /> 
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a”<br /> 


### Note:
The Bonus section of the pre-work is implemented in the products app.
When Product is created with a Brand that is not present, it gets created at the same time.
Same for the Category in Product.

Thanks for having me do this work.
--- Naazneen Jatu
