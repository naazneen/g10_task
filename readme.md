
## Products<br />

## Models are in following Heirarchy<br />
 Category 1 : M Subcategory 1 : M Product 1 : M Attribute <br />

## Views:<br />

1. Categories View / Add: http://127.0.0.1:8000/api_app/products/categories/ (GET / POST)  <br />
**POST Body**:  <br />
 {  <br />
        "category_name": "Magical Accessories",  <br />
        "category_detail": "Diagon Alley"  <br />
} <br />

2. Brand View / Add: http://127.0.0.1:8000/api_app/products/brands/ (GET / POST)<br />  
**POST Body**:  <br />
 {  <br />
        "brand_name":"Wands",<br />
        "brand_detail":"Magical wands"<br />
}<br />

3. Products View / Add: http://127.0.0.1:8000/api_app/products/productsview/ (GET / POST)<br />
**POST Body**:<br />
{<br />
    "name":"Elder wand",<br />
    "description":"This is cool",<br />
    "category":"Magical Accessories",<br />
    "brand":"Wands"<br />
}<br />


4. Edit Products : http://127.0.0.1:8000/api_app/products/productsedit/(<)productid) (GET / PATCH / DELETE)<br />
**PATCH Body**:<br />
{<br />
    "name":"my product"<br />
}<br />

6. Edit Category : http://127.0.0.1:8000/api_app/products/categoryedit/(categoryid) (GET / PATCH / DELETE)<br />
**PATCH Body**:<br />
{<br />
   "category_name": "my category"<br />  
}<br />   
   
7.	Customer Cart : http://127.0.0.1:8000/api_app/cart/mycart/ (GET / POST)  
**POST Body**: (creates a cart)   
{}   
**POST / GET Header**:  
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a” (Customer token)  
  
8.	Products in Cart :  http://127.0.0.1:8000/api_app/cart/products-in-cart/ (GET / POST)   
**POST Body**:   
{  
"product":"myna66709028169" (product id)  
"at_price":"800"  
}  
  
**POST/GET Header**:
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a”   

9. Update Products in Cart:  http://127.0.0.1:8000/api_app/cart/update-cart-product/(product_id) (PATCH / GET /  DELETE)   

**PATCH Body**:   
{  
    "quantity": 3  
}  
    
**PATCH / GET / DELETE Header**:   
Authorization: “token 16e46d02a74cebf37eb4067a4b79c79ccc9a677a”   
