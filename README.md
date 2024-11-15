Here's the formatted content for your README.md file that you can copy directly into your GitHub repository:

markdown
# URL Shortener

A simple **URL Shortener** API built using **Flask** and **MySQL** that allows users to shorten long URLs and also provides the option to customize the short link.

## Features

- Shorten long URLs with a random short code.
- Customize short codes instead of using randomly generated ones.
- Redirect from the short code back to the original long URL.

## Technologies Used

- **Flask** - Web framework for Python.
- **MySQL** - Database for storing long URLs and their corresponding short codes.
- **Postman** - Used to test the API endpoints.
- **Python 3** - The version of Python required to run the project.

## Prerequisites

- **Python 3.x** installed on your system.
- **MySQL** database server.
- **MySQL Workbench** (optional, for managing your MySQL database via GUI).

## Setup and Installation

### 1. Clone the Repository
Clone this repository to your local machine:

bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener


### 2. Create and Activate Virtual Environment (Optional but recommended)

- **Windows**:
    bash
    python -m venv venv
    venv\Scripts\activate
    
  
- **Mac/Linux**:
    bash
    python3 -m venv venv
    source venv/bin/activate
    

### 3. Install Dependencies
Install required Python packages using pip:

bash
pip install -r requirements.txt


### 4. Setup MySQL Database
Create a database named `url_shortener` in MySQL:

sql
CREATE DATABASE url_shortener;


Inside the `url_shortener` database, create a table to store URLs:

sql
CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    long_url TEXT NOT NULL,
    short_code VARCHAR(255) UNIQUE NOT NULL
);


### 5. Configure MySQL Connection
Open the `app.py` file and configure the MySQL connection:

python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # MySQL username (default: root)
app.config['MYSQL_PASSWORD'] = 'your_password'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'url_shortener'  # Database name


### 6. Run the Flask Application
Run the Flask app:

bash
python app.py


The application will start on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## API Endpoints

### 1. POST /shorten
Shortens a given long URL.

#### Request Body (JSON):
json
{
  "long_url": "https://example.com",
  "custom_code": "example1"
}


- `long_url`: The long URL that you want to shorten.
- `custom_code`: (Optional) The custom short code you want to use. If not provided, a random short code is generated.

#### Response:
json
{
  "long_url": "https://example.com",
  "short_code": "example1"
}


#### Error Response:
json
{
  "error": "Custom code already in use"
}


### 2. GET /<short_code>
Redirects to the long URL associated with the given short code.

Example:

- URL: [http://127.0.0.1:5000/example1](http://127.0.0.1:5000/example1)
- Will redirect to: https://example.com

#### Error Response:
json
{
  "error": "URL not found"
}


## Testing the API
You can use **Postman** to test the endpoints.

1. **POST** request to `/shorten` with a long URL.
2. **GET** request to `/<short_code>` to test the redirection.

## Contributing
Feel free to fork this repository and submit pull requests for any enhancements or bug fixes. Please ensure that your code follows the Python style guide (PEP 8).

## License
This project is licensed under the MIT License - see the LICENSE file for details.


### Instructions for Use:
1. Copy and paste the above content into your README.md file.
2. Make sure you replace the placeholder https://github.com/your-username/url-shortener.git with the actual repository URL once it's available.