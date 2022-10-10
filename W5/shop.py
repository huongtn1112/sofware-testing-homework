#chuong trinh chua sua loi
def get_product_reviews(price, ratio):
    # 1: nhu cầu thấp, 2: nhu cầu trung bình, 3: nhu cầu cao
    s = ""
    try:
        if ratio < 0 or ratio > 100 or price > 1000:
            return "Invalid in"
        else:
            if 50 <= price <= 1000:
                s += "a, "
            else:
                s += "b, "
            if ratio <= 20:
                s += "1"
            elif ratio <= 70:
                s += "2"
            else:
                s += "3"

    except:
        return "Invalid in"
    return s


if __name__ == '__main__':
    print(get_product_reviews(0, 50))
