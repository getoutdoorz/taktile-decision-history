# Assume this code will run when there is a merge to main branch. 
# This code will update the existing nodes with new node definition using API

import requests, json
import os, sys
from pathlib import Path

def listDecisionFlows():
    """Return list of Decision Flows in workspace"""
    url = "https://eu-central-1.taktile-org.decide.taktile.com/run/api/v1/flows/list-decision-graphs/sandbox/decide"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-Api-Key": os.environ.get("API_KEY")
    }
    payload = {
        "data": {"organization_name": "NB36"},
        "metadata": {"version": "v1.0", "entity_id": "string"},
        "control": {"execution_mode": "sync"}
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def getDecisionGraph(flow_id):
    """Return overview of nodes in a specific Decision Graph
        Input: flow_id (str): The ID of the Decision Flow to retrieve."""
    
    url = "https://eu-central-1.taktile-org.decide.taktile.com/run/api/v1/flows/get-decision-graph/sandbox/decide"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-Api-Key": os.environ.get("API_KEY")
    }
    payload = {
        "data": {"flow_id": flow_id},
        "metadata": {"version": "v1.0", "entity_id": "string"},
        "control": {"execution_mode": "sync"}
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def patchDecisionGraph(flow_id, node_id, src_code):
    """Update a specific node in a Decision Graph
        Input: flow_id (str): The ID of the Decision Flow to retrieve.
        node_id (str): The ID of the node to update.
        src_code (str): The new source code for the node."""
    
    url = "https://eu-central-1.taktile-org.decide.taktile.com/run/api/v1/flows/patch-decision-graph/sandbox/decide"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-Api-Key": os.environ.get("API_KEY")
    }
    payload = {
        "data": {"flow_id": flow_id, "node_id": node_id, "src_code": src_code},
        "metadata": {"version": "v1.0", "entity_id": "string"},
        "control": {"execution_mode": "sync"}
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def patchNodes(changed_files):
    """Patch nodes whose name matches a changed Python file.
        Input: changed_files (list): List of changed Python files."""
    
    # Get decision flows
    flows = listDecisionFlows().get("data", {}).get("flows", [])

    # Get overview of nodes in each flow
    for flow in flows:
        nodes = getDecisionGraph(flow.get("flow_id")).get("data", {}).get("graph", [])

        # Get name/id for each node
        for node in nodes:
            node_name, node_id = node.get("node_name"), node.get("node_id")

            # Check if node name matches any changed code node
            for file in changed_files:
                if Path(file).stem == node_name:

                    # Grab the updated code
                    with open(file, 'r') as f:
                        src_code = f.read()

                    # Patch the node with new source code
                    print(f"Patching node {node_name} in flow {flow.get('flow_id')}")
                    result = patchDecisionGraph(flow.get("flow_id"), node_id, src_code)
                    print(f"Patch result: {result}")


if __name__ == "__main__":
    # get list of changed files from args
    changed_files = sys.argv[1:]

    if changed_files:
        patchNodes(changed_files)
        
    else:
        print("No code nodes changed, skipping patch.")
        exit(0)