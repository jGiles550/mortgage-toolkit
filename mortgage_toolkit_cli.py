import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from utils import *
import argparse


def get_mo_pmt_cash2close(base_price, starting_rate, desired_rate, down_pmt_percent):
    
    down_payment                = get_down_payment(base_price, down_pmt_percent)
    loan_amt                    = get_loan_amount(base_price, down_payment)
    loan_amt                    = loan_amt + DESIGN_CENTER

    monthly_interest_rate       = get_monthly_interest_rate(desired_rate)
    monthly_taxes               = get_monthly_taxes(base_price)
    monthly_mortgage_insurance  = get_monthly_mortgage_insurance(loan_amt)

    monthly_payment             = get_monthly_mortgage_payment(LOAN_TERM_YRS, 
                                                               desired_rate, 
                                                               loan_amt)

    rate_buy_down               = interest_rate_buy_down(desired_rate, 
                                                         starting_rate, 
                                                         loan_amt)
    
    total_cash_to_close         = rate_buy_down + down_payment

    total_mo_payment            = ( monthly_interest_rate +
                                    monthly_taxes +
                                    monthly_mortgage_insurance +
                                    monthly_payment +
                                    HOMEOWNERS_INSURANCE +
                                    HOA_FEES )  

    return total_mo_payment, total_cash_to_close


def plot_mortgage(starting_rate, desired_rate, down_payment_percent,save_fig=False):

    base_price_lst = [400e3 + 25e3 * i for i in range(20)]
    side_bar_txt = f'STARTING RATE={starting_rate}\nDESIRED RATE={desired_rate}\nDOWNPAYMENT={down_payment_percent}%'

    x = np.linspace(base_price_lst[0], base_price_lst[-1], len(base_price_lst))
    mp, c2c = get_mo_pmt_cash2close(x, starting_rate, desired_rate, down_payment_percent)
    # c2c = get_mo_payment_and_cash_to_close(x, interest_rate, down_payment_percent)[1]

    plt.style.use('dark_background')
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(x, mp, '-r', label=f'Monthly Payment')
    ax1.set_ylabel('Monthly Payment ', color='r')
    ax1.set_xlabel('Base Price ')
    ax1.tick_params('y', colors='r')
    ax1.set_ylim(1000,10000)

    ax2 = ax1.twinx()
    ax2.plot(x, c2c, '-b', label=f'Cash2Close')
    ax2.set_ylabel('Cash2Close', color='b')
    ax2.tick_params('y', colors='b')
    ax2.set_ylim(10000,100000)

    ax1.legend(loc='upper left', bbox_to_anchor=(0, 1))
    ax2.legend(loc='upper left', bbox_to_anchor=(0, 0.9))

    plt.title('Mortgage Payment Calculator')
    plt.xlabel('Base Price [$]')
    plt.grid(True)

    plt.subplots_adjust(right=0.75)
    fig.text(0.83, 0.8, side_bar_txt, fontsize=10,bbox=dict(linewidth=2, alpha=0.5))

    plt.show()
    if save_fig:
        plt.savefig(f'mortgage_toolkit_cli_sr{starting_rate}_dr{desired_rate}_dp{down_payment_percent}.png')
    plt.close()


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Welcome to the Mortgage Toolkit!")

    parser.add_argument('bp', type=float, help="Base price of the home")
    parser.add_argument('sr', type=float, help="Starting rate (APR) of the market")
    parser.add_argument('dr', type=float, help="Desired rate (APR). The rate to buy down to")
    parser.add_argument('dp', type=int, help="Down payment in percent")
    parser.add_argument('--plot', action='store_true', help="Return a twin axes plot. ")
    parser.add_argument('--save_plot', action='store_true', help="Save the plot")
    args = parser.parse_args()

    
    if args.plot:
        try:
            plot_mortgage(args.sr,args.dr,args.dp)

        except Exception as ex:
            print(f">>>EXCEPTION: {ex}")
            print(f">>>IF RUNNING COMPILED APP, TRY --save_plot")
            
    elif args.save_plot:
        matplotlib.use('Agg')
        plot_mortgage(args.sr,args.dr,args.dp,True)
        


    total_monthly_pmt, total_cash2close = get_mo_pmt_cash2close(args.bp,args.sr,args.dr,args.dp)
    print('\n')
    print(f'# BASE PRICE = {args.bp}')
    print(f'# STARTING RATE = {args.sr}')
    print(f'# DESIRED RATE = {args.dr}')
    print(f'# DOWN PAYMENT PERCENT = {args.dp}')
    print(f'>>> TOTAL MONTHLY PAYEMENT = {total_monthly_pmt}')
    print(f'>>> TOTAL CASH TO CLOSE = {total_cash2close}')


    
if __name__ == '__main__':
    main()



