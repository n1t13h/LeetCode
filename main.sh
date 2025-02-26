#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <leetcode-problem-url>"
    exit 1
fi

# Extract the problem slug from the URL
url="$1"
slug=$(echo "$url" | awk -F'/' '{print $(NF-1)}')

echo "Extracted Problem Slug: $slug"
# Fetch problem details using LeetCode's GraphQL API
response=$(curl -s 'https://leetcode.com/graphql' \
    -H 'Content-Type: application/json' \
    --data-raw "{\"query\":\"query { question(titleSlug: \\\"$slug\\\") { questionFrontendId title } }\"}")

# Debugging: Print API response
echo "API Response: $response"

# Extract problem number and title
problem_number=$(echo "$response" | jq -r '.data.question.questionFrontendId')
problem_title=$(echo "$response" | jq -r '.data.question.title')

# Debugging: Print extracted values
echo "Extracted Problem Number: $problem_number"
echo "Extracted Problem Title: $problem_title"

# Check if API returned valid data
if [ -z "$problem_number" ] || [ -z "$problem_title" ]; then
    echo "Error: Failed to fetch problem details. Check the LeetCode URL or API response."
    exit 1
fi

# Convert title to lowercase and replace spaces with hyphens
formatted_title=$(echo "$problem_title" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')

# Folder name format: problem-number-title
folder_name="${problem_number}-${formatted_title}"

# Create the directory
mkdir -p "$folder_name"

# Create the Python file inside the directory
echo "# Solution for $problem_number. $problem_title" > "$folder_name/$folder_name.py"

echo "Created folder: $folder_name"
echo "Created file: $folder_name/$folder_name.py"
