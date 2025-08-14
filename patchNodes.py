# Assume this code will run when there is a merge to main branch. 
# This code will update the existing nodes with new node definition using API

import requests, json

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