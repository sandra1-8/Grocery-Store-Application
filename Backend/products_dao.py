from sql_connection import get_sql_connection

def get_all_products(connection):
    
    cursor = connection.cursor()
    query = """
    SELECT 
        p.product_id, 
        p.name, 
        p.uom_id, 
        p.price_per_unit, 
        u.uom_name 
    FROM gs.products p
    INNER JOIN gs.uom u
        ON p.uom_id = u.uom_id;
    """
    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        # print(product_id, name, uom_id, price_per_unit, uom_name)
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    return response

if __name__=='__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))