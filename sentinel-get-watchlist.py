# Script will authenticate to Azure using Azure CLI and then 

import requests
from azure.identity import AzureCliCredential

# grab authentication token from Azure CLI - you must first sign-in using az login command
credential = AzureCliCredential()

# grab token for management.azure.com
token = credential.get_token('https://management.azure.com/.default').token

# list watchlist items
def getWatchlist(subscription, resourcegroupname, workspacename, watchlistalias):
    headers = {
        'Authorization': 'Bearer {0}'.format(token),
        'Content-Type': 'application/json',
    }

    uri = 'https://management.azure.com/subscriptions/' + subscription + '/resourceGroups/' + resourcegroupname + '/providers/Microsoft.OperationalInsights/workspaces/' + workspacename + '/providers/Microsoft.SecurityInsights/watchlists/' + watchlistalias + '/watchlistItems?api-version=2022-07-01-preview'

    response = requests.get(uri, headers=headers)

    return(response.content)