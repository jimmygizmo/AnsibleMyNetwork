#! /usr/bin/env bash

echo
echo "EXAMPLE - TITLE OF PLAYBOOK OR GENERAL GOAL/ACTION GOES HERE"
echo "Enter the host or group value as it is configured in your inventory file."
echo "Enter 'hosts' value: "
read -r hosts

ansible-playbook -i inventory.yaml play01--RENAME-THIS.yaml \
  --extra-vars="hosts=$hosts"

