import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
df = pd.read_csv(f'{BASE_DIR}/../dataset/hotel_bookings.csv')
# print( df.info() )
# print( df.head(3) )
# print( df.columns )

print( '컬럼 순서 변경 전 컬럼 개수: ', len(df.columns) )

# 컬럼을 알파벳 순, is_canceled 마지막으로 이동 후 저장
df_new = df.reindex(columns=['adr','adults','agent','arrival_date_day_of_month','arrival_date_month',
                'arrival_date_week_number','arrival_date_year','assigned_room_type','babies',
                'booking_changes','children','company','country','customer_type','days_in_waiting_list',
                'deposit_type','distribution_channel','hotel','is_repeated_guest','lead_time',
                'market_segment','meal','previous_bookings_not_canceled','previous_cancellations',
                'required_car_parking_spaces','reservation_status_date','reservation_status',
                'reserved_room_type','stays_in_week_nights','stays_in_weekend_nights',
                'total_of_special_requests','is_canceled'])

df_new.to_csv(f'{BASE_DIR}/../dataset/hotel_2_sort_columns.csv', index=None)

print( '컬럼 순서 변경 후 컬럼 개수: ', len(df_new.columns) )