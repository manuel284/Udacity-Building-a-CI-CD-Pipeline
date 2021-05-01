# create resource group
az group create -n rg-udacity-devops -l "west europe"

# create/deploy web app
az webapp up -g rg-udacity-devops -l "west europe" --sku F1 -n toast-udacity-devops