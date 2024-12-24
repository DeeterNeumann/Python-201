'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!

'''
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from pprint import pprint

patient_id = {'medical_record_number': 'X1111111', 'name': "john smith", 'date_of_birth': '12/16/1954', 'medication_allergies': 'no known medication allergies'}

med_id = {'medical_record_number': 'X1111111', 'ndc': '00000-0000-00', 'medication_name': 'midostaurin', 'dose': '75 mg', 'directions': 'take 75 mg once daily', 'indication': 'acute myeloid leukemia'}

dispense_info = {'ndc': '00000-0000-00' , 'date_dispensed': '12/15/2024' , 'quantity_dispensed': 30}

table_choice = ['patient_info', 'medication_info', 'dispense_record'] 

def collect_patient_info():
    """
    Collect patient information from user input and insert it into the patient_info table.
    """
    medical_record_number = input("Enter medical record number (X#######): ")
    name = input("Enter patient's name: ")
    date_of_birth = input("Enter patient's date of birth (MM/DD/YYYY): ")
    medication_allergies = input("Enter medication allergies (comma-separated): ")

    new_patient = {'medical_record_number': medical_record_number, 'name': name, 'date_of_birth': date_of_birth, 'medication_allergies': medication_allergies}

    succeeded = table_insert(patient_info, **new_patient)
    if succeeded:
        print("Patient information successfully saved.")

def collect_medication_info():
    """
    Collect medication information from user input and insert it into the medication_info table.
    """
    medical_record_number = input("Enter medical record number: ")
    ndc = input("Enter drug ndc (#####-####-##): ")
    medication_name = input("Enter the medication name: ")
    dose = input("Enter the dose of the medication and units (e.g., mg, g, mEq, mL): ")
    directions = input("Enter the directions for the medication: ")
    indication = input("Enter why the patient is taking the medication: ")

    new_medication = {'medical_record_number': medical_record_number, 'ndc': ndc, 'medication_name': medication_name, 'dose': dose, 'directions': directions, 'indication': indication}
        
    succeeded = table_insert(medication_info, **new_medication)
    if succeeded:
        print("Medication information successfully saved.")
    
def collect_dispense_info():
    """
    Collect dispense information from user input and insert it into the dispense_record table.
    """
    ndc = input("Enter drug ndc (#####-####-##): ")
    date_dispensed = input("Enter the dispense date (MM/DD/YYYY): ")
    quantity_dispensed = input("Enter the quantity dispensed for the prescription: ")
    
    new_dispense = {'ndc': ndc , 'date_dispensed': date_dispensed, 'quantity_dispensed': quantity_dispensed}

    succeeded = table_insert(dispense_record, **new_dispense)
    if succeeded:
        print("Dispense information successfully saved.")

def table_insert(table, **new_row):
    try:
        with engine.connect() as connection:
            query = sqlalchemy.insert(table).values(
                **new_row
                )
            connection.execute(query)
            connection.commit()
            return True
    except SQLAlchemyError as e:
        print(f"An error occurred while saving the data: {e}")
        return False

def table_update(table, **columns):
    query = sqlalchemy.update(table).values(**columns)
    result = connection.execute(query)
    print(result.rowcount)

def select_table(*table):
    query = sqlalchemy.select(*table)
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    pprint(result_set)

def delete_info(table, column, criteria): 
    get_column = getattr(table.c, column)
    query = sqlalchemy.delete(table).where(get_column == criteria)
    results = connection.execute(query)
    print(f"{results.rowcount} rows deleted from {table}")

# hasattr - returns t/f if object exists

# def table_join(new_table, table_one, table_two)):
#     new_table = sqlalchemy.Table(f"{new_table}", metadata, autoload_with=engine)
#     join_statement = table_one.join(new_table, new_table.columns.)

engine = sqlalchemy.create_engine("mysql+pymysql://root:PASSWORD@localhost/medication_records")
connection = engine.connect()
metadata = sqlalchemy.MetaData()


patient_info = sqlalchemy.Table("patient_info", metadata,
                                sqlalchemy.Column('medical_record_number', sqlalchemy.String(8), nullable=False),
                                sqlalchemy.Column('name', sqlalchemy.String(250), nullable=False),  
	                            sqlalchemy.Column('date_of_birth', sqlalchemy.String(10), nullable=False),
                                sqlalchemy.Column('medication_allergies', sqlalchemy.String(1000), nullable=False)
                                )

medication_info = sqlalchemy.Table("medication_info", metadata,
                                   sqlalchemy.Column('medical_record_number', sqlalchemy.String(8), nullable=False),                                   
                                   sqlalchemy.Column('ndc', sqlalchemy.String(13), nullable=False),
                                   sqlalchemy.Column('medication_name', sqlalchemy.String(100)),
                                   sqlalchemy.Column('dose', sqlalchemy.String(50)),
                                   sqlalchemy.Column('directions', sqlalchemy.String(250)),
                                   sqlalchemy.Column('indication', sqlalchemy.String(250), nullable=False)
                                   )

dispense_record = sqlalchemy.Table('dispense_record', metadata,
                                   sqlalchemy.Column('ndc', sqlalchemy.String(13), nullable=False),
                                   sqlalchemy.Column('date_dispensed', sqlalchemy.String(10)),
                                   sqlalchemy.Column('quantity_dispensed', sqlalchemy.Integer())
                                   )

metadata.create_all(engine)

collect_patient_info()

collect_medication_info()

collect_dispense_info()

# # # update data in each table

table_update(patient_info, **patient_id)

table_update(medication_info, **med_id)

table_update(dispense_record, **dispense_info)

# # select data from each table

select_table(patient_info)
select_table(medication_info)
select_table(dispense_record)

# delete data from each table

delete_info(dispense_record, 'quantity_dispensed', 30)
delete_info(medication_info, 'indication', 'pain')
delete_info(patient_info, 'medication_allergies', 'sulfa')

# use at least one join in a select query

join_statement = patient_info.join(medication_info, medication_info.columns.medical_record_number == patient_info.columns.medical_record_number).join(dispense_record, dispense_record.columns.ndc == medication_info.columns.ndc)
join_query = sqlalchemy.select(patient_info.columns.medical_record_number, patient_info.columns.name, medication_info.columns.medication_name, dispense_record.columns.date_dispensed).select_from(join_statement)

result_proxy_join = connection.execute(join_query)

result_set_join = result_proxy_join.fetchall()
pprint(result_set_join)


# CLI
## input statements with loop, go through choices
### creating functions to take in data etc


# Command line arguments (*args)
# built in python library argparse
### takes python script and adds arguments to it
### ls (list all files in directory)
### grep (search in text for specific string or text file names, pass in information)


# where would the connection.commit() statement go? Inside functions