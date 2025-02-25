
# Advanced Techniques: Filtering and Faceting

# This program demonstrates advanced filtering and faceting techniques 
# using a sample dataset of products.  We'll simulate a database 
# with a list of dictionaries.

# Sample product data
products = [
    {'id': 1, 'category': 'Electronics', 'brand': 'Apple', 'price': 999, 'color': 'Silver'},
    {'id': 2, 'category': 'Electronics', 'brand': 'Samsung', 'price': 899, 'color': 'Black'},
    {'id': 3, 'category': 'Clothing', 'brand': 'Nike', 'price': 75, 'color': 'Blue'},
    {'id': 4, 'category': 'Clothing', 'brand': 'Adidas', 'price': 65, 'color': 'Red'},
    {'id': 5, 'category': 'Electronics', 'brand': 'Apple', 'price': 1299, 'color': 'Space Gray'},
    {'id': 6, 'category': 'Clothing', 'brand': 'Nike', 'price': 90, 'color': 'Green'},
    {'id': 7, 'category': 'Electronics', 'brand': 'Samsung', 'price': 1099, 'color': 'White'},
    {'id': 8, 'category': 'Books', 'brand': 'Penguin', 'price': 25, 'color': 'NA'},
    {'id': 9, 'category': 'Books', 'brand': 'HarperCollins', 'price': 30, 'color': 'NA'}

]


# Function to filter products based on criteria
def filter_products(products, criteria):
    # criteria is a dictionary where keys are fields and values are the desired values.
    # Example: {'category': 'Electronics', 'brand': 'Apple'}
    filtered_products = []
    for product in products:
        match = True
        for key, value in criteria.items():
            if product.get(key) != value:
                match = False
                break
        if match:
            filtered_products.append(product)
    return filtered_products

# Function to create facets (counts of unique values for a field)
def create_facets(products, field):
    facets = {}
    for product in products:
        value = product.get(field)
        if value is not None:
            facets[value] = facets.get(value, 0) + 1
    return facets


# Example usage: Filtering for Apple Electronics products
filtered_apple_electronics = filter_products(products, {'category': 'Electronics', 'brand': 'Apple'})
print("Apple Electronics Products:", filtered_apple_electronics)


# Example usage: Faceting on the 'category' field
category_facets = create_facets(products, 'category')
print("\nCategory Facets:", category_facets)


# Example usage: Faceting on the 'brand' field, after filtering for Clothing category
clothing_products = filter_products(products, {'category':'Clothing'})
brand_facets_clothing = create_facets(clothing_products, 'brand')
print("\nBrand Facets (Clothing):", brand_facets_clothing)

#Further improvements could include:
# - Handling more complex filtering logic (e.g., range-based filtering on price)
# - Implementing pagination for large datasets
# - Using a more robust data storage mechanism (e.g., a database) instead of a list
# - Adding more sophisticated facetting (e.g., hierarchical facets, range facets)


