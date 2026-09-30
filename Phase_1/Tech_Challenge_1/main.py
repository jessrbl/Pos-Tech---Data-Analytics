from src.data_loader import (
    locate_dataset,
    find_csv_files,
    load_datasets
)

#from src.exploratory_analysis import (
#    exploratory_analysis,
#    dataset_diagnosis,
#    analyze_keys,
#    validate_relationships
#)

from src.orders import (
    convert_to_datetime,
    delivery_analysis,
    late_deliveries,
    late_deliveries_by_state
)

from src.customers import (
    customers_by_state,
    merge_customers_with_orders,
    repurchase_analysis,
    repurchase_summary
)

from src.order_items import (
    purchase_volume,
    merge_purchases_with_orders,
    purchase_by_state       
)

def main():
    # Carregamento dos datasets
    dataset_path = locate_dataset()
    csv_files = find_csv_files(dataset_path)
    datasets = load_datasets(*csv_files)

    # Seleção dos datasets
    orders = datasets["olist_orders_dataset"]
    customers = datasets["olist_customers_dataset"]
    order_items = datasets["olist_order_items_dataset"]

    # Tratamento da tabela de pedidos
    orders = convert_to_datetime(orders)
    orders = delivery_analysis(orders)

    # Análises de pedidos
    late_percentage = late_deliveries(orders)

    # Análises de clientes
    customers_state = customers_by_state(customers)

    # Análise dos itens
    purchase_by_order = purchase_volume(order_items)

    # Merges
    orders_customers = merge_customers_with_orders(
        orders,
        customers
    )

    orders_complete = merge_purchases_with_orders(
        orders_customers,
        purchase_by_order
    )

    # Análises cruzadas
    late_by_state = late_deliveries_by_state(orders_customers)

    state_purchases = purchase_by_state(orders_complete)
    
    purchases_per_customer = repurchase_analysis(orders_customers)
    
    
      # Resumo da recompra
    (
        total_customers,
        repeat_customers,
        one_time_customers,
        repurchase_percentage
    ) = repurchase_summary(
        purchases_per_customer
    )


    # Resultados
    print("\n--- DELIVERY ANALYSIS ---")
    print(
        orders[
            ["delivery_days", "delay_days", "is_late"]
        ].describe()
    )

    print(
        f"\nPercentual de pedidos atrasados: "
        f"{late_percentage:.2f}%"
    )

    print("\n--- CUSTOMERS BY STATE ---")
    print(customers_state)

    print("\n--- LATE DELIVERIES BY STATE ---")
    print(late_by_state)

    print("\n--- PURCHASE VOLUME ---")
    print(purchase_by_order.head())

    print("\n--- PURCHASE ANALYSIS BY STATE ---")
    print(state_purchases)
    
    print("\n--- PURCHASES PER CUSTOMER ---")
    print(purchases_per_customer)
    
    print("\n--- REPURCHASE ANALYSIS ---")
    print(f"Total de clientes: {total_customers}")
    print(f"Clientes com uma compra: {one_time_customers}")
    print(f"Clientes recorrentes: {repeat_customers}")
    print(f"Taxa de recompra: {repurchase_percentage:.2f}%")

    print("\n--- ORDERS PER CUSTOMER ---")
    print(
        purchases_per_customer["total_orders"]
        .value_counts()
        .sort_index()
    )


if __name__ == "__main__":
    main()