"""
Простой скрипт с тренировкой модели Random Forest на датасете о качестве вина
"""

import os

import joblib
import pandas as pd
from loguru import logger
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, median_absolute_error

# pylint: disable=invalid-name


def load_data(path: str=os.path.join('data', 'winequality-red.csv')) -> pd.DataFrame:
    """
    Загружает датасет о качестве вина
    """
    # Используем классический датасет о качестве вина из UCI
    data = pd.read_csv(path, sep=",")
    return data

def preprocess_data(data):
    """
    Предобработка данных: разделение на признаки и целевую переменную,
    стандартизация признаков
    """
    # Разделяем на признаки и целевую переменную
    X = data.drop(columns=['quality'])
    y = data['quality']
    return X, y

def split_data(X, y):
    """
    Разделение данных на обучающую и тестовую выборки
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test

def train_model(X_train, X_test, y_train, y_test):
    """
    Обучение модели Random Forest и вывод метрик качества
    """
    # Инициализация и обучение модели
    rf_model = RandomForestRegressor(n_estimators=105, random_state=2)
    rf_model.fit(X_train, y_train)

    # Предсказания на тестовой выборке
    y_pred = rf_model.predict(X_test)

    # Вычисление метрик качества
    mae = mean_absolute_error(y_test, y_pred)
    median_ae = median_absolute_error(y_test, y_pred)

    # Вывод метрик качества
    logger.info(f"Mean Absolute Error: {mae}")
    logger.info(f"Median Absolute Error: {median_ae}")

    metrics = pd.DataFrame({
        "mae": [mae],
        "median_ae": [median_ae]
    })
    metrics.to_csv("metrics.csv", index=False)

    return rf_model


def save_model(model, path="model.joblib") -> None:
    """
    Сохранение модели на диск
    """
    models_dir = "models"
    os.makedirs(models_dir, exist_ok=True)

    model_path = os.path.join(models_dir, path)
    joblib.dump(model, model_path)


def main():
    """
    Основная функция: загрузка данных, предобработка, обучение модели и сохранение
    """

    logger.info("Starting pipeline...")

    # Загрузка данных
    logger.info("Loading data...")
    data = load_data()
    logger.info(f"Dataset shape: {data.shape}")

    # Предобработка
    logger.info("Preprocessing data...")
    X, y = preprocess_data(data)

    # Разделение на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Обучение модели
    logger.info("Training model...")
    model = train_model(X_train, X_test, y_train, y_test)

    # Сохранение модели
    logger.info("Saving model...")
    save_model(model)

    # Завершение работы
    logger.info("Pipeline completed successfully!")

if __name__ == "__main__":
    main()