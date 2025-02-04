from fabric_pipeline.data_pipeline import create_raw_table
from azure_functions.file_upload import upload_file

def test_file_upload():
    """Test if file upload is successful"""
    assert upload_file()

def test_raw_table_creation():
    """Test if raw table is created successfully"""
    assert create_raw_table()
