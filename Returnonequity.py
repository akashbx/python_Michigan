import matplotlib.pyplot as plt

def read_csv(filename):
    with open(filename, 'r') as file:
        data = []
        for line in file:
            fields = line.strip().split(',')
            data.append(fields)
    return data

def compute_avg_equity(equity):
    avg_equity = []
    for i in range(len(equity)):
        if i == 0:
            avg = equity[i]
        else:
            avg = (equity[i] + equity[i - 1]) / 2
        avg_equity.append(avg)
    return avg_equity

def clean_and_convert(row):
    """Filter empty strings and convert to float or int as appropriate"""
    return [float(val) if val.strip() != '' else 0.0 for val in row[1:]]

def main():
    filename = input("Enter filename: ")
    data = read_csv(filename)

    try:
        years = [int(val) if val.strip() != '' else 0 for val in data[1][1:]]
        sales = clean_and_convert(data[2])
        net_income = clean_and_convert(data[4])
        total_assets = clean_and_convert(data[6])
        equity = clean_and_convert(data[7])
    except (IndexError, ValueError) as e:
        print("Error while parsing data:", e)
        return

    avg_equity = compute_avg_equity(equity)
    roe_basic = [ni / ae if ae != 0 else 0 for ni, ae in zip(net_income, avg_equity)]

    net_margin = [ni / s if s != 0 else 0 for ni, s in zip(net_income, sales)]
    asset_turnover = [s / ta if ta != 0 else 0 for s, ta in zip(sales, total_assets)]
    financial_leverage = [ta / ae if ae != 0 else 0 for ta, ae in zip(total_assets, avg_equity)]

    roe_dupont = [nm * at * fl for nm, at, fl in zip(net_margin, asset_turnover, financial_leverage)]

    print("\nYear | Basic ROE | DuPont ROE")
    for y, r1, r2 in zip(years, roe_basic, roe_dupont):
        print(f"{y} | {r1:.3f}      | {r2:.3f}")

    plt.figure("Figure 1")
    plt.plot(years, net_income, 'r-', label='Net Income')
    plt.plot(years, avg_equity, 'g-', label='Avg Equity')
    plt.plot(years, roe_basic, 'b-', label='ROE (Basic)')
    plt.title("Net Income, Avg Equity, and Basic ROE")
    plt.legend()

    plt.figure("Figure 2")
    plt.plot(years, sales, label='Sales')
    plt.plot(years, total_assets, label='Total Assets')
    plt.plot(years, net_margin, label='Net Margin')
    plt.plot(years, asset_turnover, label='Asset Turnover')
    plt.plot(years, financial_leverage, label='Financial Leverage')
    plt.plot(years, roe_dupont, label='ROE (DuPont)', linewidth=2)
    plt.title("DuPont ROE Breakdown")
    plt.legend()

    plt.show()

if __name__ == "__main__":

    main()
