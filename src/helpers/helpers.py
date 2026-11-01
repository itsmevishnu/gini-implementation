def check_csv(file_path: str) -> bool:
    if file_path.endswith('csv'):
        return True
    else:
        raise Exception("File is not CSV format. Abort")

def remove_outliers(data: list) -> list :
    pass

