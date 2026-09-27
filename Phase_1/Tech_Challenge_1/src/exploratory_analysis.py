def exploratory_analysis(datasets):

    for name, df in datasets.items():

        print("=" * 60)
        print(f"DATASET: {name}")
        print("=" * 60)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nInfo:")
        df.info()

        print("\nDescribe:")
        print(df.describe(include="all"))

        print("\nMissing values:")
        print(df.isnull().sum())

        print("\nDuplicated rows:")
        print(df.duplicated().sum())


def dataset_diagnosis(datasets):

    for name, df in datasets.items():

        print("=" * 60)
        print(f"DATASET: {name}")
        print("=" * 60)

        print(f"\nLinhas: {df.shape[0]:,}")
        print(f"Colunas: {df.shape[1]}")

        missing = df.isnull().sum().sum()
        print(f"Valores ausentes: {missing:,}")

        duplicated = df.duplicated().sum()
        print(f"Linhas duplicadas: {duplicated:,}")

        print("\nColunas:")
        for column in df.columns:
            print(f" - {column}")

        print()
        
def analyze_keys(datasets):

    print("=" * 60)
    print("ANÁLISE DE CHAVES E RELACIONAMENTOS")
    print("=" * 60)

    # Customers
    customers = datasets["olist_customers_dataset"]

    print("\nCUSTOMERS")
    print(f"Registros: {len(customers):,}")
    print(f"customer_id únicos: {customers['customer_id'].nunique():,}")
    print(f"customer_unique_id únicos: {customers['customer_unique_id'].nunique():,}")

    # Orders
    orders = datasets["olist_orders_dataset"]

    print("\nORDERS")
    print(f"Registros: {len(orders):,}")
    print(f"order_id únicos: {orders['order_id'].nunique():,}")
    print(f"customer_id únicos: {orders['customer_id'].nunique():,}")

    # Order items
    items = datasets["olist_order_items_dataset"]

    print("\nORDER ITEMS")
    print(f"Registros: {len(items):,}")
    print(f"order_id únicos: {items['order_id'].nunique():,}")
    print(f"product_id únicos: {items['product_id'].nunique():,}")
    print(f"seller_id únicos: {items['seller_id'].nunique():,}")

    # Payments
    payments = datasets["olist_order_payments_dataset"]

    print("\nPAYMENTS")
    print(f"Registros: {len(payments):,}")
    print(f"order_id únicos: {payments['order_id'].nunique():,}")

    # Reviews
    reviews = datasets["olist_order_reviews_dataset"]

    print("\nREVIEWS")
    print(f"Registros: {len(reviews):,}")
    print(f"review_id únicos: {reviews['review_id'].nunique():,}")
    print(f"order_id únicos: {reviews['order_id'].nunique():,}")

    # Products
    products = datasets["olist_products_dataset"]

    print("\nPRODUCTS")
    print(f"Registros: {len(products):,}")
    print(f"product_id únicos: {products['product_id'].nunique():,}")

    # Sellers
    sellers = datasets["olist_sellers_dataset"]

    print("\nSELLERS")
    print(f"Registros: {len(sellers):,}")
    print(f"seller_id únicos: {sellers['seller_id'].nunique():,}")
    
def validate_relationships(datasets):

    print("=" * 60)
    print("VALIDAÇÃO DOS RELACIONAMENTOS")
    print("=" * 60)

    customers = datasets["olist_customers_dataset"]
    orders = datasets["olist_orders_dataset"]
    items = datasets["olist_order_items_dataset"]
    payments = datasets["olist_order_payments_dataset"]
    reviews = datasets["olist_order_reviews_dataset"]
    products = datasets["olist_products_dataset"]
    sellers = datasets["olist_sellers_dataset"]

    # Orders → Customers
    missing_customers = ~orders["customer_id"].isin(customers["customer_id"])

    print("\nORDERS → CUSTOMERS")
    print(f"Pedidos sem customer correspondente: {missing_customers.sum():,}")

    # Order Items → Orders
    missing_orders_items = ~items["order_id"].isin(orders["order_id"])

    print("\nORDER ITEMS → ORDERS")
    print(f"Itens sem pedido correspondente: {missing_orders_items.sum():,}")

    # Order Items → Products
    missing_products = ~items["product_id"].isin(products["product_id"])

    print("\nORDER ITEMS → PRODUCTS")
    print(f"Itens sem produto correspondente: {missing_products.sum():,}")

    # Order Items → Sellers
    missing_sellers = ~items["seller_id"].isin(sellers["seller_id"])

    print("\nORDER ITEMS → SELLERS")
    print(f"Itens sem vendedor correspondente: {missing_sellers.sum():,}")

    # Payments → Orders
    missing_orders_payments = ~payments["order_id"].isin(orders["order_id"])

    print("\nPAYMENTS → ORDERS")
    print(f"Pagamentos sem pedido correspondente: {missing_orders_payments.sum():,}")

    # Reviews → Orders
    missing_orders_reviews = ~reviews["order_id"].isin(orders["order_id"])

    print("\nREVIEWS → ORDERS")
    print(f"Avaliações sem pedido correspondente: {missing_orders_reviews.sum():,}")