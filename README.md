# Taktile Code Node Auto-Patcher

This repository is an example of how to update Taktile code nodes via the Decision History API whenever changes to the definitions of the code nodes are merged to the `main` branch.

## How It Works
- On every push to `main`, a GitHub Actions workflow will be triggered.
- The workflow runs a Python script which will patch Taktile code nodes if any changes are detected in the code node definitions compared to `main`.

## Key Files
- `code-nodes/` directory: Contains Python files representing code nodes (e.g., `Summarize.py`, `Multiply.py`)
- A Python script `patchNodes.py` that patches Taktile code nodes.
- `.github/workflows/main.yml`: A GitHub Actions workflow configuration that triggers the patching process.

## Requirements
- Python 3.9+
    - Required libraries: `requests`
- Taktile API key (set as a GitHub secret: `API_KEY`)

## Usage
1. Create a new branch off of `main` and checkout to that branch.
1. Update the organization name for API calls within `patchNodes.py`.
1. Make changes to the Python files in the `code-nodes/` directory.
1. Commit your changes and push the branch to GitHub.
1. Create a pull request to merge your changes into `main`.
1. Once the pull request is merged, the GitHub Actions workflow will automatically run.
    1. The workflow will automatically run and patch any matching Taktile code nodes.
    1. All output and API responses are visible in the GitHub Actions log.

## Security
- Your API key is stored securely as a GitHub secret and never exposed in logs.
