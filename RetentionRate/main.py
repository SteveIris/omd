import pandas as pd
import numpy as np


# В решении в папке курса сравнивались 2016 и 2015, а не 2017 и 2016, так что на всякий случай вот это:
FIRST_YEAR = '2016'
SECOND_YEAR = '2017'


def main():
    df_orders = pd.read_csv('orders.csv')
    df_orders['order_month'] = df_orders['order_date'].apply(lambda x: x[5:7])
    df_orders['order_year'] = df_orders['order_date'].apply(lambda x: x[0:4])

    # Чтобы в процессе долго не сравнивать строки в поисках следующего месяца, просто пронумеруем месяцы начиная с
    # января первого года:
    df_orders['order_month_number'] = (df_orders['order_year'].apply(int)-int(FIRST_YEAR))*12 + df_orders['order_month'].apply(int) - 1

    # Уберём все строки с отрицательным номером месяца:
    df_negative = df_orders[df_orders['order_month_number'] < 0]
    df_orders = df_orders.drop(df_negative.index, axis=0)

    # Считаем Retention:
    max_month = df_orders['order_month_number'].max()
    retention = []
    for month in range(max_month):
        df_users_current_month = df_orders.loc[df_orders['order_month_number'].apply(int) == month]['customer_id'].unique()
        current_amount = df_users_current_month.size
        df_users_next_month = df_orders.loc[df_orders['order_month_number'].apply(int) == month+1].loc[df_orders['customer_id'].isin(df_users_current_month)]['customer_id'].unique()
        next_amount = df_users_next_month.size
        retention.append(round(100*next_amount/current_amount, 4))
    print(retention)

    # Посчитаем среднее за каждый год:
    sec_year_start = (int(SECOND_YEAR)-int(FIRST_YEAR))*12
    first_year_mean = round(np.mean(retention[0:12]), 2)
    second_year_mean = round(np.mean(retention[sec_year_start:sec_year_start+12]), 2)
    print(first_year_mean, second_year_mean)

    # Результат для 2016 и 2017:
    # [2.1739, 7.1429, 11.25, 12.0482, 10.4167, 8.8889, 15.7303, 22.093, 10.2273, 20.0, 20.0, 7.6433, 4.4776, 11.3208, 12.1739, 21.1009, 12.3894, 11.8644, 12.7451, 27.8846, 14.7959, 23.5294, 25.0]
    # 12.3 16.12
    # Видим, что в 2017 показатель явно лучше, чем в 2016
    # Кстати, для 2015 и 2016 картина похожая: 9.98 12.3
    # Так что просим руководителя не волноваться.


if __name__ == '__main__':
    main()
