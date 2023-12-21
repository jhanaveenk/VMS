Vendor Management System with Performance Metrics:

SET UP ==> 
   ```bash 
   git clone https://github.com/jhanaveenk/VMS.git 
   ```

1. Clone the Repo by this command :
2. Setup a virtual environment:
   You can install Venv to your host Python by running this command in your terminal:

   ```bash
   pip install virtualenv
   ```
   Run the virtual environment in your project by running this command in the project directory:
   ```bash
   python<version> -m venv <virtual-environment-name>
   ```
   


3. Install all requirements through this command: pip install -r requirements.txt
4. SET UP your DATABASE in DB else default will be SQLite
5. Migrate models to the DB by these commands:
  ```bash
   python manage.py makemigrations
   python manage.py migrate
  ```
6. start the server using: python manage.py runserver and server will get started on http://127.0.0.1:8000/

If any error in packages or migration issue occurs resolve it accordingly.

AUTHENTICATION ==>
create superuser using: python manage.py createsuperuser.

Endpoints to generate tokens and refresh already generated tokens:

=> POST api/token/: when the user provides username and password and gets access_token. ![Token Geneeration](https://github.com/jhanaveenk/VMS/assets/71990959/dc4a3b9c-1b0d-43aa-8304-18afda4324bb)

=> POST api/token/refresh/: The token_refresh is needed when the access_token expires and with the refresh_token user gets new access_token. ![Refresh Token](https://github.com/jhanaveenk/VMS/assets/71990959/d91eb370-681b-4e79-8123-2d06bdce53e5)

API's ==>

1. Vendor Profile Management:
   => POST /api/vendors/: Create a new vendor. ![POST Vendor](https://github.com/jhanaveenk/VMS/assets/71990959/232484a5-3be2-4704-ba40-2d646ad7bdfc)

   => GET /api/vendors/: List all vendors. ![GET Vendor](https://github.com/jhanaveenk/VMS/assets/71990959/c06ec76a-5ec8-418a-95ef-f356aa365389)

   => GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details. ![GET Detail Vendor](https://github.com/jhanaveenk/VMS/assets/71990959/4407fd57-146a-416a-8310-d38cfec47f73)

   => PUT /api/vendors/{vendor_id}/: Update a vendor's details. ![PUT Vendor](https://github.com/jhanaveenk/VMS/assets/71990959/b96b655a-c548-4271-b6a3-fee82f35bdfb)

   => DELETE /api/vendors/{vendor_id}/: Delete a vendor. ![DELETE VENDOR](https://github.com/jhanaveenk/VMS/assets/71990959/5446edff-1e36-4d2d-83cc-ae1cccad8490)

2. Purchase Order Tracking:

   => POST /api/purchase_orders/: Create a purchase order. ![PO POST 1](https://github.com/jhanaveenk/VMS/assets/71990959/c6f1e905-d778-4738-be36-8d654da626db) ![PO POST 2](https://github.com/jhanaveenk/VMS/assets/71990959/0f78315f-566b-42c0-bdb9-de5fc8215e90)

   => GET /api/purchase_orders/: List all purchase orders with an option to filter by the vendor. ![PO GET 1](https://github.com/jhanaveenk/VMS/assets/71990959/a8b8187e-7318-457c-b98e-f0b883062423) ![PO GET 2](https://github.com/jhanaveenk/VMS/assets/71990959/08c3edcb-2714-4c1b-a96f-834aa3759c5d)

   => GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order. ![Screenshot (55)](https://github.com/jhanaveenk/VMS/assets/71990959/11e6764f-9023-4990-82de-2575afd02db5)

   => PUT /api/purchase_orders/{po_id}/: Update a purchase order. ![PO PATCH 1](https://github.com/jhanaveenk/VMS/assets/71990959/98d2a32a-d9f6-4cb7-949a-9bf146f4279c)
   ![PO PATCH 2](https://github.com/jhanaveenk/VMS/assets/71990959/088ddc3b-c9ac-445e-b66b-cd23cfa9c915)

   => DELETE /api/purchase_orders/{po_id}/: Delete a purchase order. ![DELETE PO](https://github.com/jhanaveenk/VMS/assets/71990959/c7b70b83-65ac-4e6e-b79d-f0ed45f7026b)

3. Update Acknowledgment Endpoint:

   => POST /api/purchase_orders/{po_id}/acknowledge : Endpoint for vendors to acknowledge POs. ![Acknowledgment Endpoint](https://github.com/jhanaveenk/VMS/assets/71990959/306910d1-a053-4e6f-9966-7f838fcb2b74)

4. Vendor Performance Evaluation:

   => GET /api/vendors/{vendor_id}/performance/: Retrieve a vendor's performance metrics ![Performance Metrics](https://github.com/jhanaveenk/VMS/assets/71990959/99bd362b-daa3-4d59-b5cf-3824a045b803)
