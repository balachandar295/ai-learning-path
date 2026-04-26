import csv
import os

table_html = "<div class='table-responsive'><table class='table table-bordered table-striped text-center align-middle' style='background-color: white;'><thead class='table-dark'><tr><th>Store</th><th>Laptops Sold</th><th>Tablets Sold</th><th>Mobiles Sold</th><th>Smartwatches Sold</th><th>Total Accessories</th></tr></thead><tbody><tr><td>Store A</td><td>350</td><td>200</td><td>800</td><td>150</td><td>500</td></tr><tr><td>Store B</td><td>420</td><td>180</td><td>900</td><td>210</td><td>620</td></tr><tr><td>Store C</td><td>300</td><td>250</td><td>750</td><td>180</td><td>550</td></tr><tr><td>Store D</td><td>480</td><td>320</td><td>1100</td><td>240</td><td>700</td></tr><tr><td>Store E</td><td>250</td><td>150</td><td>650</td><td>120</td><td>430</td></tr></tbody></table></div>"

questions = [
    {
        'q_text': 'What is the ratio of Laptops sold by Store A to the Tablets sold by Store D?',
        'a': '35:32', 'b': '30:31', 'c': '35:34', 'd': '7:6',
        'ans': 'a', 'exp': 'Laptops Store A = 350. Tablets Store D = 320. Ratio = 350:320 = 35:32.'
    },
    {
        'q_text': 'What is the average number of Mobiles sold across all five stores?',
        'a': '810', 'b': '840', 'c': '850', 'd': '880',
        'ans': 'b', 'exp': 'Total Mobiles = 800+900+750+1100+650 = 4200. Average = 4200 / 5 = 840.'
    },
    {
        'q_text': 'Total Accessories sold by Store B is what percentage of Mobiles sold by Store D? (Approx)',
        'a': '45.5%', 'b': '52.3%', 'c': '56.4%', 'd': '60.1%',
        'ans': 'c', 'exp': 'Accessories Store B = 620. Mobiles Store D = 1100. % = (620 / 1100) * 100 = 56.4%.'
    },
    {
        'q_text': 'What is the difference between total Laptops and total Smartwatches sold across all stores?',
        'a': '850', 'b': '900', 'c': '950', 'd': '1000',
        'ans': 'b', 'exp': 'Total Laptops = 1800. Total Smartwatches = 900. Diff = 1800 - 900 = 900.'
    },
    {
        'q_text': 'Number of Tablets sold by Store C is approximately what percent more or less than Smartwatches sold by Store B?',
        'a': '19% More', 'b': '19% Less', 'c': '24% More', 'd': '24% Less',
        'ans': 'a', 'exp': 'Tablets at C = 250. Smartwatches at B = 210. Diff = 40. (40 / 210) * 100 = 19.04% more.'
    },
    {
        'q_text': 'Find the ratio of total items (Laptops, Tablets, Mobiles, Watches, Accesories) sold by Store A to Store E.',
        'a': '20:15', 'b': '4:3', 'c': '25:13', 'd': '20:16',
        'ans': 'd', 'exp': 'Store A total = 2000. Store E total = 1600. 2000:1600 = 20:16.'
    },
    {
        'q_text': 'If the price of each Laptop is $500, what is the total revenue from Laptops for Store C?',
        'a': '$120,000', 'b': '$150,000', 'c': '$180,000', 'd': '$200,000',
        'ans': 'b', 'exp': 'Laptops at C = 300. Revenue = 300 * 500 = $150,000.'
    },
    {
        'q_text': 'Total number of Smartwatches sold by Store A, C and E together is?',
        'a': '400', 'b': '420', 'c': '450', 'd': '480',
        'ans': 'c', 'exp': 'A=150, C=180, E=120. Sum = 450.'
    },
    {
        'q_text': 'Which store sold the highest number of overall electronic items (excluding accessories)?',
        'a': 'Store A', 'b': 'Store B', 'c': 'Store C', 'd': 'Store D',
        'ans': 'd', 'exp': 'Sum without accessories: D = 480+320+1100+240 = 2140. Highest is D.'
    },
    {
        'q_text': 'Mobiles sold by Store A and B together constitute what percent of laptops sold by all stores together?',
        'a': '90.5%', 'b': '94.4%', 'c': '98.2%', 'd': '102.3%',
        'ans': 'b', 'exp': 'Mobiles A+B = 1700. Total Laptops = 1800. % = (1700 / 1800) * 100 = 94.44%.'
    },
    {
        'q_text': 'If 10% of Tablets sold by Store D were defective, how many non-defective Tablets did Store D sell?',
        'a': '280', 'b': '288', 'c': '296', 'd': '300',
        'ans': 'b', 'exp': 'Tablets at D = 320. Defective = 32. Non-defective = 320 - 32 = 288.'
    },
    {
        'q_text': 'What is the sum of Accessories sold by Store A and Store B together?',
        'a': '1020', 'b': '1120', 'c': '1220', 'd': '1320',
        'ans': 'b', 'exp': 'A = 500, B = 620. Total = 1120.'
    },
    {
        'q_text': 'The average number of Laptops sold by Store C and Store E is how much more or less than the number of Tablets sold by Store D?',
        'a': '20 Less', 'b': '45 Less', 'c': '45 More', 'd': '20 More',
        'ans': 'b', 'exp': 'Avg Laptops C & E = (300+250)/2 = 275. Tablets by D=320. Diff = 45 Less.'
    },
    {
        'q_text': 'Find the central angle of the sector representing Mobiles sold by C if total items at C are plotted on a pie chart.',
        'a': '182.4 degrees', 'b': '180.2 degrees', 'c': '184.6 degrees', 'd': '190.5 degrees',
        'ans': 'a', 'exp': 'Total at C = 1480. Mobiles = 750. Angle = (750 / 1480) * 360 = 182.4 degrees.'
    },
    {
        'q_text': 'Ratio of total Tablets sold by all stores to total Smartwatches sold by all stores?',
        'a': '10:9', 'b': '11:8', 'c': '11:9', 'd': '12:9',
        'ans': 'c', 'exp': 'Total Tablets = 1100. Total Smartwatches = 900. Ratio = 1100:900 = 11:9.'
    }
]

new_rows = []
for q in questions:
    full_question = table_html + '<br><p class="mt-3 fw-bold">' + q['q_text'] + '</p>'
    new_rows.append({
        'topic': 'Tabular Data Interpretation',
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
print('Successfully appended 15 DI questions with a shared large table.')
