const sqlProblems = [
    {
        id: 1,
        title: "Recursive Employee Hierarchy",
        difficulty: "Hard",
        description: `
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:15px; margin-bottom:15px;">
            <b style="color:#0ea5e9;"><i class="fas fa-database"></i> employees</b> table schema:
            <table style="width:100%; margin-top:10px; border-collapse: collapse; font-size: 0.85rem;">
                <tr style="background:#e0f2fe; color:#0369a1; text-align:left;">
                    <th style="padding:8px; border:1px solid #bae6fd;">Column Name</th>
                    <th style="padding:8px; border:1px solid #bae6fd;">Data Type</th>
                </tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">emp_id</td><td style="padding:8px; border:1px solid #e2e8f0;">INT (PK)</td></tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">emp_name</td><td style="padding:8px; border:1px solid #e2e8f0;">VARCHAR</td></tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">manager_id</td><td style="padding:8px; border:1px solid #e2e8f0;">INT (FK)</td></tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">salary</td><td style="padding:8px; border:1px solid #e2e8f0;">DECIMAL</td></tr>
            </table>
        </div>
        <b>Task Requirement:</b><br>
        Write a Common Table Expression (CTE) utilizing recursive joins to output the hierarchical depth (level) of every employee.
        The top-tier CEO (who has a NULL manager_id) should be Level 1. Direct reports to the CEO are Level 2, and so on. 
        Your query must SELECT the <code>emp_name</code> and the <code>hierarchy_level</code>, ordered by hierarchy_level ASC.
        `
    },
    {
        id: 2,
        title: "Consecutive Login Strengthening",
        difficulty: "Hard",
        description: `
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:15px; margin-bottom:15px;">
            <b style="color:#0ea5e9;"><i class="fas fa-database"></i> logins</b> table schema:
            <table style="width:100%; margin-top:10px; border-collapse: collapse; font-size: 0.85rem;">
                <tr style="background:#e0f2fe; color:#0369a1; text-align:left;">
                    <th style="padding:8px; border:1px solid #bae6fd;">Column Name</th>
                    <th style="padding:8px; border:1px solid #bae6fd;">Data Type</th>
                </tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">user_id</td><td style="padding:8px; border:1px solid #e2e8f0;">INT</td></tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">login_date</td><td style="padding:8px; border:1px solid #e2e8f0;">DATE</td></tr>
            </table>
        </div>
        <b>Task Requirement:</b><br>
        Security needs to isolate active streaks. Write a query that finds all <code>user_id</code>s who have logged in for at least 5 consecutive subsequent days.
        You must leverage the <code>LEAD()</code> window function computationally or perform advanced self-joins. Do not use cursor loops.
        `
    },
    {
        id: 3,
        title: "Median Department Salary",
        difficulty: "Expert",
        description: `
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:15px; margin-bottom:15px;">
            <b style="color:#0ea5e9;"><i class="fas fa-database"></i> salaries</b> table schema:
            <table style="width:100%; margin-top:10px; border-collapse: collapse; font-size: 0.85rem;">
                <tr style="background:#e0f2fe; color:#0369a1; text-align:left;">
                    <th style="padding:8px; border:1px solid #bae6fd;">Column Name</th>
                    <th style="padding:8px; border:1px solid #bae6fd;">Data Type</th>
                </tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">emp_id</td><td style="padding:8px; border:1px solid #e2e8f0;">INT</td></tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">department</td><td style="padding:8px; border:1px solid #e2e8f0;">VARCHAR</td></tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">salary</td><td style="padding:8px; border:1px solid #e2e8f0;">DECIMAL</td></tr>
            </table>
        </div>
        <b>Task Requirement:</b><br>
        Compute the exact median salary stringently for each individual department without utilizing inherent mathematically complex MEDIAN() aliases if they do not exist in standard ANSI SQL. 
        Utilize <code>ROW_NUMBER()</code> sorting ASC and DESC implicitly within a subquery or CTE to trap the center values reliably, then compute the exact median utilizing standard average operators.
        Output: <code>department</code>, <code>median_salary</code>.
        `
    },
    {
        id: 4,
        title: "Inventory Running Total",
        difficulty: "Medium",
        description: `
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:15px; margin-bottom:15px;">
            <b style="color:#0ea5e9;"><i class="fas fa-database"></i> warehouse</b> table schema:
            <table style="width:100%; margin-top:10px; border-collapse: collapse; font-size: 0.85rem;">
                <tr style="background:#e0f2fe; color:#0369a1; text-align:left;">
                    <th style="padding:8px; border:1px solid #bae6fd;">Column Name</th>
                    <th style="padding:8px; border:1px solid #bae6fd;">Data Type</th>
                </tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">product_id</td><td style="padding:8px; border:1px solid #e2e8f0;">INT</td></tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">bin_id</td><td style="padding:8px; border:1px solid #e2e8f0;">INT</td></tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">quantity</td><td style="padding:8px; border:1px solid #e2e8f0;">INT</td></tr>
                <tr><td style="padding:8px; border:1px solid #e2e8f0;">stock_date</td><td style="padding:8px; border:1px solid #e2e8f0;">DATE</td></tr>
            </table>
        </div>
        <b>Task Requirement:</b><br>
        Generate a running mathematical total of stock per product over temporal dates natively.
        Use an aggregation window function: <code>SUM(quantity) OVER(PARTITION BY product_id ORDER BY stock_date)</code> to dynamically calculate the cumulative sum on each row.
        Return <code>product_id</code>, <code>stock_date</code>, <code>quantity</code>, and <code>running_total</code>.
        `
    },
    {
        id: 5,
        title: "Isolating Retention Rate Cohorts",
        difficulty: "Expert",
        description: `
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:15px; margin-bottom:15px; display:flex; gap:15px;">
            <div style="flex:1;">
                <b style="color:#0ea5e9;"><i class="fas fa-database"></i> users</b> table:
                <table style="width:100%; margin-top:10px; border-collapse: collapse; font-size: 0.85rem;">
                    <tr style="background:#e0f2fe; color:#0369a1; text-align:left;">
                        <th style="padding:8px; border:1px solid #bae6fd;">Column Name</th>
                        <th style="padding:8px; border:1px solid #bae6fd;">Data Type</th>
                    </tr>
                    <tr><td style="padding:8px; border:1px solid #e2e8f0;">user_id</td><td style="padding:8px; border:1px solid #e2e8f0;">INT</td></tr>
                    <tr><td style="padding:8px; border:1px solid #e2e8f0;">sign_up_date</td><td style="padding:8px; border:1px solid #e2e8f0;">DATE</td></tr>
                </table>
            </div>
            <div style="flex:1;">
                <b style="color:#0ea5e9;"><i class="fas fa-database"></i> purchases</b> table:
                <table style="width:100%; margin-top:10px; border-collapse: collapse; font-size: 0.85rem;">
                    <tr style="background:#e0f2fe; color:#0369a1; text-align:left;">
                        <th style="padding:8px; border:1px solid #bae6fd;">Column Name</th>
                        <th style="padding:8px; border:1px solid #bae6fd;">Data Type</th>
                    </tr>
                    <tr><td style="padding:8px; border:1px solid #e2e8f0;">user_id</td><td style="padding:8px; border:1px solid #e2e8f0;">INT</td></tr>
                    <tr><td style="padding:8px; border:1px solid #e2e8f0;">purchase_date</td><td style="padding:8px; border:1px solid #e2e8f0;">DATE</td></tr>
                    <tr><td style="padding:8px; border:1px solid #e2e8f0;">amount</td><td style="padding:8px; border:1px solid #e2e8f0;">DECIMAL</td></tr>
                </table>
            </div>
        </div>
        <b>Task Requirement:</b><br>
        Write a highly optimized single query that mathematically determines the Day-7 retention rate cohort. We want to know what percentage of users who structurally signed up on a specific date made a strict transaction exactly 7 days after their native sign_up_date.
        `
    }
];
