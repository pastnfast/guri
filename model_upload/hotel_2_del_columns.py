import pandas as pd
import os

def delete_column(col_names):

    BASE_DIR = os.path.dirname(__file__)
    df = pd.read_csv(f'{BASE_DIR}/../dataset/hotel_2_sort_columns.csv')    
    
    # 결측치 존재하는 컬럼 출력
    print( df.isna().sum() )

    df = df.drop(col_names, axis=1)
    print( df.info() )

    # csv로 저장
    df.to_csv(f'{BASE_DIR}/../dataset/hotel_3_removeColumns.csv', index=None)


# 결측치가 많고 중요하지 않아 보이는 컬럼 삭제
# ['agent','company','country','reservation_status_date','reservation_status']
# reservation_status는 타겟 컬럼인 is_canceled와 거의 유사해서 삭제
del_col_names = ['agent','company','country','reservation_status_date','reservation_status', ]
delete_column(del_col_names)


# children 결측치 4건 중앙값으로 대치
# 파이프라인을 사용하면 필요 없음
# df['children'].fillna(df['children'].median(), inplace=True)
# print( '결측치 개수: ', df.isna().sum().sum() )