import pandas


def read_excel_to_list(excel_path,sheet_name):
    data = pandas.read_excel(excel_path, sheet_name=sheet_name,engine='openpyxl')
    dict_list = data.to_dict(orient='records')
    return dict_list

if __name__ == "__main__":
    dict_list = read_excel_to_list(r"E:\PycharmProjects\web_framwork\testcases\select_user.xlsx","select_user")
    for data in dict_list:
        print(data)
