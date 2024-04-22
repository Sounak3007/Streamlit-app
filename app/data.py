import pandas as pd
from tqdm import tqdm
from datetime import datetime

from py2neo import Graph

graph = Graph("bolt://localhost:7687", user="neo4j", password="password")
# graph.read('MATCH (n) return n')
df_elogs = pd.read_csv('./elogsdata.csv', parse_dates=['Patient_Enrolled_On', 'DiagnosisDate','TestAddedOn','Test_Tested_Date','Test_Result_Date'],low_memory=False)
#df_elogs['added_on'] = pd.to_datetime(df_elogs['added_on'], format='%Y-%m-%d')
#df_elogs['DiagnosisDate'] = pd.to_datetime(df_elogs['DiagnosisDate'], format='%Y-%m-%d')
df_elogs.reset_index(inplace=True)
df_elogs.loc[:, ['PatientAddedByDescription','PatientAddedBy_HierarchyType','TypeOfCase', 'Stage',
                 'TreatmentOutcome','DiagnosisBasis', 'SiteOfDisease','Age_Range','Gender',
                 'TestAddedByDescription','TestAddedBy_HierarchyType','Test_Type',
                 'Specimen','VisualAppearanceSputum','TestingFacilityName',
                 'RifResistance_Sensitive','Test_Stage']].fillna('NA', inplace=True)

df_elogs.loc[:, ['Age','Weight']].fillna(999, inplace=True)
df_elogs.loc[:, ['DiagnosisDate','Test_Tested_Date','Test_Result_Date','TestAddedOn']].fillna(pd.to_datetime('1900-01-01'), inplace=True)
episodes = pd.DataFrame(df_elogs.loc[:50000, ['Episode_Id','State_Name','District_Name','TBU_Name','HF_Name',
                                              'PatientAddedByDescription','PatientAddedBy_HierarchyType',
                                              'DiagnosisDate','TypeOfCase','Stage','TreatmentOutcome',
                                              'DiagnosisBasis','SiteOfDisease','Age','Age_Range','Gender',
                                              'Weight']])

episodes.columns = ['Episode_Id','State_Name','District_Name','TBU_Name','HF_Name','PatientAddedByDescription',
                    'PatientAddedBy_HierarchyType','DiagnosisDate','TypeOfCase','Stage','TreatmentOutcome',
                    'DiagnosisBasis','SiteOfDisease','Age','Age_Range','Gender','Weight']
episodes.drop_duplicates(subset='Episode_Id', inplace=True)
#episodes.loc[episodes['Patient_Enrolled_On'].isna(), 'Patient_Enrolled_On'] = pd.to_datetime("1900-01-01")
episodes.loc[episodes['DiagnosisDate'].isna(), 'DiagnosisDate'] = pd.to_datetime("1900-01-01")
# categories.rename(columns={'category_list':'category'}, inplace=True)
# categories = categories.explode('category').drop_duplicates(subset=['category'])
diagnostics = pd.DataFrame(df_elogs.loc[:50000, ['index', 'Episode_Id', 'TestAddedByDescription',
                                                 'TestAddedBy_HierarchyType','Test_Request_Id','Test_Type',
                                                 'TestAddedOn','Test_Tested_Date','Test_Result_Date',
                                                 'Delay_TestAdded_TestReported','Delay_TestReported_TestResult',
                                                 'Delay_TestAdded_TestResult','QR_Code_Available','Specimen',
                                                 'VisualAppearanceSputum','TestingFacilityName','Test_Result',
                                                 'Valid_Test','Is_Positive','RifResistance_Sensitive',
                                                 'Test_Stage']])
print(diagnostics.shape)
diagnostics.columns = ['id', 'Episode_Id', 'TestAddedByDescription','TestAddedBy_HierarchyType','Test_Request_Id'
                    ,'Test_Type','TestAddedOn','Test_Tested_Date','Test_Result_Date','Delay_TestAdded_TestReported'
                    ,'Delay_TestReported_TestResult','Delay_TestAdded_TestResult','QR_Code_Available','Specimen'
                    ,'VisualAppearanceSputum','TestingFacilityName','Test_Result','Valid_Test','Is_Positive'
                    ,'RifResistance_Sensitive','Test_Stage']
