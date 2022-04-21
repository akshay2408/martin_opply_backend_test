# Setup of this project

### Note: This Django project is conterize in order to run this application you must have docker as prerequisit.

## Step 1: Build the application
* Create a file with name ".env"
* Add the below credentials into the file (refer the example.env)

| Key | Value |
 ---- | ----- |
| DB_HOST | db_server |
| DB_PASSWORD | postgres |
| DB_USER | postgres|
| DB_NAME | postgres|
| SECRET_KEY | django-insecure-g72)n#y3bg)@c8pw1w=#g@ivbjbfmfvreg*x=-tj&8u2%l$3-s |
* Execute the below docker command to build and the images (use sudo prefix to run it in linux OS environment).
```
docker-compose up --build
```
* This command will build the up the all docker containers.
* In case any error appear after build please quit the process using "Ctrl + d" or "Cmd + d"
* Once server started please open link using http://localhost:8000/

## Step 2: Testing the endpoints
### Note: All the endpoints starts with /api except the admin panel
Only the product list, register and token endpoint does not need any authentication

**POST**

`Register yourself` [http://localhost:8000/api/user/register/] Requires the "username" and "password" <br>
`Get the token` [http://localhost:8000/api/token/] Requires the "username" and "password"<br>
`Create product` [http://localhost:8000/api/products/] <br>
`Place order` [http://localhost:8000/api/products/:pk/place-order/] <br>

**GET**

`Check product list` [http://localhost:8000/api/products/] <br>
`Check customer history` [http://localhost:8000/api/customers/:pk/orders/] <br>
