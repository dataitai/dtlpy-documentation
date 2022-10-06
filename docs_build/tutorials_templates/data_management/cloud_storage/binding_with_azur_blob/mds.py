def section1():
    """
    ## Create an Azure blob function to Continuously Sync a Bucket with Dataloop's Dataset

    If you want to catch events from the Azure blob and update the Dataloop Dataset you need to set up a blob function.
    The function will catch the blob storage events and will reflect them into the Dataloop Platform.

    ### Create the blob function
    1. Insert to Azure platform
    2. Create a Resource group
       * Choose Subscription, Name and Region
    3. Insert to the Resource group
    4. Create -> Storage account
       * Choose Subscription, your Resource group, Name and Region
    5. Create a Container in the created Storage account
       * Public access level -> Container OR Blob
    6. Go back to Resource group
    7. Create -> Function App
       * Choose Subscription, your Resource group, Name and Region
       * Publish -> Code
       * Runtime stack -> Python
       * Version -> <=3.7
    8. Need to flow the instructions in [azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python) to configure your environment and deploy the function according to this order:
       1. Configure your environment
       2. Sign in to Azure
       3. Create your local project
          * in Select a template for your project's first function choose -> Azure Blob Storage trigger
          * in Storage account select your Storage account that created in step4
          * in Resource group select your Resource group that created in step1
          * open the code file
          * add dtlpy to the requirements.txt file
          * add "disabled": false to the function.json file
          * add a function code to __init__.py file
    """


def section2():
    """
       4. Deploy the project to Azure to the function app that you create in step6
       5. Set the Crate a Azure Blob Storage trigger to your Container Name
       ![add_layer](../../../../assets/azure-blob/trriggerDataset.png)
       6. In VS code go to view tab -> Command Palette -> Azure Functions: Upload Local Settings
    9. go to the Function App -> insert to your function -> Function -> Function App
           * add the 3 secrets vars DATASET_ID, DTLPY_USERNAME, DTLPY_PASSWORD

    ### now all what you add to your Container will add auto to dataloop dataset
    """
