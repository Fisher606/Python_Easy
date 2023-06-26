from ATM_Tax import wealth_tax_check
from ATM_logger import write_to_logfile
from ATM_Messages import *
from ATM_Replenishment import replenishment

from ATM_Count import operations_count


def give_money(how_much_to_replenishment: int, amount_of_money: float, operation_count: int):
    write_to_logfile(LOGFILE_PATH, amount_of_money, WEALTH_TAX_START_INFO)
    amount_of_money, temp_str = wealth_tax_check(amount_of_money)
    write_to_logfile(LOGFILE_PATH, amount_of_money, temp_str)

    write_to_logfile(LOGFILE_PATH, amount_of_money, REPLENISHMENT_START)
    amount_of_money, operation_count, temp_str = replenishment(how_much_to_replenishment, amount_of_money,
                                                               operation_count)
    write_to_logfile(LOGFILE_PATH, amount_of_money, temp_str)

    if temp_str != ERROR_MULTIPLICTY_REPLENISHMENT:
        write_to_logfile(LOGFILE_PATH, amount_of_money, OPERATION_COUNT_START)
        operation_count, amount_of_money, temp_str = operations_count(operation_count, amount_of_money)
        write_to_logfile(LOGFILE_PATH, amount_of_money, temp_str)

    return amount_of_money, operation_count