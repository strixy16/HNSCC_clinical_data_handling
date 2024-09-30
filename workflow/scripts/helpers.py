# Helper functions for clinical data handling
import os
import pandas as pd
import re

def load_data_to_df(file_path):
    """Load clinical data from a csv or xlsx file into a pandas dataframe.

    Args:
        clinical_data_path (str): Path to the clinical data file.

    Returns:
        pd.DataFrame: A pandas dataframe containing the clinical data.
    """
     # Get the file extension
    _, file_extension = os.path.splitext(file_path)
    
    try:
        # Check if the file is an Excel file
        if file_extension == '.xlsx':
            df = pd.read_excel(file_path)
        # Check if the file is a CSV file
        elif file_extension == '.csv':
            df = pd.read_csv(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")
        
        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

def getPatientIdentifierLabel(dataframeToSearch):
    """Function to find a column in a dataframe that contains some form of patient ID or case ID (case-insensitive). 
       If multiple found, will return the first match.

    Parameters
    ----------
    dataframeToSearch : DataFrame
        Dataframe to look for a patient ID column in.

    Returns
    -------
    str
        Label for patient identifier column from the dataframe.
    """

    # regex to get patient identifier column name in the dataframes
    # catches case-insensitive variations of patient_id, patid, pat id, case_id, case id, caseid, id
    regexSearchTerm = re.compile(pattern= r'(pat)?(ient)?(case)?(\s|.)?(id|#)', flags=re.IGNORECASE)

    # Get any columns from the dataframe based on the regex
    patIdentifier = dataframeToSearch.filter(regex=regexSearchTerm).columns.to_list()

    if len(patIdentifier) > 1:
        print("Multiple patient identifier labels found. Using the first one.")
    
    elif len(patIdentifier) == 0:
        raise ValueError("Dataframe doesn't have a recognizeable patient ID column. Must contain patient or case ID.")

    return patIdentifier[0]