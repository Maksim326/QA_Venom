from fabric_pipeline.data_pipeline import create_raw_rable
from azure_functions.file_upload import upload_file

def test_file_upload():
    """
    :return:
    """
    assert upload_file

def test_raw_table_creation():
    assert create_raw_rable