Data Sources

1) Electric Vehicle Title and Registration Activity_cleaned (WA): https://data.wa.gov/Transportation/Electric-Vehicle-Title-and-Registration-Activity/rpr4-cgyd
- Source data contained commmas, which caused incorrect parsing. Cleaned data using NotePad++ find and replace capability. Any instance of a comma with a space (, ) was replace with a single space. Any combination of comma with quotes (," or ",) was replaced with a comma. See Electric_Vehicle_Title_and_Registration_Activity_WA_correctedcommas. 
- Python used to further clean data. For cleaned version of data, see Electric_Vehicle_Title_and_Registration_Activity_WA_cleaned. 

2) Elecric Vehicle Registrations by State_cleaned (source modified to only capture needed columns): https://afdc.energy.gov/data/10962
- Source contained graphic. Extracted data into csv file. 