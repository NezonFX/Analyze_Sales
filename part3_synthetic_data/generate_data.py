import argparse
import sys
import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class InvalidConfigError(Exception):
    pass

def generate_data(seed: int, years: int, num_stores: int, output_path: str) -> pd.DataFrame:
    if years <= 0:
        raise InvalidConfigError("Количество лет должно быть больше нуля.")
    if num_stores < 5:
        raise InvalidConfigError("Количество магазинов должно быть не менее 5.")
    
    np.random.seed(seed)
    
    cities = ['Минск', 'Брест', 'Гомель', 'Гродно', 'Могилев']
    store_ids = [f"ST_{i:03d}" for i in range(1, num_stores + 1)]
    store_city_map = {store: np.random.choice(cities) for store in store_ids}
    
    categories = {
        'Электроника': ['Смартфон', 'Ноутбук', 'Наушники'],
        'Одежда': ['Футболка', 'Джинсы', 'Куртка'],
        'Продукты': ['Хлеб', 'Молоко', 'Сыр']
    }
    products = [(cat, prod) for cat, prods in categories.items() for prod in prods]
    
    start_date = datetime(2021, 1, 1)
    end_date = start_date + timedelta(days=365 * years - 1)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    records = []
    
    for date in dates:
        is_weekend = date.weekday() >= 5
        day_of_year = date.dayofyear
        seasonality = np.sin(2 * np.pi * day_of_year / 365)
        
        for store in store_ids:
            for cat, prod in products:
                base_price = np.random.uniform(500, 50000) if cat == 'Электроника' else \
                             np.random.uniform(500, 5000) if cat == 'Одежда' else \
                             np.random.uniform(50, 500)
                
                trend = np.random.uniform(-0.0001, 0.0002) * (date - start_date).days
                
                season_mult = 1.5 if is_weekend else 1.0
                if cat == 'Одежда':
                    season_mult *= (1 + 0.3 * seasonality)
                elif cat == 'Продукты':
                    season_mult *= (1 - 0.2 * seasonality)
                
                is_promo = np.random.rand() < 0.1
                promo_discount = 0.8 if is_promo else 1.0
                
                price = base_price * (1 + trend) * promo_discount * np.random.uniform(0.95, 1.05)
                qty_base = np.random.poisson(5) * season_mult
                qty = int(qty_base * (1.5 if is_promo else 1.0))
                
                if qty == 0:
                    continue
                
                cost = price * np.random.uniform(0.5, 0.8)
                
                payment = np.random.choice(['наличные', 'карта', 'онлайн'], p=[0.2, 0.5, 0.3])
                
                records.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'store_id': store,
                    'city': store_city_map[store],
                    'category': cat,
                    'product': prod,
                    'qty': qty,
                    'price': round(price, 2),
                    'cost': round(cost, 2),
                    'promo': int(is_promo),
                    'payment_method': payment
                })
    
    df = pd.DataFrame(records)
    num_outliers = int(len(df) * 0.01)
    outlier_indices = np.random.choice(df.index, num_outliers, replace=False)
    df.loc[outlier_indices, 'qty'] = df.loc[outlier_indices, 'qty'] * 10
    
    num_missing = int(len(df) * 0.005)
    missing_price_indices = np.random.choice(df.index, num_missing, replace=False)
    df.loc[missing_price_indices, 'price'] = np.nan
    
    missing_pay_indices = np.random.choice(df.index, num_missing, replace=False)
    df.loc[missing_pay_indices, 'payment_method'] = np.nan
    
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Данные сохранены в {output_path} (строк: {len(df)})")
    return df

def main():
    parser = argparse.ArgumentParser(description="Генератор синтетических данных о продажах.")
    parser.add_argument('--seed', type=int, default=42, help="Сид для воспроизводимости")
    parser.add_argument('--years', type=int, default=3, help="Количество лет")
    parser.add_argument('--stores', type=int, default=5, help="Количество магазинов (мин. 5)")
    parser.add_argument('--out', type=str, default='data/sales.csv', help="Путь для сохранения CSV")
    
    args = parser.parse_args()
    
    try:
        generate_data(args.seed, args.years, args.stores, args.out)
    except InvalidConfigError as e:
        print(f"Ошибка конфигурации: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()