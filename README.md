Vendor Management System with Performance Metrics:

SET UP ==>
1. Clone the Repo by this command : 
2. Setup a virtual environment:
   You can install venv to your host Python by running this command in your terminal:
     pip install virtualenv
   Run the vitual envoiment in your project by running this commnd in project directory:
     python<version> -m venv <virtual-environment-name>

3. Install all requirments through this command: pip install -r requirements.txt
4. SET UP your own DATABSE in DB else default will be SQLite
5. Migrate models to the DB by these commands:
     python manage.py makemigrations
     python manage.py migrate
6. start the server using: python manage.py runserver and server will get started on http://127.0.0.1:8000/

If any error in packages or migration issue occurs resolve it accodingly.

AUTHENTICATION ==>
  Endpoints to generate tokens and refresh already generated tokens:
  => POST api/token/: 
  => POST api/token/refresh/:

API's ==>
1. Vendor Profile Management: 
    => POST /api/vendors/: Create a new vendor.
    => GET /api/vendors/: List all vendors
    => GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
    => PUT /api/vendors/{vendor_id}/: Update a vendor's details.
    => DELETE /api/vendors/{vendor_id}/: Delete a vendor

2. Purchase Order Tracking:
    => POST /api/purchase_orders/: Create a purchase order.
    => GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
    => GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
    => PUT /api/purchase_orders/{po_id}/: Update a purchase order.
    => DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

3. Update Acknowledgment Endpoint:
    => POST /api/purchase_orders/{po_id}/acknowledge : Endpoint for vendors to acknowledge POs

4. Vendor Performance Evaluation:
   => GET /api/vendors/{vendor_id}/performance/: Retrieve a vendor's performance metrics
