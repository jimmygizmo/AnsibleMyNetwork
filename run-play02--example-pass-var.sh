#! /usr/bin/env bash

echo
echo "EXAMPLE - TITLE OF PLAYBOOK OR GENERAL GOAL/ACTION GOES HERE."
echo "Enter the name to assign your new EC2 instance."
echo "Enter 'new_instance_name' value: "
read -r new_instance_name

echo
echo "Enter the subnet id of the subnet into which you wish to create your new EC2 instance."
echo "Enter 'new_instance_subnet_id' value: "
read -r new_instance_subnet_id

# TODO: This file is a stub/example. All names and text need to be customized.

ansible-playbook -i inventory.yaml play02--RENAME-THIS.yaml \
  --extra-vars="new_instance_name=$new_instance_name new_instance_subnet_id=$new_instance_subnet_id"

