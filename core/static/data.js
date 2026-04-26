// ============================================================
// data.js — All 18 Aptitude Topics Content
// Place this file in: core/static/data.js
// ============================================================

const topicsData = {

    // ───── LEVEL 1: FOUNDATION ─────

    "simplification": {
    "title": "Simplification & BODMAS",
    "explanation": `
        <h3>What is Simplification?</h3>
        <p>Simplification is the process of reducing a complex mathematical expression into a single numerical value. To do this correctly, we follow the <b>V-BODMAS</b> rule to determine which operation to perform first.</p>
        
        <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
            <h4 style="margin-bottom:10px;">The V-BODMAS Hierarchy:</h4>
            <p>1. <b>V</b> — Vinculum (Bar line over numbers)</p>
            <p>2. <b>B</b> — Brackets: (), {}, then []</p>
            <p>3. <b>O</b> — Of / Order (Powers, Roots, Multiplication by 'of')</p>
            <p>4. <b>D</b> — Division (÷)</p>
            <p>5. <b>M</b> — Multiplication (×)</p>
            <p>6. <b>A</b> — Addition (+)</p>
            <p>7. <b>S</b> — Subtraction (−)</p>
        </div>
        <p><b>Note:</b> Division and Multiplication have the same priority level; solve them from left to right as they appear. The same applies to Addition and Subtraction.</p>`,
        
    "formulas": `
        <h3>Essential Arithmetic Identities</h3>
        <p>These formulas help simplify expressions involving large squares or cubes instantly:</p>
        <div style="display:grid;gap:12px;margin-top:15px;">
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">(a + b)² = a² + 2ab + b²</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">(a − b)² = a² − 2ab + b²</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">a² − b² = (a + b)(a − b)</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">(a + b)³ = a³ + b³ + 3ab(a + b)</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Sum of n natural numbers = [n(n + 1)] / 2</div>
        </div>`,
        
    "examples": `
        <h3>Solved Examples</h3>
        <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
            <p><b>Example 1:</b> Solve 20 + 15 ÷ 3 × 2 − 5</p>
            <p>Step 1 (Division): 20 + 5 × 2 − 5</p>
            <p>Step 2 (Multiplication): 20 + 10 − 5</p>
            <p>Step 3 (Add/Sub): 30 − 5 = <b>25</b></p>
        </div>
        
        <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
            <p><b>Example 2:</b> 100 − [20 + {30 − (10 − 5)}]</p>
            <p>Step 1 (Inner Bracket): 100 − [20 + {30 − 5}]</p>
            <p>Step 2 (Curly Bracket): 100 − [20 + 25]</p>
            <p>Step 3 (Square Bracket): 100 − 45 = <b>55</b></p>
        </div>
        
        <div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;">
            <p><b>Example 3:</b> Solve 98 × 98 − 2 × 2 using a² − b²</p>
            <p>Pattern: (98 + 2)(98 − 2)</p>
            <p>Result: 100 × 96 = <b>9600</b></p>
        </div>`,
        
    "tips": `
        <h3>Expert Calculation Hacks</h3>
        <ul style="list-style:none;padding:0;display:grid;gap:12px;">
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>The 11 Rule:</b> To multiply a 2-digit number by 11, add the two digits and place the sum in the middle (e.g., 25 × 11: 2+5=7, Result = 275).</li>
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Last Digit Check:</b> If options have different last digits, calculate only the unit digit of the expression to save time.</li>
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Digital Sum:</b> For massive multiplications, the sum of digits of the question must equal the sum of digits of the answer.</li>
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Approximation:</b> If options are far apart, round numbers to the nearest zero (e.g., treat 49.8 as 50) for a 5-second estimate.</li>
        </ul>`
},

    "number_system": {
    "title": "Number System",
    "explanation": `
        <h3>What is the Number System?</h3>
        <p>The Number System is a way of representing numbers on the number line. Understanding the classification of numbers is the first step in solving complex quantitative problems.</p>
        
        <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
            <h4 style="margin-bottom:10px;">Classification of Numbers:</h4>
            <p>• <b>Natural Numbers (N):</b> 1, 2, 3, ... (starts from 1)</p>
            <p>• <b>Whole Numbers (W):</b> 0, 1, 2, 3, ... (starts from 0)</p>
            <p>• <b>Integers (Z):</b> ..., -3, -2, -1, 0, 1, 2, 3, ...</p>
            <p>• <b>Rational Numbers:</b> Can be expressed as p/q (e.g., 2/3, 5)</p>
            <p>• <b>Prime Numbers:</b> Numbers with exactly two factors: 1 and itself (2, 3, 5, 7, 11...)</p>
            <p>• <b>Composite Numbers:</b> Numbers with more than two factors (4, 6, 8, 9...)</p>
        </div>
        
        <p><b>Pro-Tip:</b> '1' is neither prime nor composite. '2' is the only even prime number.</p>`,
        
    "formulas": `
        <h3>Mastering Divisibility Rules</h3>
        <p>Use these rules to check if a large number is divisible by a digit without actual division:</p>
        <div style="display:grid;gap:12px;margin-top:15px;">
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Div by 3: Sum of digits is divisible by 3.</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Div by 4: Last two digits are divisible by 4.</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Div by 6: Number is divisible by both 2 and 3.</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Div by 8: Last three digits are divisible by 8.</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Div by 9: Sum of digits is divisible by 9.</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Div by 11: (Sum of digits at odd places) - (Sum of digits at even places) = 0 or multiple of 11.</div>
        </div>`,
        
    "examples": `
        <h3>Solved Examples</h3>
        <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
            <p><b>Example 1:</b> Find the unit digit of 3^67.</p>
            <p>Cyclicity of 3 is 4 {3, 9, 7, 1}.</p>
            <p>Step 1: Divide power by 4: 67 ÷ 4 = Remainder 3.</p>
            <p>Step 2: 3rd term in cycle is 7. Answer: <b>7</b></p>
        </div>
        
        <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
            <p><b>Example 2:</b> Is 12345 divisible by 3?</p>
            <p>Sum of digits: 1+2+3+4+5 = 15.</p>
            <p>Since 15 is divisible by 3, <b>Yes</b>, the number is divisible.</p>
        </div>`,
        
    "tips": `
        <h3>Number System Shortcuts</h3>
        <ul style="list-style:none;padding:0;display:grid;gap:12px;">
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Unit Digit of 0, 1, 5, 6:</b> These numbers always result in the same unit digit regardless of the power (e.g., 5^n always ends in 5).</li>
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Checking for Prime:</b> To check if N is prime, test divisibility only up to √N.</li>
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Consecutive Integers:</b> The product of 'n' consecutive integers is always divisible by n! (n factorial).</li>
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Face Value vs Place Value:</b> Face value of 5 in 452 is 5; Place value is 50.</li>
        </ul>`
},

    "lcm_hcf": {
    "title": "LCM & HCF",
    "explanation": `
        <h3>What are LCM and HCF?</h3>
        <p><b>HCF (Highest Common Factor)</b> is the largest number that divides two or more numbers exactly. It is also known as GCM (Greatest Common Measure) or GCD (Greatest Common Divisor).</p>
        <p><b>LCM (Lowest Common Multiple)</b> is the smallest number which is exactly divisible by each of the given numbers.</p>
        
        <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
            <h4 style="margin-bottom:10px;">How to Identify the Problem Type:</h4>
            <p>• <b>Ask for HCF if:</b> You need to split things into smaller sections, arrange items into rows/groups, or find the "greatest" possible size.</p>
            <p>• <b>Ask for LCM if:</b> You need to find when events will happen together again (like bells tolling or runners on a track), or find the "smallest" quantity.</p>
        </div>
        `,
        
    "formulas": `
        <h3>Key Formulas & Properties</h3>
        <p>These relationships are essential for solving competitive exam problems quickly:</p>
        <div style="display:grid;gap:12px;margin-top:15px;">
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Product of Two Numbers = HCF × LCM</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">HCF of Fractions = HCF of Numerators / LCM of Denominators</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">LCM of Fractions = LCM of Numerators / HCF of Denominators</div>
            <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">HCF of co-prime numbers is always 1.</div>
        </div>`,
        
    "examples": `
        <h3>Solved Examples</h3>
        <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
            <p><b>Example 1:</b> The HCF of two numbers is 11 and their LCM is 693. If one number is 77, find the other.</p>
            <p>Formula: First Number × Second Number = HCF × LCM</p>
            <p>Step: 77 × X = 11 × 693</p>
            <p>Calculation: X = (11 × 693) / 77 = 693 / 7 = <b>99</b></p>
        </div>
        
        <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
            <p><b>Example 2:</b> Find the greatest number which can divide 1356, 1868 and 2764 leaving the same remainder 12 in each case.</p>
            <p>Step 1: Subtract the remainder: 1344, 1856, 2752.</p>
            <p>Step 2: Find the HCF of these three numbers.</p>
            <p>Result: <b>64</b></p>
        </div>`,
        
    "tips": `
        <h3>LCM & HCF Pro-Tips</h3>
        <ul style="list-style:none;padding:0;display:grid;gap:12px;">
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>The Difference Method:</b> HCF of two numbers is either their difference or a factor of their difference. (e.g., HCF of 48 and 60: Difference is 12. 12 divides both, so HCF is 12).</li>
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Ratio Shortcut:</b> If the ratio of two numbers is a:b and their HCF is H, then the numbers are (aH) and (bH), and their LCM is (abH).</li>
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Bell Problems:</b> Whenever you see "bells tolling together" or "traffic lights changing," you almost always need to find the LCM.</li>
            <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Prime Factorization:</b> For HCF, take the <i>lowest</i> power of common prime factors. For LCM, take the <i>highest</i> power of all prime factors.</li>
        </ul>`
},

    "averages": {
        "title": "Averages",
        "explanation": `
            <h3>What is Average?</h3>
            <p>Average (or Arithmetic Mean) is a central value of a set of numbers. It represents the "equal distribution" of a total sum among all members of a group.</p>
            
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Key Concepts:</h4>
                <p>• <b>Mean:</b> Sum of all values divided by total count.</p>
                <p>• <b>Weighted Average:</b> Used when different groups have different sizes or importance.</p>
                <p>• <b>Deviation:</b> If a new value is added that is higher than the average, the overall average increases.</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Average = (Sum of Observations) / (Number of Observations)</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Sum = Average × Number of Observations</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Average Speed = (2xy) / (x + y) [For same distance]</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Avg of first 'n' natural numbers = (n + 1) / 2</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> The average age of 5 students is 14. If a teacher's age is added, the average becomes 16. Find the teacher's age.</p>
                <p>Total age of 5 students = 5 × 14 = 70</p>
                <p>Total age of 6 people (inc. teacher) = 6 × 16 = 96</p>
                <p>Teacher's age = 96 − 70 = <b>26 years</b></p>
            </div>`,
        "tips": `
            <h3>Average Shortcuts</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Consecutive Numbers:</b> The average of an arithmetic progression (like 2, 4, 6, 8) is exactly the middle term.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>The 'Assumed Mean' Method:</b> To average large numbers (e.g., 705, 710, 715), assume 710 as mean and just average the differences (-5, 0, +5).</li>
            </ul>`
    },

    "percentages": {
        "title": "Percentages",
        "explanation": `
            <h3>What is Percentage?</h3>
            <p>Percentage means "parts per hundred." It is the most common way to compare ratios and represent growth, discounts, and results.</p>
            
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Fraction to % Essentials:</h4>
                <p>• 1/2 = 50% | 1/3 = 33.33% | 1/4 = 25%</p>
                <p>• 1/5 = 20% | 1/6 = 16.66% | 1/8 = 12.5%</p>
                <p>• 1/9 = 11.11% | 1/11 = 9.09% | 1/12 = 8.33%</p>
            </div>`,
        "formulas": `
            <h3>Percentage Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Percentage = (Value / Total) × 100</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">% Change = [(New - Old) / Old] × 100</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Successive % Change = a + b + (ab/100)</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">x% of y = y% of x</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> Price of sugar increases by 25%. By how much % should a family reduce consumption to keep the budget same?</p>
                <p>Formula: [r / (100 + r)] × 100</p>
                <p>Step: [25 / 125] × 100 = 1/5 × 100 = <b>20%</b></p>
            </div>`,
        "tips": `
            <h3>Percentage Hacks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Splitting Method:</b> To find 15% of 440, find 10% (44) and 5% (22). Total = 44 + 22 = 66.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Net Change:</b> If a value increases by x% and then decreases by x%, there is always a net decrease of (x/10)² %.</li>
            </ul>`
    },

    "ratio_proportion": {
        "title": "Ratio & Proportion",
        "explanation": `
            <h3>Core Concepts</h3>
            <p><b>Ratio</b> is the comparison of two quantities by division (a:b). <b>Proportion</b> is an equation that states two ratios are equal (a:b = c:d).</p>
            
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Direct vs Inverse Proportion:</h4>
                <p>• <b>Direct:</b> If x increases, y increases (e.g., more pens = more cost).</p>
                <p>• <b>Inverse:</b> If x increases, y decreases (e.g., more workers = less time).</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">If a:b = c:d, then (a × d) = (b × c)</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Duplicate Ratio of a:b = a²:b²</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Mean Proportional between a and b = √(a × b)</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Compounded Ratio of (a:b) and (c:d) = (ac:bd)</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> A:B = 2:3 and B:C = 4:5. Find A:B:C.</p>
                <p>Step 1: Make B equal in both ratios (LCM of 3 and 4 = 12).</p>
                <p>Step 2: A:B = 8:12, B:C = 12:15.</p>
                <p>Answer: <b>8:12:15</b></p>
            </div>`,
        "tips": `
            <h3>Ratio Pro-Tips</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Value vs Ratio:</b> Never add a constant to a ratio (e.g., 2:3 + 5 is not 7:8). Always use variables like 2x and 3x.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Alligation Method:</b> This ratio technique is the fastest way to solve mixture and average problems.</li>
            </ul>`
    },


    // ───── LEVEL 2: CORE ─────
"profit_loss": {
        "title": "Profit & Loss",
        "explanation": `
            <h3>What is Profit & Loss?</h3>
            <p>Profit/Loss is always calculated on <b>Cost Price (CP)</b>. Discount is always calculated on <b>Marked Price (MP)</b>. Never mix these up!</p>
            
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Key Terms:</h4>
                <p>• <b>CP:</b> Cost Price — what you paid</p>
                <p>• <b>SP:</b> Selling Price — what you sold for</p>
                <p>• <b>MP:</b> Marked Price — printed/listed price</p>
                <p>• <b>Discount:</b> Reduction on Marked Price</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Profit = SP − CP | Loss = CP − SP</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Profit% = (Profit/CP) × 100</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">SP = CP × (1 + P%/100) or CP × (1 − L%/100)</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Discount% = (Discount/MP) × 100</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">SP = MP × (1 − D%/100)</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> CP=₹500, SP=₹600. Profit%?</p>
                <p>Profit = 100 → Profit% = (100/500)×100 = <b>20%</b></p>
            </div>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;">
                <p><b>Example 2:</b> MP=₹800, Discount=10%. SP?</p>
                <p>SP = 800 × 0.9 = <b>₹720</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Multiplying factor:</b> 20% profit → SP = 1.2×CP. 15% loss → SP = 0.85×CP.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Two items same SP:</b> One P% profit one P% loss: Always a net loss of (P/10)²%.</li>
            </ul>`
    },

    "si_ci": {
        "title": "Simple & Compound Interest",
        "explanation": `
            <h3>SI vs CI</h3>
            <p><b>Simple Interest (SI)</b> — calculated on original principal every year.</p>
            <p style="margin-top:8px;"><b>Compound Interest (CI)</b> — calculated on principal + accumulated interest. CI ≥ SI always.</p>
            
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Key difference for 2 years:</h4>
                <p>CI − SI = P(R/100)²</p>
                <p style="margin-top:8px;">This difference grows each year!</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">SI = (P × R × T) / 100</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">CI Amount = P(1 + R/100)ᵀ</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">CI = P(1 + R/100)ᵀ − P</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> SI on ₹5000 at 8% for 3 years?</p>
                <p>SI = (5000×8×3)/100 = <b>₹1200</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Rule of 72:</b> Years to double money at r% CI ≈ 72/r.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Successive %:</b> 10% CI for 2 years: Effective rate = 10+10+1 = 21%.</li>
            </ul>`
    },

    "time_work": {
        "title": "Time & Work",
        "explanation": `
            <h3>What is Time & Work?</h3>
            <p>If a person completes a task in N days, they do <b>1/N of the work per day</b>. When multiple people work together, add their rates.</p>
            
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Golden Rule:</h4>
                <p>Total Work = Rate × Time</p>
                <p style="margin-top:8px;"><b>LCM method:</b> assume total work = LCM of all days. Find units/day by each person. Much faster!</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Rate = 1/Time</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">A+B together: T = AB/(A+B)</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">MDH formula: M₁D₁H₁/W₁ = M₂D₂H₂/W₂</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example:</b> A does job in 10 days, B in 15 days. Together?</p>
                <p>LCM = 30. A=3 units/day, B=2 units/day. Total=5. Time = 30/5 = <b>6 days</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Pipe filling:</b> Inlet adds (+), outlet subtracts (-). Net rate = Inlet − Outlet.</li>
            </ul>`
    },

    "time_distance": {
        "title": "Time & Distance",
        "explanation": `
            <h3>What is Time, Speed & Distance?</h3>
            <p>Speed, Distance and Time are interconnected. Average speed is NOT the simple average of speeds.</p>
            
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Relative Speed:</h4>
                <p>• Same direction: |a − b|</p>
                <p>• Opposite direction: a + b</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Distance = Speed × Time</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">km/h to m/s: × 5/18 | m/s to km/h: × 18/5</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Train crossing platform: dist = train + platform length</div>
            </div>`,
        "examples": `
            <h3>Solved Example</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example:</b> Going at 60, returning at 40 km/h. Avg speed?</p>
                <p>Avg = 2×60×40/(60+40) = 4800/100 = <b>48 km/h</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Train vs Pole:</b> Crossing a pole only uses train length as distance.</li>
            </ul>`
    },

    "ages": {
        "title": "Problems on Ages",
        "explanation": `
            <h3>What are Age Problems?</h3>
            <p>Always define one variable and express everything relative to it.</p>
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Standard Setup:</h4>
                <p>Present age = x | n years ago = x−n | n years after = x+n</p>
            </div>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Age difference stays constant forever.</div>
            </div>`,
        "examples": `
            <h3>Solved Example</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example:</b> A:B = 3:5. After 10 years ratio is 5:7. Present ages?</p>
                <p>(3x+10)/(5x+10) = 5/7 → 21x+70 = 25x+50 → x=5. A=15, B=25.</p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>MCQ shortcut:</b> Try answer options in ratio conditions — fastest for exam.</li>
            </ul>`
    },

    "partnership": {
        "title": "Partnership",
        "explanation": `
            <h3>What is Partnership?</h3>
            <p>Profit is shared in proportion to <b>Capital × Time</b>.</p>
            
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Profit Ratio:</h4>
                <p>Profit Ratio = C₁×T₁ : C₂×T₂</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Person's profit = (His ratio / Total ratio) × Total profit</div>
            </div>`,
        "examples": `
            <h3>Solved Example</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example:</b> A invests ₹5000 for 12 months, B ₹6000 for 10 months. Ratio?</p>
                <p>A = 60000, B = 60000. Ratio = 1:1.</p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Working partner salary</b> is deducted from total profit first, then split.</li>
            </ul>`
    },
    // ───── LEVEL 3: ADVANCED ─────

    "pc": {
        "title": "Permutation & Combination",
        "explanation": `
            <h3>P vs C — The Key Question</h3>
            <p><b>Permutation</b> = arrangement (order matters). <b>Combination</b> = selection (order doesn't matter).</p>
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <p>• "Arrange" → Permutation (nPr)</p>
                <p>• "Select / Choose / Committee" → Combination (nCr)</p>
                <p>• Circular → (n−1)!</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">nPr = n! / (n−r)!</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">nCr = n! / [r! × (n−r)!]</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">nCr = nC(n−r) &nbsp;|&nbsp; nC0 = nCn = 1</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Circular = (n−1)!</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Identical items: n! / (p! × q! × ...)</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> Arrange 3 from 5 people in a row?</p>
                <p>5P3 = 5×4×3 = <b>60 ways</b></p>
            </div>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;">
                <p><b>Example 2:</b> Committee of 3 from 7 people?</p>
                <p>7C3 = (7×6×5)/(3×2×1) = <b>35 ways</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Arrange = P, Choose = C.</b> First identify the keyword in the question.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Vowels together:</b> Treat all vowels as one unit. Arrange units × arrange vowels within.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>At least/at most:</b> Use complementary counting — subtract from total.</li>
            </ul>`
    },

    "probability": {
        "title": "Probability",
        "explanation": `
            <h3>What is Probability?</h3>
            <p>Probability measures the likelihood of an event. Ranges from 0 (impossible) to 1 (certain). Key: Sample Space = all possible outcomes.</p>
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Deck of Cards:</h4>
                <p>52 cards | 4 suits (13 each)</p>
                <p>Suits: Hearts ♥, Diamonds ♦, Clubs ♣, Spades ♠</p>
                <p>Each: A, 2–10, J, Q, K (13 cards)</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">P(E) = Favorable outcomes / Total outcomes</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">P(not E) = 1 − P(E)</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">P(A or B) = P(A) + P(B) − P(A∩B)</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">P(A and B) = P(A) × P(B) [independent]</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> Drawing a king from a deck?</p>
                <p>P = 4/52 = <b>1/13</b></p>
            </div>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;">
                <p><b>Example 2:</b> Two dice rolled. P(sum=7)?</p>
                <p>Favorable: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6</p>
                <p>P = 6/36 = <b>1/6</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>At least one:</b> P(at least 1) = 1 − P(none). Always use complement.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Without replacement:</b> Denominator decreases each draw. Don't forget!</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Mutually exclusive:</b> P(A or B) = P(A) + P(B). No subtraction needed.</li>
            </ul>`
    },

    "mensuration": {
        "title": "Mensuration",
        "explanation": `
            <h3>What is Mensuration?</h3>
            <p>Mensuration deals with calculation of Area, Volume, Perimeter, and Surface Area of 2D and 3D shapes. Requires memorizing formulas but once done, questions are straightforward.</p>
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">2D vs 3D:</h4>
                <p>• <b>2D:</b> Area and Perimeter</p>
                <p>• <b>3D:</b> Volume, Curved Surface Area (CSA), Total Surface Area (TSA)</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:10px;margin-top:15px;">
                <div style="background:#f8fafc;padding:13px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Circle: Area = πr² | Perimeter = 2πr</div>
                <div style="background:#f8fafc;padding:13px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Triangle: Area = ½ × b × h | Heron's = √[s(s-a)(s-b)(s-c)]</div>
                <div style="background:#f8fafc;padding:13px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Rectangle: Area = l×b | Perimeter = 2(l+b)</div>
                <div style="background:#f8fafc;padding:13px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Cube: Vol = a³ | TSA = 6a²</div>
                <div style="background:#f8fafc;padding:13px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Cylinder: Vol = πr²h | CSA = 2πrh</div>
                <div style="background:#f8fafc;padding:13px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Cone: Vol = ⅓πr²h | CSA = πrl</div>
                <div style="background:#f8fafc;padding:13px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Sphere: Vol = (4/3)πr³ | SA = 4πr²</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> Area of circle with radius 7cm?</p>
                <p>= π × 7² = 22/7 × 49 = <b>154 cm²</b></p>
            </div>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;">
                <p><b>Example 2:</b> Volume of cylinder r=5, h=10?</p>
                <p>= π × 25 × 10 = <b>250π cm³</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Use π = 22/7</b> when radius is multiple of 7. Use 3.14 otherwise.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Diagonal of rectangle:</b> √(l²+b²). Diagonal of cube: a√3.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>If dimensions doubled:</b> Area × 4, Volume × 8. Memorize these scale factors.</li>
            </ul>`
    },

    "alligation": {
        "title": "Alligation & Mixtures",
        "explanation": `
            <h3>What is Alligation?</h3>
            <p>Alligation is the rule to find the ratio in which two ingredients at different prices/concentrations must be mixed to get a desired mean price/concentration.</p>
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Alligation Cross Method:</h4>
                <p>Cheaper Price &nbsp;&nbsp;&nbsp;&nbsp; Costlier Price</p>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↘ Mean Price ↙</p>
                <p>(Costlier−Mean) : (Mean−Cheaper)</p>
                <p>= Ratio of Cheaper : Costlier</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Ratio = (d−m) : (m−c) where d=dear, c=cheap, m=mean</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Final conc after replacement: C×(1−x/V)ⁿ</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Where x=removed per step, V=total volume, n=steps</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> Mix rice at ₹10/kg and ₹15/kg to get ₹12/kg. Ratio?</p>
                <p>Cheap=10, Dear=15, Mean=12</p>
                <p>Ratio = (15−12):(12−10) = 3:2</p>
                <p>Mix <b>3 parts at ₹10 and 2 parts at ₹15</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Mean must be between</b> cheaper and costlier. If not, check your values.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Replacement formula:</b> Memorize C×(1−x/V)ⁿ — appears frequently in bank exams.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Works for %age too:</b> Mix 20% and 50% solution to get 30% — same cross method.</li>
            </ul>`
    },

    "trains": {
        "title": "Problems on Trains",
        "explanation": `
            <h3>Trains — Key Concept</h3>
            <p>Train problems are special cases of Time, Speed & Distance. The key difference: <b>the length of the train matters</b> when crossing a pole, platform, or another train.</p>
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Distance covered:</h4>
                <p>• Cross a pole/person → only train's length</p>
                <p>• Cross a platform → train length + platform length</p>
                <p>• Cross another train → sum of both lengths</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Time = Distance / Speed</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Same direction: Rel speed = |s₁ − s₂|</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Opposite direction: Rel speed = s₁ + s₂</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">km/h → m/s: × 5/18</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> Train 200m long at 72 km/h. Time to cross 300m platform?</p>
                <p>Speed = 72 × 5/18 = 20 m/s</p>
                <p>Distance = 200+300 = 500m</p>
                <p>Time = 500/20 = <b>25 seconds</b></p>
            </div>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;">
                <p><b>Example 2:</b> Two trains 100m and 150m at 60 & 40 km/h opposite. Crossing time?</p>
                <p>Rel speed = 100 km/h = 250/9 m/s</p>
                <p>Time = 250/(250/9) = <b>9 seconds</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Always convert km/h to m/s</b> (×5/18) when length is in meters.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Stationary object:</b> Person or pole — distance = train length only.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Two trains same dir:</b> Faster train must cover its own length + slower train's length to fully pass.</li>
            </ul>`
    },

    "boats_streams": {
        "title": "Boats & Streams",
        "explanation": `
            <h3>Boats & Streams</h3>
            <p><b>Downstream:</b> boat and stream same direction — speeds add. <b>Upstream:</b> against stream — subtract. The boat's speed in still water = average of upstream and downstream speeds.</p>
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Remember:</h4>
                <p>• Still water speed b = (D + U) / 2</p>
                <p>• Stream speed s = (D − U) / 2</p>
            </div>`,
        "formulas": `
            <h3>Key Formulas</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Downstream (D) = b + s</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Upstream (U) = b − s</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">b = (D + U) / 2 &nbsp;|&nbsp; s = (D − U) / 2</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Round trip avg = 2DU/(D+U)</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> 36km downstream in 4hrs, 24km upstream in 6hrs. Still water speed?</p>
                <p>D = 9 km/h, U = 4 km/h</p>
                <p>Still water = (9+4)/2 = <b>6.5 km/h</b></p>
            </div>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;">
                <p><b>Example 2:</b> Still water=10, stream=2. 60km round trip time?</p>
                <p>D=12, U=8 → Time = 60/12 + 60/8 = 5+7.5 = <b>12.5 hours</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Write D and U first</b> always — then derive b and s. Don't skip this step.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Round trip average:</b> 2DU/(D+U) — same as harmonic mean formula.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Man swims in river:</b> Same as boats. Stream = current speed.</li>
            </ul>`
    },

    // ───── LOGICAL REASONING ─────

    "number_series": {
        "title": "Number Series",
        "explanation": `
            <h3>What is Number Series?</h3>
            <p>Number series questions require you to find the missing number or the wrong number in a given sequence of numbers.</p>
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">Common Patterns:</h4>
                <p>• <b>Difference/Sum:</b> Add or subtract a constant or varying number.</p>
                <p>• <b>Squares/Cubes:</b> Sequence of perfect squares or cubes (e.g., n², n³, n²±1).</p>
                <p>• <b>Multiplication/Division:</b> Multiply or divide by a pattern.</p>
                <p>• <b>Alternating/Mixed Pattern:</b> Two series combined into one.</p>
            </div>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Always check the difference (d1) and double difference (d2) first.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">If numbers grow very fast → check for Multiplication or Cubes.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">If numbers grow slowly → check for Addition or Difference.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> 2, 5, 10, 17, 26, ?</p>
                <p>Differences: 3, 5, 7, 9... (odd numbers)</p>
                <p>Next difference = 11. Answer: 26 + 11 = <b>37</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Memorize squares</b> up to 30 and cubes up to 15. Many series are simply n²±1 or n³±1.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Double difference method:</b> When the first differences don't make sense, find the difference of differences.</li>
            </ul>`
    },

    "alphabet_series": {
        "title": "Alphabet Series",
        "explanation": `
            <h3>What is Alphabet Series?</h3>
            <p>A sequence of letters following a specific mathematical pattern based on their alphabetical positions.</p>
            <div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;">
                <h4 style="margin-bottom:10px;">EJOTY Shortcut:</h4>
                <p>E=5, J=10, O=15, T=20, Y=25.</p>
                <p>Use this to quickly find alphabetical ranks without counting from A every time.</p>
            </div>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Forward Rank: A=1 to Z=26</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Backward Rank = 27 - Forward Rank</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Opposite Pairs: A-Z, B-Y, C-X, D-W (Sum of ranks = 27)</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> A, C, F, J, ?</p>
                <p>Positions: 1, 3, 6, 10...</p>
                <p>Differences: +2, +3, +4. Next difference is +5.</p>
                <p>Position 15 = <b>O</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Write down A-M and N-Z below it</b> on your rough sheet during the exam to quickly see opposite pairs.</li>
            </ul>`
    },

    "alphanumeric_series": {
        "title": "Alphanumeric Series",
        "explanation": `
            <h3>What is Alphanumeric Series?</h3>
            <p>Sequences containing letters, numbers, and sometimes symbols. You must find the missing term or analyze the pattern.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Treat the numbers and letters as separate alternating series.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Pay attention to 'preceded by' (comes before) and 'followed by' (comes after).</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> 2B, 4C, 8E, 14H, ?</p>
                <p>Numbers: 2, 4, 8, 14 (+2, +4, +6). Next is +8 → 22.</p>
                <p>Letters: B(2), C(3), E(5), H(8). Diff: +1, +2, +3. Next is +4 → 12 (L).</p>
                <p>Answer: <b>22L</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Break it down:</b> Solve the number pattern first, then the letter pattern.</li>
            </ul>`
    },

    "coding_decoding": {
        "title": "Coding – Decoding",
        "explanation": `
            <h3>What is Coding – Decoding?</h3>
            <p>Words are converted to artificial language rules. You must decipher the logic and apply it to a new word.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Letter shifting: Letters shifted by +1, -2, etc.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Reversal: The entire word or pairs of letters are reversed.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Substitution: A letter is replaced directly by a number or symbol.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> If DOG is coded as FQI, how is CAT coded?</p>
                <p>D(+2)=F, O(+2)=Q, G(+2)=I. Logic is +2.</p>
                <p>C(+2)=E, A(+2)=C, T(+2)=V. Answer: <b>ECV</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Write the rank numbers</b> above the letters to instantly spot addition/subtraction patterns.</li>
            </ul>`
    },

    "blood_relations": {
        "title": "Blood Relations",
        "explanation": `
            <h3>What is Blood Relations?</h3>
            <p>Questions test your ability to determine familial relationships based on a chain of given facts.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Male: Represented by a square or (+) sign.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Female: Represented by a circle or (-) sign.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Siblings: Horizontal line (-).</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Generations: Vertical line (|) for parent-child.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Couples: Double line (=).</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> Pointing to a photograph, a man said, "I have no brother, and that man's father is my father's son." Whose photograph was it?</p>
                <p>The speaker has no brother, so "my father's son" is the speaker himself.</p>
                <p>Therefore, "that man's father is the speaker".</p>
                <p>Answer: <b>His son's photograph</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Draw a family tree diagram:</b> Never solve blood relation problems mentally if there are more than 3 people involved.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Work backwards:</b> Start from the end of the sentence (e.g., "my father's son").</li>
            </ul>`
    },

    "direction_sense": {
        "title": "Direction Sense Test",
        "explanation": `
            <h3>What is Direction Sense?</h3>
            <p>Determine the final direction or distance of a person from their starting point after traveling in multiple directions.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Standard compass map: North is Up, South is Down, East is Right, West is Left.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Pythagoras Theorem: Distance² = Base² + Height² (for shortest distance).</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">When facing North: Left = West, Right = East. When facing South, it's reversed.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> Walk 3km North, turn right walk 4km. Shortest distance from start?</p>
                <p>Base = 4, Height = 3.</p>
                <p>Dist² = 3² + 4² = 9 + 16 = 25. Dist = <b>5km</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Always draw a quick sketch</b> as you read the question. Don't wait till the end.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>A right turn means 90° clockwise.</b> A left turn means 90° anti-clockwise.</li>
            </ul>`
    },

    "syllogism": {
        "title": "Syllogism",
        "explanation": `
            <h3>What is Syllogism?</h3>
            <p>Syllogism involves determining if conclusions logically follow from given statements (premises), regardless of real-world facts.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Universal Affirmative: All A are B</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Universal Negative: No A is B</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Particular Affirmative: Some A are B</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Particular Negative: Some A are not B</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Statements:</b> All cats are dogs. Some dogs are birds.</p>
                <p><b>Conclusions:</b> I. Some cats are birds. / II. Some dogs are cats.</p>
                <p>Conclusion I does not follow (no direct link). Conclusion II follows directly from the first statement.</p>
                <p>Answer: <b>Only II follows</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Always draw a Venn Diagram</b> for the given statements before reading the conclusions. Read strict 'definitely true' conditions.</li>
            </ul>`
    },

    "venn_diagrams": {
        "title": "Venn Diagrams",
        "explanation": `
            <h3>What are Venn Diagrams?</h3>
            <p>Using circles to represent sets and their logical relationships algebraically and visually.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">n(A ∪ B) = n(A) + n(B) - n(A ∩ B)</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">For three sets: n(A ∪ B ∪ C) = n(A)+n(B)+n(C) - n(A∩B) - n(B∩C) - n(C∩A) + n(A∩B∩C)</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> 50 like Tea, 40 like Coffee, 20 like both. Total distinct people?</p>
                <p>Total = 50 + 40 - 20 = <b>70 people</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Identify the 'only' regions:</b> E.g., 'Only Tea' = Total Tea - Both.</li>
            </ul>`
    },

    "order_ranking": {
        "title": "Order & Ranking",
        "explanation": `
            <h3>What is Order & Ranking?</h3>
            <p>Determining the position or rank of a person/object from the top/bottom or left/right ends of a sequence.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Total = (Rank from Left) + (Rank from Right) - 1</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Rank from Left = Total - Rank from Right + 1</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Between Two People = Total - (Left Rank + Right Rank) [For non-overlapping]</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> Rohan is 15th from left and 20th from right in a row. How many boys are there?</p>
                <p>Total = 15 + 20 - 1 = <b>34 boys</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Overlapping case:</b> If (Left + Right) > Total, then people between them = (Left + Right) - Total - 2.</li>
            </ul>`
    },

    "linear_seating": {
        "title": "Linear Seating Arrangement",
        "explanation": `
            <h3>What is Linear Seating?</h3>
            <p>Arranging people or objects in a straight line (single row or double parallel rows) based on given conditions.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Facing North: Left is your left, Right is your right.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Facing South: Left is your right, Right is your left.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> A sits immediate left of B. C sits second to right of B. Order?</p>
                <p>Order is: A, B, _, C. (Assuming North facing)</p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Start with definite information:</b> Pick the clue that anchors someone to an extreme end or gives exact gaps quickly.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Parallel Rows:</b> Draw two lines and mark the left/right for both distinctly before solving.</li>
            </ul>`
    },

    "circular_seating": {
        "title": "Circular Seating Arrangement",
        "explanation": `
            <h3>What is Circular Seating?</h3>
            <p>Arranging people around a circular (or square/rectangular) table inward or outward facing.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Facing Center: Right = Anti-clockwise, Left = Clockwise.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Facing Outside: Right = Clockwise, Left = Anti-clockwise.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> 4 friends. A is opposite C. B is immediate right of A (center facing). Who is left of A?</p>
                <p>If B is on immediate right (anti-clockwise), then the remaining person (D) is on immediate left (clockwise).</p>
                <p>Answer: <b>D</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Always draw the circle and evenly space the dashed lines</b> before putting in letters.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>"And/But"</b> refers to the first person, <b>"Who/Whose"</b> refers to the second person mentioned immediately before the comma.</li>
            </ul>`
    },

    "statement_conclusion": {
        "title": "Statement & Conclusion",
        "explanation": `
            <h3>What is Statement & Conclusion?</h3>
            <p>You need to decide which conclusion logically and definitely follows purely from the information given in the statement.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">No outside knowledge should be assumed outside of universally accepted truths.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Words like "all, always, only, definitely" in conclusions often make them invalid unless explicitly stated.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Statement:</b> In a T20 match, India scored 200 runs. 160 runs were scored by spinners.</p>
                <p><b>Conclusions:</b> I. 80% of the team consists of spinners. II. Opening batsmen were spinners.</p>
                <p>Neither follows logically (scoring runs doesn't mean team composition or batting order).</p>
                <p>Answer: <b>Neither I nor II follows</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Be objective:</b> Do not let personal opinions or outside facts interfere with the logic of the specific statement.</li>
            </ul>`
    },

    "logical_puzzles": {
        "title": "Logical Puzzles (Floor / Box / Scheduling)",
        "explanation": `
            <h3>What are Logical Puzzles?</h3>
            <p>Complex arrangements linking multiple variables (e.g., Person + Floor + Profession or Person + Box + Color).</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Create a table. Cross (X) out negative conditions explicitly.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">In floor puzzles, number floors from bottom (1) to top (n).</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example 1:</b> A lives on an even floor above floor 2 but not the top floor (Total 6 floors). Where does A live?</p>
                <p>Even floors above 2: 4, 6. Since not top (6), A must live on <b>Floor 4</b>.</p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Make multiple possibilities/cases</b> simultaneously rather than rubbing and rewriting. Eliminate cases as you read further conditions.</li>
            </ul>`
    },

    "data_sufficiency": {
        "title": "Data Sufficiency",
        "explanation": `
            <h3>What is Data Sufficiency?</h3>
            <p>You don't need to find the exact answer! You just need to determine if the given statements provide enough data to find an answer.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Check Statement I alone.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Check Statement II alone.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Only if BOTH fail individually, combine I + II and check again.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Question:</b> What is the value of x?</p>
                <p>I. x² = 25 &nbsp; II. x > 0</p>
                <p>Statement I gives x=5 or x=-5 (Not sufficient). Statement II doesn't give a value (Not sufficient).</p>
                <p>Combined: x=5. Answer: <b>Both statements combined are sufficient</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Do not calculate the final answer</b>, it wastes time. Just verify that a unique answer can be found.</li>
            </ul>`
    },

    "input_output": {
        "title": "Input – Output",
        "explanation": `
            <h3>What is Input – Output?</h3>
            <p>A machine processes a string of words and numbers following a certain pattern (sorting by alphabet, ascending/descending) step by step.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Shifting logic: Element moves from one end to another.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Replacement logic: Element is substituted by a mathematical rule.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p>Look at the Final Step: 'Apple 15 Ball 28 Cat 45'.</p>
                <p>Logic: Ascending alphabetical word followed by Ascending number.</p>
                <p>Apply this exact sequential logic to the new given input.</p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Look at the final step FIRST</b> to figure out the ultimate goal (e.g. descending order). Then look at Step 1 to figure out the process.</li>
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Auto-fill method:</b> Write initials instead of full words during solving to save massive time.</li>
            </ul>`
    },

    "critical_reasoning": {
        "title": "Critical Reasoning",
        "explanation": `
            <h3>What is Critical Reasoning?</h3>
            <p>Evaluating passages to find strengthening/weakening arguments, inferences, and central conclusions.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Strengthen: Provides evidence that makes the conclusion more likely.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Weaken: Exposes a flaw or provides counter-evidence.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Inference: What must be true based on the passage.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Argument:</b> The new highway reduced commute times by 50%.</p>
                <p><b>Weaken:</b> People are now taking longer trips because the road is better, nullifying the time saved.</p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Identify the core Conclusion</b> first. Every correct answer must relate directly to that conclusion, not just peripheral details.</li>
            </ul>`
    },

    "statement_assumption": {
        "title": "Statement & Assumption / Course of Action",
        "explanation": `
            <h3>What is Statement & Assumption?</h3>
            <p>An assumption is an unstated, hidden premise that the author must believe to be true for the argument to make sense.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Assumption Test: If the assumption is proven FALSE, the statement should collapse.</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Course of Action: Must solve the problem or minimize it without creating bigger new problems.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Statement:</b> "Please switch off mobile phones inside the theatre."</p>
                <p><b>Assumption I:</b> People sometimes ring their mobiles during movies.</p>
                <p><b>Assumption II:</b> People will ignore the notice.</p>
                <p>They put up the notice naturally assuming it will be obeyed, so II is invalid. Assumption I is a valid reason to post the sign.</p>
                <p>Answer: <b>Only Assumption I is valid</b></p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Course of action:</b> Do not select extreme actions (like firing an employee for a minor error). Choose practical, procedural steps.</li>
            </ul>`
    },

    "analytical_reasoning": {
        "title": "Analytical Reasoning (Multiple Variables)",
        "explanation": `
            <h3>What is Analytical Reasoning?</h3>
            <p>Solving highly complex conditional matrices matching entities with their attributes. Often involves 3+ variables.</p>`,
        "formulas": `
            <h3>Key Concepts</h3>
            <div style="display:grid;gap:12px;margin-top:15px;">
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Create a Grid (Tick/Cross method).</div>
                <div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Use Fixed vs Floating variables: Fix the days of the week or months on the left column because they follow natural chronological order.</div>
            </div>`,
        "examples": `
            <h3>Solved Examples</h3>
            <div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;">
                <p><b>Example:</b> 5 people drive 5 different cars to 5 different cities on 5 days of a week.</p>
                <p>Always fix 'Days of the week' on your left-hand column. Then fill in standard info.</p>
            </div>`,
        "tips": `
            <h3>Expert Tips & Tricks</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:12px;">
                <li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Negative clues are powerful.</b> "A does not drive a Honda and didn't go on Tuesday" gives massive elimination power in a grid.</li>
            </ul>`
    },

    "tabular_di": {
        "title": "Tabular Data Interpretation",
        "explanation": "<h3>What is Tabular DI?</h3><p>Information presented systematically in rows and columns. It requires reading intersecting data points and performing quick calculations.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Always read the titles and units (in thousands, percentages, etc.) before jumping into numbers.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Find the exact value by cross-referencing Row X and Column Y.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Use Approximation:</b> Don't calculate exact decimals if options are far apart.</li></ul>"
    },
    "bar_graph": {
        "title": "Bar Graph",
        "explanation": "<h3>What is a Bar Graph?</h3><p>Visual representation of data using rectangular bars where the length of the bar is proportional to the value it represents.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Observe the Y-axis scale carefully. Sometimes it starts from a non-zero value (kink).</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Comparing the heights of two bars gives you the direct ratio or difference of sales between two years.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Visual estimation:</b> You can often answer 'which year had maximum growth' just by looking at the steepness or height difference visually.</li></ul>"
    },
    "pie_chart": {
        "title": "Pie Chart",
        "explanation": "<h3>What is a Pie Chart?</h3><p>A circular graphic divided into slices to illustrate numerical proportion. The arc length of each slice is proportional to the quantity it represents.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>100% = 360 degrees</div><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>1% = 3.6 degrees</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>If a sector is 72 degrees, its percentage = (72/360)*100 = 20%.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Memorize fractions:</b> 1/4 = 90 deg, 1/3 = 120 deg. This speeds up conversions immensely.</li></ul>"
    },
    "line_graph": {
        "title": "Line Graph",
        "explanation": "<h3>What is a Line Graph?</h3><p>Displays information as a series of data points connected by straight line segments. Ideal for showing continuous changes over time.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Steep slope = rapid change. Flat line = no change.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Measuring the percentage increase of population from 2010 to 2015 by comparing the vertical displacement.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Beware of the scale:</b> Look at how much each grid line represents on the Y-axis.</li></ul>"
    },
    "simple_caselet": {
        "title": "Simple Caselet DI",
        "explanation": "<h3>What is a Caselet?</h3><p>A paragraph containing numerical data without any tables or graphs. You must construct your own table or Venn diagram to organize the data.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Read line by line and immediately tabulate it. Do not read the whole paragraph multiple times.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Out of 100 students, 40 play cricket, 60 play football. Use a 2x2 matrix or Venn diagram to classify them.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Structure first:</b> Draw the empty table outline based on the categories before filling in numbers.</li></ul>"
    },
    "percentage_di": {
        "title": "Percentage-based DI",
        "explanation": "<h3>What is Percentage DI?</h3><p>Graphs or tables where data is explicitly given in percentages, requiring constant base conversions to absolute values.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>A is what % of B? = (A/B) * 100</div><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>% Change = (Final - Initial) / Initial * 100</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>If income is 120 and expenditure is 100, profit % = (20/100)*100 = 20%.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Base matters:</b> Always double-check what the percentage is taken out of (the denominator).</li></ul>"
    },
    "multiple_bar_graph": {
        "title": "Multiple Bar Graph DI",
        "explanation": "<h3>What is a Multiple Bar Graph?</h3><p>Two or more bars grouped together for each category on the X-axis, used to compare multiple variables across time/categories.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Ensure you correctly map the legend (colors/patterns) to the respective variables.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Comparing imports (blue bar) vs exports (red bar) over 5 different years.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Visual differences:</b> To find the greatest difference between two variables, look for the widest gap in bar heights.</li></ul>"
    },
    "multiple_pie_chart": {
        "title": "Multiple Pie Chart DI",
        "explanation": "<h3>What are Multiple Pie Charts?</h3><p>Two pie charts given simultaneously. Usually, one represents the total population and the other represents a sub-population (e.g., males).</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Sub-group value = (Total % from Chart 1 * Total Value) * (Sub-group % from Chart 2)</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Chart 1: Total Employees (1000). Chart 2: Female Employees (400). Find male employees in IT dept.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Don't mix bases:</b> Never subtract percentages directly from two different pie charts if their total base values are different.</li></ul>"
    },
    "mixed_graph": {
        "title": "Mixed Graph DI",
        "explanation": "<h3>What is Mixed Graph DI?</h3><p>Data split between two different types of charts, like a Pie Chart + a Table, or a Bar Graph + a Line Graph.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Synthesize data: Extract Value A from Chart 1, and apply the ratio/percentage from Chart 2 to get the final answer.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Pie chart shows total students per state. Table shows ratio of boys to girls in those states.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Extract only what you need:</b> Do not calculate the exact table for all categories in advance. Calculate only what the question asks.</li></ul>"
    },
    "ratio_di": {
        "title": "Ratio-based DI",
        "explanation": "<h3>What is Ratio DI?</h3><p>Graphs where the y-axis directly represents a ratio (e.g., Import/Export ratio = 1.25). You must decipher absolute values based on given fragments.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Ratio > 1 means numerator > denominator. Ratio < 1 means numerator < denominator.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>If Import/Export = 0.8 and Export is 100, then Import = 0.8 * 100 = 80.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Convert to fractions:</b> Convert 1.25 to 5/4 or 0.8 to 4/5. Dealing with fractions is faster than multiplying decimals.</li></ul>"
    },
    "average_di": {
        "title": "Average-based DI",
        "explanation": "<h3>What is Average-based DI?</h3><p>Questions heavily focused on finding the mean of various fluctuating data points across months or categories from a graph.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Average = Sum of all terms / Number of terms</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Finding the average production of Company A across years 2011 to 2015.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Use deviation method:</b> Guess a central mean, calculate + and - deviations of other values, average the deviations, and add it back to the assumed mean.</li></ul>"
    },
    "data_comparison": {
        "title": "Data Comparison DI",
        "explanation": "<h3>What is Data Comparison?</h3><p>Instead of finding exact values, you must deduce which quantity is larger, or arrange them in ascending/descending order.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Visual estimation is paramount. Compare fractions by cross-multiplication.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Which year showed the maximum percentage growth compared to the previous year?</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Look for low base, high gap:</b> Maximum percentage growth usually happens when the previous year's value was visibly low and the jump is high.</li></ul>"
    },
    "complex_caselet": {
        "title": "Complex Caselet DI",
        "explanation": "<h3>What is a Complex Caselet?</h3><p>Lengthy paragraphs involving 3 or more variables (e.g., Men, Women, Children across 4 different departments with sub-conditions).</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Create a rigid matrix structure before filling data. Fill absolute numbers and define unknowns as 'x' or 'y'.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>A town has 5000 people. 30% are male, out of male 20% are engineers... Fill out the matrix comprehensively.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Link the clues:</b> Clues in line 6 might be required to solve the equation formed in line 2. Build the full tree.</li></ul>"
    },
    "missing_data": {
        "title": "Missing Data DI",
        "explanation": "<h3>What is Missing Data DI?</h3><p>A table or chart is provided with deliberate blank spaces or question marks. You have to deduce the missing values using total sums or separate clues.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Total = (Sum of knowns) + (Sum of unknowns). Deduce unknowns hierarchically.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>A table of class marks. Total is given as 500. Sum of 4 subjects is 420. Missing subject = 80.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Don't calculate every blank:</b> Only solve for the blanks that are explicitly demanded by the specific question.</li></ul>"
    },
    "arithmetic_di": {
        "title": "Arithmetic-based DI",
        "explanation": "<h3>What is Arithmetic DI?</h3><p>DI sets based strictly on arithmetic topics like Time & Work, Speed Distance Time, Simple Interest, or Profit & Loss.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Apply the fundamental arithmetic formulas (e.g., SI = PRT/100) using the variables presented visually.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>A bar graph showing the 'Speed of Boat' and 'Speed of Stream' for 5 different rivers on different days.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Master arithmetic basics first:</b> You cannot solve Arithmetic DI without a strong grasp of the foundational quantitative formulas.</li></ul>"
    },
    "data_sufficiency_di": {
        "title": "Data Sufficiency (DI)",
        "explanation": "<h3>What is Data Sufficiency (DI)?</h3><p>Deciding whether the data given in Statements I, II, or III combined with a graph is adequate to find a unique answer to the question asked.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Never calculate the final answer. Just verify you have enough non-redundant variables to solve the equation.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Find total sales. Statement 1: Profit is 20%. Statement 2: Cost price is 5000. Combined, they are sufficient.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Watch out for redundancy:</b> If statement II provides the same relative ratio as the graph already gives, it is useless.</li></ul>"
    },
    "logical_di": {
        "title": "Logical DI",
        "explanation": "<h3>What is Logical DI?</h3><p>A hybrid of Logical Puzzles and DI. It uses numbers but follows complex logic rules, max-min logic, and game theories (e.g., tournaments, betting, token exchange).</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Understand the flow of the puzzle. Form extreme case assumptions (What is the maximum possible? What is the minimum?).</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>A round-robin tournament table where win, loss, and draw points are given, but half the table is obscured.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Look for the anchor point:</b> Look for the person who won ALL games or LOST all games to start filling the matrix easily.</li></ul>"
    },
    "advanced_mixed_di": {
        "title": "Advanced Mixed DI",
        "explanation": "<h3>What is Advanced Mixed DI?</h3><p>Interlinked 3+ visual representations (e.g., Pie Chart + Radar Graph + Funnel Chart) representing layers of a funnel or massive comparative datasets.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Flowchart methodology: Track a single variable as it passes through the filters represented by the multiple charts.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Chart 1: Applicant Pool. Chart 2: Cleared Written. Chart 3: Cleared Interview. Calculate attrition rate.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Beware of the changing base:</b> The 10% in Chart 2 is likely 10% of the SUB-POOL from Chart 1, not the absolute total.</li></ul>"
    },
    "spotting_errors": {
        "title": "Spotting Errors",
        "explanation": "<h3>What is Spotting Errors?</h3><p>Identifying grammatical, syntactical, or vocabulary errors in a given sentence structure.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Focus heavily on Subject-Verb Agreement, Tense Consistency, Prepositions, and Articles.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Incorrect: 'One of the boy is missing.' Correct: 'One of the boys is missing.'</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Elimination Strategy:</b> Read the sentence silently. Often, your brain will naturally stumble on the awkward phrasing before you consciously spot the grammar rule.</li></ul>"
    },
    "synonyms": {
        "title": "Synonyms",
        "explanation": "<h3>What are Synonyms?</h3><p>Words that have exactly or nearly the same meaning as another word in the same language.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Context dictates meaning. A word might have multiple synonyms depending on how it's used in a sentence.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Abundant -> Plentiful, Copious. Fastidious -> Meticulous, Particular.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Root words:</b> Knowing Greek and Latin roots (e.g., 'bene' = good) can help you guess definitions of unknown words.</li></ul>"
    },
    "antonyms": {
        "title": "Antonyms",
        "explanation": "<h3>What are Antonyms?</h3><p>Words opposite in meaning to another (e.g., good and bad).</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Prefixes often form antonyms (un-, in-, dis-, non-, anti-).</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Cacophony -> Harmony. Ephemeral -> Permanent.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Beware the trick:</b> Exams often place the exact synonym as Option A to trick rushed students who forgot they were looking for an antonym.</li></ul>"
    },
    "spellings": {
        "title": "Spellings",
        "explanation": "<h3>What are Spelling Tests?</h3><p>Identifying the correctly or incorrectly spelled word among a set of similar looking options.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>'I before E, except after C' (with exceptions like weird, their).</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Correct: Accommodation (two C's, two M's). Correct: Embarrass (two R's, two S's).</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Write them out:</b> If confused, write down the word on scratch paper before looking at the options. Muscle memory often spells it correctly.</li></ul>"
    },
    "selecting_words": {
        "title": "Selecting Words",
        "explanation": "<h3>What is Selecting Words?</h3><p>Also known as fill-in-the-blanks, it requires choosing the most appropriate word to complete a sentence's meaning logically and grammatically.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Prepositional collocations (e.g., 'accused of', 'addicted to') dictate the correct word choice.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>He is _____ of spider. (Option: scared / afraid). Answer: afraid, because it is followed by 'of'.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Tone matching:</b> A formal sentence requires a formal word choice, even if an informal synonym is available.</li></ul>"
    },
    "one_word_substitution": {
        "title": "One Word Substitution",
        "explanation": "<h3>What is One Word Substitution?</h3><p>Replacing a roundabout, wordy phrase with a single, precise word to improve vocabulary and sentence crispness.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Suffixes hint at meaning: '-cide' (killing), '-logy' (study of), '-phobia' (fear).</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>'A person who loves books' -> Bibliophile. 'Study of birds' -> Ornithology.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Group learning:</b> Learn these in thematic batches (e.g., types of doctors, types of governments, types of fears).</li></ul>"
    },
    "sentence_formation": {
        "title": "Sentence Formation",
        "explanation": "<h3>What is Sentence Formation?</h3><p>Connecting given clauses or fragments to construct a meaningful, grammatically sound sentence.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Subject + Verb + Object remains the core structure of English sentences.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Fragments: (1) to the store (2) went (3) John. Ordered: (3) -> (2) -> (1).</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Find the subject first:</b> Identify 'who' or 'what' is performing the action, then locate the action (verb).</li></ul>"
    },
    "sentence_correction": {
        "title": "Sentence Correction",
        "explanation": "<h3>What is Sentence Correction?</h3><p>Replacing an underlined portion of a sentence with a grammatically superior alternative from the given options.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Parallelism, Pronoun ambiguity, and Misplaced Modifiers are the most frequently tested concepts here.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Wrong: I like running, swimming, and to hike. Correct: I like running, swimming, and hiking. (Parallelism)</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Shorter is often better:</b> If two options are grammatically correct, the more concise one without redundancy is usually the answer.</li></ul>"
    },
    "sentence_improvement": {
        "title": "Sentence Improvement",
        "explanation": "<h3>What is Sentence Improvement?</h3><p>Similar to sentence correction, but also tests stylistic choices, vocabulary up-gradation, and conciseness, not just raw grammar.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Avoid redundancy (e.g., 'return back' -> 'return', 'past history' -> 'history').</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Original: He was a man of very few words. Improved: He was taciturn.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Check 'No Improvement':</b> Around 15-20% of these questions are already perfect. Don't force a change if it sounds right.</li></ul>"
    },
    "completing_statements": {
        "title": "Completing Statements",
        "explanation": "<h3>What is Completing Statements?</h3><p>A partial sentence is provided, and you must select the logical clause that completes its meaning flawlessly.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Conjunctions act as road signs. 'Although' signals a contrast. 'Therefore' signals a result.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>'Although he was utterly exhausted, _____' -> (he continued working through the night).</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Predict the ending:</b> Cover the options, guess how the sentence *should* logically end, and then find the match.</li></ul>"
    },
    "ordering_words": {
        "title": "Ordering of Words",
        "explanation": "<h3>What is Ordering Words?</h3><p>Jumbled parts (P, Q, R, S) of a single sentence need to be arranged to make a meaningful, grammatical sentence.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Identify mandatory pairs: Nouns + relative pronouns (e.g., 'The man' + 'who was running').</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>(P) the boy (Q) in the red shirt (R) is (S) my brother. -> P - Q - R - S.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Start and End:</b> Prepositions rarely end sentences. Subjects usually start them. Eliminate options based on the first/last letter.</li></ul>"
    },
    "ordering_sentences": {
        "title": "Ordering of Sentences",
        "explanation": "<h3>What are Para Jumbles?</h3><p>Arranging 4-6 randomized, complete sentences into a logical, coherent paragraph.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Look for transition words: First, However, Therefore. Look for pronouns (He, They) pointing back to nouns in previous sentences.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>A sentence starting with 'This device' must logically follow the sentence that introduces the device's name.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Spot the introductory sentence:</b> The sentence that establishes the generalized theme, without using pronouns or conjunctions, is always first.</li></ul>"
    },
    "paragraph_formation": {
        "title": "Paragraph Formation",
        "explanation": "<h3>What is Paragraph Formation?</h3><p>Synthesizing disconnected ideas into a structured narrative flow, often involving determining the main theme and supporting details.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Chronological order: Time-based events naturally flow from past to present to future.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Arranging historical events: Cause -> Event -> Immediate Effect -> Long-term Consequence.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>General to Specific:</b> Paragraphs generally move from a broad overarching statement down to specific examples and data points.</li></ul>"
    },
    "cloze_test": {
        "title": "Cloze Test",
        "explanation": "<h3>What is a Cloze Test?</h3><p>A paragraph with 5-10 numbered blanks. You must select the right vocabulary and grammar to fill each blank, maintaining the passage's overall tone.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Forward/Backward reading: The clue to blank #3 is often hidden in sentence #4.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>He is an ____ worker. He never takes breaks. (Options: lazy, erratic, industrious). Answer: industrious.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Skimming first:</b> ALWAYS read the entire passage quickly ignoring the blanks first to understand the overarching theme (e.g., is it positive or negative?).</li></ul>"
    },
    "reading_comprehension": {
        "title": "Reading Comprehension",
        "explanation": "<h3>What is Reading Comprehension?</h3><p>Reading a dense 300-800 word passage and answering questions testing your ability to extract facts, infer author tone, and summarize ideas.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Fact vs Inference: Facts are explicitly written. Inferences are deductions based strictly on the text, not outside knowledge.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Question: 'What is the author's primary purpose?' (Requires understanding the holistic passage, not just one paragraph).</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Keywords scanning:</b> Don't memorize the passage. Identify keywords in the question, and scan the text to locate that specific data point.</li></ul>"
    },
    "idioms_phrases": {
        "title": "Idioms and Phrases",
        "explanation": "<h3>What are Idioms?</h3><p>Expressions whose meaning is not predictable from the usual meanings of its constituent words.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Literal translation is always a trap option in multiple choice questions.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>'Bite the bullet' -> to face a difficult situation courageously.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Contextual guessing:</b> If you don't know the idiom, read the rest of the sentence to deduce whether it implies something positive, negative, fast, or slow.</li></ul>"
    },
    "change_of_voice": {
        "title": "Change of Voice",
        "explanation": "<h3>What is Active to Passive Voice?</h3><p>Converting sentences so the subject reflects the recipient of the action rather than the doer, without changing tense.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Object becomes Subject. Subject becomes Object (by...). Auxiliary verb is modified (e.g., is -> is being). V3 (past participle) is always used.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Active: The chef cooked the meal. Passive: The meal was cooked by the chef.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Check the tense:</b> If the active sentence is past continuous, the passive MUST be past continuous. Tense never shifts in Voice change!</li></ul>"
    },
    "change_of_speech": {
        "title": "Change of Speech",
        "explanation": "<h3>What is Direct to Indirect Speech?</h3><p>Reporting what someone said without using their exact words or quotation marks, requiring shifts in pronouns and tenses.</p>",
        "formulas": "<h3>Key Concepts</h3><div style='display:grid;gap:12px;margin-top:15px;'><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;'>Unlike Voice, Tense SHIFTS back in time here. (Present -> Past, Past -> Past Perfect). 'Tomorrow' -> 'The next day'.</div></div>",
        "examples": "<h3>Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p>Direct: He said, 'I am working.' Indirect: He said that he was working.</p></div>",
        "tips": "<h3>Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>🔥 <b>Universal truths bypass rules:</b> If the statement is a universal truth ('The sun rises in the east'), the tense NEVER changes in reported speech.</li></ul>"
    },

    // ───── NON-VERBAL REASONING — BASIC ─────

    "nv_series": {
        "title": "Series (Non-Verbal)",
        "explanation": `<h3>What is Non-Verbal Series?</h3><p>A sequence of figures that follow a visual pattern. Your task is to identify the rule governing the changes (rotation, size, shading, number of elements) and select the next figure.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Common Patterns:</h4><p>• <b>Rotation:</b> Figures rotate 45°, 90°, 180° clockwise/anti-clockwise.</p><p>• <b>Size Change:</b> Figures grow or shrink progressively.</p><p>• <b>Shading:</b> Shaded portion shifts position each step.</p><p>• <b>Addition/Removal:</b> Elements are added or removed each step.</p></div>`,
        "formulas": `<h3>Key Approaches</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Step 1: Find what changes between figure 1→2. Step 2: Verify with 2→3. Step 3: Apply the rule to 3→4.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Check rotation angle, number of sides, shading pattern, and position of inner elements separately.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Example 1:</b> Triangle → Square → Pentagon → ?</p><p>Pattern: Sides increase by 1 each step.</p><p>Answer: <b>Hexagon (6 sides)</b></p></div><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example 2:</b> Arrow pointing right → down → left → ?</p><p>Pattern: Rotating 90° clockwise each step.</p><p>Answer: <b>Arrow pointing up</b></p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Isolate one element at a time:</b> Analyse shading, shape, and size separately before combining.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Rotation shortcut:</b> Check if the figure looks the same after 90° vs 180° — many tricks hide here.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Eliminate wrong options:</b> Cancel any option that violates even one part of the pattern.</li></ul>`
    },

    "nv_analogy": {
        "title": "Analogy (Non-Verbal)",
        "explanation": `<h3>What is Non-Verbal Analogy?</h3><p>Two figures are related in a specific way (Figure A : Figure B). You must apply the same relationship to Figure C and find Figure D from the given options.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Key Relationships:</h4><p>• <b>Mirror/Flip:</b> B is the horizontal or vertical mirror of A.</p><p>• <b>Rotation:</b> B is A rotated by a fixed angle.</p><p>• <b>Addition/Removal:</b> A specific element is added or removed from A to get B.</p><p>• <b>Shading reversal:</b> Black parts become white and vice versa.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">A is to B → identify transformation → apply to C → find D.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Common transformations: Rotate 90°/180°, Mirror (H/V), Scale up/down, Add/remove inner shapes.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Example:</b> Square with a dot inside : Circle with a dot inside :: Triangle with a dot inside : ?</p><p>Relationship: The outer shape changes but the inner dot is preserved.</p><p>Answer: <b>Pentagon with a dot inside</b></p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>State the rule in words</b> before looking at options — prevents visual confusion.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Check shading and line type</b> (solid vs dashed) — often the hidden differentiator.</li></ul>`
    },

    "nv_classification": {
        "title": "Classification (Non-Verbal)",
        "explanation": `<h3>What is Non-Verbal Classification?</h3><p>Among 4 or 5 given figures, all but one share a specific visual property. You must identify the ODD ONE OUT — the figure that doesn't fit the group.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Common grouping rules:</h4><p>• Same number of sides</p><p>• Same shading pattern</p><p>• Same orientation/rotation</p><p>• Same symmetry (symmetric vs asymmetric)</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Group figures by: (1) Shape type, (2) Number of sides, (3) Shading, (4) Symmetry, (5) Orientation.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> Triangle, Square, Pentagon, Circle, Rectangle</p><p>All except Circle have straight sides/edges.</p><p>Odd one out: <b>Circle</b></p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Count elements:</b> The odd figure often differs in the count of lines, dots, or angles.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Think symmetry:</b> Some sets group figures by axis of symmetry — vertical, horizontal, or both.</li></ul>`
    },

    "nv_mirror_images": {
        "title": "Mirror Images",
        "explanation": `<h3>What are Mirror Images?</h3><p>When a figure is placed in front of a mirror, its reflection is the mirror image. In exams, a figure is shown and you must choose its correct mirror image from the options.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Types of Mirrors:</h4><p>• <b>Vertical mirror (left ↔ right):</b> Left and right sides are swapped. Top and bottom remain same.</p><p>• <b>Horizontal mirror (top ↔ bottom):</b> Top and bottom are swapped. Left and right remain same.</p></div>`,
        "formulas": `<h3>Key Rules</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Vertical mirror: Left ↔ Right (most common in exams).</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Letters: b↔d, p↔q, F→mirrored-F, R→mirrored-R.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Symmetric letters/digits unchanged in vertical mirror: A, H, I, M, O, T, U, V, W, X, Y | 0, 8.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Example 1:</b> Mirror image of the letter 'F'?</p><p>F faces right → mirror image faces left (like a backwards F).</p></div><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example 2:</b> Mirror image of '3'?</p><p>3 opens to the right → mirror image opens to the left (like ε).</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Mentally fold the image:</b> Imagine folding the page along the mirror line — what would you see on the other side?</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Clock test:</b> Mirror image of a clock at 3:00 shows 9:00 on a vertical mirror. Use this to verify complex figures.</li></ul>`
    },

    "nv_water_images": {
        "title": "Water Images",
        "explanation": `<h3>What are Water Images?</h3><p>A water image is the reflection of a figure in still water — equivalent to a <b>horizontal mirror</b> (upside-down reflection). The top and bottom are swapped, but left and right remain the same.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Water Image vs Mirror Image:</h4><p>• <b>Mirror Image:</b> Left ↔ Right swapped (vertical flip).</p><p>• <b>Water Image:</b> Top ↔ Bottom swapped (horizontal flip / upside-down).</p></div>`,
        "formulas": `<h3>Key Rules</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Water image = figure flipped upside down. Top becomes bottom, bottom becomes top.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Symmetric horizontally (top=bottom): A, C, D, E, H, I, K, O, X — look same in water.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Example:</b> Water image of the letter 'A'?</p><p>A has horizontal symmetry → its water image looks the same (∧ → ∨ shape).</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Rotate your paper 180° mentally</b> — that is the water image of any figure.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Don't confuse with mirror:</b> Water = upside down. Mirror = left-right flipped. The question always specifies which.</li></ul>`
    },

    "nv_embedded_images": {
        "title": "Embedded Images",
        "explanation": `<h3>What are Embedded Images?</h3><p>A simple figure (key figure) is hidden within a complex figure. You must find which of the given complex figures contains the key figure exactly (without distortion, rotation is usually allowed unless specified).</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>What to look for:</h4><p>• The key figure must appear exactly as given (same size, same angles).</p><p>• Parts of the key figure may be shared with other lines in the complex figure.</p><p>• Do not allow distortion — only exact shapes count.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Trace only the lines of the key figure inside the complex image without lifting your pencil.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> Key figure: a simple triangle. Complex figure has many overlapping shapes.</p><p>Strategy: Identify any 3 lines forming the triangle's exact angles inside the complex figure.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Count the sides:</b> If key is a 4-sided figure, scan the complex figure for exactly 4 connected line segments.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Use corners:</b> Unique angles in the key figure are the easiest feature to match inside the complex one.</li></ul>`
    },

    // ───── NON-VERBAL REASONING — INTERMEDIATE ─────

    "nv_figure_matrix": {
        "title": "Figure Matrix",
        "explanation": `<h3>What is Figure Matrix?</h3><p>A 3×3 grid of figures where all cells follow a row-wise and column-wise pattern. One cell (usually bottom-right) is missing and must be determined from options.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Common Rules:</h4><p>• Each row has a consistent transformation (rotation, shading, count).</p><p>• Each column also satisfies a separate or same rule.</p><p>• Combining row and column rules together gives the answer.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Analyse Row 1 → Row 2 → derive rule → verify with Column → apply to find missing.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Check: rotation, shading, number of elements, size, position of inner figures.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> Each row has Circle, Square, Triangle with increasing shading (white→grey→black). The missing cell in row 3, col 3 should be a <b>black triangle</b>.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Check both row AND column:</b> The answer must satisfy both the row rule and the column rule simultaneously.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Use elimination:</b> If an option violates either rule, discard it immediately.</li></ul>`
    },

    "nv_pattern_completion": {
        "title": "Pattern Completion",
        "explanation": `<h3>What is Pattern Completion?</h3><p>A large figure or design is shown with a part cut out (marked with '?'). You must select the piece from options that correctly fills the gap to complete the overall pattern without any break or mismatch.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Key focus areas:</h4><p>• Line continuity at edges of the missing piece.</p><p>• Shading or color must match surrounding area.</p><p>• The piece must fit without rotation (unless stated).</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Examine all 4 edges of the missing region. The correct piece must have matching lines/patterns on every edge.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Strategy:</b> Check the top-left corner of the missing space — it must connect seamlessly with the existing figure. Then check the right edge, then the bottom edge. Only one option will pass all checks.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Edge-first approach:</b> Focus on the boundary lines of the missing piece rather than the center design.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Look for symmetry:</b> If the main figure is symmetric, the missing piece must also be consistent with the axis of symmetry.</li></ul>`
    },

    "nv_paper_folding": {
        "title": "Paper Folding",
        "explanation": `<h3>What is Paper Folding?</h3><p>A square sheet of paper is folded once (or more times) along a specified line. You must determine how the paper looks when unfolded — specifically, where the holes or cut marks appear.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Key Concepts:</h4><p>• A hole punched after folding creates <b>multiple holes</b> when unfolded (mirror positions).</p><p>• Fold direction determines the axis of reflection.</p><p>• Layers stack → each punch creates marks on all layers.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">When folded and punched → unfold mentally by reflecting the hole across the fold line. Number of holes = 2ⁿ where n = number of folds.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> Paper folded once (vertically). Hole punched on the right side near center.</p><p>When unfolded: 2 holes appear — one on the right and one mirror-positioned on the left.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Use actual paper:</b> Practice by folding real paper and punching holes — the visual memory is extremely powerful.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Reflect carefully:</b> Reflect the hole position across the exact fold line, not the center of the paper.</li></ul>`
    },

    "nv_paper_cutting": {
        "title": "Paper Cutting",
        "explanation": `<h3>What is Paper Cutting?</h3><p>A sheet is folded and then a portion is cut away. When unfolded, you must identify the resulting shape/pattern. This combines folding logic with cut geometry.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Key Concepts:</h4><p>• A diagonal cut on a folded corner creates triangle cutouts.</p><p>• A cut along the fold line removes a strip symmetrically.</p><p>• More folds = more copies of the cut pattern when unfolded.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Step 1: Note all fold lines. Step 2: Find what is cut. Step 3: Unfold mentally — each fold reflects the cut symmetrically.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> Paper folded once diagonally. A triangular piece cut from the folded edge.</p><p>When unfolded: A square or diamond-shaped hole appears (two reflected triangles joined).</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Work backwards:</b> In the options, count expected holes. With n folds and 1 cut, you get 2ⁿ identical cut sections.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Cut on fold = symmetric shape:</b> A V-cut on the fold line creates a diamond when unfolded.</li></ul>`
    },

    "nv_grouping_images": {
        "title": "Grouping of Images",
        "explanation": `<h3>What is Grouping of Images?</h3><p>Several figures are given (typically 9). You must classify them into 3 groups of 3, where each group shares a common visual property. Multiple valid-looking groups may be present — find the most consistent grouping.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Common Grouping Criteria:</h4><p>• Same outer shape (circle, square, triangle, etc.)</p><p>• Same inner design or symbol</p><p>• Same shading or fill pattern</p><p>• Same number of sides or elements</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Pick one clear property first (e.g., shape). Group all figures sharing that property. Verify the remaining figures form exactly 2 more groups.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> 9 figures — 3 with circles, 3 with triangles, 3 with squares as outer shapes.</p><p>Grouping: {1,4,7} circles | {2,5,8} triangles | {3,6,9} squares.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Start with the most obvious property</b> — shape or shading is usually the clearest grouping factor.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Verify cross-properties:</b> A secondary property (like inner design) often confirms or refines your grouping.</li></ul>`
    },

    "nv_shape_construction": {
        "title": "Shape Construction",
        "explanation": `<h3>What is Shape Construction?</h3><p>Multiple pieces (given separately) must be mentally assembled to form a specific shape — usually a square, triangle, or rectangle. You must identify which combination of pieces forms the complete shape.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Key Concepts:</h4><p>• Pieces must fit without overlap and without gaps.</p><p>• Pieces may be rotated but not flipped (unless the question allows it).</p><p>• The total area of pieces = area of target shape.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Step 1: Estimate total area of target shape. Step 2: Identify which pieces sum to that area. Step 3: Mentally slot pieces together checking edge compatibility.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> Target: large square. Pieces: two right-angled triangles of equal size.</p><p>Placing the two triangles hypotenuse-to-hypotenuse forms the square. ✓</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Match edges first:</b> Find pieces whose edge lengths are equal — these fit together.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Area check:</b> Quickly eliminate options where the combined area clearly doesn't match the target.</li></ul>`
    },

    // ───── NON-VERBAL REASONING — ADVANCED ─────

    "nv_cubes_dice": {
        "title": "Cubes and Dice",
        "explanation": `<h3>What are Cubes and Dice Problems?</h3><p>These problems test your ability to visualize 3D objects. You may be asked about opposite faces, visible faces, or how a painted cube looks when cut. Dice problems require knowing which faces are opposite each other.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Standard Dice:</h4><p>Opposite face pairs: 1↔6, 2↔5, 3↔4. Opposite faces always sum to 7.</p><h4>Cube Painting:</h4><p>If a cube is painted and cut into n³ smaller cubes: 3-face painted = 8 (corners), 2-face painted = 12(n−2), 1-face painted = 6(n−2)², 0-face painted = (n−2)³.</p></div>`,
        "formulas": `<h3>Key Formulas</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Standard die: opposite faces sum to 7 (1↔6, 2↔5, 3↔4).</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Cube cut into n×n×n: Corners(3 faces) = 8 | Edges(2 faces) = 12(n−2) | Faces(1 face) = 6(n−2)² | Inside(0 faces) = (n−2)³</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Example 1:</b> A cube painted red on all faces, cut into 27 smaller cubes. How many have exactly 2 painted faces?</p><p>n=3 → 12(3−2) = 12 × 1 = <b>12 cubes</b></p></div><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example 2:</b> Dice shows 1 on top, 2 facing you. What is on the bottom?</p><p>Opposite of 1 = <b>6</b></p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Memorize opposite faces:</b> 1-6, 2-5, 3-4. This solves 50% of dice questions instantly.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Non-standard dice:</b> When two positions are given, use the common-face method to derive the opposite face.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Painted cube formula:</b> Memorize the 4 formulas — they cover 100% of cube painting questions.</li></ul>`
    },

    "nv_analytical_reasoning": {
        "title": "Analytical Reasoning (Non-Verbal)",
        "explanation": `<h3>What is Analytical Reasoning?</h3><p>Complex visual puzzles where multiple rules, conditions, and visual relationships must be analyzed simultaneously to arrive at the answer. Questions test your ability to track changes in position, shading, shape, and count across figures.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Types of questions:</h4><p>• Multi-step transformation sequences.</p><p>• Figure sets where all but one follow a rule.</p><p>• Finding the figure that completes a logical set.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">List all observable properties → find which property changes systematically → identify the rule → apply to find answer.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> In a set of 5 figures, 4 are symmetric. One is not. The non-symmetric figure = odd one out. Strategy: check each figure for symmetry along vertical/horizontal axis.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>List properties systematically:</b> Write: shape, shading, rotation, count, symmetry. This prevents missing a hidden rule.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>One rule at a time:</b> Confirm one rule fully before moving to the next. Don't try to spot everything at once.</li></ul>`
    },

    "nv_rule_detection": {
        "title": "Rule Detection",
        "explanation": `<h3>What is Rule Detection?</h3><p>A set of figures is given that follow a specific underlying rule. You must identify that rule from the first set and then apply it to a second set to find the missing figure. It is a higher-order analogy problem.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Common rules to detect:</h4><p>• Clockwise rotation of a specific element.</p><p>• Progressive increase/decrease in number of elements.</p><p>• Alternating shading pattern.</p><p>• Combination of two or more simple rules.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Set 1: Observe rule. → Set 2: Apply exact same rule → Find the answer figure.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> Set 1: Small square inside large square → circle inside large square. Rule: inner shape changes to circle. Set 2: Small triangle inside pentagon → <b>circle inside pentagon</b>.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>State the rule explicitly:</b> Write it in one clear sentence before applying it to Set 2.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Beware of composite rules:</b> Some questions combine two changes — e.g., rotate AND change shading.</li></ul>`
    },

    "nv_dot_situation": {
        "title": "Dot Situation",
        "explanation": `<h3>What is Dot Situation?</h3><p>A figure containing geometric shapes (circles, triangles, rectangles, etc.) is shown with a dot placed in a specific region. You must identify which other figure from the options has a dot placed in the <b>same relative region</b> (same intersection of shapes).</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Key Concept:</h4><p>The dot must be in a region that belongs to the same combination of shapes — inside some shapes and outside others — as in the original.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Step 1: For the original dot, note: which shapes it is inside AND which it is outside. Step 2: Find the option where a dot can be placed in a region with the same membership.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> Original: Dot is inside the circle and triangle, but outside the rectangle.</p><p>Correct option: Must have a region that is inside both circle and triangle but outside the rectangle.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Define the region precisely:</b> "Inside A, inside B, outside C" — then match this description to the options.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Draw with pencil:</b> Mark which shapes overlap in each option to clearly identify regions.</li></ul>`
    },

    "nv_image_analysis": {
        "title": "Image Analysis",
        "explanation": `<h3>What is Image Analysis?</h3><p>A composite question type requiring detailed visual analysis — counting elements, comparing properties, identifying changes, or deriving conclusions from complex multi-part figures. Tests holistic visual reasoning.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>What these questions test:</h4><p>• Counting hidden lines, triangles, or shapes within a complex figure.</p><p>• Identifying changes between two apparently identical figures.</p><p>• Analysing patterns in a figure to answer multiple sub-questions.</p></div>`,
        "formulas": `<h3>Key Approach</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">For counting triangles: count by size (smallest, medium, large) and sum. Avoid double counting by being systematic.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Formula for triangles in a star: T = n×(n+2)×(2n+1)/8 for specific configurations. Learn by practice.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Example:</b> How many triangles in a figure with 2 horizontal and 2 vertical lines crossing?</p><p>Systematic approach: Count 1-unit, 2-unit, and full triangles separately, then add.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Be systematic when counting:</b> Go from smallest to largest, mark each counted figure to avoid recounting.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Compare figures spot-the-difference:</b> Scan quadrant by quadrant (top-left, top-right, bottom-left, bottom-right).</li></ul>`
    },

    "nv_figure_matrix_problems": {
        "title": "Figure Matrix Problems",
        "explanation": `<h3>What are Figure Matrix Problems?</h3><p>An advanced version of the Figure Matrix topic, featuring larger grids, multi-element figures, and compound rules. Both row AND column logic must be simultaneously satisfied, and rules are less obvious — requiring deeper analysis.</p><div style="background:#f8fafc;padding:20px;border-radius:15px;border-left:6px solid #6c63ff;margin:20px 0;"><h4>Advanced patterns include:</h4><p>• Superimposition: Row 1 + Row 2 = Row 3 (combined figure).</p><p>• XOR logic: Elements present in exactly one of two figures appear in the third.</p><p>• Complex rotations combined with element addition.</p></div>`,
        "formulas": `<h3>Key Approaches</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Superimposition rule: Fig_C = Fig_A + Fig_B (all elements combined).</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">XOR rule: Fig_C contains elements in Fig_A or Fig_B but NOT both.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Always verify with both remaining rows/columns before finalizing answer.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;border-left:5px solid #22c55e;"><p><b>Superimposition Example:</b></p><p>Row 1: {circle, triangle}. Row 2: {square, cross}. Row 3: {circle, triangle, square, cross} — all combined.</p><p>Missing cell must contain all elements from the two cells to its left.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Test superimposition first</b> — it is the most common advanced matrix rule in competitive exams.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Count elements in each cell</b> — if counts follow a pattern (1, 2, 3 per row), the structure itself is the rule.</li><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Verify against both dimensions:</b> Check your final answer satisfies both the row rule and the column rule.</li></ul>`
    },

    // ───── PUZZLES — BASIC ─────

    "sudoku": {
        "title": "Sudoku",
        "explanation": `<h3>What is Sudoku?</h3><p>A logic-based, combinatorial number-placement puzzle. In standard 9×9 Sudoku, the objective is to fill a grid with digits so that each column, each row, and each of the nine 3×3 subgrids contain all of the digits from 1 to 9.</p>`,
        "formulas": `<h3>Rules of the Game</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Row Rule: Each row must contain numbers 1-9 without repetition.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Column Rule: Each column must contain numbers 1-9 without repetition.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Box Rule: Each 3x3 subgrid must contain numbers 1-9 without repetition.</div></div>`,
        "examples": `<h3>Solving Strategy</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Scanning:</b> Look for rows/columns that already have 7-8 numbers filled. The remaining 1-2 numbers are easy to place by elimination.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Don't guess:</b> Every move in Sudoku can be justified by logic. If you guess, you might break the whole grid later.</li></ul>`
    },

    "number_puzzles": {
        "title": "Number Puzzles",
        "explanation": `<h3>What are Number Puzzles?</h3><p>Logic puzzles involving numerical relationships, often presented in grids or shapes where a missing number must be found based on the pattern of surrounding numbers.</p>`,
        "formulas": `<h3>Common Operations</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Arithmetic: Addition, Subtraction, Multiplication, Division.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Squares/Cubes: Check if numbers are squares or cubes of their indices.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Grid:</b> 2, 4, 8 | 3, 9, 27 | 4, 16, ? <br> Logic: n, n², n³. <br> Answer: <b>64</b></p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Check the diagonal:</b> In grid puzzles, patterns often flow diagonally or from the edges toward the center.</li></ul>`
    },

    "missing_letters": {
        "title": "Missing Letters Puzzles",
        "explanation": `<h3>What are Missing Letters Puzzles?</h3><p>Finding the missing letter in a sequence or grid where letters correspond to their alphabetical positions (A=1, B=2, etc.).</p>`,
        "formulas": `<h3>Alpha-Numeric Logic</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">A=1, B=2 ... Z=26.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">E-J-O-T-Y: 5-10-15-20-25 (Reference points).</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Series:</b> A, D, G, J, ? <br> Logic: +3 (1, 4, 7, 10, 13). <br> Answer: <b>M</b></p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Convert to numbers quickly:</b> It's much easier to see a pattern in (3, 6, 9) than in (C, F, I).</li></ul>`
    },

    "picture_puzzles": {
        "title": "Picture Puzzles",
        "explanation": `<h3>What are Picture Puzzles?</h3><p>Visual logic challenges where you must find a hidden object, identify a difference, or determine the logic of a visual sequence.</p>`,
        "formulas": `<h3>Visual Scanning</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Quadrant Method: Divide the image into 4 parts and scan each systematically.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Find the Odd Shape:</b> 4 triangles facing up, 1 triangle facing down. Answer: The downward triangle.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Look for silhouettes:</b> Sometimes objects are hidden by their outlines merging with the background.</li></ul>`
    },

    "pattern_puzzles": {
        "title": "Pattern Puzzles",
        "explanation": `<h3>What are Pattern Puzzles?</h3><p>Identifying repeating sequences or transformations in geometric designs.</p>`,
        "formulas": `<h3>Symmetry & Rotation</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Mirror Symmetry: Reflection along an axis.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Rotational Logic: 90°, 180°, 270° turns.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Pattern:</b> Black dot moves clockwise from corner to corner. Answer: Next corner in clockwise direction.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Simplify:</b> Focus on only one moving part of the pattern at a time.</li></ul>`
    },

    "odd_figure": {
        "title": "Odd Figure Puzzles",
        "explanation": `<h3>What are Odd Figure Puzzles?</h3><p>Determining which figure among a set does not belong based on a shared characteristic (shading, sides, orientation).</p>`,
        "formulas": `<h3>Classification Criteria</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Geometrical properties: Number of vertices, edges, or curves.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Internal elements: Number of dots, arrows, or shaded regions.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Set:</b> Square, Rectangle, Rhombus, Circle. <br> Answer: <b>Circle</b> (it has no straight sides).</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Rule of Majority:</b> The property must apply to ALL other figures except the one you choose.</li></ul>`
    },

    // ───── PUZZLES — INTERMEDIATE ─────

    "logical_puzzles": {
        "title": "Logical Puzzles",
        "explanation": `<h3>What are Logical Puzzles?</h3><p>Verbal or numerical descriptions of a situation where you must deduce the relationships between entities (e.g., Who sits where?).</p>`,
        "formulas": `<h3>Deduction Tools</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Grid Method: Use a table to mark YES (tick) and NO (cross).</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Tree Diagram: Good for family or organizational relationships.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Clue:</b> A is taller than B. C is taller than A. Who is the tallest? Answer: <b>C</b></p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Read all clues first:</b> Sometimes the last clue gives a concrete starting point.</li></ul>`
    },

    "clock_puzzles": {
        "title": "Clock Puzzles",
        "explanation": `<h3>What are Clock Puzzles?</h3><p>Problems involving angles between hands, time loss/gain, or mirror images of clocks.</p>`,
        "formulas": `<h3>Hand Dynamics</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Angle Formula: |(30H - 5.5M)| where H is hour and M is minutes.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Minute hand moves 6° per minute. Hour hand moves 0.5° per minute.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Angle at 3:00:</b> |(30*3 - 5.5*0)| = 90°. Answer: <b>90°</b></p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Mirror Clock:</b> (11:60 - Given Time) gives the mirror image time.</li></ul>`
    },

    "calendar_puzzles": {
        "title": "Calendar Puzzles",
        "explanation": `<h3>What are Calendar Puzzles?</h3><p>Calculating the day of the week for a given date or finding number of odd days.</p>`,
        "formulas": `<h3>Odd Days Logic</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Odd Days: Remainder after dividing total days by 7.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Leap Year: Divisible by 4. Century year must be divisible by 400.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Clue:</b> If today is Monday, what day is it after 100 days? <br> 100 / 7 = Remainder 2. Monday + 2 days = <b>Wednesday</b>.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;grid-gap:12px;display:grid;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Reference Year:</b> 2000 was a Sunday (0 odd days). Use it as a base for modern dates.</li></ul>`
    },

    "math_puzzles": {
        "title": "Mathematical Puzzles",
        "explanation": `<h3>What are Mathematical Puzzles?</h3><p>Equations or word problems where you must find values of variables using creative arithmetic (e.g., Cryptarithmetic).</p>`,
        "formulas": `<h3>Key Logic</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Substitution: Replace symbols with digits 0-9.</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Zero Rule: Variables cannot start with zero in multi-digit numbers.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Puzzle:</b> A + A = B. B is twice A. If A=4, B=8. Logic must hold for the whole set.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Units Digit:</b> Always start solving from the rightmost column (units place).</li></ul>`
    },

    "dice_puzzles": {
        "title": "Dice Puzzles",
        "explanation": `<h3>What are Dice Puzzles?</h3><p>Visualizing a dice in different positions to identify faces opposite to each other.</p>`,
        "formulas": `<h3>Face Mapping</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Two positions given: If one face is common, move clockwise to map other faces.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Standard Dice:</b> Face opposite 2 is 5 (Sum=7). Face opposite 1 is 6.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Adjacent Faces:</b> A face cannot be opposite to another face if they are visible together.</li></ul>`
    },

    "matchstick_puzzles": {
        "title": "Matchstick Puzzles",
        "explanation": `<h3>What are Matchstick Puzzles?</h3><p>Rearranging or removing a specific number of matchsticks to correct an equation or create a specific shape.</p>`,
        "formulas": `<h3>Transformation Logic</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Digit Mapping: '6' can become '0', '9', or '5' by moving 1 stick.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Eq: 5+7=2.</b> Move 1 stick from '7' to '5' to make it '9-7=2'.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Think Symbols:</b> A '+' can become a '-' just by removing one stick.</li></ul>`
    },

    // ───── PUZZLES — ADVANCED ─────

    "grid_puzzles": {
        "title": "Grid Puzzles",
        "explanation": `<h3>What are Grid Puzzles?</h3><p>Complex 2D arrays where objects must be placed according to several constraints (e.g., Einstein's Riddle).</p>`,
        "formulas": `<h3>Matrix Solving</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Cross-Reference: Fill a grid with categories (Person, Color, Pet). Mark 'X' for impossible and 'O' for definite matches.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Clue:</b> The man in the Red house has a Dog. A does not live in the Red house. Result: A does not have a Dog.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Elimination is key:</b> Every 'O' you place in a cell lets you put 'X' in all other cells in that row and column.</li></ul>`
    },

    "sequence_puzzles": {
        "title": "Sequence Puzzles",
        "explanation": `<h3>What are Sequence Puzzles?</h3><p>Complex chains of numbers or symbols where the rule changes based on position or previous terms.</p>`,
        "formulas": `<h3>Advanced Series</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Fibonacci: T(n) = T(n-1) + T(n-2).</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Double Series: Two alternating patterns in one sequence.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Series:</b> 1, 2, 4, 7, 11, ? <br> Logic: +1, +2, +3, +4, +5. Answer: <b>16</b></p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Look for the gap:</b> Calculate the difference between consecutive terms first.</li></ul>`
    },

    "arrangement_puzzles": {
        "title": "Arrangement Puzzles",
        "explanation": `<h3>What are Arrangement Puzzles?</h3><p>Organizing items based on relative position, height, or preference (e.g., Seating arrangements).</p>`,
        "formulas": `<h3>Structural Logic</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Linear: A-B-C-D-E. Circular: Clockwise vs Anti-clockwise.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Clue:</b> 5 people in a row. A is at the end. B is next to A. Result: B is at 2nd or 4th position.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Draw it:</b> Never solve arrangement puzzles without a quick sketch.</li></ul>`
    },

    "symbol_puzzles": {
        "title": "Symbol Puzzles",
        "explanation": `<h3>What are Symbol Puzzles?</h3><p>Mathematical operations represented by non-standard symbols (+ means *, * means /).</p>`,
        "formulas": `<h3>Operator Decoding</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">BODMAS: Brackets, Orders, Division, Multiplication, Addition, Subtraction.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Clue:</b> If '+' is '-', '-' is '*', '*' is '/', find 10*5+3. <br> Decoded: (10/5) - 3 = 2 - 3 = <b>-1</b>.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Rewrite the equation:</b> Don't solve mentally; write the equation with NEW symbols first.</li></ul>`
    },

    "cross_number": {
        "title": "Cross Number Puzzles",
        "explanation": `<h3>What are Cross Number Puzzles?</h3><p>Numerical equivalent of a crossword where clues are math problems and answers are digits.</p>`,
        "formulas": `<h3>Grid Constraints</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Intersection check: The digit must satisfy BOTH the horizontal and vertical clue.</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Clue 1 Across:</b> A square of 12 (144). <b>Clue 1 Down:</b> A multiple of 10. Result: The first digit must be '1'.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Smallest range first:</b> Solve clues that have the fewest possible numerical solutions first.</li></ul>`
    },

    "brain_teasers": {
        "title": "Brain Teaser Puzzles",
        "explanation": `<h3>What are Brain Teasers?</h3><p>Lateral thinking puzzles that require you to look beyond the obvious wording and find a logical loophole.</p>`,
        "formulas": `<h3>Thinking Patterns</h3><div style="display:grid;gap:12px;margin-top:15px;"><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;font-family:monospace;">Identify Assumptions: What are you assuming that isn't stated?</div><div style="background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #6c63ff;font-family:monospace;">Semantic loopholes: Check if a word has multiple meanings (e.g., 'match').</div></div>`,
        "examples": `<h3>Solved Examples</h3><div style="background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;"><p><b>Riddle:</b> What has keys but can't open locks? Answer: <b>A Piano</b>.</p></div>`,
        "tips": `<h3>Expert Tips</h3><ul style="list-style:none;padding:0;display:grid;gap:12px;"><li style="background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;">🔥 <b>Occam's Razor:</b> Often the simplest explanation that fits ALL facts is the correct one.</li></ul>`
    },
"number_series": {
        "title": "Number Series",
        "explanation": "<h3>What is Number Series?</h3><p>A number series is a sequence of numbers arranged in a specific order following a definite rule or pattern. The rule could be addition, subtraction, multiplication, division, squares, cubes, or a combination of these operations between consecutive terms.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Arithmetic Series:</b> Each term differs by a constant value (common difference d). Nth term = a + (n-1)d<br><br><b>Geometric Series:</b> Each term is multiplied by a constant ratio (r). Nth term = a \u00d7 r^(n-1)<br><br><b>Square Series:</b> 1, 4, 9, 16, 25... \u2192 terms are n\u00b2<br><br><b>Cube Series:</b> 1, 8, 27, 64, 125... \u2192 terms are n\u00b3<br><br><b>Difference Series:</b> Find differences between consecutive terms, then find the pattern in those differences.<br><br><b>Fibonacci Pattern:</b> Each term = sum of previous two terms \u2192 1, 1, 2, 3, 5, 8, 13...</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> 2, 4, 8, 16, 32, ?<br>Each term \u00d7 2 \u2192 <b>Answer: 64</b></p><br><p><b>Example 2:</b> 1, 4, 9, 16, 25, ?<br>1\u00b2, 2\u00b2, 3\u00b2, 4\u00b2, 5\u00b2 \u2192 next = 6\u00b2 \u2192 <b>Answer: 36</b></p><br><p><b>Example 3:</b> 3, 5, 9, 15, 23, 33, ?<br>Differences: 2, 4, 6, 8, 10 \u2192 next difference = 12. 33 + 12 = <b>Answer: 45</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always find the difference between consecutive terms first. If differences aren't constant, find the difference of differences.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Look for squares and cubes when numbers grow rapidly.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 If the series alternates, split into two separate series (odd positions, even positions).</li></ul>"
    },
    "alphabet_series": {
        "title": "Alphabet Series",
        "explanation": "<h3>What is Alphabet Series?</h3><p>Alphabet Series is a sequence of letters arranged following a mathematical pattern based on their positions in the alphabet (A=1, B=2, C=3 ... Z=26). The pattern could involve skipping letters, reversing, or combining position values.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Position Rule:</b> A=1, B=2, C=3 ... Z=26<br><br><b>EJOTY Shortcut:</b> E=5, J=10, O=15, T=20, Y=25. Count 5 forward or backward from these anchors.<br><br><b>Reverse Position:</b> A=26, B=25 ... Z=1 (used in coding questions). Formula: 27 - forward position.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> A, C, E, G, ?<br>Positions: 1, 3, 5, 7 \u2192 +2 each \u2192 next = 9 = <b>Answer: I</b></p><br><p><b>Example 2:</b> Z, W, T, Q, ?<br>Positions: 26, 23, 20, 17 \u2192 -3 each \u2192 next = 14 = <b>Answer: N</b></p><br><p><b>Example 3:</b> B, D, G, K, P, ?<br>Differences: +2, +3, +4, +5 \u2192 next difference = +6. P = 16, 16+6 = 22 = <b>Answer: V</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Memorize EJOTY \u2014 it saves counting time in exams.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always convert letters to numbers, find the pattern, convert back.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Reverse alphabet questions: use 27 minus position number.</li></ul>"
    },
    "alphanumeric_series": {
        "title": "Alphanumeric Series",
        "explanation": "<h3>What is Alphanumeric Series?</h3><p>Alphanumeric Series contains a mix of alphabets, numbers, and sometimes symbols arranged in a specific pattern. You need to identify the rule governing both the letter part and the number part separately, then combine them to find the missing term.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Treat letters and numbers separately:</b><br>1. Find the pattern in letters alone.<br>2. Find the pattern in numbers alone.<br>3. Combine both patterns for the answer.<br><br><b>Common patterns:</b> Letters: +1, +2, +3 in position. Numbers: \u00d72, +5, squares, etc.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> A1, B4, C9, D16, ?<br>Letters: A,B,C,D \u2192 +1 \u2192 next = E. Numbers: 1,4,9,16 \u2192 squares \u2192 next = 25. <b>Answer: E25</b></p><br><p><b>Example 2:</b> Z1, X2, V4, T8, ?<br>Letters: Z,X,V,T \u2192 -2 each \u2192 next = R. Numbers: 1,2,4,8 \u2192 \u00d72 \u2192 next = 16. <b>Answer: R16</b></p><br><p><b>Example 3:</b> A2Z, B4Y, C6X, D8W, ?<br>Letters (front): A,B,C,D \u2192 +1 \u2192 E. Numbers: 2,4,6,8 \u2192 +2 \u2192 10. Letters (back): Z,Y,X,W \u2192 -1 \u2192 V. <b>Answer: E10V</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always split letters and numbers and solve independently.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Numbers often follow geometric progression in harder questions.</li></ul>"
    },
    "coding_decoding": {
        "title": "Coding - Decoding",
        "explanation": "<h3>What is Coding - Decoding?</h3><p>In Coding-Decoding, a word or number is coded using a specific rule, and you must decode another word using the same rule. The coding could involve shifting letters, reversing words, replacing letters with numbers, or using mirror positions.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Letter Shifting:</b> Each letter shifted by +n or -n positions.<br><br><b>Reverse Coding:</b> A\u2194Z, B\u2194Y, C\u2194X... Formula: Coded = 27 - Original position.<br><br><b>Number to Letter:</b> Replace each letter with its position number (A=1, B=2).<br><br><b>Opposite Letter Pairs:</b> A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> If MANGO = OCPIQ, what is APPLE?<br>M\u2192O (+2), A\u2192C (+2), N\u2192P (+2). APPLE + 2 = <b>Answer: CRRNG</b></p><br><p><b>Example 2:</b> If CAT = 24, DOG = 26, then PIG = ?<br>C+A+T = 3+1+20 = 24. P+I+G = 16+9+7 = <b>Answer: 32</b></p><br><p><b>Example 3:</b> If BOOK is coded as YLLO, what is PEN?<br>B(2)\u2192Y(25). Rule: 27 minus original position (mirror). P(16)\u2192K(11), E(5)\u2192V(22), N(14)\u2192M(13). <b>Answer: KVM</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 First identify the rule: is it +n, -n, reverse, or number-based?</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Check the shift value by comparing first and last letters.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Opposite letter trick: sum of positions of paired letters = 27.</li></ul>"
    },
    "blood_relations": {
        "title": "Blood Relations",
        "explanation": "<h3>What is Blood Relations?</h3><p>Blood Relations questions test your ability to decode family relationships from given statements or coded relationships. You must determine how two people are related to each other based on a chain of given relationships.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Paternal side:</b> Father's brother = Uncle, Father's sister = Aunt, Father's father = Grandfather.<br><br><b>Maternal side:</b> Mother's brother = Maternal Uncle, Mother's sister = Aunt, Mother's father = Maternal Grandfather.<br><br><b>Generations:</b> Same = Brother/Cousin. +1 = Father/Uncle. +2 = Grandfather. -1 = Son/Nephew.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> A is B's father. B is C's sister. D is C's mother. How is A related to D?<br>B and C are siblings \u2192 A is father, D is mother. <b>Answer: A is D's Husband</b></p><br><p><b>Example 2:</b> Pointing to a girl, Ram says \"She is the daughter of the only son of my grandfather.\" How is the girl related to Ram?<br>Only son of Ram's grandfather = Ram's father. Daughter of Ram's father = <b>Answer: Sister</b></p><br><p><b>Example 3:</b> P is the brother of Q. Q is the mother of R. R is the sister of S. How is P related to S?<br>Q is mother of R and S. P is brother of Q. <b>Answer: P is Uncle of S</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always draw a family tree \u2014 never solve in your head. Use Square for Male, Circle for Female.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 'Only son/daughter' means no siblings.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Gender clues are critical \u2014 watch for male/female indicators.</li></ul>"
    },
    "direction_sense": {
        "title": "Direction Sense Test",
        "explanation": "<h3>What is Direction Sense?</h3><p>Direction Sense questions test your ability to track movement across different directions and calculate the final position or distance from the starting point. The key skill is correctly identifying left and right turns based on current facing direction.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>4 Main Directions:</b> North, South, East, West.<br><br><b>Turns:</b> Facing North \u2192 Turn Right = East. Facing South \u2192 Turn Right = West. Facing East \u2192 Turn Right = South. Facing West \u2192 Turn Right = North.<br><br><b>Shortest Distance (Pythagoras):</b> \u221a(horizontal\u00b2 + vertical\u00b2)<br><br><b>Shadow Rule:</b> Morning sun (East) \u2192 Shadow West. Evening sun (West) \u2192 Shadow East.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> Ravi walks 5m North, turns right walks 4m, turns right walks 5m. Where is he from start?<br>North 5m \u2192 East 4m \u2192 South 5m. <b>Answer: 4 metres East</b></p><br><p><b>Example 2:</b> A goes 3m East, turns left 4m North, turns left 3m West. Distance from start?<br>East 3m \u2192 North 4m \u2192 West 3m. <b>Answer: 4 metres North</b></p><br><p><b>Example 3:</b> Starting facing North, Priya turns right, walks 6m. Turns right again, walks 8m. Turns left walks 6m. How far from start?<br>East 6m + East 6m = 12m Horizontal. South 8m Vertical. \u221a(12\u00b2 + 8\u00b2) = \u221a208 = <b>Answer: 14.4m</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always draw the path on paper \u2014 never visualize mentally.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 'Turn left' and 'turn right' depend on which direction you're currently facing.</li></ul>"
    },
    "syllogism": {
        "title": "Syllogism",
        "explanation": "<h3>What is Syllogism?</h3><p>Syllogism is a form of deductive reasoning where conclusions are drawn from two or more given statements (premises). You must determine which conclusions logically follow from the given statements, regardless of real-world truth.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Rules:</b> All + All = All. All + No = No. Some + All = Some. Some + No = Some Not.<br><br><b>Invalid cases:</b> Two particular premises (Some+Some) give NO conclusion. Two negative premises (No+No) give NO conclusion.<br><br><b>Complementary Pair:</b> If one conclusion says 'Some A are B' and other says 'No A is B' \u2192 Either one must be true.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> All dogs are animals. All animals are living beings.<br>I: All dogs are living beings. II: Some living beings are dogs.<br><b>Answer: Both conclusions follow</b></p><br><p><b>Example 2:</b> No pen is pencil. All pencils are erasers.<br>I: No pen is eraser. II: Some erasers are not pens.<br><b>Answer: Both conclusions follow</b></p><br><p><b>Example 3:</b> Some cats are dogs. Some dogs are lions.<br>I: Some cats are lions. II: All lions are cats.<br>Some+Some = No conclusion. <b>Answer: Neither conclusion follows</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Never use real-world knowledge \u2014 only logic matters.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Draw Venn diagrams for complex questions.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 'Some' means at least one \u2014 it could be all.</li></ul>"
    },
    "venn_diagrams": {
        "title": "Venn Diagrams",
        "explanation": "<h3>What are Venn Diagrams?</h3><p>Venn Diagram questions use overlapping circles to show relationships between different groups. You must find the count of elements in specific regions \u2014 only in one group, in multiple groups, or in none \u2014 using the given data.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>For 2 sets:</b> Total = n(A) + n(B) - n(A\u2229B) + Neither<br><br><b>For 3 sets:</b> Total = n(A)+n(B)+n(C) - n(A\u2229B) - n(B\u2229C) - n(A\u2229C) + n(A\u2229B\u2229C) + Neither<br><br><b>Only A:</b> n(A) - n(A\u2229B) - n(A\u2229C) + n(A\u2229B\u2229C)</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> 100 students. 60 like cricket, 50 like football, 30 like both. How many like neither?<br>Total playing = 60+50-30 = 80. Neither = 100-80 = <b>Answer: 20 students</b></p><br><p><b>Example 2:</b> In above, how many like only cricket?<br>Only Cricket = 60-30 = <b>Answer: 30 students</b></p><br><p><b>Example 3:</b> 90 people. 40 Tea, 35 Coffee, 20 Juice. T\u2229C=15, C\u2229J=10, T\u2229J=8, All=5.<br>Total drinking = 40+35+20 - 15 - 10 - 8 + 5 = 67. Neither = 90-67 = <b>Answer: 23 people</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always start with the innermost region (all overlapping) and work outward.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 'Exactly one' = those in only one group, not shared.</li></ul>"
    },
    "order_ranking": {
        "title": "Order & Ranking",
        "explanation": "<h3>What is Order & Ranking?</h3><p>Order and Ranking questions involve arranging people or objects in a sequence (row, queue, class) and finding a specific person's position from either end, or the total count of people based on given rank information.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Total number of persons:</b> Total = Rank from Left + Rank from Right - 1<br><br><b>Rank from other end:</b> Rank from Right = Total - Rank from Left + 1<br><br><b>Persons between:</b> Between = Total - (Left + Right rank)</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> Asha is 8th from left and 13th from right in a row. Total students?<br>Total = 8 + 13 - 1 = <b>Answer: 20 students</b></p><br><p><b>Example 2:</b> In a class of 45, Ravi ranks 18th from top. Rank from bottom?<br>Rank from bottom = 45 - 18 + 1 = <b>Answer: 28th</b></p><br><p><b>Example 3:</b> A is 12th from left. B is 15th from right. 4 people sit between them. A is left of B. Total?<br>Total = 12 + 4 + 15 = <b>Answer: 31 people</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 The formula Total = Left + Right - 1 is the most important \u2014 memorize it.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 When they ask 'at least' \u2014 positions may overlap, use minimum formula.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 'Between' means exclusive \u2014 doesn't include A and B themselves.</li></ul>"
    },
    "linear_seating": {
        "title": "Seating Arrangement (Linear)",
        "explanation": "<h3>What is Linear Seating Arrangement?</h3><p>People are seated in a straight row either facing North (facing you) or facing South (facing away). You must determine each person's exact position by applying all given conditions step by step using a process of elimination.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Facing North:</b> Your left = row's left, Your right = row's right.<br><br><b>Facing South:</b> Left and right are reversed from your perspective.<br><br><b>Immediate neighbour:</b> Sitting directly next to a person. Not immediate neighbour: At least one person between them.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> P, Q, R, S, T sit in a row. R is at the rightmost end. Q is left of R. P between Q and T. S is at leftmost end.<br><b>Answer: S, T, P, Q, R</b></p><br><p><b>Example 2:</b> A, B, C, D, E. B and D are neighbours. C is at one end. A is 3rd from left. E is neighbour of A only.<br><b>Answer: C, B, A, E, D</b></p><br><p><b>Example 3:</b> 6 people A,B,C,D,E,F. A is 3rd from left. C and D at ends. E between A and B. F is immediate left of C.<br><b>Answer: D, E, A, B, F, C</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always make a blank row with numbered positions first.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Start with the most definite clue (someone at an end, exact position given).</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Use negative clues last to eliminate options.</li></ul>"
    },
    "circular_seating": {
        "title": "Circular Seating Arrangement",
        "explanation": "<h3>What is Circular Seating Arrangement?</h3><p>People sit around a round table. The key difference from linear arrangement is that there is no fixed left or right end \u2014 left and right depend on which direction the person is facing (inward or outward).</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Facing Centre (inward):</b> Left = anti-clockwise direction, Right = clockwise direction.<br><br><b>Facing Outside (outward):</b> Left = clockwise direction, Right = anti-clockwise direction.<br><br><b>Number of arrangements:</b> For n people in a circle = (n-1)!</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> A,B,C,D face centre. A is right of B. C is opposite A. D is left of A.<br><b>Answer (clockwise): B, A, C, D</b></p><br><p><b>Example 2:</b> M,N,O,P,Q face centre. N is 2nd right of M. O is neighbour of N. P is 2nd left of M. Q is between P and O.<br><b>Answer (clockwise): M, N, O, Q, P</b></p><br><p><b>Example 3:</b> A,B,C,D,E,F face centre. B is 3rd left of E. A is 2nd right of B. C is immediate right of F. D is 2nd left of C.<br><b>Answer (clockwise): E, A, C, F, D, B</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always fix one person's position as reference (treat as top of circle).</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Draw a circle immediately and place people as clues come.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 'Opposite' means directly across in an even-numbered circle.</li></ul>"
    },
    "statement_conclusion": {
        "title": "Statement & Conclusion",
        "explanation": "<h3>What is Statement & Conclusion?</h3><p>One or more statements are given followed by conclusions. You must determine which conclusions logically and directly follow from the given statements alone \u2014 not from general knowledge or assumptions.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Conclusion follows if:</b> It is directly supported by the statement, it does not go beyond what the statement says, it requires no outside assumptions.<br><br><b>Conclusion does NOT follow if:</b> It is too broad/narrow, requires assumptions, or contradicts the statement.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> Statement: \"Smoking causes lung cancer.\"<br>I: All smokers get lung cancer (\u274c too extreme). II: Smoking is harmful (\u2705 implied).<br><b>Answer: Only Conclusion II follows</b></p><br><p><b>Example 2:</b> Statement: \"Most students who study score well.\"<br>I: All who score well study (\u274c reverses). II: Regular study helps (\u2705 supported).<br><b>Answer: Only Conclusion II follows</b></p><br><p><b>Example 3:</b> Statement: \"Govt gives free laptops to students.\"<br>I: Students need laptops (\u2705 implied reason). II: All students are poor (\u274c too extreme).<br><b>Answer: Only Conclusion I follows</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Never use outside knowledge \u2014 stick strictly to the statement.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Watch for extreme words: 'all', 'never', 'only', 'always' \u2014 they usually make conclusions invalid.</li></ul>"
    },
    "logical_puzzles": {
        "title": "Logical Puzzles (Floor/Box)",
        "explanation": "<h3>What are Floor/Box Puzzles?</h3><p>Placing people or objects in stacked positions (floors of a building or stacked boxes) based on given conditions. You must determine who lives on which floor or which box is in which position using a process of logical elimination.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Floor Puzzles:</b> Ground floor = Floor 1, Top floor = highest numbered floor. 'Above' means a higher floor number.<br><br><b>Immediately above/below:</b> Means exactly one floor gap.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> A,B,C,D on floors 1-4. A above B. C on 3. D on 1. B not on 2.<br><b>Answer: D=1, B=2 (Wait, B not on 2 so B=4?), correct is D=1, B=2, C=3, A=4</b></p><br><p><b>Example 2:</b> 5 boxes. Red immediately above Blue. Green at top. Yellow immediately below Red. White at bottom.<br><b>Answer: Green, Blue, Red, Yellow, White (top to bottom)</b></p><br><p><b>Example 3:</b> A,B,C,D,E on 1-5. B is 2 floors above D. A topmost. C between D and B. E immediately below A.<br><b>Answer: D=1, C=2, B=3, E=4, A=5</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Make a vertical table with floor numbers before reading clues.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Start with absolute positions (exact floor given).</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Use 'immediately above/below' clues early \u2014 they lock two people together.</li></ul>"
    },
    "data_sufficiency": {
        "title": "Data Sufficiency",
        "explanation": "<h3>What is Data Sufficiency?</h3><p>A question is followed by two statements. You must determine whether the data in the statements is sufficient to answer the question \u2014 you do NOT need to actually solve the question, only judge if it CAN be solved uniquely.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Options:</b><br>(A) 1 alone sufficient<br>(B) 2 alone sufficient<br>(C) Both together sufficient<br>(D) Either alone sufficient<br>(E) Both together insufficient<br><br><b>Rule:</b> If exactly one answer is always possible \u2192 sufficient. If multiple answers \u2192 insufficient.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> What is value of x?<br>1: x + 5 = 10 (Unique x=5). 2: x\u00b2 = 25 (x=5 or -5).<br><b>Answer: A (Statement 1 alone sufficient)</b></p><br><p><b>Example 2:</b> Is n an even number?<br>1: n/2 is whole number (yes). 2: n+1 is odd (yes).<br><b>Answer: D (Either statement alone is sufficient)</b></p><br><p><b>Example 3:</b> What is area of rectangle?<br>1: Length = 10. 2: Width = 5. Neither alone is enough.<br><b>Answer: C (Both statements together are sufficient)</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Never assume values \u2014 test multiple cases to check if the answer is unique.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Eliminate answer choices systematically \u2014 first check Statement 1 alone, then Statement 2 alone.</li></ul>"
    },
    "input_output": {
        "title": "Input - Output",
        "explanation": "<h3>What is Input-Output?</h3><p>Input-Output questions involve a machine that processes a given input (row of words/numbers) through multiple steps, rearranging elements in a specific pattern at each step. You must identify the rule and predict a step's output.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Common Patterns:</b><br>Words: Alphabetical order, word length.<br>Numbers: Ascending or descending arrangement.<br>Mixed: Words and numbers arranged alternately.<br><b>Step count:</b> Each step moves one or two elements to their final position.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> Input: 5 cat 3 ball 8 apple 1 dog<br>Step 1: 1 apple 5 cat 3 ball 8 dog. Step 2: 1 apple 3 ball 5 cat 8 dog.<br><b>Answer: Step 2 is final output</b></p><br><p><b>Example 2:</b> Input: win 41 best 23 lion 67 aim 5<br>Step 3: aim 5 best 23 lion 41 win 67. Rule: alternating alphabetically and ascending numbers.<br><b>Answer: aim 5 best 23 lion 41 win 67</b></p><br><p><b>Example 3:</b> Input: 84 why 32 not 56 how 17 done<br>Step 1: 17 done 84 why 32 not 56 how. Step 2: 17 done 32 how 84 why 56 not.<br><b>Answer: Step 2</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always study at least 3 steps before concluding the rule.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Count how many elements are 'fixed' (in final position) after each step.</li></ul>"
    },
    "critical_reasoning": {
        "title": "Critical Reasoning",
        "explanation": "<h3>What is Critical Reasoning?</h3><p>Tests your ability to analyze arguments, identify assumptions, strengthen or weaken conclusions, and evaluate the logical structure of arguments. These appear heavily in CAT, GMAT, and bank exams.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Strengthen:</b> Add a fact that fills the logical gap between premise and conclusion.<br><br><b>Weaken:</b> Find a fact that breaks the connection between premise and conclusion.<br><br><b>Assumption (Negation test):</b> Negate the assumption \u2014 if the argument falls apart, it is the correct assumption.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> Argument: \"Company X increased ad budget. Therefore, sales will increase.\"<br>Assumption: Advertising drives sales.<br><b>Answer: Correct assumption</b></p><br><p><b>Example 2:</b> Argument: \"All toppers eat breakfast. Ravi is a topper. Ravi eats breakfast.\"<br>Conclusion I: Ravi eats breakfast. (\u2705 valid deduction).<br><b>Answer: Only Conclusion I follows</b></p><br><p><b>Example 3:</b> Argument: \"City banned plastic. Littering decreased by 40%.\"<br>Weakener: A massive cleanliness campaign also ran simultaneously.<br><b>Answer: This weakens the claim that the ban caused the decrease.</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 The conclusion is never the last sentence always \u2014 find it by the word 'therefore/hence'.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Weakeners attack the gap between premise and conclusion, not the premise itself.</li></ul>"
    },
    "statement_assumption": {
        "title": "Statement & Assumption",
        "explanation": "<h3>What is Statement & Assumption?</h3><p>An assumption is an unstated belief that the speaker takes for granted. You must identify what the speaker assumes to be true without explicitly saying it. Course of Action: Evaluate if a proposed action solves the problem.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Assumption IS implicit if:</b> Essential for the statement to make sense, reasonable, not already stated.<br><br><b>Course of Action FOLLOWS if:</b> It directly addresses the problem, is practical, doesn't create a bigger problem.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> Statement: \"Please carry an umbrella today.\" \u2014 Weather app.<br>Assumption I: It may rain (\u2705 Implicit). II: Person doesn't own umbrella (\u274c Not implicit).<br><b>Answer: Only I is implicit</b></p><br><p><b>Example 2:</b> Problem: Road accidents increasing due to overspeeding.<br>Action I: Install speed cameras (\u2705 Follows). Action II: Ban all vehicles (\u274c Extreme).<br><b>Answer: Only Action I follows</b></p><br><p><b>Example 3:</b> Statement: \"Children who read more have better vocabulary.\"<br>Assumption: Reading improves language (\u2705 Implicit). Action: Encourage reading (\u2705 Follows).<br><b>Answer: Both implicit and follows</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Use the negation test: negate the assumption \u2014 if the statement becomes meaningless \u2192 it's implicit.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Course of action must solve the root cause, not just the symptom.</li></ul>"
    },
    "analytical_reasoning": {
        "title": "Analytical Reasoning (Multi-Variable)",
        "explanation": "<h3>What is Multi-Variable Analytical Reasoning?</h3><p>Complex puzzles involving assigning multiple attributes (like name, profession, city, colour, floor) to multiple people simultaneously. These are the hardest reasoning puzzles and require careful grid-based solving.</p>",
        "formulas": "<h3>Formulas & Rules</h3><div style='background:#f8fafc;padding:15px;border-radius:10px;border-left:5px solid #00d4ff;'><b>Grid Technique:</b> Create a grid with people as rows and all attributes as columns. Fill in confirmed facts with \u2713 and eliminated options with \u2717.<br><br><b>Steps:</b> 1. Read all clues. 2. Enter definite clues. 3. Use relational clues to eliminate. 4. Revisit clues after each deduction.</div>",
        "examples": "<h3>Solved Examples</h3><div style='background:#f0fdf4;padding:20px;border-radius:12px;margin-bottom:15px;border-left:5px solid #22c55e;'><p><b>Example 1:</b> A, B, C are doctors, engineers, teachers. A not doctor. B not engineer. C is doctor.<br><b>Answer: A=Engineer, B=Teacher, C=Doctor</b></p><br><p><b>Example 2:</b> P,Q,R,S from Delhi, Mumbai, Chennai, Kolkata. P not from Delhi or Mumbai. Q from Chennai. R from Delhi.<br><b>Answer: P=Kolkata, Q=Chennai, R=Delhi, S=Mumbai</b></p><br><p><b>Example 3:</b> 4 friends. Different pet, different hobby. B reads. D cooks. C has bird. A has dog, does not paint.<br><b>Answer: A=Dog/Gaming, B=Fish/Reading, C=Bird/Painting, D=Cat/Cooking</b></p></div>",
        "tips": "<h3>Expert Tips</h3><ul style='list-style:none;padding:0;display:grid;gap:12px;'><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Always use a grid \u2014 never attempt multi-variable puzzles mentally.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 Enter 'not' clues as \u2717 immediately \u2014 they narrow options fast.</li><li style='background:#fff7ed;padding:15px;border-radius:10px;border-left:5px solid #f97316;'>\ud83d\udca1 When only one option remains in a row or column, it's confirmed.</li></ul>"
    }
};
