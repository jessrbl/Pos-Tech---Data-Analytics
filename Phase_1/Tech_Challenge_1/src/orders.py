import pandas as pd


def convert_to_datetime(orders):
    orders["order_purchase_timestamp"] = pd.to_datetime(
        orders["order_purchase_timestamp"], errors="coerce"
    )
    orders["order_approved_at"] = pd.to_datetime(
        orders["order_approved_at"], errors="coerce"
    )
    orders["order_delivered_carrier_date"] = pd.to_datetime(
        orders["order_delivered_carrier_date"], errors="coerce"
    )
    orders["order_delivered_customer_date"] = pd.to_datetime(
        orders["order_delivered_customer_date"], errors="coerce"
    )
    orders["order_estimated_delivery_date"] = pd.to_datetime(
        orders["order_estimated_delivery_date"], errors="coerce"
    )
    return orders


def delivery_analysis(orders):
    orders["order_month"] = orders["order_purchase_timestamp"].dt.to_period("M")
    orders["delivery_days"] = (
        orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]
    ).dt.days
    orders["delay_days"] = (
        orders["order_delivered_customer_date"] - orders["order_estimated_delivery_date"]
    ).dt.days
    orders["is_late"] = orders["delay_days"] > 0
    return orders

def late_deliveries(orders):
    late_percentage = orders["is_late"].mean() * 100

    return late_percentage

def late_deliveries_by_state(orders_customers):
    late_orders = orders_customers[
        orders_customers["is_late"]
    ]

    late_by_state = (
        orders_customers.groupby("customer_state")
        .agg(
            total_orders=("order_id", "nunique"),
            late_orders=("is_late", "sum"),
            late_percentage=("is_late", "mean")
        )
    )

    late_by_state["late_percentage"] *= 100

    average_delay = (
        late_orders.groupby("customer_state")["delay_days"]
        .mean()
    )

    late_by_state["average_delay"] = average_delay

    return late_by_state.sort_values(
        "late_percentage",
        ascending=False
    )