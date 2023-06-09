### notes_app
#Description
#This project is a web application built using Django Rest Framework (DRF) on the backend
#and React.js on the frontend. The purpose of this application is to provide a seamless integration 
#between the two technologies and create a robust and responsive web application.

Installation
------------
Install from **pip**:

.. code-block:: sh

        pip install django
        pip install django
.. code-block:: sh

    python -m pip install django-cors-headers

and then add it to your installed apps:

.. code-block:: python

    INSTALLED_APPS = [
        ...,
        "corsheaders",
        ...,
    ]
