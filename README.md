# 🔗 URL Shortener API

A simple URL Shortener API built with Flask and MySQL that allows users to shorten long URLs with custom or random codes. 

## ✨ Features

- Shorten long URLs with random codes
- Create custom short codes
- Redirect from short code to original URL

## 🛠️ Tech Stack

- Python 3.x
- Flask
- MySQL
- Postman (for testing)

## 📋 Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

## 🚀 Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/AshwinSaklecha/urlShortener.git
    cd urlShortener
    ```

2. **Create Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup MySQL Database**
    ```sql
    CREATE DATABASE url_shortener;
    USE url_shortener;
    CREATE TABLE urls (
        id INT AUTO_INCREMENT PRIMARY KEY,
        long_url TEXT NOT NULL,
        short_code VARCHAR(255) UNIQUE NOT NULL
    );
    ```

5. **Configure Environment Variables**
    Create a `.env` file in the root directory:
    ```plaintext
    MYSQL_HOST=localhost
    MYSQL_USER=root
    MYSQL_PASSWORD=your_mysql_password
    MYSQL_DB=url_shortener
    ```

6. **Run the Application**
    ```bash
    python app.py
    ```

    The server will start at `http://127.0.0.1:5000`

## 🔌 API Endpoints

### 1. Create Short URL
- **Endpoint:** `POST /shorten`
- **Content-Type:** `application/json`
- **Request Body:**
    ```json
    {
        "long_url": "https://example.com/very/long/url",
        "custom_code": "mycode"
    }
    ```
- **Response:**
    ```json
    {
        "long_url": "https://example.com/very/long/url",
        "short_code": "mycode"
    }
    ```

### 2. Access Short URL
- **Endpoint:** `GET /<short_code>`
- **Example:** `http://127.0.0.1:5000/mycode`
- **Response:** Redirects to original URL

## 🧪 Testing with Postman

1. **Create Short URL:**
   - Method: POST
   - URL: `http://127.0.0.1:5000/shorten`
   - Headers: `Content-Type: application/json`
   - Body (raw JSON):
    ```json
    {
        "long_url": "https://youtu.be/example",
        "custom_code": "video123"
    }
    ```

2. **Access Short URL:**
   - Method: GET
   - URL: `http://127.0.0.1:5000/video123`

## ⚠️ Common Issues

1. **Database Connection Error:**
   - Verify MySQL is running
   - Check `.env` credentials
   - Ensure database and table exist

2. **Module Not Found:**
   - Activate virtual environment
   - Run `pip install -r requirements.txt`

3. **Port Already in Use:**
   - Stop other services using port 5000
   - Or modify the port in `app.py`

## 📝 License

MIT License - feel free to use and modify for your projects.
