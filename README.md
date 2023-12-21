Vendor Management System with Performance Metrics:

SET UP ==>
1. Clone the Repo by this command : 
2. Setup a virtual environment:
   You can install Venv to your host Python by running this command in your terminal:
     pip install virtualenv
   Run the virtual environment in your project by running this command in the project directory:
     python<version> -m venv <virtual-environment-name>

3. Install all requirements through this command: pip install -r requirements.txt
4. SET UP your DATABASE in DB else default will be SQLite
5. Migrate models to the DB by these commands:
     python manage.py makemigrations
     python manage.py migrate
6. start the server using: python manage.py runserver and server will get started on http://127.0.0.1:8000/

If any error in packages or migration issue occurs resolve it accordingly.


AUTHENTICATION ==>
create superuser using: python manage.py createsuperuser.

  Endpoints to generate tokens and refresh already generated tokens:
  
  => POST api/token/: when the user provides username and password and gets access_token
  
  => POST api/token/refresh/: The token_refresh is needed when the access_token expires and with the refresh_token user gets new access_token.
  

API's ==>
1. Vendor Profile Management: 
    => POST /api/vendors/: Create a new vendor.  ![POST Vendor](https://github.com/jhanaveenk/VMS/assets/71990959/232484a5-3be2-4704-ba40-2d646ad7bdfc)

    => GET /api/vendors/: List all vendors.  ![GET Vendor](https://github.com/jhanaveenk/VMS/assets/71990959/c06ec76a-5ec8-418a-95ef-f356aa365389)

    => GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details. ![GET Detail Vendor](https://github.com/jhanaveenk/VMS/assets/71990959/4407fd57-146a-416a-8310-d38cfec47f73)

    => PUT /api/vendors/{vendor_id}/: Update a vendor's details. ![PUT Vendor](https://github.com/jhanaveenk/VMS/assets/71990959/b96b655a-c548-4271-b6a3-fee82f35bdfb)

    => DELETE /api/vendors/{vendor_id}/: Delete a vendor. ![DELETE VENDOR](https://github.com/jhanaveenk/VMS/assets/71990959/5446edff-1e36-4d2d-83cc-ae1cccad8490)


3. Purchase Order Tracking:
   
    => POST /api/purchase_orders/: Create a purchase order.
   
    => GET /api/purchase_orders/: List all purchase orders with an option to filter by the vendor.
   
    => GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
   
    => PUT /api/purchase_orders/{po_id}/: Update a purchase order.
   
    => DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

5. Update Acknowledgment Endpoint:
   
    => POST /api/purchase_orders/{po_id}/acknowledge : Endpoint for vendors to acknowledge POs

7. Vendor Performance Evaluation:
   
   => GET /api/vendors/{vendor_id}/performance/: Retrieve a vendor's performance metrics
