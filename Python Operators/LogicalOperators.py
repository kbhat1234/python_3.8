has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income or has_good_credit:
    print('Eligible for loan')
else:
    print('Not eligible for loan')


if has_good_credit and has_high_income and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan')

if has_good_credit or has_high_income or not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan')