import pytest

def check_file_upload(func):
    def wrapper(*args, **kwargs):
        print("Checking if the file was uploaded...")
        result = func(*args, **kwargs)
        assert result, "File upload Failed"
        print("File upload Passed")
        return result
    return wrapper


def check_raw_table(func):
    def wrapper(*args, **kwargs):
        print("Checking if raw table was created...")
        result = func(*args, **kwargs)
        assert result, "Raw table creation Failed"
        print("Raw table creation successfull")
        return result
    return wrapper