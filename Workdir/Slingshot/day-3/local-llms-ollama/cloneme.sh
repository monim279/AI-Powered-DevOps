#!/bin/bash

# Clone the repo
git clone https://github.com/cloudmafia/ai-assisted-devops.git

# Navigate to the cloned directory
cd ai-assisted-devops

# Copy the README file from the public repo and save it as a new file in the cloned directory
echo "# AI Assisted DevOps Overview"
cat README.md > overview.md

# Create an HTML page for the overview using the markdown syntax
echo "## AI Assisted DevOps Overview"
echo ""
echo "<h1>Ai Assisted DevOps</h1>"
echo "<p>AI-assisted devops is a framework that uses artificial intelligence to streamline and automate development processes.</p>"
echo "</body><html></html>"

# Create an HTML page for the README file using the markdown syntax
cat > README.html <<EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ai Assisted Devops</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Ai Assisted Devops</h1>
    <p>Ai-assisted devops is a framework that uses artificial intelligence to streamline and automate development processes.</p>
    <ul>
        <li>Uses natural language processing (NLP) to improve code readability</li>
        <li>Utilizes machine learning algorithms for automated testing and deployment</li>
        <li>Employs computer vision to detect and prevent common errors</li>
    </ul>
EOF

# Add the README HTML file as an asset in the cloned directory
cp README.html overview.md

# Update the main README file with a brief description of the project
cat > main.readme <<EOF
# AI Assisted Devops Overview
## Description
AI-assisted devops is a framework that uses artificial intelligence to streamline and automate development processes.
It leverages natural language processing, machine learning algorithms, and computer vision to improve code readability, detect common errors, and enhance overall development efficiency.
### Features
- Uses NLP for improved code readability
- Utilizes ML for automated testing and deployment
- Employs CV for error detection
## Installation
Clone the repository using git
Navigate to the cloned directory
Copy the README file to a new location
Create an HTML page in the cloned directory
EOF

# Update the main README file with a brief description of the project
cat > main.readme <<EOF
# AI Assisted Devops Overview
## Description
AI-assisted devops is a framework that uses artificial intelligence to streamline and automate development processes.
It leverages natural language processing, machine learning algorithms, and computer vision to improve code readability, detect common errors, and enhance overall development efficiency.
### Features
- Uses NLP for improved code readability
- Utilizes ML for automated testing and deployment
- Employs CV for error detection
## Installation
Clone the repository using git
Navigate to the cloned directory
Copy the README file to a new location
Create an HTML page in the cloned directory

EOF

# Save changes to the main README file
echo ""

# Output the overview of the project using both README files
cat overview.md
cat main.readme

