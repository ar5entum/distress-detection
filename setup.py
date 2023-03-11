from kaggle.api.kaggle_api_extended import KaggleApi
import os
os.system('pip install -r requirements.txt')

# !pip install -r requirements.txt #uncomment and run instead if the above command doesn't work

# https://github.com/Kaggle/kaggle-api

# os.environ['KAGGLE_USERNAME'] = 'YOUR_USERNAME'
# os.environ['KAGGLE_KEY'] = 'YOUR_KEY'

api = KaggleApi()
api.authenticate()

print('Downloading datasets...')
api.dataset_download_files(
    'wcukierski/enron-email-dataset', path='datasets', unzip=True)
api.dataset_download_files(
    'mrmorj/hate-speech-and-offensive-language-dataset', path='datasets', unzip=True)
api.dataset_download_files(
    'rajathmc/cornell-moviedialog-corpus', path='datasets', unzip=True)
print('Setup complete, exitted successfully')
