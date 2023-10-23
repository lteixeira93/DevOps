import configparser

from pathlib import Path

cfg_file = '../config/pet_sqa.ini'
cfg_file_dir = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfg_file_dir).joinpath(cfg_file)
print(CONFIG_FILE)

# Reading keys from pet_sqa.ini
config.read(CONFIG_FILE)


def get_pet_api_url():
    return config['pet']['url']


def get_store_api_url():
    return config['pet']['url']


print(get_pet_api_url())
