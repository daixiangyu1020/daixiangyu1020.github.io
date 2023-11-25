stop_loss = float(input('止损价:\n'))
entrance = float(input('入场价\n'))
price_exit = float(input('离场价\n'))
rate_risk = entrance - stop_loss
rate_return = entrance - price_exit
r = -(rate_return/rate_risk)
print('R值:\n', f'{r:.2f}')
