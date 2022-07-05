from loan_calculator import AmortizationCalculator


if __name__ == '__main__':
    calc = AmortizationCalculator(
        principal=100000,
        interest_rate=0.10,
        period=12
    )
    calc.amortization_schedule()
    schedule = calc.schedule
    print(schedule)
