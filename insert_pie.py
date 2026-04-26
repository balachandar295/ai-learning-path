import csv
import os

pie_html = "<div class='d-flex flex-column align-items-center justify-content-center pt-3' style='margin: 20px;'><div style='width: 200px; height: 200px; border-radius: 50%; background: conic-gradient(#ff6b6b 0% 25%, #4ecdc4 25% 60%, #ffe66d 60% 80%, #1a535c 80% 100%);'></div><div style='display:flex; flex-wrap:wrap; gap:15px; margin-top: 25px; justify-content:center;'><div style='display:flex; align-items:center;'><span style='width:15px;height:15px;background:#ff6b6b;display:inline-block;margin-right:5px;border-radius:3px;'></span> Rent (25%)</div><div style='display:flex; align-items:center;'><span style='width:15px;height:15px;background:#4ecdc4;display:inline-block;margin-right:5px;border-radius:3px;'></span> Food (35%)</div><div style='display:flex; align-items:center;'><span style='width:15px;height:15px;background:#ffe66d;display:inline-block;margin-right:5px;border-radius:3px;'></span> Transport (20%)</div><div style='display:flex; align-items:center;'><span style='width:15px;height:15px;background:#1a535c;display:inline-block;margin-right:5px;border-radius:3px;'></span> Savings (20%)</div></div></div><p class='text-center text-muted mb-4'>Monthly Expenses Distribution (Total = $4000)</p>"

questions = [
    {
        'q_text': 'What is the amount spent on Food every month?',
        'a': '$1200', 'b': '$1400', 'c': '$1500', 'd': '$1600',
        'ans': 'b', 'exp': 'Food accounts for 35%. 35% of 4000 = 0.35 * 4000 = $1400.'
    },
    {
        'q_text': 'What is the central angle for the sector representing Rent?',
        'a': '80 degrees', 'b': '90 degrees', 'c': '100 degrees', 'd': '120 degrees',
        'ans': 'b', 'exp': 'Rent is 25%. Central angle = 25% of 360 = 90 degrees.'
    },
    {
        'q_text': 'How much more money is spent on Food compared to Rent?',
        'a': '$200', 'b': '$300', 'c': '$400', 'd': '$500',
        'ans': 'c', 'exp': 'Food(35%) - Rent(25%) = 10% difference. 10% of 4000 = $400.'
    },
    {
        'q_text': 'If Savings were to decrease by 50%, what would be the revised Savings amount?',
        'a': '$300', 'b': '$400', 'c': '$500', 'd': '$800',
        'ans': 'b', 'exp': 'Savings = 20% of 4000 = 800. Half of 800 = $400.'
    },
    {
        'q_text': 'Ratio of expenditure on Transport to expenditure on Rent is:',
        'a': '2:3', 'b': '3:4', 'c': '4:5', 'd': '5:6',
        'ans': 'c', 'exp': 'Transport = 20%, Rent = 25%. Ratio = 20:25 = 4:5.'
    },
    {
        'q_text': 'The amount spent on Transport and Savings combined perfectly matches the amount spent on?',
        'a': 'Food', 'b': 'Rent', 'c': 'None of the above', 'd': 'Both A and B',
        'ans': 'c', 'exp': 'Transport(20%) + Savings(20%) = 40%. No single category is 40%.'
    },
    {
        'q_text': 'What is the total expenditure excluding Savings?',
        'a': '$3000', 'b': '$3100', 'c': '$3200', 'd': '$3400',
        'ans': 'c', 'exp': 'Savings = 20%. Excluded = 80%. 80% of 4000 = $3200.'
    },
    {
        'q_text': 'If the total income increases by 10% and percentages remain the same, what will be the new expenditure on Transport?',
        'a': '$800', 'b': '$850', 'c': '$880', 'd': '$920',
        'ans': 'c', 'exp': 'New income = 4400. Transport = 20% of 4400 = 880.'
    },
    {
        'q_text': 'What is the central angle corresponding to Savings?',
        'a': '60 degrees', 'b': '72 degrees', 'c': '90 degrees', 'd': '108 degrees',
        'ans': 'b', 'exp': 'Savings = 20%. 20% of 360 = 72 degrees.'
    },
    {
        'q_text': 'Difference between central angles of Food and Transport is:',
        'a': '45 degrees', 'b': '54 degrees', 'c': '64 degrees', 'd': '72 degrees',
        'ans': 'b', 'exp': 'Food is 35%, Transport is 20%. Diff = 15%. 15% of 360 = 54 degrees.'
    },
    {
        'q_text': 'If Rent increases by $200 (taken from Food, assuming total is constant), what is the new percentage for Rent?',
        'a': '28%', 'b': '30%', 'c': '32%', 'd': '35%',
        'ans': 'b', 'exp': 'Rent was 1000. New rent = 1200. Total = 4000. 1200/4000 * 100 = 30%.'
    },
    {
        'q_text': 'The average monthly expense on Food, Transport and Rent is:',
        'a': '$1066.67', 'b': '$1080.33', 'c': '$1120.67', 'd': '$1200.00',
        'ans': 'a', 'exp': 'Food=1400, Transport=800, Rent=1000. Sum = 3200. 3200 / 3 = 1066.67.'
    },
    {
        'q_text': 'Savings amount is what percent of the combined spending on Rent and Food?',
        'a': '30%', 'b': '33.33%', 'c': '35.5%', 'd': '40%',
        'ans': 'b', 'exp': 'Savings = 800. Rent+Food = 1000+1400 = 2400. (800 / 2400) * 100 = 33.33%.'
    },
    {
        'q_text': 'Total sum of central angles of all sectors on the pie chart is:',
        'a': '100 degrees', 'b': '180 degrees', 'c': '360 degrees', 'd': '400 degrees',
        'ans': 'c', 'exp': 'A complete pie chart always represents 360 degrees.'
    },
    {
        'q_text': 'If Transport cost becomes zero and is entirely moved to Savings, Savings will represent what fraction of the total?',
        'a': '1/5', 'b': '1/4', 'c': '1/3', 'd': '2/5',
        'ans': 'd', 'exp': 'New Savings = 20% + 20% = 40%. 40% = 40/100 = 2/5.'
    }
]

new_rows = []
for q in questions:
    full_question = pie_html + '<br><p class="mt-3 fw-bold">' + q['q_text'] + '</p>'
    new_rows.append({
        'topic': 'Pie Chart',
        'question': full_question,
        'option_a': q['a'],
        'option_b': q['b'],
        'option_c': q['c'],
        'option_d': q['d'],
        'correct': q['ans'],
        'explanation': q['exp'],
        'difficulty': 'Medium'
    })

file_path = os.path.join(os.path.dirname(__file__), 'aptitude_questions.csv')
with open(file_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['topic', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct', 'explanation', 'difficulty'])
    writer.writerows(new_rows)
print('Successfully appended 15 DI questions with a shared Pie Chart.')
