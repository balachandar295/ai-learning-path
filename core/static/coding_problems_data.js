const codingProblems = [
  {
    "title": "Electricity Bill Calculator",
    "difficulty": "Easy",
    "acceptance": "44.7%",
    "id": 1,
    "topic": "Practical",
    "description": "Calculate the electricity bill based on units consumed.\n\nRates:\n- 1-100 units at $1/unit\n- 101-200 units at $2/unit\n- Above 200 units at $5/unit\n\nConstraints:\n- `0 <= units <= 10^5`",
    "examples": [
      {
        "input": "Units = 150",
        "output": "200",
        "explanation": "100*1 + 50*2 = 200"
      },
      {
        "input": "Units = 50",
        "output": "50",
        "explanation": "50*1 = 50"
      }
    ]
  },
  {
    "title": "ATM Withdrawal Simulation",
    "difficulty": "Medium",
    "acceptance": "94.0%",
    "id": 2,
    "topic": "Practical",
    "description": "Simulate an ATM: Handle balance check, withdraw, and deposit operations securely. Ensure the balance never goes below zero.",
    "examples": [
      {
        "input": "Balance=1000, Withdraw=500",
        "output": "Remaining: 500",
        "explanation": "1000 - 500 = 500"
      },
      {
        "input": "Balance=100, Withdraw=200",
        "output": "Insufficient Funds",
        "explanation": "Cannot withdraw more than balance."
      }
    ]
  },
  {
    "title": "Student Grade Analyzer",
    "difficulty": "Easy",
    "acceptance": "84.9%",
    "id": 3,
    "topic": "Practical",
    "description": "Given a list of student marks, calculate the average score, determine the letter grade (A, B, C, F), and identify the topper.\n\nGrading Scale:\n- >= 90: A\n- 80-89: B\n- 70-79: C\n- < 70: F",
    "examples": [
      {
        "input": "Marks = [80, 90, 70]",
        "output": "Avg: 80, Grade: B, Topper Score: 90",
        "explanation": "Average is exactly 80. Max is 90."
      },
      {
        "input": "Marks = [95, 92, 99]",
        "output": "Avg: 95.3, Grade: A, Topper Score: 99",
        "explanation": "Average is > 90."
      }
    ]
  },
  {
    "title": "Shopping Cart Calculator",
    "difficulty": "Medium",
    "acceptance": "71.5%",
    "id": 4,
    "topic": "Practical",
    "description": "Calculate the total price for items in a shopping cart. Apply a 10% discount if the total exceeds $500.",
    "examples": [
      {
        "input": "Items: [200, 400]",
        "output": "Total: 540",
        "explanation": "600 is > 500, so 10% discount applies (600 - 60)."
      },
      {
        "input": "Items: [100, 150]",
        "output": "Total: 250",
        "explanation": "No discount applied."
      }
    ]
  },
  {
    "title": "Parking Fee Calculator",
    "difficulty": "Easy",
    "acceptance": "53.2%",
    "id": 5,
    "topic": "Practical",
    "description": "Calculate parking fee based on hours parked. First 2 hours cost $10 total. Every additional hour costs $5.",
    "examples": [
      {
        "input": "Hours = 4",
        "output": "20",
        "explanation": "First 2 hrs = $10. Remaining 2 hrs = 2 * $5 = $10. Total $20."
      },
      {
        "input": "Hours = 1",
        "output": "10",
        "explanation": "Flat fee for first 2 hours."
      }
    ]
  },
  {
    "title": "Diamond Pattern",
    "difficulty": "Medium",
    "acceptance": "70.9%",
    "id": 6,
    "topic": "Logic",
    "description": "Print a perfect diamond pattern using stars ('*') based on a given height N.\nThe height N represents the number of rows in the upper half of the diamond (including the middle widest row).\n\nConstraints:\n- `1 <= N <= 50`\n- The output must be exactly formatted with trailing/leading spaces where necessary to center the stars.",
    "examples": [
      {
        "input": "N = 3",
        "output": "  *  \n *** \n*****\n *** \n  *  ",
        "explanation": "The maximum width is 2*3 - 1 = 5 stars. The pattern is perfectly centered."
      },
      {
        "input": "N = 2",
        "output": " * \n***\n * ",
        "explanation": "The maximum width is 2*2 - 1 = 3 stars."
      }
    ]
  },
  {
    "title": "Pascal Triangle",
    "difficulty": "Medium",
    "acceptance": "58.6%",
    "id": 7,
    "topic": "Logic",
    "description": "Generate the first N rows of Pascal's Triangle. Each number is the sum of the two numbers directly above it.",
    "examples": [
      {
        "input": "N = 3",
        "output": "1\n1 1\n1 2 1",
        "explanation": "Standard binomial coefficients."
      },
      {
        "input": "N = 4",
        "output": "1\n1 1\n1 2 1\n1 3 3 1",
        "explanation": "Fourth row adds adjacent pairs."
      }
    ]
  },
  {
    "title": "Number Pyramid",
    "difficulty": "Easy",
    "acceptance": "51.0%",
    "id": 8,
    "topic": "Logic",
    "description": "Print a centered pyramid of numbers up to N rows. Row i should contain the number i repeated i times.",
    "examples": [
      {
        "input": "N = 3",
        "output": "  1  \n 2 2 \n3 3 3",
        "explanation": "3 rows, centered."
      },
      {
        "input": "N = 2",
        "output": " 1 \n2 2",
        "explanation": "2 rows, simple."
      }
    ]
  },
  {
    "title": "Snake Pattern Matrix",
    "difficulty": "Medium",
    "acceptance": "80.6%",
    "id": 9,
    "topic": "Logic",
    "description": "Print a 2D matrix in snake fashion (row 1 left-to-right, row 2 right-to-left, row 3 left-to-right, etc.).",
    "examples": [
      {
        "input": "[[1,2],[3,4]]",
        "output": "1, 2, 4, 3",
        "explanation": "Row 1 is normal, Row 2 is reversed."
      },
      {
        "input": "[[1,2,3],[4,5,6],[7,8,9]]",
        "output": "1, 2, 3, 6, 5, 4, 7, 8, 9",
        "explanation": "Rows alternate direction."
      }
    ]
  },
  {
    "title": "Spiral Matrix Print",
    "difficulty": "Hard",
    "acceptance": "70.0%",
    "id": 10,
    "topic": "Logic",
    "description": "Given an M x N matrix, return all elements of the matrix in spiral order (clockwise starting from top-left).",
    "examples": [
      {
        "input": "[[1,2,3],[4,5,6],[7,8,9]]",
        "output": "1, 2, 3, 6, 9, 8, 7, 4, 5",
        "explanation": "Outer shell first, then inner."
      },
      {
        "input": "[[1,2],[3,4]]",
        "output": "1, 2, 4, 3",
        "explanation": "2x2 wraps around instantly."
      }
    ]
  },
  {
    "title": "Find Second Largest Number",
    "difficulty": "Easy",
    "acceptance": "69.4%",
    "id": 11,
    "topic": "Algorithm",
    "description": "Find the second largest strictly unique number in an array of integers.\n\nConstraints:\n- `1 <= arr.length <= 10^5`",
    "examples": [
      {
        "input": "[1, 5, 2, 5, 4]",
        "output": "4",
        "explanation": "Largest is 5. Second unique largest is 4."
      },
      {
        "input": "[2, 2]",
        "output": "-1",
        "explanation": "No second largest exists."
      }
    ]
  },
  {
    "title": "Find Duplicate in List",
    "difficulty": "Easy",
    "acceptance": "73.2%",
    "id": 12,
    "topic": "Algorithm",
    "description": "Identify the first repeating number in a list of integers.\n\nConstraints:\n- Expected O(N) time complexity.",
    "examples": [
      {
        "input": "[1, 2, 3, 2, 1]",
        "output": "2",
        "explanation": "2 appears twice and is the first duplicate encountered."
      },
      {
        "input": "[4, 5, 6, 7]",
        "output": "-1",
        "explanation": "No duplicates exist."
      }
    ]
  },
  {
    "title": "Rotate Array Left / Right",
    "difficulty": "Medium",
    "acceptance": "34.6%",
    "id": 13,
    "topic": "Algorithm",
    "description": "Rotate an integer array by K positions to the left or right in-place.\n\nConstraints:\n- `O(1)` extra space required.",
    "examples": [
      {
        "input": "[1,2,3,4,5], K=2, Dir=Right",
        "output": "[4,5,1,2,3]",
        "explanation": "Last two elements moved to front."
      },
      {
        "input": "[1,2,3,4,5], K=1, Dir=Left",
        "output": "[2,3,4,5,1]",
        "explanation": "First element moved to back."
      }
    ]
  },
  {
    "title": "Find Missing Number",
    "difficulty": "Easy",
    "acceptance": "83.5%",
    "id": 14,
    "topic": "Algorithm",
    "description": "Given an array containing n distinct numbers taken from `0, 1, 2, ..., n`, find the one that is missing from the array.",
    "examples": [
      {
        "input": "[3,0,1]",
        "output": "2",
        "explanation": "Array has length 3, so contains numbers 0-3. 2 is missing."
      },
      {
        "input": "[0,1]",
        "output": "2",
        "explanation": "Length is 2, range is 0-2. 2 is missing."
      }
    ]
  },
  {
    "title": "Check Balanced Parentheses",
    "difficulty": "Medium",
    "acceptance": "91.9%",
    "id": 15,
    "topic": "Algorithm",
    "description": "Verify if a given string of parentheses `()`, `{}`, `[]` is mathematically balanced and properly nested.",
    "examples": [
      {
        "input": "s = '()[]{}'",
        "output": "True",
        "explanation": "Every open bracket has a matching closing bracket."
      },
      {
        "input": "s = '([)]'",
        "output": "False",
        "explanation": "Improperly nested."
      }
    ]
  },
  {
    "title": "Password Strength Checker",
    "difficulty": "Easy",
    "acceptance": "76.3%",
    "id": 16,
    "topic": "AI",
    "description": "Rate password strength based on length, symbols, digits, and case variety. Return 'Weak', 'Medium', or 'Strong'.",
    "examples": [
      {
        "input": "Pass123!",
        "output": "Strong",
        "explanation": "Has upper, lower, digit, symbol, length > 8."
      },
      {
        "input": "password",
        "output": "Weak",
        "explanation": "No digits, symbols, or uppercase."
      }
    ]
  },
  {
    "title": "Spam Message Detector",
    "difficulty": "Medium",
    "acceptance": "72.1%",
    "id": 17,
    "topic": "AI",
    "description": "Check if a message is spam based on basic keyword matching (e.g., 'win', 'free', 'prize', 'urgent') and abnormal capitalization.",
    "examples": [
      {
        "input": "WIN a FREE prize NOW!",
        "output": "Spam",
        "explanation": "Contains multiple trigger words and all-caps."
      },
      {
        "input": "Hello, see you tomorrow.",
        "output": "Not Spam",
        "explanation": "Normal conversational text."
      }
    ]
  },
  {
    "title": "Username Generator",
    "difficulty": "Easy",
    "acceptance": "59.2%",
    "id": 18,
    "topic": "AI",
    "description": "Generate a list of 3 unique, available usernames based on a user's first name, last name, and birth year.",
    "examples": [
      {
        "input": "John Doe, 1990",
        "output": "['jdoe90', 'john_d_1990', 'doejohn90']",
        "explanation": "Generates valid combinations."
      },
      {
        "input": "Alice Smith, 1995",
        "output": "['asmith95', 'alice_s_1995', 'smithalice95']",
        "explanation": "Standard variants."
      }
    ]
  },
  {
    "title": "Simple Chatbot Logic",
    "difficulty": "Medium",
    "acceptance": "37.5%",
    "id": 19,
    "topic": "AI",
    "description": "Implement a rule-based engine that parses user intents. If input contains 'time', return current time. If 'help', return instructions.",
    "examples": [
      {
        "input": "'What is the time?'",
        "output": "'It is currently 12:00'",
        "explanation": "Intent parsed successfully."
      },
      {
        "input": "'I need help'",
        "output": "'Here are the commands...'",
        "explanation": "Help intent recognized."
      }
    ]
  },
  {
    "title": "Auto Email Validator",
    "difficulty": "Easy",
    "acceptance": "70.2%",
    "id": 20,
    "topic": "AI",
    "description": "Validate an email address structure rigorously using Regex patterns. Must contain `@`, valid domain, and TLD.",
    "examples": [
      {
        "input": "'test.user@domain.co.uk'",
        "output": "Valid",
        "explanation": "Follows standard email RFC rules."
      },
      {
        "input": "'test@domain'",
        "output": "Invalid",
        "explanation": "Missing TLD."
      }
    ]
  },
  {
    "title": "Guess the Number",
    "difficulty": "Easy",
    "acceptance": "37.5%",
    "id": 21,
    "topic": "Game",
    "description": "Simulate a guessing game. Given a target number, respond with 'Too High', 'Too Low', or 'Correct' for each guess.",
    "examples": [
      {
        "input": "Target=50, Guess=40",
        "output": "Too Low",
        "explanation": "40 < 50."
      },
      {
        "input": "Target=50, Guess=50",
        "output": "Correct",
        "explanation": "Exact match."
      }
    ]
  },
  {
    "title": "Rock Paper Scissors",
    "difficulty": "Easy",
    "acceptance": "58.3%",
    "id": 22,
    "topic": "Game",
    "description": "Implement rock-paper-scissors game logic. Determine the winner given Player 1 and Player 2 moves.",
    "examples": [
      {
        "input": "'Rock', 'Scissors'",
        "output": "'Player 1 Wins'",
        "explanation": "Rock crushes Scissors."
      },
      {
        "input": "'Paper', 'Paper'",
        "output": "'Draw'",
        "explanation": "Identical choices."
      }
    ]
  },
  {
    "title": "Tic Tac Toe Logic",
    "difficulty": "Hard",
    "acceptance": "77.0%",
    "id": 23,
    "topic": "Game",
    "description": "Given a 3x3 grid state, determine if 'X' wins, 'O' wins, it's a 'Draw', or 'Ongoing'.",
    "examples": [
      {
        "input": "['X','X','X'], ['O','.','.'], ['.','O','.']",
        "output": "'X Wins'",
        "explanation": "X occupies the entire top row."
      },
      {
        "input": "['X','O','X'], ['O','X','O'], ['O','X','O']",
        "output": "'Draw'",
        "explanation": "Grid full, no winner."
      }
    ]
  },
  {
    "title": "Dice Simulator",
    "difficulty": "Easy",
    "acceptance": "39.3%",
    "id": 24,
    "topic": "Game",
    "description": "Simulate rolling N standard 6-sided dice and return the total sum and individual rolls.",
    "examples": [
      {
        "input": "N = 2",
        "output": "Sum: 8, Rolls: [3, 5]",
        "explanation": "Randomly generated rolls."
      },
      {
        "input": "N = 1",
        "output": "Sum: 4, Rolls: [4]",
        "explanation": "Single die."
      }
    ]
  },
  {
    "title": "Word Scramble Game",
    "difficulty": "Medium",
    "acceptance": "73.9%",
    "id": 25,
    "topic": "Game",
    "description": "Given a word, scramble it programmatically. Then check if a user's guess matches the original word.",
    "examples": [
      {
        "input": "Word: 'APPLE', Guess: 'APPLE'",
        "output": "Correct",
        "explanation": "Guess matches the un-scrambled original."
      },
      {
        "input": "Word: 'APPLE', Guess: 'PAPEL'",
        "output": "Incorrect",
        "explanation": "Wrong guess."
      }
    ]
  },
  {
    "title": "LRU Cache Simulation",
    "difficulty": "Hard",
    "acceptance": "37.4%",
    "id": 26,
    "topic": "Interview",
    "description": "Design and implement a data structure for Least Recently Used (LRU) cache. It should support `get` and `put` in O(1) average time.",
    "examples": [
      {
        "input": "Capacity=2, put(1,1), put(2,2), get(1), put(3,3), get(2)",
        "output": "get(1)->1, get(2)->-1",
        "explanation": "2 was evicted when 3 was added."
      },
      {
        "input": "Capacity=1, put(1,1), put(2,2), get(1)",
        "output": "get(1)->-1",
        "explanation": "1 evicted immediately when 2 was added."
      }
    ]
  },
  {
    "title": "Rate Limiter System",
    "difficulty": "Hard",
    "acceptance": "52.5%",
    "id": 27,
    "topic": "Interview",
    "description": "Design a rate limiter that allows only K requests per second for a specific user ID using a Token Bucket or Sliding Window.",
    "examples": [
      {
        "input": "Limit=1/sec, Req(t=0s), Req(t=0.5s)",
        "output": "Allow, Reject",
        "explanation": "Second request arrived too soon."
      },
      {
        "input": "Limit=2/sec, Req(t=0s), Req(t=0.5s)",
        "output": "Allow, Allow",
        "explanation": "Limit is 2, both accepted."
      }
    ]
  },
  {
    "title": "URL Shortener Logic",
    "difficulty": "Medium",
    "acceptance": "43.4%",
    "id": 28,
    "topic": "Interview",
    "description": "Write an algorithm to encode a long URL to a short 6-character code using Base62, and decode it back.",
    "examples": [
      {
        "input": "Encode 'google.com'",
        "output": "sh.rt/Ab12xZ",
        "explanation": "Hash generated and stored."
      },
      {
        "input": "Decode 'sh.rt/Ab12xZ'",
        "output": "'google.com'",
        "explanation": "Retrieved from hash mapping."
      }
    ]
  },
  {
    "title": "Leaderboard System",
    "difficulty": "Hard",
    "acceptance": "32.7%",
    "id": 29,
    "topic": "Interview",
    "description": "Design a real-time leaderboard system that tracks top 10 scores efficiently among millions of players.",
    "examples": [
      {
        "input": "addScore(1, 100), addScore(2, 200), top(1)",
        "output": "Player 2",
        "explanation": "Player 2 has the highest score."
      },
      {
        "input": "addScore(3, 300), top(2)",
        "output": "[Player 3, Player 2]",
        "explanation": "Sorted dynamically."
      }
    ]
  },
  {
    "title": "Task Scheduler",
    "difficulty": "Hard",
    "acceptance": "56.8%",
    "id": 30,
    "topic": "Interview",
    "description": "Given a list of tasks and a cooldown period `n`, find the minimum CPU intervals required to finish all tasks.",
    "examples": [
      {
        "input": "Tasks = ['A','A','B','B'], n=2",
        "output": "5",
        "explanation": "A -> B -> idle -> A -> B"
      },
      {
        "input": "Tasks = ['A','A','A','B','B','B'], n=2",
        "output": "8",
        "explanation": "A -> B -> idle -> A -> B -> idle -> A -> B"
      }
    ]
  },
  {
    "title": "Two Sum",
    "difficulty": "Hard",
    "acceptance": "66.6%",
    "id": 31,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Two Sum**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Three Sum",
    "difficulty": "Medium",
    "acceptance": "38.7%",
    "id": 32,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Three Sum**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Container With Most Water",
    "difficulty": "Medium",
    "acceptance": "58.8%",
    "id": 33,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Container With Most Water**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Trapping Rain Water",
    "difficulty": "Easy",
    "acceptance": "37.7%",
    "id": 34,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Trapping Rain Water**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Product of Array Except Self",
    "difficulty": "Medium",
    "acceptance": "38.5%",
    "id": 35,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Product of Array Except Self**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Maximum Subarray",
    "difficulty": "Medium",
    "acceptance": "38.3%",
    "id": 36,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Maximum Subarray**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Merge Intervals",
    "difficulty": "Medium",
    "acceptance": "49.1%",
    "id": 37,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Merge Intervals**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Find Minimum in Rotated Sorted Array",
    "difficulty": "Easy",
    "acceptance": "35.1%",
    "id": 38,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Find Minimum in Rotated Sorted Array**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Search in Rotated Sorted Array",
    "difficulty": "Medium",
    "acceptance": "40.5%",
    "id": 39,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Search in Rotated Sorted Array**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Contains Duplicate",
    "difficulty": "Medium",
    "acceptance": "50.4%",
    "id": 40,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Contains Duplicate**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Best Time to Buy and Sell Stock",
    "difficulty": "Hard",
    "acceptance": "84.8%",
    "id": 41,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Best Time to Buy and Sell Stock**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Subarray Sum Equals K",
    "difficulty": "Medium",
    "acceptance": "61.5%",
    "id": 42,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Subarray Sum Equals K**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Next Permutation",
    "difficulty": "Medium",
    "acceptance": "65.0%",
    "id": 43,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Next Permutation**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Sort Colors",
    "difficulty": "Hard",
    "acceptance": "45.7%",
    "id": 44,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Sort Colors**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Move Zeroes",
    "difficulty": "Hard",
    "acceptance": "17.0%",
    "id": 45,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Move Zeroes**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Find All Duplicates in an Array",
    "difficulty": "Medium",
    "acceptance": "73.8%",
    "id": 46,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Find All Duplicates in an Array**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Longest Substring Without Repeating Characters",
    "difficulty": "Hard",
    "acceptance": "75.6%",
    "id": 47,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Substring Without Repeating Characters**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Longest Palindromic Substring",
    "difficulty": "Hard",
    "acceptance": "42.2%",
    "id": 48,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Palindromic Substring**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Valid Anagram",
    "difficulty": "Medium",
    "acceptance": "16.8%",
    "id": 49,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Valid Anagram**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Group Anagrams",
    "difficulty": "Easy",
    "acceptance": "20.3%",
    "id": 50,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Group Anagrams**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Valid Parentheses",
    "difficulty": "Medium",
    "acceptance": "65.6%",
    "id": 51,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Valid Parentheses**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Generate Parentheses",
    "difficulty": "Easy",
    "acceptance": "23.2%",
    "id": 52,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Generate Parentheses**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Longest Valid Parentheses",
    "difficulty": "Hard",
    "acceptance": "40.6%",
    "id": 53,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Valid Parentheses**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Minimum Window Substring",
    "difficulty": "Medium",
    "acceptance": "60.3%",
    "id": 54,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Minimum Window Substring**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Valid Palindrome",
    "difficulty": "Easy",
    "acceptance": "59.6%",
    "id": 55,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Valid Palindrome**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Longest Repeating Character Replacement",
    "difficulty": "Medium",
    "acceptance": "18.9%",
    "id": 56,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Repeating Character Replacement**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Palindromic Substrings",
    "difficulty": "Hard",
    "acceptance": "37.3%",
    "id": 57,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Palindromic Substrings**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Encode and Decode Strings",
    "difficulty": "Medium",
    "acceptance": "38.4%",
    "id": 58,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Encode and Decode Strings**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Find All Anagrams in a String",
    "difficulty": "Easy",
    "acceptance": "26.7%",
    "id": 59,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Find All Anagrams in a String**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Reverse Linked List",
    "difficulty": "Hard",
    "acceptance": "38.7%",
    "id": 60,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Reverse Linked List**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Merge Two Sorted Lists",
    "difficulty": "Hard",
    "acceptance": "23.8%",
    "id": 61,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Merge Two Sorted Lists**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Linked List Cycle",
    "difficulty": "Medium",
    "acceptance": "81.0%",
    "id": 62,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Linked List Cycle**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Reorder List",
    "difficulty": "Medium",
    "acceptance": "67.0%",
    "id": 63,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Reorder List**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Remove Nth Node From End of List",
    "difficulty": "Medium",
    "acceptance": "40.8%",
    "id": 64,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Remove Nth Node From End of List**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Copy List with Random Pointer",
    "difficulty": "Medium",
    "acceptance": "38.9%",
    "id": 65,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Copy List with Random Pointer**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Merge k Sorted Lists",
    "difficulty": "Medium",
    "acceptance": "27.9%",
    "id": 66,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Merge k Sorted Lists**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Reverse Nodes in k-Group",
    "difficulty": "Hard",
    "acceptance": "80.6%",
    "id": 67,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Reverse Nodes in k-Group**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Intersection of Two Linked Lists",
    "difficulty": "Easy",
    "acceptance": "24.6%",
    "id": 68,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Intersection of Two Linked Lists**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Palindrome Linked List",
    "difficulty": "Medium",
    "acceptance": "72.0%",
    "id": 69,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Palindrome Linked List**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Swapping Nodes in a Linked List",
    "difficulty": "Medium",
    "acceptance": "32.1%",
    "id": 70,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Swapping Nodes in a Linked List**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Odd Even Linked List",
    "difficulty": "Medium",
    "acceptance": "75.2%",
    "id": 71,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Odd Even Linked List**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Add Two Numbers",
    "difficulty": "Medium",
    "acceptance": "82.2%",
    "id": 72,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Add Two Numbers**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Maximum Depth of Binary Tree",
    "difficulty": "Hard",
    "acceptance": "56.1%",
    "id": 73,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Maximum Depth of Binary Tree**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Same Tree",
    "difficulty": "Medium",
    "acceptance": "36.8%",
    "id": 74,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Same Tree**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Invert Binary Tree",
    "difficulty": "Medium",
    "acceptance": "20.0%",
    "id": 75,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Invert Binary Tree**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Binary Tree Maximum Path Sum",
    "difficulty": "Easy",
    "acceptance": "70.5%",
    "id": 76,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Binary Tree Maximum Path Sum**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Binary Tree Level Order Traversal",
    "difficulty": "Hard",
    "acceptance": "46.5%",
    "id": 77,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Binary Tree Level Order Traversal**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Serialize and Deserialize Binary Tree",
    "difficulty": "Medium",
    "acceptance": "50.8%",
    "id": 78,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Serialize and Deserialize Binary Tree**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Subtree of Another Tree",
    "difficulty": "Medium",
    "acceptance": "23.7%",
    "id": 79,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Subtree of Another Tree**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Construct Binary Tree from Preorder and Inorder Traversal",
    "difficulty": "Medium",
    "acceptance": "25.2%",
    "id": 80,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Construct Binary Tree from Preorder and Inorder Traversal**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Validate Binary Search Tree",
    "difficulty": "Hard",
    "acceptance": "65.5%",
    "id": 81,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Validate Binary Search Tree**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Kth Smallest Element in a BST",
    "difficulty": "Medium",
    "acceptance": "29.4%",
    "id": 82,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Kth Smallest Element in a BST**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Lowest Common Ancestor of a BST",
    "difficulty": "Medium",
    "acceptance": "78.7%",
    "id": 83,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Lowest Common Ancestor of a BST**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Implement Trie (Prefix Tree)",
    "difficulty": "Medium",
    "acceptance": "25.2%",
    "id": 84,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Implement Trie (Prefix Tree)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Design Add and Search Words Data Structure",
    "difficulty": "Medium",
    "acceptance": "81.3%",
    "id": 85,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Design Add and Search Words Data Structure**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Search II",
    "difficulty": "Easy",
    "acceptance": "26.5%",
    "id": 86,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Word Search II**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Number of Islands",
    "difficulty": "Medium",
    "acceptance": "46.8%",
    "id": 87,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Number of Islands**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Clone Graph",
    "difficulty": "Easy",
    "acceptance": "68.2%",
    "id": 88,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Clone Graph**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Max Area of Island",
    "difficulty": "Medium",
    "acceptance": "25.2%",
    "id": 89,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Max Area of Island**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Pacific Atlantic Water Flow",
    "difficulty": "Medium",
    "acceptance": "54.7%",
    "id": 90,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Pacific Atlantic Water Flow**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Surrounded Regions",
    "difficulty": "Medium",
    "acceptance": "77.9%",
    "id": 91,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Surrounded Regions**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Rotting Oranges",
    "difficulty": "Hard",
    "acceptance": "21.7%",
    "id": 92,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Rotting Oranges**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Walls and Gates",
    "difficulty": "Medium",
    "acceptance": "33.0%",
    "id": 93,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Walls and Gates**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Course Schedule",
    "difficulty": "Hard",
    "acceptance": "73.4%",
    "id": 94,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Course Schedule**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Course Schedule II",
    "difficulty": "Hard",
    "acceptance": "49.9%",
    "id": 95,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Course Schedule II**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Redundant Connection",
    "difficulty": "Hard",
    "acceptance": "24.1%",
    "id": 96,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Redundant Connection**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Number of Connected Components in an Undirected Graph",
    "difficulty": "Easy",
    "acceptance": "16.5%",
    "id": 97,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Number of Connected Components in an Undirected Graph**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Graph Valid Tree",
    "difficulty": "Easy",
    "acceptance": "75.2%",
    "id": 98,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Graph Valid Tree**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Ladder",
    "difficulty": "Medium",
    "acceptance": "45.9%",
    "id": 99,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Word Ladder**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Alien Dictionary",
    "difficulty": "Medium",
    "acceptance": "33.0%",
    "id": 100,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Alien Dictionary**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Network Delay Time",
    "difficulty": "Medium",
    "acceptance": "81.7%",
    "id": 101,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Network Delay Time**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Cheapest Flights Within K Stops",
    "difficulty": "Medium",
    "acceptance": "46.6%",
    "id": 102,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Cheapest Flights Within K Stops**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Climbing Stairs",
    "difficulty": "Hard",
    "acceptance": "25.7%",
    "id": 103,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Climbing Stairs**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Min Cost Climbing Stairs",
    "difficulty": "Medium",
    "acceptance": "34.3%",
    "id": 104,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Min Cost Climbing Stairs**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "House Robber",
    "difficulty": "Medium",
    "acceptance": "32.1%",
    "id": 105,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **House Robber**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "House Robber II",
    "difficulty": "Medium",
    "acceptance": "35.5%",
    "id": 106,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **House Robber II**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Longest Palindromic Substring",
    "difficulty": "Medium",
    "acceptance": "26.0%",
    "id": 107,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Longest Palindromic Substring**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Palindromic Substrings",
    "difficulty": "Medium",
    "acceptance": "22.4%",
    "id": 108,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Palindromic Substrings**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Decode Ways",
    "difficulty": "Easy",
    "acceptance": "15.6%",
    "id": 109,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Decode Ways**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Coin Change",
    "difficulty": "Medium",
    "acceptance": "26.8%",
    "id": 110,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Coin Change**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Maximum Product Subarray",
    "difficulty": "Easy",
    "acceptance": "59.8%",
    "id": 111,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Maximum Product Subarray**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Break",
    "difficulty": "Medium",
    "acceptance": "37.5%",
    "id": 112,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Word Break**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Longest Increasing Subsequence",
    "difficulty": "Medium",
    "acceptance": "48.1%",
    "id": 113,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Longest Increasing Subsequence**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Partition Equal Subset Sum",
    "difficulty": "Hard",
    "acceptance": "47.2%",
    "id": 114,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Partition Equal Subset Sum**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Unique Paths",
    "difficulty": "Easy",
    "acceptance": "75.7%",
    "id": 115,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Unique Paths**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Longest Common Subsequence",
    "difficulty": "Easy",
    "acceptance": "69.1%",
    "id": 116,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Longest Common Subsequence**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Edit Distance",
    "difficulty": "Medium",
    "acceptance": "71.3%",
    "id": 117,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Edit Distance**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Target Sum",
    "difficulty": "Hard",
    "acceptance": "48.8%",
    "id": 118,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Target Sum**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Interleaving String",
    "difficulty": "Medium",
    "acceptance": "16.7%",
    "id": 119,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Interleaving String**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Permutations",
    "difficulty": "Hard",
    "acceptance": "70.3%",
    "id": 120,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Permutations**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Subsets",
    "difficulty": "Easy",
    "acceptance": "81.5%",
    "id": 121,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Subsets**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Combination Sum",
    "difficulty": "Easy",
    "acceptance": "36.4%",
    "id": 122,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Combination Sum**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Combination Sum II",
    "difficulty": "Easy",
    "acceptance": "66.1%",
    "id": 123,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Combination Sum II**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Search",
    "difficulty": "Hard",
    "acceptance": "71.7%",
    "id": 124,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Word Search**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Palindrome Partitioning",
    "difficulty": "Hard",
    "acceptance": "37.5%",
    "id": 125,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Palindrome Partitioning**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Letter Combinations of a Phone Number",
    "difficulty": "Hard",
    "acceptance": "66.5%",
    "id": 126,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Letter Combinations of a Phone Number**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "N-Queens",
    "difficulty": "Easy",
    "acceptance": "57.3%",
    "id": 127,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **N-Queens**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Sudoku Solver",
    "difficulty": "Medium",
    "acceptance": "71.3%",
    "id": 128,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Sudoku Solver**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Restore IP Addresses",
    "difficulty": "Medium",
    "acceptance": "45.0%",
    "id": 129,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Restore IP Addresses**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Rotate Image",
    "difficulty": "Medium",
    "acceptance": "34.4%",
    "id": 130,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Rotate Image**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Spiral Matrix",
    "difficulty": "Medium",
    "acceptance": "80.2%",
    "id": 131,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Spiral Matrix**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Set Matrix Zeroes",
    "difficulty": "Medium",
    "acceptance": "39.4%",
    "id": 132,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Set Matrix Zeroes**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Happy Number",
    "difficulty": "Medium",
    "acceptance": "15.5%",
    "id": 133,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Happy Number**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Plus One",
    "difficulty": "Medium",
    "acceptance": "25.1%",
    "id": 134,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Plus One**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Pow(x, n)",
    "difficulty": "Easy",
    "acceptance": "83.0%",
    "id": 135,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Pow(x, n)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Multiply Strings",
    "difficulty": "Hard",
    "acceptance": "16.3%",
    "id": 136,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Multiply Strings**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Detect Squares",
    "difficulty": "Easy",
    "acceptance": "62.9%",
    "id": 137,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Detect Squares**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Max Points on a Line",
    "difficulty": "Medium",
    "acceptance": "59.4%",
    "id": 138,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Max Points on a Line**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Single Number",
    "difficulty": "Medium",
    "acceptance": "37.2%",
    "id": 139,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Single Number**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Number of 1 Bits",
    "difficulty": "Medium",
    "acceptance": "63.7%",
    "id": 140,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Number of 1 Bits**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Counting Bits",
    "difficulty": "Hard",
    "acceptance": "28.2%",
    "id": 141,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Counting Bits**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Missing Number",
    "difficulty": "Hard",
    "acceptance": "57.9%",
    "id": 142,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Missing Number**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Reverse Bits",
    "difficulty": "Medium",
    "acceptance": "60.3%",
    "id": 143,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Reverse Bits**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Sum of Two Integers",
    "difficulty": "Hard",
    "acceptance": "20.0%",
    "id": 144,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Sum of Two Integers**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Kth Largest Element in a Stream",
    "difficulty": "Medium",
    "acceptance": "34.9%",
    "id": 145,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Kth Largest Element in a Stream**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Last Stone Weight",
    "difficulty": "Medium",
    "acceptance": "43.6%",
    "id": 146,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Last Stone Weight**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "K Closest Points to Origin",
    "difficulty": "Medium",
    "acceptance": "42.7%",
    "id": 147,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **K Closest Points to Origin**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Kth Largest Element in an Array",
    "difficulty": "Medium",
    "acceptance": "15.7%",
    "id": 148,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Kth Largest Element in an Array**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Task Scheduler",
    "difficulty": "Easy",
    "acceptance": "38.5%",
    "id": 149,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Task Scheduler**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Design Twitter",
    "difficulty": "Medium",
    "acceptance": "23.1%",
    "id": 150,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Design Twitter**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Find Median from Data Stream",
    "difficulty": "Medium",
    "acceptance": "36.5%",
    "id": 151,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Find Median from Data Stream**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Merge k Sorted Lists",
    "difficulty": "Hard",
    "acceptance": "39.5%",
    "id": 152,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Merge k Sorted Lists**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Binary Search",
    "difficulty": "Easy",
    "acceptance": "56.8%",
    "id": 153,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Binary Search**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Search a 2D Matrix",
    "difficulty": "Hard",
    "acceptance": "54.0%",
    "id": 154,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Search a 2D Matrix**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Koko Eating Bananas",
    "difficulty": "Easy",
    "acceptance": "76.3%",
    "id": 155,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Koko Eating Bananas**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Find Minimum in Rotated Sorted Array",
    "difficulty": "Hard",
    "acceptance": "37.1%",
    "id": 156,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Find Minimum in Rotated Sorted Array**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Search in Rotated Sorted Array",
    "difficulty": "Hard",
    "acceptance": "21.7%",
    "id": 157,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Search in Rotated Sorted Array**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Time Based Key-Value Store",
    "difficulty": "Hard",
    "acceptance": "60.6%",
    "id": 158,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Time Based Key-Value Store**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Median of Two Sorted Arrays",
    "difficulty": "Medium",
    "acceptance": "69.3%",
    "id": 159,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Median of Two Sorted Arrays**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Two Sum (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "34.0%",
    "id": 160,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Two Sum (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Three Sum (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "70.2%",
    "id": 161,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Three Sum (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Container With Most Water (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "20.8%",
    "id": 162,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Container With Most Water (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Trapping Rain Water (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "61.1%",
    "id": 163,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Trapping Rain Water (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Product of Array Except Self (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "56.1%",
    "id": 164,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Product of Array Except Self (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Maximum Subarray (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "32.0%",
    "id": 165,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Maximum Subarray (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Merge Intervals (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "51.3%",
    "id": 166,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Merge Intervals (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Find Minimum in Rotated Sorted Array (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "56.6%",
    "id": 167,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Find Minimum in Rotated Sorted Array (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Search in Rotated Sorted Array (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "51.3%",
    "id": 168,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Search in Rotated Sorted Array (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Contains Duplicate (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "79.2%",
    "id": 169,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Contains Duplicate (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Best Time to Buy and Sell Stock (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "24.0%",
    "id": 170,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Best Time to Buy and Sell Stock (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Subarray Sum Equals K (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "69.0%",
    "id": 171,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Subarray Sum Equals K (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Next Permutation (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "59.6%",
    "id": 172,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Next Permutation (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Sort Colors (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "33.7%",
    "id": 173,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Sort Colors (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Move Zeroes (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "72.0%",
    "id": 174,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Move Zeroes (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Find All Duplicates in an Array (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "58.2%",
    "id": 175,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Find All Duplicates in an Array (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Longest Substring Without Repeating Characters (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "24.1%",
    "id": 176,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Substring Without Repeating Characters (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Longest Palindromic Substring (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "54.9%",
    "id": 177,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Palindromic Substring (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Valid Anagram (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "65.9%",
    "id": 178,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Valid Anagram (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Group Anagrams (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "45.2%",
    "id": 179,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Group Anagrams (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Valid Parentheses (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "20.3%",
    "id": 180,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Valid Parentheses (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Generate Parentheses (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "76.8%",
    "id": 181,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Generate Parentheses (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Longest Valid Parentheses (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "70.7%",
    "id": 182,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Valid Parentheses (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Minimum Window Substring (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "38.4%",
    "id": 183,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Minimum Window Substring (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Valid Palindrome (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "50.5%",
    "id": 184,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Valid Palindrome (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Longest Repeating Character Replacement (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "68.3%",
    "id": 185,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Repeating Character Replacement (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Palindromic Substrings (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "49.2%",
    "id": 186,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Palindromic Substrings (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Encode and Decode Strings (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "50.9%",
    "id": 187,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Encode and Decode Strings (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Find All Anagrams in a String (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "56.8%",
    "id": 188,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Find All Anagrams in a String (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Reverse Linked List (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "59.0%",
    "id": 189,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Reverse Linked List (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Merge Two Sorted Lists (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "78.5%",
    "id": 190,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Merge Two Sorted Lists (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Linked List Cycle (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "20.5%",
    "id": 191,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Linked List Cycle (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Reorder List (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "61.1%",
    "id": 192,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Reorder List (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Remove Nth Node From End of List (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "68.8%",
    "id": 193,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Remove Nth Node From End of List (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Copy List with Random Pointer (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "31.2%",
    "id": 194,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Copy List with Random Pointer (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Merge k Sorted Lists (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "62.7%",
    "id": 195,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Merge k Sorted Lists (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Reverse Nodes in k-Group (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "45.2%",
    "id": 196,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Reverse Nodes in k-Group (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Intersection of Two Linked Lists (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "34.1%",
    "id": 197,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Intersection of Two Linked Lists (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Palindrome Linked List (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "19.3%",
    "id": 198,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Palindrome Linked List (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Swapping Nodes in a Linked List (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "51.0%",
    "id": 199,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Swapping Nodes in a Linked List (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Odd Even Linked List (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "67.2%",
    "id": 200,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Odd Even Linked List (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Add Two Numbers (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "82.6%",
    "id": 201,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Add Two Numbers (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Maximum Depth of Binary Tree (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "52.4%",
    "id": 202,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Maximum Depth of Binary Tree (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Same Tree (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "80.0%",
    "id": 203,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Same Tree (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Invert Binary Tree (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "64.2%",
    "id": 204,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Invert Binary Tree (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Binary Tree Maximum Path Sum (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "58.7%",
    "id": 205,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Binary Tree Maximum Path Sum (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Binary Tree Level Order Traversal (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "58.9%",
    "id": 206,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Binary Tree Level Order Traversal (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Serialize and Deserialize Binary Tree (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "27.6%",
    "id": 207,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Serialize and Deserialize Binary Tree (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Subtree of Another Tree (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "61.8%",
    "id": 208,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Subtree of Another Tree (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Construct Binary Tree from Preorder and Inorder Traversal (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "82.8%",
    "id": 209,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Construct Binary Tree from Preorder and Inorder Traversal (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Validate Binary Search Tree (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "15.2%",
    "id": 210,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Validate Binary Search Tree (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Kth Smallest Element in a BST (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "48.7%",
    "id": 211,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Kth Smallest Element in a BST (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Lowest Common Ancestor of a BST (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "40.1%",
    "id": 212,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Lowest Common Ancestor of a BST (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Implement Trie (Prefix Tree) (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "47.3%",
    "id": 213,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Implement Trie (Prefix Tree) (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Design Add and Search Words Data Structure (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "65.1%",
    "id": 214,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Design Add and Search Words Data Structure (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Search II (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "84.1%",
    "id": 215,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Word Search II (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Number of Islands (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "70.2%",
    "id": 216,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Number of Islands (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Clone Graph (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "17.4%",
    "id": 217,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Clone Graph (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Max Area of Island (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "27.3%",
    "id": 218,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Max Area of Island (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Pacific Atlantic Water Flow (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "20.6%",
    "id": 219,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Pacific Atlantic Water Flow (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Surrounded Regions (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "38.9%",
    "id": 220,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Surrounded Regions (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Rotting Oranges (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "41.9%",
    "id": 221,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Rotting Oranges (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Walls and Gates (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "60.5%",
    "id": 222,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Walls and Gates (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Course Schedule (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "61.3%",
    "id": 223,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Course Schedule (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Course Schedule II (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "79.1%",
    "id": 224,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Course Schedule II (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Redundant Connection (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "54.4%",
    "id": 225,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Redundant Connection (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Number of Connected Components in an Undirected Graph (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "55.4%",
    "id": 226,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Number of Connected Components in an Undirected Graph (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Graph Valid Tree (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "54.3%",
    "id": 227,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Graph Valid Tree (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Ladder (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "52.5%",
    "id": 228,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Word Ladder (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Alien Dictionary (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "48.0%",
    "id": 229,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Alien Dictionary (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Network Delay Time (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "47.1%",
    "id": 230,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Network Delay Time (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Cheapest Flights Within K Stops (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "65.5%",
    "id": 231,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Cheapest Flights Within K Stops (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Climbing Stairs (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "83.4%",
    "id": 232,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Climbing Stairs (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Min Cost Climbing Stairs (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "34.0%",
    "id": 233,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Min Cost Climbing Stairs (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "House Robber (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "82.8%",
    "id": 234,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **House Robber (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "House Robber II (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "62.2%",
    "id": 235,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **House Robber II (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Longest Palindromic Substring (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "16.7%",
    "id": 236,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Longest Palindromic Substring (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Palindromic Substrings (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "23.0%",
    "id": 237,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Palindromic Substrings (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Decode Ways (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "20.8%",
    "id": 238,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Decode Ways (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Coin Change (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "31.3%",
    "id": 239,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Coin Change (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Maximum Product Subarray (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "67.0%",
    "id": 240,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Maximum Product Subarray (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Break (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "40.5%",
    "id": 241,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Word Break (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Longest Increasing Subsequence (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "43.6%",
    "id": 242,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Longest Increasing Subsequence (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Partition Equal Subset Sum (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "35.7%",
    "id": 243,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Partition Equal Subset Sum (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Unique Paths (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "66.2%",
    "id": 244,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Unique Paths (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Longest Common Subsequence (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "35.1%",
    "id": 245,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Longest Common Subsequence (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Edit Distance (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "51.4%",
    "id": 246,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Edit Distance (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Target Sum (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "84.2%",
    "id": 247,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Target Sum (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Interleaving String (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "47.6%",
    "id": 248,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Interleaving String (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Permutations (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "62.6%",
    "id": 249,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Permutations (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Subsets (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "60.2%",
    "id": 250,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Subsets (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Combination Sum (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "34.7%",
    "id": 251,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Combination Sum (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Combination Sum II (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "17.6%",
    "id": 252,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Combination Sum II (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Search (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "57.6%",
    "id": 253,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Word Search (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Palindrome Partitioning (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "37.1%",
    "id": 254,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Palindrome Partitioning (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Letter Combinations of a Phone Number (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "19.9%",
    "id": 255,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Letter Combinations of a Phone Number (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "N-Queens (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "53.8%",
    "id": 256,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **N-Queens (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Sudoku Solver (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "15.1%",
    "id": 257,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Sudoku Solver (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Restore IP Addresses (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "20.6%",
    "id": 258,
    "topic": "DSA: Backtracking",
    "description": "Solve the classic Backtracking problem: **Restore IP Addresses (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 20`\n- The solution set must not contain duplicate combinations.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Rotate Image (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "80.4%",
    "id": 259,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Rotate Image (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Spiral Matrix (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "76.8%",
    "id": 260,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Spiral Matrix (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Set Matrix Zeroes (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "45.0%",
    "id": 261,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Set Matrix Zeroes (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Happy Number (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "36.8%",
    "id": 262,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Happy Number (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Plus One (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "28.8%",
    "id": 263,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Plus One (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Pow(x, n) (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "18.4%",
    "id": 264,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Pow(x, n) (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Multiply Strings (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "80.7%",
    "id": 265,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Multiply Strings (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Detect Squares (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "34.5%",
    "id": 266,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Detect Squares (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Max Points on a Line (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "58.9%",
    "id": 267,
    "topic": "DSA: Math & Geometry",
    "description": "Solve the classic Math & Geometry problem: **Max Points on a Line (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Single Number (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "20.3%",
    "id": 268,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Single Number (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Number of 1 Bits (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "80.0%",
    "id": 269,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Number of 1 Bits (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Counting Bits (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "42.2%",
    "id": 270,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Counting Bits (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Missing Number (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "73.7%",
    "id": 271,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Missing Number (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Reverse Bits (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "79.0%",
    "id": 272,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Reverse Bits (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Sum of Two Integers (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "51.7%",
    "id": 273,
    "topic": "DSA: Bit Manipulation",
    "description": "Solve the classic Bit Manipulation problem: **Sum of Two Integers (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `0 <= N <= 10^4`\n- Optimization is key to passing all test cases.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Kth Largest Element in a Stream (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "56.1%",
    "id": 274,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Kth Largest Element in a Stream (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Last Stone Weight (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "35.3%",
    "id": 275,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Last Stone Weight (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "K Closest Points to Origin (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "23.6%",
    "id": 276,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **K Closest Points to Origin (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Kth Largest Element in an Array (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "38.6%",
    "id": 277,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Kth Largest Element in an Array (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Task Scheduler (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "21.5%",
    "id": 278,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Task Scheduler (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Design Twitter (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "34.9%",
    "id": 279,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Design Twitter (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Find Median from Data Stream (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "73.2%",
    "id": 280,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Find Median from Data Stream (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Merge k Sorted Lists (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "58.8%",
    "id": 281,
    "topic": "DSA: Heap / Priority Queue",
    "description": "Solve the classic Heap / Priority Queue problem: **Merge k Sorted Lists (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Binary Search (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "68.6%",
    "id": 282,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Binary Search (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Search a 2D Matrix (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "38.2%",
    "id": 283,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Search a 2D Matrix (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Koko Eating Bananas (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "69.2%",
    "id": 284,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Koko Eating Bananas (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Find Minimum in Rotated Sorted Array (Variant 1)",
    "difficulty": "Easy",
    "acceptance": "27.8%",
    "id": 285,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Find Minimum in Rotated Sorted Array (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Search in Rotated Sorted Array (Variant 1)",
    "difficulty": "Medium",
    "acceptance": "27.7%",
    "id": 286,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Search in Rotated Sorted Array (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Time Based Key-Value Store (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "63.5%",
    "id": 287,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Time Based Key-Value Store (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Median of Two Sorted Arrays (Variant 1)",
    "difficulty": "Hard",
    "acceptance": "60.4%",
    "id": 288,
    "topic": "DSA: Binary Search",
    "description": "Solve the classic Binary Search problem: **Median of Two Sorted Arrays (Variant 1)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Two Sum (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "22.5%",
    "id": 289,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Two Sum (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Three Sum (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "48.1%",
    "id": 290,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Three Sum (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Container With Most Water (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "45.1%",
    "id": 291,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Container With Most Water (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Trapping Rain Water (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "84.0%",
    "id": 292,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Trapping Rain Water (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Product of Array Except Self (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "46.3%",
    "id": 293,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Product of Array Except Self (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Maximum Subarray (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "36.4%",
    "id": 294,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Maximum Subarray (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Merge Intervals (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "75.7%",
    "id": 295,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Merge Intervals (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Find Minimum in Rotated Sorted Array (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "24.8%",
    "id": 296,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Find Minimum in Rotated Sorted Array (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Search in Rotated Sorted Array (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "37.6%",
    "id": 297,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Search in Rotated Sorted Array (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Contains Duplicate (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "78.9%",
    "id": 298,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Contains Duplicate (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Best Time to Buy and Sell Stock (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "76.7%",
    "id": 299,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Best Time to Buy and Sell Stock (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Subarray Sum Equals K (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "39.6%",
    "id": 300,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Subarray Sum Equals K (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Next Permutation (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "74.7%",
    "id": 301,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Next Permutation (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Sort Colors (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "32.5%",
    "id": 302,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Sort Colors (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Move Zeroes (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "29.7%",
    "id": 303,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Move Zeroes (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Find All Duplicates in an Array (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "17.5%",
    "id": 304,
    "topic": "DSA: Arrays",
    "description": "Solve the classic Arrays problem: **Find All Duplicates in an Array (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "nums = [2,7,11,15], target = 9",
        "output": "Output depends on problem specific goals",
        "explanation": "This is a generic array example."
      },
      {
        "input": "nums = [3,2,4], target = 6",
        "output": "Output depends on goal",
        "explanation": "Second generic example."
      }
    ]
  },
  {
    "title": "Longest Substring Without Repeating Characters (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "71.9%",
    "id": 305,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Substring Without Repeating Characters (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Longest Palindromic Substring (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "48.9%",
    "id": 306,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Palindromic Substring (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Valid Anagram (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "66.1%",
    "id": 307,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Valid Anagram (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Group Anagrams (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "33.3%",
    "id": 308,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Group Anagrams (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Valid Parentheses (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "75.5%",
    "id": 309,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Valid Parentheses (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Generate Parentheses (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "29.2%",
    "id": 310,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Generate Parentheses (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Longest Valid Parentheses (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "22.6%",
    "id": 311,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Valid Parentheses (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Minimum Window Substring (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "36.3%",
    "id": 312,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Minimum Window Substring (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Valid Palindrome (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "51.8%",
    "id": 313,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Valid Palindrome (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Longest Repeating Character Replacement (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "44.3%",
    "id": 314,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Longest Repeating Character Replacement (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Palindromic Substrings (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "32.1%",
    "id": 315,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Palindromic Substrings (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Encode and Decode Strings (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "60.3%",
    "id": 316,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Encode and Decode Strings (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Find All Anagrams in a String (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "74.0%",
    "id": 317,
    "topic": "DSA: Strings",
    "description": "Solve the classic Strings problem: **Find All Anagrams in a String (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "s = 'abcabcbb'",
        "output": "Expected String or Integer",
        "explanation": "Validates string manipulation logic."
      },
      {
        "input": "s = 'pwwkew'",
        "output": "Expected Result",
        "explanation": "Edge case check."
      }
    ]
  },
  {
    "title": "Reverse Linked List (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "64.2%",
    "id": 318,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Reverse Linked List (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Merge Two Sorted Lists (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "22.2%",
    "id": 319,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Merge Two Sorted Lists (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Linked List Cycle (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "72.8%",
    "id": 320,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Linked List Cycle (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Reorder List (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "69.5%",
    "id": 321,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Reorder List (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Remove Nth Node From End of List (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "49.2%",
    "id": 322,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Remove Nth Node From End of List (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Copy List with Random Pointer (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "69.9%",
    "id": 323,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Copy List with Random Pointer (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Merge k Sorted Lists (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "31.4%",
    "id": 324,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Merge k Sorted Lists (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Reverse Nodes in k-Group (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "65.7%",
    "id": 325,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Reverse Nodes in k-Group (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Intersection of Two Linked Lists (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "74.2%",
    "id": 326,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Intersection of Two Linked Lists (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Palindrome Linked List (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "30.1%",
    "id": 327,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Palindrome Linked List (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Swapping Nodes in a Linked List (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "28.8%",
    "id": 328,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Swapping Nodes in a Linked List (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Odd Even Linked List (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "58.5%",
    "id": 329,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Odd Even Linked List (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Add Two Numbers (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "36.5%",
    "id": 330,
    "topic": "DSA: Linked Lists",
    "description": "Solve the classic Linked Lists problem: **Add Two Numbers (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Maximum Depth of Binary Tree (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "17.4%",
    "id": 331,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Maximum Depth of Binary Tree (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Same Tree (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "57.9%",
    "id": 332,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Same Tree (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Invert Binary Tree (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "59.1%",
    "id": 333,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Invert Binary Tree (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Binary Tree Maximum Path Sum (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "57.0%",
    "id": 334,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Binary Tree Maximum Path Sum (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Binary Tree Level Order Traversal (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "64.6%",
    "id": 335,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Binary Tree Level Order Traversal (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Serialize and Deserialize Binary Tree (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "15.9%",
    "id": 336,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Serialize and Deserialize Binary Tree (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Subtree of Another Tree (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "49.6%",
    "id": 337,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Subtree of Another Tree (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Construct Binary Tree from Preorder and Inorder Traversal (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "21.2%",
    "id": 338,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Construct Binary Tree from Preorder and Inorder Traversal (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Validate Binary Search Tree (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "36.9%",
    "id": 339,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Validate Binary Search Tree (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Kth Smallest Element in a BST (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "40.2%",
    "id": 340,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Kth Smallest Element in a BST (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Lowest Common Ancestor of a BST (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "59.3%",
    "id": 341,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Lowest Common Ancestor of a BST (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Implement Trie (Prefix Tree) (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "66.1%",
    "id": 342,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Implement Trie (Prefix Tree) (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Design Add and Search Words Data Structure (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "46.8%",
    "id": 343,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Design Add and Search Words Data Structure (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Search II (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "74.5%",
    "id": 344,
    "topic": "DSA: Trees",
    "description": "Solve the classic Trees problem: **Word Search II (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Number of Islands (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "33.5%",
    "id": 345,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Number of Islands (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Clone Graph (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "39.0%",
    "id": 346,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Clone Graph (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Max Area of Island (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "23.1%",
    "id": 347,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Max Area of Island (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Pacific Atlantic Water Flow (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "43.2%",
    "id": 348,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Pacific Atlantic Water Flow (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Surrounded Regions (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "46.4%",
    "id": 349,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Surrounded Regions (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Rotting Oranges (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "43.8%",
    "id": 350,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Rotting Oranges (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Walls and Gates (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "38.4%",
    "id": 351,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Walls and Gates (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Course Schedule (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "40.2%",
    "id": 352,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Course Schedule (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Course Schedule II (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "45.1%",
    "id": 353,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Course Schedule II (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Redundant Connection (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "35.2%",
    "id": 354,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Redundant Connection (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Number of Connected Components in an Undirected Graph (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "45.5%",
    "id": 355,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Number of Connected Components in an Undirected Graph (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Graph Valid Tree (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "41.5%",
    "id": 356,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Graph Valid Tree (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Ladder (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "69.6%",
    "id": 357,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Word Ladder (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Alien Dictionary (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "18.6%",
    "id": 358,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Alien Dictionary (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Network Delay Time (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "64.7%",
    "id": 359,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Network Delay Time (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Cheapest Flights Within K Stops (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "44.9%",
    "id": 360,
    "topic": "DSA: Graphs",
    "description": "Solve the classic Graphs problem: **Cheapest Flights Within K Stops (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- The number of nodes in the graph/tree is in the range `[0, 10^4]`.\n- `-10^4 <= Node.val <= 10^4`\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Climbing Stairs (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "63.6%",
    "id": 361,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Climbing Stairs (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Min Cost Climbing Stairs (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "55.6%",
    "id": 362,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Min Cost Climbing Stairs (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "House Robber (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "23.5%",
    "id": 363,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **House Robber (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "House Robber II (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "76.7%",
    "id": 364,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **House Robber II (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Longest Palindromic Substring (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "81.8%",
    "id": 365,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Longest Palindromic Substring (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Palindromic Substrings (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "83.4%",
    "id": 366,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Palindromic Substrings (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Decode Ways (Variant 2)",
    "difficulty": "Medium",
    "acceptance": "32.0%",
    "id": 367,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Decode Ways (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Coin Change (Variant 2)",
    "difficulty": "Hard",
    "acceptance": "48.4%",
    "id": 368,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Coin Change (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Maximum Product Subarray (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "17.8%",
    "id": 369,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Maximum Product Subarray (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  },
  {
    "title": "Word Break (Variant 2)",
    "difficulty": "Easy",
    "acceptance": "80.5%",
    "id": 370,
    "topic": "DSA: Dynamic Programming",
    "description": "Solve the classic Dynamic Programming problem: **Word Break (Variant 2)**.\n\nYou must implement an optimal algorithm that meets the strict time and space complexities associated with this problem.\n\n### Constraints:\n- `1 <= input.length <= 10^5`\n- `-10^9 <= input[i] <= 10^9`\n- `O(N)` or `O(N log N)` time complexity expected.\n\n### Notes:\n- Ensure edge cases (like empty inputs or single-element inputs) are handled properly.",
    "examples": [
      {
        "input": "Generic Input A",
        "output": "Expected Output A",
        "explanation": "Example case 1 showing normal execution."
      },
      {
        "input": "Generic Input B",
        "output": "Expected Output B",
        "explanation": "Example case 2 showing edge case handling."
      }
    ]
  }
];

if (typeof module !== 'undefined') {
  module.exports = codingProblems;
}
