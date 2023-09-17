import json


def read_json(file_name, local=False, custom_path=''):
    """
    :param finle_name: filename
    :return: data
    """
    if custom_path:
        base = custom_path
    else:
        if local:
            base = 'C:/Users/Administrator/Desktop/'
        else:
            base = 'database/'
    try:
        f = open(base + file_name + '.json')
        data = json.load(f)
        f.close()
    except Exception as e:
        print(e)
        data = []

    return data


def save_json(data, name, local=False, custom_path=''):
    if custom_path:
        base = custom_path
    else:
        if local:
            base = 'C:/Users/Administrator/Desktop/'
        else:
            base = 'database/'
    jsonString = json.dumps(data)
    jsonFile = open(base + name + '.json', "w")
    jsonFile.write(jsonString)
    jsonFile.close()


def round_any(d, rounded_values=4):
    if type(d) == dict:
        for key in d:
            d[key] = round_any(d[key], rounded_values)
    elif type(d) in [list, set, tuple]:
        for i in range(len(d)):
            d[i] = round_any(d[i], rounded_values)
    else:
        try:
            d = rounded(d, rounded_values=rounded_values)
        except:
            pass
    return d


def rounded(number, n=0, rounded_values=2):
    if number is None:
        return None
    if abs(number) >= 1 or n > 10:
        return round(number / (10 ** n), rounded_values + n)
    else:
        return rounded(number * 10, n + 1, rounded_values)


def list_flatter(listi):
    result = []
    for el in listi:
        if type(el) == list:
            for e in el:
                result.append(e)
        else:
            result.append(el)
    return result
