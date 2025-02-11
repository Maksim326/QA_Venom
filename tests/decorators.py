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

#Data Pipeline	EVENT HUB	 	 	Testing framework
 	 	 	launch strategy	Trigger through fabric schedule
 	 	 	 	place the files in test path
file gets dropped at test path	 	 	 	 
file dropped event has been created	 	 	 	 
correlation ID	 	get corelation ID based on file path in the event hub	 	 
file path	 	 	 	 
Azure funtion initiatead with	 	 	 	 
correlation ID	 	 	 	 
file path	azure file movement event	 	 	 
config.json	 	get event for the corelation ID	 	run the  tests for the azure funtions
 	 	 	 	 
raw table load	 	 	 	 
correlation ID	publish event with raw table load	 	 	 
file path	 	get event for the corelation ID	 	 
 	 	 	 	run the tests for the raw table load
