#!/bin/bash

# Command 1: Helm Upgrade - neo4j deployement
helm upgrade --install my-neo4j-release neo4j/neo4j -f neo4j-values.yaml

# Command 2: kubectl apply - streamlit deployment
kubectl create -f k8s-streamlit.yaml
