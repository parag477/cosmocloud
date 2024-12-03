
# Student Management System

A simple **Student Management System** built with **FastAPI** and **MongoDB** for managing student data. This project provides basic CRUD operations for creating, retrieving, updating, and deleting student records.

## Features
- **Create a new student**: Add a student to the database.
- **List students**: Retrieve a list of students with optional filtering by country and minimum age.
- **Get a specific student**: Retrieve student details by ID.
- **Update student**: Update specific fields of a student record.
- **Delete student**: Remove a student from the database.

## Tech Stack
- **Backend**: FastAPI
- **Database**: MongoDB (with Motor for async interaction)
- **Validation**: Pydantic
- **Environment Variables**: dotenv for managing configuration
- **API Documentation**: FastAPI auto-generates Swagger documentation for easy testing.

## Prerequisites
- Python 3.7+
- MongoDB instance (local or hosted on MongoDB Atlas or Render)
- `pip` (Python package manager)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   ```

2. **Set Up Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB**:
   - If using **MongoDB Atlas** or a local MongoDB instance, make sure to update the connection string in `.env` file:
     ```
     MONGODB_URL=mongodb://localhost:27017  # Local MongoDB URL or your MongoDB Atlas URL
     ```

5. **Create `.env` File**:
   - Add your MongoDB connection URL to the `.env` file:
     ```
     MONGODB_URL=your_mongodb_connection_string_here
     ```

6. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   This will start the FastAPI server on `http://127.0.0.1:8000`.

## Endpoints

### 1. **Create a Student** (`POST /students`)
Creates a new student.

**Request body**:
```json
{
  "name": "John Doe",
  "age": 20,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
```

**Response**:
```json
{
  "id": "507f1f77bcf86cd799439011"
}
```

### 2. **List Students** (`GET /students`)
Retrieve a list of students with optional filtering by country and minimum age.

**Query parameters**:
- `country`: Filter by country (optional).
- `age`: Filter by minimum age (optional).

**Response**:
```json
{
  "data": [
    {
      "name": "John Doe",
      "age": 20
    },
    {
      "name": "Jane Smith",
      "age": 22
    }
  ]
}
```

### 3. **Get a Student** (`GET /students/{student_id}`)
Retrieve a specific student by their ID.

**Response**:
```json
{
  "id": "507f1f77bcf86cd799439011",
  "name": "John Doe",
  "age": 20,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
```

### 4. **Update a Student** (`PATCH /students/{student_id}`)
Update the student's information.

**Request body**:
```json
{
  "age": 21,
  "address": {
    "city": "Los Angeles",
    "country": "USA"
  }
}
```

**Response**:
```json
{}
```

### 5. **Delete a Student** (`DELETE /students/{student_id}`)
Delete a student by their ID.

**Response**:
```json
{}
```

## API Documentation
Once the server is running, FastAPI automatically generates interactive API documentation, available at:
- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

## Deployment on Render

1. **Create a New Web Service on Render**:
   - Go to [Render](https://render.com) and create a new web service.
   - Connect your GitHub repository.

2. **Configure the Web Service**:
   - Select the correct branch.
   - Set the **build command**: `pip install -r requirements.txt`.
   - Set the **start command**: `uvicorn main:app --host 0.0.0.0 --port 10000`.

3. **Set Environment Variables**:
   - Go to the **Environment** section and add `MONGODB_URL` with your MongoDB connection string.

4. **Deploy the Application**:
   - After configuring the settings, click on **Create Web Service**.
   - The app will be deployed and a public URL will be provided.

## Testing

You can test the API using tools like **Postman** or **curl** by sending HTTP requests to the endpoints.

## Contributing

Feel free to fork this project and submit pull requests with improvements, bug fixes, or new features. Make sure to follow the coding standards and include relevant tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Author
Your Name or Organization Name
