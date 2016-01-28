def best_stocks(data):
    pairs = []
    data = map(float, data.split())
    
    for i in range(len(data) - 2):
        stock_a = data[i]
        for j in range(i + 2, len(data)):
            stock_b = data[j]
            if stock_b > stock_a:
                pairs.append((stock_a, stock_b))
    
    largest = 0
    for pair in pairs:
        x, y = pair
        profit = y - x
        if profit > largest:
            largest = profit
            big_pair = pair

    return big_pair

if __name__ == "__main__":
    data = '19.35 19.30 18.88 18.93 18.95 19.03 19.00 18.97 18.97 18.98'
    print best_stocks(data)