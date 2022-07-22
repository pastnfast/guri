import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
df = pd.read_csv(f'{BASE_DIR}/../dataset/hotel_3_removeColumns.csv')
X = df.iloc[:,:-1]
y = df.iloc[:,[-1]] # 파이프라인이 2차원 행렬 요구

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import joblib 

# 수치형 변수: SimpleImputer 결측치는 중앙값으로 대치 & 정규화
numeric_features = ['adr','adults','arrival_date_day_of_month','arrival_date_week_number','arrival_date_year','babies','booking_changes','children','days_in_waiting_list','is_repeated_guest','lead_time','previous_bookings_not_canceled','previous_cancellations','required_car_parking_spaces','stays_in_week_nights','stays_in_weekend_nights','total_of_special_requests']
numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])

# 범주형 변수: 원핫인코딩
categorical_features = ['arrival_date_month','assigned_room_type','customer_type','deposit_type','distribution_channel','hotel','market_segment','meal','reserved_room_type']
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ('numerical', numeric_transformer, numeric_features),
        ('categorical', categorical_transformer, categorical_features),
    ]
)

# 모델 파라미터 적용
xgb = XGBClassifier(booster='gbtree', eval_metric='logloss', use_label_encoder=False,
                   max_depth=6, learning_rate=0.1, n_estimators=100, n_jobs=-1)

# 전처리 후 모델 fit
clf = Pipeline( steps=[("preprocessor", preprocessor), ("classifier", xgb)] )

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

clf.fit(X_train, y_train)

# 정확도 train, test
print("train model score: %.3f" % clf.score(X_train, y_train))
print("test model score: %.3f" % clf.score(X_test, y_test))

# classification report
print( classification_report(y_test, clf.predict(X_test)) )

# 모델 저장

file_name = f'{BASE_DIR}/../trained_models/xgb.pkl' 
joblib.dump(xgb, file_name)