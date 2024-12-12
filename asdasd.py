import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Suppress TensorFlow INFO/WARNING logs
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # Disable oneDNN optimizations

import yfinance as yf
from datetime import datetime
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import Label, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense, Dropout # type: ignore
from tensorflow.keras.callbacks import EarlyStopping # type: ignore
import tensorflow.keras.backend as K # type: ignore
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
from datetime import datetime
import matplotlib.dates
import mplcursors
import nltk
