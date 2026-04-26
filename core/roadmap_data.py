DEVELOPER_ROADMAPS = {
    "frontend-developer": {
        "name": "Frontend Developer",
        "description": "Builds the user interface of websites.",
        "phases": [
            {"title": "Internet Basics", "topics": ["How the internet works", "What is HTTP?", "Browsers and how they work", "DNS and its resolution process"]},
            {"title": "HTML", "topics": ["Basics", "Semantic HTML", "Forms and Validations", "Conventions and Best Practices", "Accessibility", "SEO Basics"]},
            {"title": "CSS", "topics": ["Basics", "Making Layouts (Flexbox, Grid)", "Responsive design and Media Queries", "Animations", "CSS Frameworks (Tailwind, Bootstrap)"]},
            {"title": "JavaScript", "topics": ["Syntax & Basic Constructs", "DOM Manipulation", "Fetch API / Ajax", "ES6+ Concepts", "Hoisting, Closures, Prototypal Inheritance"]},
            {"title": "Version Control", "topics": ["Git basics", "GitHub / GitLab", "Branching models"]},
            {"title": "Frontend Frameworks", "topics": ["React (Hooks, Components, Context API)", "Angular (Directives, Services, RxJS)", "Vue (Directives, Vuex)"]},
            {"title": "State Management", "topics": ["Redux (for React)", "NgRx (for Angular)", "Vuex (for Vue)"]},
            {"title": "Build Tools", "topics": ["Webpack", "Vite", "NPM / Yarn", "Task Runners"]}
        ]
    },
    "backend-developer": {
        "name": "Backend Developer",
        "description": "Handles server, database, and APIs.",
        "phases": [
            {"title": "Internet & OS Basics", "topics": ["Terminal usage", "OS Fundamentals", "Basic Networking (TCP/IP, HTTP)"]},
            {"title": "Programming Language", "topics": ["Python", "Java", "Node.js", "PHP", "Ruby", "C# (Choose one and master)"]},
            {"title": "Version Control", "topics": ["Git", "GitHub/GitLab/BitBucket"]},
            {"title": "Relational Databases", "topics": ["PostgreSQL", "MySQL", "Database Design", "Normalization", "Joins, Indexes"]},
            {"title": "NoSQL Databases", "topics": ["MongoDB", "Redis", "Cassandra", "When to use NoSQL"]},
            {"title": "APIs and Web Services", "topics": ["REST", "JSON APIs", "GraphQL", "gRPC", "SOAP"]},
            {"title": "Caching", "topics": ["CDN", "Server-side caching", "Redis", "Memcached"]},
            {"title": "Security Basics", "topics": ["HTTPS", "CORS", "OAuth 2.0 / JWT", "OWASP Top 10", "Hashing (BCrypt)"]},
            {"title": "Testing", "topics": ["Unit testing", "Integration testing", "Mocking code"]},
            {"title": "CI/CD & Deployment", "topics": ["Docker", "Basic Kubernetes", "Jenkins / GitHub Actions", "AWS / DigitalOcean"]}
        ]
    },
    "full-stack-developer": {
        "name": "Full-Stack Developer",
        "description": "Works on both frontend and backend.",
        "phases": [
            {"title": "Internet & Basic Frontend", "topics": ["HTML", "CSS", "Basic JavaScript", "DOM Manipulation"]},
            {"title": "Backend Language", "topics": ["Node.js OR Python OR Java"]},
            {"title": "Version Control", "topics": ["Git", "GitHub"]},
            {"title": "Databases", "topics": ["SQL (PostgreSQL/MySQL)", "NoSQL (MongoDB)"]},
            {"title": "Frontend Framework", "topics": ["React OR Angular OR Vue"]},
            {"title": "Backend Framework", "topics": ["Express OR Django OR Spring Boot"]},
            {"title": "APIs", "topics": ["RESTful Routing", "API Authentication (JWT)"]},
            {"title": "Deployment", "topics": ["Docker Basics", "Heroku/Vercel/Render", "Nginx/Apache Settings"]}
        ]
    },
    "mobile-app-developer": {
        "name": "Mobile App Developer",
        "description": "Builds mobile applications.",
        "phases": [
            {"title": "Programming Languages", "topics": ["Kotlin (Android) or Swift (iOS)", "Dart (Cross-platform)", "JavaScript (Cross-platform)"]},
            {"title": "Native Development Fundamentals", "topics": ["App Lifecycles", "UI Layouts and Views", "Navigation and Routing"]},
            {"title": "Data Storage", "topics": ["SQLite/Room", "Core Data", "SharedPreferences / User Defaults", "Remote Data Fetching"]},
            {"title": "Architecture Patterns", "topics": ["MVC", "MVVM", "Clean Architecture"]},
            {"title": "Cross-Platform Frameworks (Optional)", "topics": ["Flutter", "React Native"]},
            {"title": "Device APIs", "topics": ["Camera", "Location/GPS", "Sensors", "Push Notifications"]},
            {"title": "Publishing", "topics": ["App Store Connect", "Google Play Console", "App Signing"]}
        ]
    },
    "android-developer": {
        "name": "Android Developer",
        "description": "Develops Android apps.",
        "phases": [
            {"title": "Language Fundamentals", "topics": ["Kotlin Basics", "Java Basics (Legacy)", "Coroutines"]},
            {"title": "Android Studio & Tools", "topics": ["Gradle Build System", "Android Emulator", "Logcat Debugging"]},
            {"title": "Android Core", "topics": ["Activities & Fragments", "Intents", "Services", "Broadcast Receivers"]},
            {"title": "UI Components", "topics": ["XML Layouts", "ConstraintLayout", "RecyclerView", "Jetpack Compose (Modern UI)"]},
            {"title": "Jetpack Architecture", "topics": ["ViewModel", "LiveData/StateFlow", "Room Database", "Navigation Component"]},
            {"title": "Networking", "topics": ["Retrofit", "OkHttp", "JSON Parsing (Moshi/Gson)"]},
            {"title": "Dependency Injection", "topics": ["Dagger", "Hilt", "Koin"]}
        ]
    },
    "ios-developer": {
        "name": "iOS Developer",
        "description": "Develops Apple iPhone apps.",
        "phases": [
            {"title": "Language Fundamentals", "topics": ["Swift Basics", "Optionals", "Closures", "Structs vs Classes"]},
            {"title": "IDE & Tools", "topics": ["Xcode", "Interface Builder", "Instruments"]},
            {"title": "UI Development", "topics": ["UIKit", "Storyboards/XIBs", "Auto Layout", "SwiftUI (Modern UI)"]},
            {"title": "iOS Core Concepts", "topics": ["View Controller Lifecycle", "Delegation Pattern", "Protocols"]},
            {"title": "Data Management", "topics": ["Core Data", "UserDefaults", "File System", "Codable"]},
            {"title": "Networking", "topics": ["URLSession", "AlamoFire", "Combine Framework"]},
            {"title": "Dependency Management", "topics": ["CocoaPods", "Swift Package Manager (SPM)"]}
        ]
    },
    "game-developer": {
        "name": "Game Developer",
        "description": "Creates video games.",
        "phases": [
            {"title": "Language Fundamentals", "topics": ["C++ (for Unreal/Custom)", "C# (for Unity)"]},
            {"title": "Math & Physics Foundations", "topics": ["Linear Algebra (Vectors, Matrices)", "Trigonometry", "Collision Detection"]},
            {"title": "Game Engines", "topics": ["Unity (Component System)", "Unreal Engine (Blueprints)", "Godot"]},
            {"title": "Game Loops & Architecture", "topics": ["Update Loops", "Entity-Component System (ECS)", "State Machines"]},
            {"title": "Graphics & Rendering", "topics": ["Shaders", "Lighting", "Materials", "OpenGL / DirectX basics"]},
            {"title": "Audio & Input", "topics": ["Sound processing", "Input handling (Keyboard, Controller)"]},
            {"title": "AI in Games", "topics": ["Pathfinding (A*)", "NavMeshes", "Behavior Trees"]}
        ]
    },
    "data-scientist": {
        "name": "Data Scientist",
        "description": "Analyzes data and builds models.",
        "phases": [
            {"title": "Fundamentals", "topics": ["Python / R", "Statistics & Probability", "Linear Algebra", "Calculus"]},
            {"title": "Data Manipulation", "topics": ["Pandas", "NumPy", "SQL", "Data Cleaning"]},
            {"title": "Data Visualization", "topics": ["Matplotlib", "Seaborn", "Tableau / PowerBI", "Plotly"]},
            {"title": "Machine Learning", "topics": ["Supervised Learning (Regression, Classification)", "Unsupervised Learning (Clustering, PCA)"]},
            {"title": "ML Libraries", "topics": ["Scikit-learn", "XGBoost", "LightGBM"]},
            {"title": "Model Evaluation", "topics": ["Cross-validation", "Hyperparameter tuning", "ROC/AUC, Precision/Recall"]},
            {"title": "Deployment Basics", "topics": ["Flask/FastAPI for model serving", "Pickle / ONNX", "Docker basics"]}
        ]
    },
    "machine-learning-developer": {
        "name": "Machine Learning Developer",
        "description": "Builds ML models.",
        "phases": [
            {"title": "Programming & Math", "topics": ["Python", "Linear Algebra", "Calculus", "Optimization Algorithms (Gradient Descent)"]},
            {"title": "Data Processing", "topics": ["NumPy", "Pandas", "Feature Engineering", "Data Normalization"]},
            {"title": "Traditional ML Fundamentals", "topics": ["Decision Trees", "Random Forests", "SVMs", "K-Means"]},
            {"title": "Deep Learning Basics", "topics": ["Neural Networks", "Backpropagation", "Activation Functions"]},
            {"title": "Deep Learning Frameworks", "topics": ["TensorFlow", "PyTorch", "Keras"]},
            {"title": "MLOps", "topics": ["MLflow", "Model versioning", "Kubeflow", "GCP/AWS ML Services"]}
        ]
    },
    "ai-developer": {
        "name": "AI Developer",
        "description": "Creates AI systems and applications.",
        "phases": [
            {"title": "Core Foundations", "topics": ["Python", "Algorithms & Data Structures", "Probability & Statistics"]},
            {"title": "Machine Learning", "topics": ["Supervised & Unsupervised Learning", "Scikit-Learn"]},
            {"title": "Deep Learning", "topics": ["Neural Networks", "PyTorch / TensorFlow"]},
            {"title": "Natural Language Processing (NLP)", "topics": ["Tokenization", "Word Embeddings (Word2Vec)", "Transformers", "LLMs (GPT/BERT)"]},
            {"title": "Computer Vision", "topics": ["CNNs", "Image Classification", "Object Detection (YOLO)", "OpenCV"]},
            {"title": "Generative AI", "topics": ["GANs", "Diffusion Models", "Prompt Engineering"]},
            {"title": "Deployment", "topics": ["ONNX", "TensorRT", "FastAPI model serving"]}
        ]
    },
    "devops-engineer": {
        "name": "DevOps Engineer",
        "description": "Manages deployment and infrastructure.",
        "phases": [
            {"title": "OS & CLI", "topics": ["Linux/Unix Administration", "Bash Scripting", "Networking (DNS, TCP/IP)"]},
            {"title": "Version Control", "topics": ["Git workflow", "GitHub / GitLab administration"]},
            {"title": "Containers", "topics": ["Docker", "Docker Compose", "Container Registry"]},
            {"title": "Orchestration", "topics": ["Kubernetes (Pods, Services, Deployments)", "Helm"]},
            {"title": "CI/CD", "topics": ["Jenkins", "GitHub Actions", "GitLab CI", "CircleCI"]},
            {"title": "Infrastructure as Code (IaC)", "topics": ["Terraform", "Ansible", "CloudFormation", "Chef/Puppet"]},
            {"title": "Cloud Providers", "topics": ["AWS (EC2, S3, RDS, IAM)", "Azure", "GCP"]},
            {"title": "Monitoring & Logging", "topics": ["Prometheus", "Grafana", "ELK Stack", "Datadog"]}
        ]
    },
    "cloud-developer": {
        "name": "Cloud Developer",
        "description": "Builds cloud applications.",
        "phases": [
            {"title": "Programming & APIs", "topics": ["Python / Go / Node.js", "REST APIs", "GraphQL"]},
            {"title": "Cloud Fundamentals", "topics": ["Compute (EC2, VMs)", "Storage (S3, Blobs)", "Networking (VPCs, Subnets)"]},
            {"title": "Serverless Technologies", "topics": ["AWS Lambda", "Azure Functions", "Google Cloud Functions"]},
            {"title": "Cloud Databases", "topics": ["DynamoDB", "CosmosDB", "RDS / Cloud SQL"]},
            {"title": "Infrastructure as Code", "topics": ["Terraform", "AWS CDK", "ARM Templates"]},
            {"title": "Security", "topics": ["IAM (Identity & Access Management)", "Key Management", "WAF"]},
            {"title": "Messaging & Events", "topics": ["SQS / SNS", "Kafka", "EventBridge"]}
        ]
    },
    "cybersecurity-developer": {
        "name": "Cybersecurity Developer",
        "description": "Builds secure software systems.",
        "phases": [
            {"title": "Networking Basics", "topics": ["TCP/IP", "OSI Model", "DNS/DHCP", "Firewalls", "VPNs"]},
            {"title": "OS Security", "topics": ["Linux Security", "Windows Internals", "Active Directory"]},
            {"title": "Scripting & Programming", "topics": ["Python", "Bash", "C/C++ basics", "PowerShell"]},
            {"title": "Ethical Hacking / Penetration Testing", "topics": ["Kali Linux", "Metasploit", "Nmap", "Wireshark"]},
            {"title": "Application Security", "topics": ["OWASP Top 10", "SQL Injection", "XSS", "CSRF", "Burp Suite"]},
            {"title": "Cryptography", "topics": ["Symmetric/Asymmetric Encryption", "Hashing algorithms", "PKI/Certificates"]},
            {"title": "Security Operations (SecOps)", "topics": ["SIEM tools (Splunk, QRadar)", "Intrusion Detection (IDS/IPS)", "Incident Response"]}
        ]
    },
    "blockchain-developer": {
        "name": "Blockchain Developer",
        "description": "Develops blockchain applications.",
        "phases": [
            {"title": "Programming Fundamentals", "topics": ["JavaScript / TypeScript", "Python", "Go"]},
            {"title": "Cryptography Basics", "topics": ["Hash Functions (SHA-256)", "Public-Key Cryptography", "Digital Signatures"]},
            {"title": "Blockchain Concepts", "topics": ["Decentralization", "Consensus Algorithms (PoW, PoS)", "Distributed Ledgers"]},
            {"title": "Smart Contracts", "topics": ["Solidity", "Vyper", "Rust (for Solana)"]},
            {"title": "Ethereum Ecosystem", "topics": ["Ethereum Virtual Machine (EVM)", "Truffle", "Hardhat", "Ganache", "ERC Tokens (ERC-20, ERC-721)"]},
            {"title": "Web3 integration", "topics": ["Web3.js", "Ethers.js", "Metamask Integration"]},
            {"title": "DeFi & Advanced Concepts", "topics": ["Oracles (Chainlink)", "DAOs", "Zero-Knowledge Proofs (ZKPs)"]}
        ]
    },
    "embedded-systems-developer": {
        "name": "Embedded Systems Developer",
        "description": "Works with hardware and microcontrollers.",
        "phases": [
            {"title": "Programming Languages", "topics": ["C", "C++", "Assembly basics"]},
            {"title": "Hardware Fundamentals", "topics": ["Digital Logic", "Microcontrollers (MCU)", "Microprocessors"]},
            {"title": "Development Boards", "topics": ["Arduino", "Raspberry Pi", "STM32", "ESP32"]},
            {"title": "Communication Protocols", "topics": ["I2C", "SPI", "UART / USART", "CAN bus"]},
            {"title": "Real-Time Operating Systems", "topics": ["RTOS Basics", "FreeRTOS", "Thread synchronization", "Interrupts"]},
            {"title": "Interfacing & Sensors", "topics": ["GPIO", "ADC / DAC", "PWM", "Sensor Integration"]},
            {"title": "Testing & Debugging", "topics": ["Oscilloscopes", "Logic Analyzers", "JTAG/SWD Debugging"]}
        ]
    },
    "desktop-application-developer": {
        "name": "Desktop Application Developer",
        "description": "Builds desktop software.",
        "phases": [
            {"title": "Programming Languages", "topics": ["C#", "C++", "Java", "Python", "JavaScript (Electron)"]},
            {"title": "GUI Frameworks (C# / Windows)", "topics": ["WPF", "WinForms", "UWP", "MAUI"]},
            {"title": "GUI Frameworks (Cross-Platform)", "topics": ["Electron", "Qt", "Tauri", "JavaFX", "Tkinter"]},
            {"title": "OS Integration", "topics": ["File System Access", "Registry (Windows)", "System Tray", "Native Notifications"]},
            {"title": "Database Integration", "topics": ["SQLite", "Local Storage", "Entity Framework"]},
            {"title": "Packaging & Distribution", "topics": [".MSI/.EXE Creation", "App Store Publishing", "Auto-updaters (Squirrel)"]}
        ]
    },
    "ar-vr-developer": {
        "name": "AR / VR Developer",
        "description": "Creates virtual reality and augmented reality apps.",
        "phases": [
            {"title": "Programming Languages", "topics": ["C# (for Unity)", "C++ (for Unreal)"]},
            {"title": "3D Math & Physics", "topics": ["Vectors", "Quaternions", "Transforms", "Collisions"]},
            {"title": "Game Engines", "topics": ["Unity", "Unreal Engine"]},
            {"title": "AR SDKs", "topics": ["ARKit (iOS)", "ARCore (Android)", "Vuforia", "Spark AR"]},
            {"title": "VR SDKs", "topics": ["Oculus SDK", "OpenVR", "SteamVR", "WebXR"]},
            {"title": "Optimization", "topics": ["Draw Calls", "Polygon Count Reduction", "Baking Lighting"]},
            {"title": "UX for XR", "topics": ["Locomotion", "Spatial Audio", "Gaze and Controllers"]}
        ]
    },
    "database-developer": {
        "name": "Database Developer",
        "description": "Designs database systems.",
        "phases": [
            {"title": "Database Fundamentals", "topics": ["Relational vs NoSQL", "ACID Properties", "CAP Theorem"]},
            {"title": "SQL Mastery", "topics": ["DDL, DML, DCL", "Complex Joins", "Subqueries", "Window Functions"]},
            {"title": "Relational Databases", "topics": ["MySQL", "PostgreSQL", "Oracle", "SQL Server"]},
            {"title": "Advanced RDBMS", "topics": ["Stored Procedures", "Triggers", "Views", "Indexing Strategies"]},
            {"title": "NoSQL Databases", "topics": ["MongoDB (Document)", "Redis (Key-Value)", "Neo4j (Graph)", "Cassandra (Wide-column)"]},
            {"title": "Data Modeling", "topics": ["Entity-Relationship (ER) Diagrams", "Normalization (1NF-3NF)", "Denormalization for performance"]},
            {"title": "Database Administration (DBA)", "topics": ["Backup/Restore", "Replication", "Sharding", "Query Optimization"]}
        ]
    },
    "api-developer": {
        "name": "API Developer",
        "description": "Creates REST APIs and services.",
        "phases": [
            {"title": "Networking & Protocols", "topics": ["HTTP/HTTPS", "Methods (GET, POST, PUT, DELETE)", "Status Codes"]},
            {"title": "API Architectures", "topics": ["RESTful APIs", "GraphQL", "gRPC", "WebSockets"]},
            {"title": "Backend Languages/Frameworks", "topics": ["Node.js (Express)", "Python (FastAPI, Django REST)", "Java (Spring Boot)", "Go"]},
            {"title": "API Design & Documentation", "topics": ["OpenAPI / Swagger", "Postman", "Versioning strategies"]},
            {"title": "Security", "topics": ["OAuth 2.0", "JWT (JSON Web Tokens)", "API Keys", "Rate Limiting", "CORS"]},
            {"title": "Testing", "topics": ["Unit Testing", "Endpoint Testing", "Load Testing (JMeter/K6)"]},
            {"title": "Deployment & Gateways", "topics": ["Kong", "AWS API Gateway", "Nginx"]}]
    },
    "wordpress-developer": {
        "name": "WordPress Developer",
        "description": "Builds WordPress websites.",
        "phases": [
            {"title": "Web Basics", "topics": ["HTML", "CSS", "JavaScript basics"]},
            {"title": "Programming Language", "topics": ["PHP Basics", "PHP in WordPress", "MySQL basics"]},
            {"title": "WordPress Core", "topics": ["Posts vs Pages", "Taxonomies", "Custom Post Types (CPTs)", "Advanced Custom Fields (ACF)"]},
            {"title": "Theme Development", "topics": ["Theme Hierarchy", "Template Tags", "The Loop", "Child Themes"]},
            {"title": "Plugin Development", "topics": ["Actions and Filters", "Shortcodes", "Plugin Architecture"]},
            {"title": "Page Builders", "topics": ["Elementor", "Divi", "Gutenberg Block Development"]},
            {"title": "Optimization & Security", "topics": ["Caching (W3 Total Cache)", "SEO (Yoast)", "Hardening WordPress"]}
        ]
    },
    "shopify-developer": {
        "name": "Shopify Developer",
        "description": "Builds e-commerce stores.",
        "phases": [
            {"title": "Web Fundamentals", "topics": ["HTML", "CSS", "JavaScript", "JSON"]},
            {"title": "Shopify Ecosystem", "topics": ["Shopify Admin Setup", "Products, Collections", "Navigation"]},
            {"title": "Liquid Templating", "topics": ["Liquid Basics", "Objects", "Tags", "Filters"]},
            {"title": "Theme Development", "topics": ["Shopify CLI", "Dawn Theme structure", "Theme Architecture 2.0 (Sections & Blocks)"]},
            {"title": "Storefront API & Headless", "topics": ["GraphQL Basics", "Hydrogen framework", "React integration"]},
            {"title": "App Development", "topics": ["Polaris UI", "Node.js / Ruby for Apps", "Shopify App Bridge", "Webhooks"]},
            {"title": "Optimization", "topics": ["Core Web Vitals", "Image Optimization", "SEO for e-commerce"]}
        ]
    },
    "salesforce-developer": {
        "name": "Salesforce Developer",
        "description": "Develops CRM systems.",
        "phases": [
            {"title": "Salesforce Fundamentals", "topics": ["CRM Concepts", "Objects & Fields", "Relationships", "Validation Rules"]},
            {"title": "Data Modeling & Management", "topics": ["Data Loader", "SOQL (Salesforce Object Query Language)", "SOSL"]},
            {"title": "Apex Programming", "topics": ["Apex Classes", "Triggers", "Testing (Code Coverage)", "Asynchronous Apex (Batches, Futures)"]},
            {"title": "Lightning Framework", "topics": ["Aura Components", "Lightning Web Components (LWC)", "JavaScript for LWC"]},
            {"title": "Integration", "topics": ["REST APIs", "SOAP APIs", "Outbound Messages"]},
            {"title": "Declarative Automation", "topics": ["Flows", "Process Builder (Legacy)", "Workflow Rules"]},
            {"title": "Deployment", "topics": ["Change Sets", "Salesforce DX (CLI)", "Ant Migration Tool"]}
        ]
    },
    "automation-developer": {
        "name": "Automation Developer",
        "description": "Builds automation scripts and bots.",
        "phases": [
            {"title": "Programming & Scripting", "topics": ["Python", "Bash", "PowerShell"]},
            {"title": "Web Automation", "topics": ["Selenium", "Puppeteer", "Playwright", "Cypress"]},
            {"title": "Web Scraping", "topics": ["BeautifulSoup", "Scrapy", "Requests", "Handling CAPTCHAs"]},
            {"title": "API Automation", "topics": ["REST integrations", "Postman scripting", "OAuth automation"]},
            {"title": "RPA (Robotic Process Automation)", "topics": ["UiPath", "Automation Anywhere", "Blue Prism"]},
            {"title": "Task Scheduling", "topics": ["Cron Jobs", "Windows Task Scheduler", "Celery", "Airflow"]},
            {"title": "Testing Automation", "topics": ["PyTest", "JUnit", "CI/CD integration"]}
        ]
    },
    "software-engineer": {
        "name": "Software Engineer",
        "description": "Builds large software systems.",
        "phases": [
            {"title": "Computer Science Fundamentals", "topics": ["Data Structures (Trees, Graphs, Hash Maps)", "Algorithms (Sorting, Searching, Dynamic Programming)", "Time & Space Complexity (Big O)"]},
            {"title": "Core Languages", "topics": ["Java / C++ / Python", "Object-Oriented Programming (OOP)"]},
            {"title": "System Design", "topics": ["High-Level Design (HLD)", "Low-Level Design (LLD)", "Microservices vs Monolith", "Scaling (Horizontal vs Vertical)"]},
            {"title": "Design Patterns", "topics": ["Creational (Singleton, Factory)", "Structural (Adapter, Decorator)", "Behavioral (Observer, Strategy)"]},
            {"title": "Databases & Messaging", "topics": ["RDBMS vs NoSQL", "Message Queues (Kafka, RabbitMQ)"]},
            {"title": "Software Development Life Cycle", "topics": ["Agile Methodology", "Scrum", "Jira", "Code Reviews"]},
            {"title": "Testing & QA", "topics": ["TDD (Test-Driven Development)", "BDD", "Clean Code principles"]}
        ]
    },
    "ui-developer": {
        "name": "UI Developer",
        "description": "Focuses on interface design and user experience.",
        "phases": [
            {"title": "Design Fundamentals", "topics": ["Color Theory", "Typography", "Spacing & Alignment", "Visual Hierarchy"]},
            {"title": "Design Tools", "topics": ["Figma", "Adobe XD", "Sketch", "Wireframing", "Prototyping"]},
            {"title": "Web Foundations", "topics": ["HTML5", "CSS3", "Semantic Markup", "Accessibility (WCAG)"]},
            {"title": "Advanced CSS", "topics": ["Flexbox & Grid", "CSS Variables", "SASS / LESS", "CSS Animations (Keyframes, Transitions)"]},
            {"title": "CSS Frameworks", "topics": ["Tailwind CSS", "Bootstrap", "Material UI", "Chakra UI"]},
            {"title": "JavaScript (UI Focused)", "topics": ["DOM Manipulation", "Event Listeners", "Basic React/Vue for Components"]},
            {"title": "Responsive Design", "topics": ["Mobile-First Approach", "Media Queries", "Cross-Browser Testing"]}
        ]
    }
}
