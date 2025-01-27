# Bookify

### Project setup

- Clone the repository and open the terminal from the root directory of the project

- Make a virtual environment
  ```
  python3 -m venv venv
  ```
- Activate the environment
  on linux:
  ```
  source venv/bin/activate
  ```
  on windows:
  ```
  venv\Scripts\activate
  ```
- Install packages in `requirements.txt` in the venv you created
  ```
  pip install -r requirements.txt
  ```
- Run the application
  ```
  python3 manage.py runserver
  ```
- Now, the application is running at at http://127.0.0.1:8000/
- You can route to http://127.0.0.1:8000/swagger/ to open API documentation and interact with it
