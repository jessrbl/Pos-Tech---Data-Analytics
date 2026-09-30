import pandas as pd


def purchase_volume(order_items):
    purchase_by_order = (
        order_items.groupby("order_id")
        .agg(
            total_items=("order_item_id", "count"),
            total_price=("price", "sum"),
            total_freight=("freight_value", "sum")
        )
    )

    purchase_by_order["total_value"] = (
        purchase_by_order["total_price"]
        + purchase_by_order["total_freight"]
    )

    purchase_by_order["freight_percentage"] = (
        purchase_by_order["total_freight"]
        / purchase_by_order["total_price"]
    ) * 100

    return purchase_by_order

def merge_purchases_with_orders(orders_customers, purchase_by_order):
    orders_complete = orders_customers.merge(
        purchase_by_order,
        on="order_id",
        how="left"
    )

    return orders_complete

def purchase_by_state(orders_complete):
    state_purchases = (
        orders_complete.groupby("customer_state")
        .agg(
            total_orders=("order_id", "nunique"),
            total_sales=("total_price", "sum"),
            total_freight=("total_freight", "sum"),
            average_order_value=("total_price", "mean"),
            average_freight=("total_freight", "mean")
        )
    )

    state_purchases["freight_percentage"] = (
        state_purchases["total_freight"]
        / state_purchases["total_sales"]
    ) * 100

    return state_purchases.sort_values(
        "total_sales",
        ascending=False
    )