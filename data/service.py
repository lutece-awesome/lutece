from os import path, listdir, system
from data.constant import DATA_PATH, INPUT_FILE_EXTENSION, DATA_ZIP_NAME
import zipfile

class DataService:

    @staticmethod
    def get_cases_count( problem_pk ):
        dr = path.join( path.expanduser( DATA_PATH ) , str( problem_pk ) )
        return len( list( filter( lambda x : path.splitext( x )[1] == INPUT_FILE_EXTENSION , listdir( dr ) ) ) )

    @staticmethod
    def create_data_dir( problem_pk ):
        dr = path.join( path.expanduser( DATA_PATH ) , str( problem_pk ) )
        script = f'mkdir {dr} >/dev/null'
        system( script )

    @staticmethod
    def extract_data( problem_pk ):
        dr = path.join( path.expanduser( DATA_PATH ) , str( problem_pk ) )
        with zipfile.ZipFile( path.join( dr , DATA_ZIP_NAME ) ) as zip_file:
            zip_file.extractall( path = dr )

    @staticmethod
    def check_datazip( zip_file ):
        pass