# Charity Chain

A blockchain-based platform for transparent charitable donations and spending tracking.

## Features

- User registration and authentication
- Charity registration and  mm approval system
- Blockchain-based donation tracking
- Transparent spending records for charities
- Admin dashboard for charity management
- Real-time blockchain explorer
- PostgreSQL database integration

## Tech Stack

- Python 3.x
- Flask
- PostgreSQL (via Supabase)
- SQLAlchemy
- Blockchain (Custom Implementation)
- Bootstrap 5
- jQuery

## Prerequisites

- Python 3.x
- PostgreSQL database (provided via Supabase)
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/charity-chain.git
cd charity-chain
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Environment Setup:
   - Create a `.env` file in the project root
   - Add the following environment variables:
   ```
   # Database Configuration
   DATABASE_URL=postgresql://postgres:your_password@your_host:5432/your_database

   # Flask Secret Key (for session management and security)
   SECRET_KEY=your_secret_key

   # Flask Environment
   FLASK_ENV=development
   FLASK_DEBUG=1
   ```

5. Initialize the database:
```bash
flask db upgrade
```

6. Create an admin user:
```bash
python setup_admin.py
```

7. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5001`

## Project Structure

```
charity-chain/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── utils/
├── instance/
├── migrations/
├── requirements.txt
├── run.py
├── setup_admin.py
└── .env
```

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Flask secret key for session management
- `FLASK_ENV`: Application environment (development/production)
- `FLASK_DEBUG`: Debug mode (1 for enabled, 0 for disabled)

## Database Configuration

The application uses PostgreSQL hosted on Supabase. Make sure to:
1. Set up your PostgreSQL database
2. Update the `DATABASE_URL` in your `.env` file
3. Ensure proper database permissions are set

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security Notes

- Never commit the `.env` file to version control
- Use strong, unique passwords for database access
- Keep your `SECRET_KEY` secure and change it in production
- Regularly update dependencies to patch security vulnerabilities

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This is a simulation for educational purposes only. No real cryptocurrencies or funds are involved. 
