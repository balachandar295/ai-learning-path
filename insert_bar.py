import csv
import os

bar_html = "<div class='d-flex align-items-end justify-content-center pt-5' style='height: 250px; gap: 20px; border-bottom: 2px solid #ccc; border-left: 2px solid #ccc; padding-bottom: 5px; margin: 20px;'><div style='display:flex; flex-direction:column; align-items:center;'><span style='font-size:12px; font-weight:bold;'>120</span><div style='width: 40px; height: 120px; background-color: #007bff; border-radius: 4px 4px 0 0;'></div><span style='font-size:14px; margin-top:5px;'>2018</span></div><div style='display:flex; flex-direction:column; align-items:center;'><span style='font-size:12px; font-weight:bold;'>150</span><div style='width: 40px; height: 150px; background-color: #007bff; border-radius: 4px 4px 0 0;'></div><span style='font-size:14px; margin-top:5px;'>2019</span></div><div style='display:flex; flex-direction:column; align-items:center;'><span style='font-size:12px; font-weight:bold;'>100</span><div style='width: 40px; height: 100px; background-color: #007bff; border-radius: 4px 4px 0 0;'></div><span style='font-size:14px; margin-top:5px;'>2020</span></div><div style='display:flex; flex-direction:column; align-items:center;'><span style='font-size:12px; font-weight:bold;'>180</span><div style='width: 40px; height: 180px; background-color: #007bff; border-radius: 4px 4px 0 0;'></div><span style='font-size:14px; margin-top:5px;'>2021</span></div><div style='display:flex; flex-direction:column; align-items:center;'><span style='font-size:12px; font-weight:bold;'>250</span><div style='width: 40px; height: 250px; background-color: #007bff; border-radius: 4px 4px 0 0;'></div><span style='font-size:14px; margin-top:5px;'>2022</span></div></div><p class='text-center text-muted mb-4'>Annual Car Production (in thousands)</p>"

questions = [
    {
        'q_text': 'What is the sum of car production in 2018 and 2021?',
        'a': '280,000', 'b': '300,000', 'c': '320,000', 'd': '350,000',
        'ans': 'b', 'exp': '2018 = 120k. 2021 = 180k. 120+180 = 300.'
    },
    {
        'q_text': 'What is the percentage increase in production from 2018 to 2019?',
        'a': '20%', 'b': '25%', 'c': '30%', 'd': '33.3%',
        'ans': 'b', 'exp': 'Increase = 150 - 120 = 30. (30 / 120) * 100 = 25%.'
    },
    {
        'q_text': 'What is the average production over all 5 years?',
        'a': '150,000', 'b': '160,000', 'c': '170,000', 'd': '180,000',
        'ans': 'b', 'exp': 'Total = 120+150+100+180+250 = 800. Average = 800 / 5 = 160.'
    },
    {
        'q_text': 'What is the ratio of production in 2020 to production in 2022?',
        'a': '2:5', 'b': '2:3', 'c': '3:5', 'd': '4:5',
        'ans': 'a', 'exp': '100 : 250 = 10:25 = 2:5.'
    },
    {
        'q_text': 'In which year was the car production minimum?',
        'a': '2018', 'b': '2019', 'c': '2020', 'd': '2021',
        'ans': 'c', 'exp': 'Production was 100k in 2020, which is the lowest.'
    },
    {
        'q_text': 'percentage decrease in production in 2020 as compared to previous year (2019) is:',
        'a': '33.33%', 'b': '30%', 'c': '25%', 'd': '40%',
        'ans': 'a', 'exp': 'Decrease = 150 - 100 = 50. % = (50 / 150) * 100 = 33.33%.'
    },
    {
        'q_text': 'Total production in 2019 and 2020 together is equal to production in which year?',
        'a': '2018', 'b': '2021', 'c': '2022', 'd': 'None',
        'ans': 'c', 'exp': '2019 = 150. 2020 = 100. Sum = 250. This is equal to 2022.'
    },
    {
        'q_text': 'Production in 2022 is what percentage more than average production of all years?',
        'a': '40%', 'b': '50%', 'c': '56.25%', 'd': '62.5%',
        'ans': 'c', 'exp': 'Average = 160. 2022 = 250. Diff = 90. (90 / 160) * 100 = 56.25%.'
    },
    {
        'q_text': 'Difference between maximum and minimum production is:',
        'a': '100,000', 'b': '120,000', 'c': '150,000', 'd': '180,000',
        'ans': 'c', 'exp': 'Max = 250 (2022). Min = 100 (2020). Diff = 150k.'
    },
    {
        'q_text': 'Total production from 2018 to 2020 is what percent of total production overall?',
        'a': '45.15%', 'b': '46.25%', 'c': '47.5%', 'd': '48%',
        'ans': 'b', 'exp': '2018+2019+2020 = 120+150+100 = 370. Total = 800. % = (370 / 800) * 100 = 46.25%.'
    },
    {
        'q_text': 'If production in 2023 increases by 20% over 2022, what will be the 2023 production?',
        'a': '280,000', 'b': '300,000', 'c': '320,000', 'd': '350,000',
        'ans': 'b', 'exp': '2022 = 250. 20% of 250 = 50. 250 + 50 = 300k.'
    },
    {
        'q_text': 'Ratio of overall total production to production in 2021?',
        'a': '40:9', 'b': '4:1', 'c': '30:7', 'd': '35:9',
        'ans': 'a', 'exp': 'Total = 800. 2021 = 180. Ratio = 800:180 = 40:9.'
    },
    {
        'q_text': 'In how many years was the production more than the average production?',
        'a': '1', 'b': '2', 'c': '3', 'd': '4',
        'ans': 'b', 'exp': 'Average = 160. Years > 160 are 2021 (180), 2022 (250). Total 2 years.'
    },
    {
        'q_text': 'Production of 2018 is what percent of production of 2020?',
        'a': '100%', 'b': '110%', 'c': '120%', 'd': '125%',
        'ans': 'c', 'exp': '2018 = 120. 2020 = 100. (120 / 100) * 100 = 120%.'
    },
    {
        'q_text': 'If 5% of cars produced in 2022 were defective, number of non-defective cars is:',
        'a': '230,000', 'b': '235,500', 'c': '237,500', 'd': '240,000',
        'ans': 'c', 'exp': '5% of 250k = 12.5k. 250k - 12.5k = 237,500.'
    }
]

new_rows = []
for q in questions:
    full_question = bar_html + '<br><p class="mt-3 fw-bold">' + q['q_text'] + '</p>'
    new_rows.append({
        'topic': 'Bar Graph',
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
print('Successfully appended 15 DI questions with a shared Bar Graph.')
