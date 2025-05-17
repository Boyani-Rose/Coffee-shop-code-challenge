# Coffee-shop-code-challenge

# Coffee Shop Domain Modeling

## Overview
This Python application models a Coffee Shop using object-oriented principles. It includes three main classes: `Customer`, `Coffee`, and `Order`.

## Features
- Customers can place multiple orders.
- Coffees can have many orders.
- Orders belong to one customer and one coffee.
- Includes aggregate methods and relationships.
- Input validation with error handling.
- A `debug.py` file for interactive testing.

## Setup
1. Create and activate the virtual environment:
   ```bash
   pipenv install
   pipenv shell
   pipenv install pytest

2. Run the debug script:

bash
Copy code
python debug.py

Project Structure

coffee_shop/

customer.py — Contains the Customer class.

coffee.py — Contains the Coffee class.

order.py — Contains the Order class.

debug.py — For testing functionality.

Author
Rose Momanyi– Coffee Shop Domain Modeling Project – 2025