diagnostics.loc[diagnostics['Test_Tested_Date'].isna(), 'Test_Tested_Date'] = pd.to_datetime("1900-01-01")
diagnostics.loc[diagnostics['Test_Result_Date'].isna(), 'Test_Result_Date'] = pd.to_datetime("1900-01-01")
diagnostics.loc[diagnostics['TestAddedOn'].isna(), 'TestAddedOn'] = pd.to_datetime("1900-01-01")
diagnostics.drop_duplicates(subset='id', inplace=True)
print(diagnostics.shape)
diagnostics.head()
def add_episodes(graph, episodes):
    # Adds patient nodes to the Neo4j graph.

    tx = graph.begin()

    for index, row in tqdm(episodes.iloc[:, :].iterrows()):
        # print(row)
        tx.evaluate(
            '''
   CREATE( e:Episode {Episode_Id: $Episode_Id, State_Name: $State_Name,District_Name: $District_Name, 
            TBU_Name: $TBU_Name,HF_Name: $HF_Name, PatientAddedByDescription: $PatientAddedByDescription, 
            PatientAddedBy_HierarchyType: $PatientAddedBy_HierarchyType, DiagnosisDate: $DiagnosisDate, 
            TypeOfCase: $TypeOfCase, Stage: $Stage, TreatmentOutcome: $TreatmentOutcome, 
            DiagnosisBasis: $DiagnosisBasis, SiteOfDisease: $SiteOfDisease, Age: $Age, Age_Range: $Age_Range, 
            Gender: $Gender, Weight: $Weight})

    ''', parameters={'Episode_Id': row['Episode_Id'], 'State_Name': row['State_Name'],
                     'District_Name': row['District_Name'],'TBU_Name': row['TBU_Name'],
                     'HF_Name': row['HF_Name'],'PatientAddedByDescription': row['PatientAddedByDescription'],
                     'PatientAddedBy_HierarchyType': row['PatientAddedBy_HierarchyType'],
                     'DiagnosisDate': row['DiagnosisDate'],'TypeOfCase': row['TypeOfCase'],
                     'Stage': row['Stage'], 'TreatmentOutcome': row['TreatmentOutcome'],
                     'DiagnosisBasis': row['DiagnosisBasis'],'SiteOfDisease': row['SiteOfDisease'],
                     'Age': row['Age'], 'Age_Range': row['Age_Range'], 'Gender': row['Gender'],
                     'Weight': row['Weight'] }
        )
    graph.commit(tx)
    # return graph.run(query, parameters = {'rows':episodes.to_dict('records')})
    return True
def add_diagnostics(graph, diagnostics):
    # Adds patient nodes to the Neo4j graph.

    tx = graph.begin()

    for index, row in tqdm(diagnostics.iterrows()):
        tx.evaluate(
            '''
   CREATE( d:Diagnostic {id: $id, Episode_Id:$Episode_Id,TestAddedByDescription: $TestAddedByDescription, TestAddedBy_HierarchyType: $TestAddedBy_HierarchyType, Test_Request_Id: $Test_Request_Id, Test_Type: $Test_Type, TestAddedOn: $TestAddedOn, Test_Tested_Date: $Test_Tested_Date, Test_Result_Date: $Test_Result_Date, Delay_TestAdded_TestReported: $Delay_TestAdded_TestReported, Delay_TestReported_TestResult: $Delay_TestReported_TestResult, Delay_TestAdded_TestResult: $Delay_TestAdded_TestResult, QR_Code_Available: $QR_Code_Available, Specimen: $Specimen, VisualAppearanceSputum: $VisualAppearanceSputum, TestingFacilityName: $TestingFacilityName, Test_Result: $Test_Result, Valid_Test: $Valid_Test, Is_Positive: $Is_Positive, RifResistance_Sensitive: $RifResistance_Sensitive, Test_Stage: $Test_Stage})
   WITH d
    MATCH
    (d:Diagnostic),
    (e:Episode)
    WHERE d.Episode_Id = $Episode_Id AND e.Episode_Id = $Episode_Id
    CREATE (d)-[r:RELTYPE]->(e)
    ''', parameters={'id': row['id']
                , 'Episode_Id': row['Episode_Id']
                ,'TestAddedByDescription': row['TestAddedByDescription']
                ,'TestAddedBy_HierarchyType': row['TestAddedBy_HierarchyType']
                ,'Test_Request_Id': row['Test_Request_Id']
                ,'Test_Type': row['Test_Type']
                ,'TestAddedOn': row['TestAddedOn']
                ,'Test_Tested_Date': row['Test_Tested_Date']
                ,'Test_Result_Date': row['Test_Result_Date']
                ,'Delay_TestAdded_TestReported': row['Delay_TestAdded_TestReported']
                ,'Delay_TestReported_TestResult': row['Delay_TestReported_TestResult']
                ,'Delay_TestAdded_TestResult': row['Delay_TestAdded_TestResult']
                ,'QR_Code_Available': row['QR_Code_Available']
                ,'Specimen': row['Specimen']
                ,'VisualAppearanceSputum': row['VisualAppearanceSputum']
                ,'TestingFacilityName': row['TestingFacilityName']
                ,'Test_Result': row['Test_Result']
                ,'Valid_Test': row['Valid_Test']
                ,'Is_Positive': row['Is_Positive']
                ,'RifResistance_Sensitive': row['RifResistance_Sensitive']
                ,'Test_Stage': row['Test_Stage']}
        )
    graph.commit(tx)
    return True
add_episodes(graph, episodes)
add_diagnostics(graph,diagnostics)
tx = graph.begin()
tx.evaluate('CREATE CONSTRAINT episode IF NOT EXISTS FOR (e:Episode) REQUIRE e.Episode_Id IS UNIQUE')
tx.commit
tx = graph.begin()
tx.evaluate('CREATE CONSTRAINT diagnostic IF NOT EXISTS FOR (d:Diagnostic) REQUIRE d.id IS UNIQUE')
tx.commit