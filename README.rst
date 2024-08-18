=========================
Django File Read/Write API
=========================

This Django application provides API endpoints to read from and write to text files stored on the server. It uses Django REST Framework to handle HTTP requests.

Installation
============

1. To install this package, you can use `pip`:

   .. code-block:: bash

      pip install git+https://github.com/Mdmanish/file-stream.git@master#egg=file_stream&subdirectory=dist/file_stream-0.1.0.tar.gz

2. Add the app to your Django project's `INSTALLED_APPS` in `settings.py`:

   .. code-block:: python

      INSTALLED_APPS = [
          ...
          'file_stream',
      ]

3. Include the app's URLs in your project's `urls.py`:

   .. code-block:: python

      from django.urls import path, include

      urlpatterns = [
          ...
          path('api/', include('file_stream.urls')),
      ]

Usage
=====

This app provides the following API endpoints:

1. **GET /api/file/**

   Reads the content of a specified file.

   **Query Parameters:**
   - `filename` (required): The name of the file to be read.

   **Response:**
   - `200 OK`: Returns the file content.
   - `400 Bad Request`: If the filename is not provided or the file does not exist.
   - `500 Internal Server Error`: If an error occurs while reading the file.

   **Example Request:**

   .. code-block:: bash

      curl -X GET "http://localhost:8000/api/file/?filename=example.txt"

   **Example Response:**

   .. code-block:: json

      {
          "content": "File content here"
      }

2. **POST /api/file/**

   Creates or overwrites a file with the specified content.

   **Request Body:**
   - `filename` (required): The name of the file to create.
   - `content` (required): The content to write to the file.

   **Response:**
   - `201 Created`: If the file is created or updated successfully.
   - `400 Bad Request`: If the request data is invalid.
   - `500 Internal Server Error`: If an error occurs while writing the file.

   **Example Request:**

   .. code-block:: bash

      curl -X POST "http://localhost:8000/api/file/" -H "Content-Type: application/json" -d '{
          "filename": "example.txt",
          "content": "Hello, world!"
      }'

   **Example Response:**

   .. code-block:: json

      {
          "message": "File 'example.txt' created successfully."
      }

Contributing
============

Feel free to fork this repository and submit pull requests with improvements or bug fixes.

License
=======

This project is licensed under the MIT License.
