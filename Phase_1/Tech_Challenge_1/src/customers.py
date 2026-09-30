import pandas as pd

def customers_by_state(customers):
    customers_state = (
        customers.groupby("customer_state")
        .agg(
            total_customers=("customer_unique_id", "nunique")
        )
        .sort_values("total_customers", ascending=False)
    )

    return customers_state

def merge_customers_with_orders(orders, customers):
    orders_customers = orders.merge(
        customers[
            [
                "customer_id",
                "customer_unique_id",
                "customer_state"
            ]
        ],
        on="customer_id",
        how="left"
    )

    return orders_customers

def repurchase_analysis(orders_customers):
    purchases_per_customer = (
        orders_customers.groupby("customer_unique_id")
        .agg(
            total_orders=("order_id", "nunique")
        )
    )

    purchases_per_customer["is_repeat_customer"] = (
        purchases_per_customer["total_orders"] > 1
    )

    return purchases_per_customer

def repurchase_summary(purchases_per_customer):
    total_customers = len(purchases_per_customer)

    repeat_customers = (
        purchases_per_customer["is_repeat_customer"].sum()
    )

    one_time_customers = (
        total_customers - repeat_customers
    )

    repurchase_percentage = (
        repeat_customers / total_customers
    ) * 100

    return (
        total_customers,
        repeat_customers,
        one_time_customers,
        repurchase_percentage
    )