examples = """
#How many total notifications are there?
MATCH (e) return COUNT(distinct e.Episode_Id) as Result;
#How many total notifications are in Year 2022?
MATCH (e) e.DiagnosisDate.year =2022 return COUNT(distinct e.Episode_Id) as Result;
#How many diagnosed patients are there?
MATCH (e) where e.Stage contains "DIAGNOSED" return COUNT(distinct e.Episode_Id) as Result;
#show total patients grouped by treatment stage
MATCH (e:Episode)
RETURN e.Stage as Stage, count(DISTINCT e.Episode_Id) as NumberOfPatients;
#What is DSTB in TB? 
Return "DSTB is a case where a person is infected with TB bacteria that are susceptible to all the first line anti-TB drugs."  as Result;
#What is DRTB in TB? 
Return "Drug-resistant TB (DR TB) is spread the same way that drug-susceptible TB is spread. TB is spread through the air from one person to another."  as Result;
#What is TPT  in TB? 
Return "Tuberculosis (TB) preventive treatment (or TPT) consists of a course of one or more anti-tuberculosis medicines given with the intention of preventing the development of TB disease."  as Result;
#How many DSTB patients are there? 
MATCH (e) where e.TypeOfCase contains 'Retreatment: Others' or  e.TypeOfCase contains 'New' or  e.TypeOfCase contains 'Retreatment: Recurrent' or  e.TypeOfCase contains 'Retreatment: Treatment after failure' or  e.TypeOfCase contains 'Retreatment: Treatment after lost to follow up' or  e.TypeOfCase contains 'NULL'
return COUNT(distinct e.Episode_Id) as Result;
#How many DRTB patients are there? 
MATCH (e) where e.TypeOfCase contains 'PMDT'
return COUNT(distinct e.Episode_Id) as Result;
#How many TBI patients are there? 
MATCH (e) where e.TypeOfCase contains 'TPT (TB Prevention Therapy)'
return COUNT(distinct e.Episode_Id) as Result;
#How many Test are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null
return COUNT(distinct d.Test_Request_Id) as Result;
#How many Test are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null
return COUNT(distinct d.Test_Request_Id) as Result;
#How many Test are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null
return COUNT(distinct d.Test_Request_Id) as Result;
#How many Test are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null 
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Test are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null 
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Microscopy ZN and Fluorescent Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and (d.Test_Type contains "Microscopy" or d.Test_Type contains "Fluorescent" )
return COUNT(distinct d.Test_Request_Id) as Result;
#How many Microscopy ZN and Fluorescent Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and (d.Test_Type contains "Microscopy" or d.Test_Type contains "Fluorescent" )
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Microscopy ZN and Fluorescent Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and (d.Test_Type contains "Microscopy" or d.Test_Type contains "Fluorescent" )
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Microscopy ZN and Fluorescent Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and (d.Test_Type contains "Microscopy" or d.Test_Type contains "Fluorescent" )
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Microscopy ZN and Fluorescent Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and (d.Test_Type contains "Microscopy" or d.Test_Type contains "Fluorescent" )
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CBNAAT Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "CBNAAT"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CBNAAT Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "CBNAAT"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CBNAAT Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "CBNAAT"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CBNAAT Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "CBNAAT"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CBNAAT Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "CBNAAT"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Truenat (MTB) Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB)"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Truenat (MTB) Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB)"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many   Truenat (MTB) Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB)"
return COUNT(distinct d.Test_Request_Id)as Result;
#How many  Truenat (MTB) Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB)"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Truenat (MTB) Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB)"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Truenat (MTB-RIF) Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB-RIF)"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Truenat (MTB-RIF) Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB-RIF)"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many   Truenat (MTB-RIF) Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB-RIF)"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Truenat (MTB-RIF) Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB-RIF)"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Truenat (MTB-RIF) Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "Trunat (MTB-RIF)"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Culture Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "Culture"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Culture Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "Culture"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Culture Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "Culture"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Culture Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "Culture"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Culture Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "Culture"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  FLLPA  Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "F Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  FLLPA Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "F Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  FLLPA Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "F Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  FLLPA Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "F Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  FLLPA Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "F Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  SLLPA Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "S Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  SLLPA Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "S Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  SLLPA Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "S Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  SLLPA Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "S Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  SLLPA Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "S Line LPA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  DST Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "DST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  DST Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "DST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  DST Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "DST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  DST Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "DST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  DST Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "DST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Chest X Ray Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "X Ray"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Chest X Ray Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "X Ray"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Chest X Ray Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "X Ray"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Chest X Ray Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "X Ray"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Chest X Ray Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "X Ray"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Cytopathology Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "Cytopatho"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Cytopathology Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "Cytopatho"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Cytopathology Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "Cytopatho"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Cytopathology Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "Cytopatho"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Cytopathology Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "Cytopatho"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Histopathology Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "Histopath"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Histopathology Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "Histopath"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Histopathology Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "Histopath"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Histopathology Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "Histopath"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Histopathology Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "Histopath"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Gene Sequencing Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "Gene"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Gene Sequencing Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "Gene"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Gene Sequencing Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "Gene"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Gene Sequencing Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "Gene"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Gene Sequencing Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "Gene"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Other Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "Other"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Other Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "Other"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Other Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "Other"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Other Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "Other"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  Other Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "Other"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  TST Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "TST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  TST Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "TST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  TST Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "TST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  TST Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "TST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  TST Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "TST"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  IGRA Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "IGRA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  IGRA Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "IGRA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  IGRA Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "IGRA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  IGRA Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "IGRA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  IGRA Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "IGRA"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CY-TB Tests are added Today? 
MATCH (d) where date(d.TestAddedOn) = date()-Duration({days: 0}) and d.TestAddedOn is not null and d.Test_Type contains "CY"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CY-TB Tests are added in last 30 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 30}) and d.TestAddedOn is not null and d.Test_Type contains "CY"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CY-TB Tests are added in last 60 days? 
MATCH (d) where date(d.TestAddedOn) >= date()-Duration({days: 60}) and d.TestAddedOn is not null and d.Test_Type contains "CY"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CY-TB Tests are added in the year 2023? 
MATCH (d) where d.TestAddedOn.year =2023 and d.TestAddedOn is not null and d.Test_Type contains "CY"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many  CY-TB Tests are added in the last 5 years? 
MATCH (d) where d.TestAddedOn.year <=2024 and d.TestAddedOn is not null and d.Test_Type contains "CY"
return COUNT(distinct d.Test_Request_Id) as Result;
#How many patients are there  whose Status is Result;s Available? 
MATCH (d) where d.Test_Result; contains "Available"
return COUNT(distinct d.Episode_Id) as Result;
#How many  patients are there  whose Status is Result;s Pending? 
MATCH (d) where d.Test_Result; contains "Pending"
return COUNT(distinct d.Episode_Id) as Result;
#SHow the total count of DSTB Patients in last 30 days? 
MATCH (e) where date(e.DiagnosisDate) >= date()-Duration({days: 30}) and e.TypeOfCase contains 'Retreatment: Others' or  e.TypeOfCase contains 'New' or  e.TypeOfCase contains 'Retreatment: Recurrent' or  e.TypeOfCase contains 'Retreatment: Treatment after failure' or  e.TypeOfCase contains 'Retreatment: Treatment after lost to follow up' or  e.TypeOfCase contains 'NULL'
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of DRTB Patients in last 30 days? 
MATCH (e) where date(e.DiagnosisDate) >= date()-Duration({days: 30}) and e.TypeOfCase contains ("PMDT") 
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of TBI  Patients in last 30 days? 
MATCH (e) where date(e.DiagnosisDate) >= date()-Duration({days: 30}) and e.TypeOfCase contains ("TPT (TB Prevention Therapy)")
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of DSTB Patients in last 60 days? 
MATCH (e) where date(e.DiagnosisDate) >= date()-Duration({days: 60}) and e.TypeOfCase contains 'Retreatment: Others' or  e.TypeOfCase contains 'New' or  e.TypeOfCase contains 'Retreatment: Recurrent' or  e.TypeOfCase contains 'Retreatment: Treatment after failure' or  e.TypeOfCase contains 'Retreatment: Treatment after lost to follow up' or  e.TypeOfCase contains 'NULL'
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of DRTB Patients in last 60 days? 
MATCH (e) where date(e.DiagnosisDate) >= date()-Duration({days: 60}) and e.TypeOfCase contains ("PMDT") 
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of TBI  Patients in last 60 days? 
MATCH (e) where date(e.DiagnosisDate) >= date()-Duration({days: 60}) and e.TypeOfCase contains ("TPT (TB Prevention Therapy)")
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of DSTB patients  in the year 2023? 
MATCH (e) where e.DiagnosisDate.year = 2023 and e.TypeOfCase contains 'Retreatment: Others' or  e.TypeOfCase contains 'New' or  e.TypeOfCase contains 'Retreatment: Recurrent' or  e.TypeOfCase contains 'Retreatment: Treatment after failure' or  e.TypeOfCase contains 'Retreatment: Treatment after lost to follow up' or  e.TypeOfCase contains 'NULL'
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of DRTB patients in the year 2023? 
MATCH (e) where e.DiagnosisDate.year = 2023 and e.TypeOfCase contains ("PMDT") 
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of TPT patients in the year 2023? 
MATCH (e) where e.DiagnosisDate.year = 2023 and e.TypeOfCase contains ("TPT (TB Prevention Therapy)")
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of DSTB patients in the last five years? 
MATCH (e) where e.DiagnosisDate.year <=  2024 and e.TypeOfCase contains 'Retreatment: Others' or  e.TypeOfCase contains 'New' or  e.TypeOfCase contains 'Retreatment: Recurrent' or  e.TypeOfCase contains 'Retreatment: Treatment after failure' or  e.TypeOfCase contains 'Retreatment: Treatment after lost to follow up' or  e.TypeOfCase contains 'NULL'
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of DRTB patients in the last  five year? 
MATCH (e) where e.DiagnosisDate.year <=  2024 and e.TypeOfCase contains ("PMDT") 
return COUNT(distinct e.Episode_Id) as Result;
#SHow the total count of TPT patients in the  last five year? 
MATCH (e) where e.DiagnosisDate.year <=  2024 and e.TypeOfCase contains ("TPT (TB Prevention Therapy)")
return COUNT(distinct e.Episode_Id) as Result;
#How many patients are there whose Result is  Positive? 
MATCH (d) where d.Is_Positive = 1
return COUNT(distinct d.Episode_Id) as Result;
#How many patients are there whose Result is  Negative? 
MATCH (d) where d.Is_Positive = 0
return COUNT(distinct d.Episode_Id) as Result
"""
