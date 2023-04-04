from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Define the connection string for the SQL Server database
connection_string = 'DRIVER={SQL Server};SERVER=your_server_name;DATABASE=your_database_name;UID=your_username;PWD=your_password'

# Define the routes for the web app
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    # Connect to the SQL Server database
    conn = pyodbc.connect(connection_string)

    # Retrieve product information from the database
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    # Close the database connection
    conn.close()

    return render_template('shop.html', products=products)

@app.route('/more_info', methods=['POST'])
def more_info():
    # Retrieve the product ID from the form data
    product_id = request.form['product_id']

    # Connect to the SQL Server database
    conn = pyodbc.connect(connection_string)

    # Retrieve the product information from the database
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', product_id)
    product = cursor.fetchone()

    # Close the database connection
    conn.close()

    return render_template('more_info.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
